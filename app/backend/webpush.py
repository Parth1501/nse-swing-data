"""Minimal Web Push sender (RFC 8291 aes128gcm + RFC 8292 VAPID).

Written on top of `cryptography` only, so the image needs no compiled extras.
"""
import base64
import json
import os
import struct
import time
from urllib.parse import urlparse

import httpx
from cryptography.hazmat.primitives import hashes, hmac, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def b64u(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def b64u_dec(text: str) -> bytes:
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


def _hmac(key: bytes, data: bytes) -> bytes:
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(data)
    return h.finalize()


def _pub_bytes(key) -> bytes:
    return key.public_key().public_bytes(
        serialization.Encoding.X962, serialization.PublicFormat.UncompressedPoint
    )


def generate_vapid_keys() -> tuple[str, str]:
    """Returns (private, public) as base64url strings."""
    key = ec.generate_private_key(ec.SECP256R1())
    priv = key.private_numbers().private_value.to_bytes(32, "big")
    return b64u(priv), b64u(_pub_bytes(key))


def load_private_key(private_b64: str):
    value = int.from_bytes(b64u_dec(private_b64), "big")
    return ec.derive_private_key(value, ec.SECP256R1())


def encrypt(payload: bytes, p256dh: str, auth: str, salt: bytes | None = None,
            server_key=None) -> bytes:
    """Encrypts one push message body (single record, aes128gcm)."""
    ua_pub_bytes = b64u_dec(p256dh)
    auth_secret = b64u_dec(auth)
    ua_pub = ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256R1(), ua_pub_bytes)
    server_key = server_key or ec.generate_private_key(ec.SECP256R1())
    as_pub_bytes = _pub_bytes(server_key)
    shared = server_key.exchange(ec.ECDH(), ua_pub)

    prk_key = _hmac(auth_secret, shared)
    ikm = _hmac(prk_key, b"WebPush: info\x00" + ua_pub_bytes + as_pub_bytes + b"\x01")
    salt = salt or os.urandom(16)
    prk = _hmac(salt, ikm)
    cek = _hmac(prk, b"Content-Encoding: aes128gcm\x00\x01")[:16]
    nonce = _hmac(prk, b"Content-Encoding: nonce\x00\x01")[:12]

    cipher = AESGCM(cek).encrypt(nonce, payload + b"\x02", None)
    rs = 4096
    header = salt + struct.pack("!IB", rs, len(as_pub_bytes)) + as_pub_bytes
    return header + cipher


def vapid_header(endpoint: str, private_b64: str, public_b64: str, subject: str) -> str:
    url = urlparse(endpoint)
    claims = {"aud": f"{url.scheme}://{url.netloc}", "exp": int(time.time()) + 12 * 3600, "sub": subject}
    head = b64u(json.dumps({"typ": "JWT", "alg": "ES256"}, separators=(",", ":")).encode())
    body = b64u(json.dumps(claims, separators=(",", ":")).encode())
    signing_input = f"{head}.{body}".encode()
    der = load_private_key(private_b64).sign(signing_input, ec.ECDSA(hashes.SHA256()))
    r, s = decode_dss_signature(der)
    sig = b64u(r.to_bytes(32, "big") + s.to_bytes(32, "big"))
    return f"vapid t={head}.{body}.{sig}, k={public_b64}"


def send(sub: dict, data: dict, private_b64: str, public_b64: str, subject: str,
         ttl: int = 6 * 3600, urgency: str = "high", client: httpx.Client | None = None) -> int:
    """Sends one notification. Returns the HTTP status (404/410 = subscription gone)."""
    body = encrypt(json.dumps(data).encode(), sub["p256dh"], sub["auth"])
    headers = {
        "Authorization": vapid_header(sub["endpoint"], private_b64, public_b64, subject),
        "Content-Encoding": "aes128gcm",
        "Content-Type": "application/octet-stream",
        "TTL": str(ttl),
        "Urgency": urgency,
    }
    own = client is None
    client = client or httpx.Client(timeout=15)
    try:
        return client.post(sub["endpoint"], content=body, headers=headers).status_code
    finally:
        if own:
            client.close()
