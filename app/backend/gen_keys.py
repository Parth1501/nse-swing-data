"""Prints fresh VAPID keys, an invite code and an admin token as .env lines."""
import secrets

from webpush import generate_vapid_keys

priv, pub = generate_vapid_keys()
print(f"VAPID_PRIVATE_KEY={priv}")
print(f"VAPID_PUBLIC_KEY={pub}")
print(f"INVITE_CODE={secrets.token_hex(4)}")
print(f"ADMIN_TOKEN={secrets.token_urlsafe(32)}")
