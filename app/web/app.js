"use strict";

// ---------- helpers ----------
const $ = (sel, el = document) => el.querySelector(sel);
const view = $("#view");
const esc = (v) => String(v ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const n = (v) => (v === "" || v === null || v === undefined || isNaN(+v) ? null : +v);
const fmt = (v, d = 2) => (n(v) === null ? "–" : (+v).toLocaleString("en-IN", { maximumFractionDigits: d, minimumFractionDigits: 0 }));
const rs = (v) => (n(v) === null ? "–" : "₹" + fmt(v));
const pct = (v, d = 2) => (n(v) === null ? "–" : (+v > 0 ? "+" : "") + (+v).toFixed(d) + "%");
const cls = (v) => (n(v) === null ? "" : +v > 0 ? "up" : +v < 0 ? "down" : "");
const compact = (v) => {
  v = n(v); if (v === null) return "–";
  const a = Math.abs(v);
  if (a >= 1e7) return (v / 1e7).toFixed(2) + "Cr";
  if (a >= 1e5) return (v / 1e5).toFixed(2) + "L";
  if (a >= 1e3) return (v / 1e3).toFixed(1) + "K";
  return String(Math.round(v));
};
const ago = (iso) => {
  if (!iso) return "";
  const t = new Date(iso.replace(" ", "T") + (/[zZ]|[+-]\d\d:?\d\d$/.test(iso) ? "" : "+05:30"));
  const s = (Date.now() - t) / 1000;
  if (isNaN(s)) return iso;
  if (s < 90) return "just now";
  if (s < 3600) return Math.round(s / 60) + " min ago";
  if (s < 86400) return Math.round(s / 3600) + " h ago";
  return t.toLocaleDateString("en-IN", { day: "numeric", month: "short" }) + ", " + t.toLocaleTimeString("en-IN", { hour: "2-digit", minute: "2-digit" });
};
const trendChip = (label, t) => `<span class="chip ${t === "up" || t === "bullish" ? "up" : t === "down" || t === "bearish" ? "down" : ""}">${esc(label)} ${esc(t || "–")}</span>`;
const skeleton = (k = 3) => Array(k).fill('<div class="skeleton"></div>').join("");

function toast(msg) {
  const t = document.createElement("div");
  t.className = "toast"; t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 2800);
}

async function api(path, opts = {}) {
  const r = await fetch(path, {
    credentials: "same-origin",
    headers: { "Content-Type": "application/json" },
    ...opts,
    body: opts.body ? JSON.stringify(opts.body) : undefined,
  });
  if (r.status === 401) { state.me = null; go("#/login"); throw new Error("signed out"); }
  const data = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(data.error || r.statusText);
  return data;
}

const state = { me: undefined, config: null, ocExpiry: 0, feedKind: "" };
const isIOS = /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
const isStandalone = () => matchMedia("(display-mode: standalone)").matches || navigator.standalone === true;

// ---------- router ----------
const routes = {
  "": home, "options": options, "ideas": ideas, "trades": trades, "feed": feed,
  "item": item, "settings": settings, "login": loginView,
};
function go(hash) { if (location.hash !== hash) location.hash = hash; else render(); }

async function render() {
  const [, name = "", arg] = (location.hash || "#/").split("/");
  if (state.me === undefined) {
    try { state.me = await api("/api/me"); } catch { state.me = null; }
  }
  if (!state.me && name !== "login") return go("#/login");
  $("#tabs").classList.toggle("hidden", name === "login");
  document.querySelectorAll("#tabs a").forEach((a) => a.classList.toggle("on", a.dataset.tab === (name || "home")));
  const fn = routes[name] || home;
  try {
    await fn(arg ? decodeURIComponent(arg) : undefined);
  } catch (e) {
    if (e.message !== "signed out") view.innerHTML = `<div class="empty">Could not load this.<br><span class="small">${esc(e.message)}</span></div>`;
  }
}
window.addEventListener("hashchange", () => { window.scrollTo(0, 0); render(); });

$("#refresh").addEventListener("click", async (e) => {
  e.currentTarget.classList.add("spin");
  await render();
  setTimeout(() => $("#refresh").classList.remove("spin"), 300);
});
document.addEventListener("visibilitychange", () => { if (!document.hidden && state.me) render(); });

// ---------- views ----------
async function loginView() {
  view.innerHTML = `
    <div class="login">
      <div class="logo"></div>
      <div class="big">Swing Desk</div>
      <p class="muted">Option chain reads, swing ideas, trade updates and reviews, with notifications.</p>
      <form id="lf">
        <label class="small muted">Your name</label>
        <input type="text" name="name" autocomplete="name" required maxlength="60">
        <label class="small muted">Invite code</label>
        <input type="password" name="code" autocomplete="off" required>
        <div class="err" id="lerr"></div>
        <button class="btn block">Sign in</button>
      </form>
    </div>`;
  $("#lf").addEventListener("submit", async (e) => {
    e.preventDefault();
    const f = new FormData(e.target);
    try {
      await api("/api/login", { method: "POST", body: { name: f.get("name"), code: f.get("code") } });
      state.me = await api("/api/me");
      go("#/");
    } catch (err) { $("#lerr").textContent = err.message; }
  });
}

function itemCard(it) {
  const label = (state.config?.kinds || {})[it.kind] || it.kind;
  return `<a class="card tap" href="#/item/${encodeURIComponent(it.id)}">
    <div class="row"><span class="item-kind k-${esc(it.kind)}">${esc(label)}</span><span class="tiny muted">${esc(ago(it.created_at))}</span></div>
    <div class="item-title">${esc(it.title)}</div>
    ${it.summary ? `<div class="item-sum">${esc(it.summary)}</div>` : ""}
  </a>`;
}

async function banners() {
  let out = "";
  if (!isStandalone()) {
    out += isIOS
      ? `<div class="banner"><p><b>Install on iPhone:</b> tap <b>Share</b> ⎋ then <b>Add to Home Screen</b>, and open the app from that icon to turn on notifications.</p></div>`
      : `<div class="banner"><p><b>Install the app</b> for notifications and full-screen use.</p><button class="btn" id="installBtn">Install</button></div>`;
  }
  if (isStandalone() || !isIOS) {
    const sub = await currentSub();
    if ("Notification" in window && Notification.permission !== "denied" && !sub) {
      out += `<div class="banner"><p>Get a notification for each new list, review, option chain read and trade update.</p><button class="btn" id="notifBtn">Turn on</button></div>`;
    }
  }
  return out;
}

function wireBanners() {
  $("#installBtn")?.addEventListener("click", async () => {
    if (deferredInstall) { deferredInstall.prompt(); deferredInstall = null; }
    else toast("Use your browser menu ⋮ → Install app / Add to Home screen");
  });
  $("#notifBtn")?.addEventListener("click", async () => {
    try { await enablePush(allKinds()); toast("Notifications are on"); render(); } catch (e) { toast(e.message); }
  });
}

async function home() {
  view.innerHTML = skeleton(4);
  const [d, b] = await Promise.all([api("/api/overview"), banners()]);
  const oc = d.oc || {}, tr = d.track_record || {}, nf = d.nifty || {};
  const spot = oc.spot ?? nf.close;
  view.innerHTML = `
    ${b}
    <div class="card">
      <div class="hero">
        <div>
          <div class="small muted">Nifty 50 ${oc.as_of ? "· " + esc(oc.as_of.slice(11, 16)) + " IST" : ""}</div>
          <div class="big num">${fmt(spot)}</div>
        </div>
        <div class="chips">
          ${trendChip("Weekly", oc.trend_weekly)}${trendChip("125m", oc.trend_125m)}${trendChip("25m", oc.trend_25m)}
        </div>
      </div>
      <div class="grid" style="margin-top:14px">
        <div class="stat"><div class="k">Put wall</div><div class="v up">${fmt(oc.put_wall, 0)}</div></div>
        <div class="stat"><div class="k">Call wall</div><div class="v down">${fmt(oc.call_wall, 0)}</div></div>
        <div class="stat"><div class="k">PCR (near)</div><div class="v">${fmt(oc.pcr_near)}</div></div>
        <div class="stat"><div class="k">Max pain</div><div class="v">${fmt(oc.max_pain, 0)}</div></div>
        <div class="stat wide"><div class="k">Implied range to ${esc(oc.expiry || "expiry")}</div><div class="v">${oc.implied_range ? fmt(oc.implied_range[0], 0) + " – " + fmt(oc.implied_range[1], 0) : "–"}</div></div>
      </div>
    </div>

    <h2>Latest</h2>
    ${d.latest.length ? d.latest.map(itemCard).join("") : `<div class="card muted small">Nothing posted yet. Morning lists, reviews and option chain reads will show up here.</div>`}

    <h2>Track record</h2>
    <div class="grid three">
      <div class="stat"><div class="k">Win rate (T1+)</div><div class="v up">${fmt(tr.win_rate_t1_or_better_pct, 1)}%</div></div>
      <div class="stat"><div class="k">Avg closed</div><div class="v ${cls(tr.avg_return_closed_pct)}">${pct(tr.avg_return_closed_pct)}</div></div>
      <div class="stat"><div class="k">Open trades</div><div class="v">${d.open_trades}</div></div>
    </div>

    <h2>Global markets</h2>
    <div class="card">
      ${(d.global?.items || []).map((g) => `<div class="mkt"><div class="name">${esc(String(g.name || "").replace(/\s*\(.*\)$/, ""))}<div class="tiny muted">${esc(g.for_date || "")}</div></div><div class="val">${fmt(g.value)}<span class="tiny ${cls(g.change_pct)}">${pct(g.change_pct)}</span></div></div>`).join("") || '<span class="muted small">No data yet.</span>'}
    </div>

    <p class="tiny muted" style="text-align:center">Data ${esc(d.data_date || "")} · ${esc((d.repo_head || "").split(" ").slice(2).join(" "))}<br>Analysis only, not investment advice.</p>
  `;
  wireBanners();
}

function spark(points) {
  const v = points.map((p) => p.spot).filter((x) => x);
  if (v.length < 2) return "";
  const lo = Math.min(...v), hi = Math.max(...v), w = 300, h = 60, pad = 4;
  const xy = v.map((y, i) => `${(i / (v.length - 1)) * w},${h - pad - ((y - lo) / (hi - lo || 1)) * (h - 2 * pad)}`).join(" ");
  const up = v[v.length - 1] >= v[0];
  return `<svg class="spark" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none"><polyline points="${xy}" fill="none" stroke="var(${up ? "--up" : "--down"})" stroke-width="2" vector-effect="non-scaling-stroke"/></svg>
    <div class="row tiny muted"><span>${esc(points[0].t)} · ${fmt(v[0])}</span><span>${esc(points[points.length - 1].t)} · ${fmt(v[v.length - 1])}</span></div>`;
}

async function options() {
  view.innerHTML = skeleton(4);
  const d = await api("/api/option-chain");
  const L = d.learning || {};
  const exps = L.expiries || [];
  if (!exps.length && !d.chains.length) { view.innerHTML = `<div class="empty">No option chain data yet.</div>`; return; }
  const i = Math.min(state.ocExpiry, Math.max(exps.length, d.chains.length) - 1);
  const e = exps[i] || {};
  const ch = d.chains.find((c) => c.expiry === e.expiry) || d.chains[i] || { strikes: [] };
  const maxOI = Math.max(1, ...ch.strikes.flatMap((s) => [s.ce_oi || 0, s.pe_oi || 0]));
  const atm = ch.strikes.reduce((b, s) => (Math.abs(s.strike - ch.spot) < Math.abs(b - ch.spot) ? s.strike : b), ch.strikes[0]?.strike);
  const verdict = (title, p) => p ? `<div class="verdict"><div class="p">${esc(title)}: ${esc(p.pattern)}</div><div class="t">${esc(p.verdict)}</div>
      ${p.writers ? `<div class="p" style="margin-top:6px">Writers: ${esc(p.writers)}</div><div class="t">${esc(p.writers_verdict)}</div>` : ""}
      ${p.writers_trend_verdict ? `<div class="t" style="margin-top:6px"><b>With trend (${esc(p.trend)}):</b> ${esc(p.writers_trend_verdict)}</div>` : ""}</div>` : "";

  view.innerHTML = `
    <div class="row" style="margin-bottom:10px">
      <div class="seg">${exps.map((x, k) => `<button data-k="${k}" class="${k === i ? "on" : ""}">${esc(x.type)} ${esc((x.expiry || "").slice(5))}</button>`).join("")}</div>
      <span class="tiny muted">${esc((d.snapshot_ist || L.as_of || "").slice(11, 16))} IST</span>
    </div>
    <div class="card">
      <div class="hero"><div><div class="small muted">Spot</div><div class="big num">${fmt(e.spot ?? ch.spot)}</div></div>
        <div class="chips">${trendChip("Weekly", L.trend_weekly)}${trendChip("125m", L.trend_125m)}${trendChip("25m", L.trend_25m)}</div></div>
      <div class="grid" style="margin-top:14px">
        <div class="stat"><div class="k">Put wall</div><div class="v up">${fmt(e.put_wall, 0)}</div></div>
        <div class="stat"><div class="k">Call wall</div><div class="v down">${fmt(e.call_wall, 0)}</div></div>
        <div class="stat"><div class="k">PCR near</div><div class="v">${fmt(e.pcr_near)}</div></div>
        <div class="stat"><div class="k">Max pain</div><div class="v">${fmt(e.max_pain, 0)}</div></div>
        <div class="stat"><div class="k">Days left</div><div class="v">${fmt(e.dte, 1)}</div></div>
        <div class="stat"><div class="k">ATM IV</div><div class="v">${fmt(e.atm_iv, 1)}</div></div>
        <div class="stat wide"><div class="k">Implied move ${pct(e.implied_move_pct)}</div><div class="v">${e.implied_range ? fmt(e.implied_range[0], 0) + " – " + fmt(e.implied_range[1], 0) : "–"}</div></div>
      </div>
    </div>

    ${d.spot_path.length > 1 ? `<h2>Today (${d.snapshots_today} snapshots)</h2><div class="card">${spark(d.spot_path)}</div>` : ""}

    <h2>Pattern read</h2>
    <div class="card">${verdict("Since last snapshot", e.intraday)}${verdict("Since open", e.day)}${!e.intraday && !e.day ? '<span class="muted small">No read yet.</span>' : ""}
      <div class="tiny muted" style="margin-top:8px">Learned from live snapshots since 14 Oct 2026. Analysis only, not advice.</div></div>

    <h2>Open interest near the money</h2>
    <div class="card" style="padding:8px 6px">
      <table class="ladder">
        <thead><tr><th>CE ΔOI</th><th>CE OI</th><th>CE LTP</th><th>Strike</th><th>PE LTP</th><th>PE OI</th><th>PE ΔOI</th></tr></thead>
        <tbody>${ch.strikes.map((s) => `
          <tr class="${s.strike === atm ? "atm" : ""} ${s.strike === e.call_wall ? "wall-c" : ""} ${s.strike === e.put_wall ? "wall-p" : ""}">
            <td class="${cls(s.ce_chg_oi)}">${compact(s.ce_chg_oi)}</td>
            <td><div class="bar ce" style="width:${((s.ce_oi || 0) / maxOI) * 100}%"></div><span>${compact(s.ce_oi)}</span></td>
            <td>${fmt(s.ce_ltp, 1)}</td>
            <td class="strike">${fmt(s.strike, 0)}</td>
            <td>${fmt(s.pe_ltp, 1)}</td>
            <td><div class="bar pe" style="width:${((s.pe_oi || 0) / maxOI) * 100}%"></div><span>${compact(s.pe_oi)}</span></td>
            <td class="${cls(s.pe_chg_oi)}">${compact(s.pe_chg_oi)}</td>
          </tr>`).join("")}</tbody>
      </table>
      <div class="row tiny muted" style="padding:8px 6px 2px"><span>Total CE OI ${compact(ch.total_ce_oi)}</span><span>Total PE OI ${compact(ch.total_pe_oi)}</span></div>
    </div>`;
  view.querySelectorAll(".seg button").forEach((b) => b.addEventListener("click", () => { state.ocExpiry = +b.dataset.k; options(); }));
}

async function ideas() {
  view.innerHTML = skeleton(4);
  const d = await api("/api/ideas");
  const card = (x) => `
    <div class="card">
      <div class="row">
        <div><b>${esc(x.symbol)}</b> <span class="tiny muted">#${esc(x.rank)} · ${esc(x.sector)}</span></div>
        <div class="num">${rs(x.close)} <span class="small ${cls(x.chg_pct)}">${pct(x.chg_pct)}</span></div>
      </div>
      <div class="chips" style="margin-top:6px">
        ${x.eligible ? '<span class="chip up">On the list</span>' : '<span class="chip">Watch only</span>'}
        ${x.entry_style ? `<span class="chip accent">${esc(x.entry_style)}</span>` : ""}
        ${x.warning ? `<span class="chip warn">${esc(x.warning)}</span>` : ""}
      </div>
      <div class="zone">
        <div class="stat"><div class="k">Buy zone</div><div class="v small">${fmt(x.entry_low)}–${fmt(x.entry_high)}</div></div>
        <div class="stat"><div class="k">T1 (+3%)</div><div class="v small up">${fmt(x.t1)}</div></div>
        <div class="stat"><div class="k">T2 (+6%)</div><div class="v small up">${fmt(x.t2)}</div></div>
      </div>
      ${x.zone_status ? `<div class="small ${/above|below/i.test(x.zone_status) ? "warn" : "up"}">${esc(x.zone_status)}</div>` : ""}
      ${!x.eligible && x.not_eligible_because ? `<div class="small muted" style="margin-top:4px">Why not listed: ${esc(x.not_eligible_because)}</div>` : ""}
      <details><summary>Why this setup${x.chart ? " · chart" : ""}</summary>
        <div class="small" style="margin-top:6px">${esc(x.reason)}</div>
        <div class="tiny muted" style="margin-top:6px">Support ${rs(x.support)} (${esc(x.support_kind)}) · resistance ${rs(x.resistance)} · room ${pct(x.room_pct, 1)} · 1M ${pct(x.ret_1m, 1)} · 3M ${pct(x.ret_3m, 1)}</div>
        ${x.chart ? `<img class="chart-img" loading="lazy" src="${esc(x.chart)}" alt="${esc(x.symbol)} chart">` : ""}
      </details>
    </div>`;
  const listed = d.ideas.filter((x) => x.eligible), watch = d.ideas.filter((x) => !x.eligible);
  view.innerHTML = `
    <div class="small muted">Scan of ${esc(d.data_date)} · ${esc(d.stocks_analysed)} stocks · ${esc(d.eligible_count)} on the list</div>
    <h2>On the list</h2>
    ${listed.length ? listed.map(card).join("") : '<div class="card muted small">No stock passed every rule in the last scan.</div>'}
    <h2>Watch list (top ranked, not listed)</h2>
    ${watch.slice(0, 8).map(card).join("")}
    <h2>Value shortlist ${d.value.data_date ? "· " + esc(d.value.data_date) : ""}</h2>
    <div class="card"><div class="table-wrap"><table class="simple">
      <thead><tr><th>Stock</th><th>Score</th><th>ROCE</th><th>Profit CAGR</th><th>P/E</th><th>Off high</th></tr></thead>
      <tbody>${d.value.shortlist.map((v) => `<tr><td><b>${esc(v.symbol)}</b><div class="tiny muted">${esc(v.industry)}</div></td><td>${fmt(v.score, 0)}</td><td>${fmt(v.roce_pct, 1)}%</td><td>${fmt(v.profit_cagr_pct, 1)}%</td><td>${fmt(v.pe, 1)}</td><td class="down">${fmt(v.pct_below_high52, 1)}%</td></tr>`).join("")}</tbody>
    </table></div></div>`;
}

async function trades() {
  view.innerHTML = skeleton(4);
  const d = await api("/api/trades");
  const tr = d.track_record || {};
  const statusChip = (s) => `<span class="chip ${/T2|Full/.test(s) ? "up" : /T1|Partial/.test(s) ? "up" : /Failed/.test(s) ? "down" : /Waiting|Not bought/.test(s) ? "" : "accent"}">${esc(s)}</span>`;
  const row = (p, open) => `
    <div class="card">
      <div class="row"><div><b>${esc(p.symbol)}</b> <span class="tiny muted">listed ${esc(p.list_date)}</span></div>
        <div class="num big ${cls(open ? p.current_pct : p.return_pct)}" style="font-size:18px">${pct(open ? p.current_pct : p.return_pct)}</div></div>
      <div class="row" style="margin-top:4px">${statusChip(p.status)}<span class="tiny muted">${esc(p.last_event)} · ${esc(p.last_event_date)}</span></div>
      <div class="tiny muted" style="margin-top:6px">Zone ${fmt(p.entry_low)}–${fmt(p.entry_high)} · T1 ${fmt(p.t1)} · T2 ${fmt(p.t2)}${p.fill_price ? ` · filled ${fmt(p.fill_price)} on ${esc(p.fill_date)}` : ""}${p.days_held ? ` · day ${fmt(p.days_held, 0)}` : ""}${p.max_dip_pct ? ` · max dip ${pct(p.max_dip_pct, 1)}` : ""}</div>
    </div>`;
  view.innerHTML = `
    <div class="grid">
      <div class="stat"><div class="k">Picks since ${esc(tr.since || "")}</div><div class="v">${fmt(tr.picks, 0)}</div></div>
      <div class="stat"><div class="k">Win rate T1+</div><div class="v up">${fmt(tr.win_rate_t1_or_better_pct, 1)}%</div></div>
      <div class="stat"><div class="k">Full wins T2</div><div class="v up">${fmt(tr.full_win_rate_t2_pct, 1)}%</div></div>
      <div class="stat"><div class="k">Avg closed</div><div class="v ${cls(tr.avg_return_closed_pct)}">${pct(tr.avg_return_closed_pct)}</div></div>
      <div class="stat"><div class="k">Avg max dip</div><div class="v down">${pct(tr.avg_max_dip_closed_pct)}</div></div>
      <div class="stat"><div class="k">Failed</div><div class="v">${fmt(tr.failed, 0)} / ${fmt(tr.closed, 0)}</div></div>
    </div>
    <h2>Open (${d.open.length})</h2>
    ${d.open.map((p) => row(p, true)).join("") || '<div class="card muted small">No open trades.</div>'}
    <h2>Recently closed</h2>
    ${d.closed.map((p) => row(p, false)).join("")}`;
}

async function feed() {
  const kinds = state.config?.kinds || {};
  view.innerHTML = `<div class="chips" id="kinds" style="margin-bottom:12px">
      <button class="chip ${!state.feedKind ? "on" : ""}" data-k="">All</button>
      ${Object.entries(kinds).map(([k, v]) => `<button class="chip ${state.feedKind === k ? "on" : ""}" data-k="${esc(k)}">${esc(v)}</button>`).join("")}
    </div><div id="items">${skeleton(3)}</div>`;
  view.querySelectorAll("#kinds button").forEach((b) => b.addEventListener("click", () => { state.feedKind = b.dataset.k; feed(); }));
  const d = await api("/api/feed?limit=50" + (state.feedKind ? "&kind=" + encodeURIComponent(state.feedKind) : ""));
  $("#items").innerHTML = d.items.length ? d.items.map(itemCard).join("") : `<div class="empty">Nothing here yet.</div>`;
}

async function item(id) {
  view.innerHTML = skeleton(2);
  const it = await api("/api/feed/" + encodeURIComponent(id));
  const label = (state.config?.kinds || {})[it.kind] || it.kind;
  view.innerHTML = `
    <a href="javascript:history.back()" class="small">‹ Back</a>
    <div class="card" style="margin-top:10px">
      <div class="row"><span class="item-kind k-${esc(it.kind)}">${esc(label)}</span><span class="tiny muted">${esc(ago(it.created_at))}</span></div>
      <h1 style="font-size:20px;margin:6px 0 10px">${esc(it.title)}</h1>
      ${it.symbols.length ? `<div class="chips" style="margin-bottom:10px">${it.symbols.map((s) => `<span class="chip accent">${esc(s)}</span>`).join("")}</div>` : ""}
      <div class="prose">${it.body_html}</div>
    </div>
    <p class="tiny muted" style="text-align:center">Analysis only, not investment advice.</p>`;
}

// ---------- push ----------
let deferredInstall = null;
window.addEventListener("beforeinstallprompt", (e) => { e.preventDefault(); deferredInstall = e; });

const allKinds = () => Object.keys(state.config?.kinds || {});
async function swReg() { return "serviceWorker" in navigator ? navigator.serviceWorker.ready : null; }
async function currentSub() {
  try { const r = await swReg(); return r && r.pushManager ? await r.pushManager.getSubscription() : null; } catch { return null; }
}
function keyBytes(b64) {
  const s = atob((b64 + "=".repeat((4 - (b64.length % 4)) % 4)).replace(/-/g, "+").replace(/_/g, "/"));
  return Uint8Array.from(s, (c) => c.charCodeAt(0));
}
async function enablePush(kinds) {
  if (!("PushManager" in window)) throw new Error(isIOS ? "Add the app to your Home Screen first, then open it from there." : "This browser does not support notifications.");
  const perm = await Notification.requestPermission();
  if (perm !== "granted") throw new Error("Notifications were not allowed.");
  const reg = await swReg();
  let sub = await reg.pushManager.getSubscription();
  if (!sub) sub = await reg.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey: keyBytes(state.config.vapid_public_key) });
  await api("/api/push/subscribe", { method: "POST", body: { subscription: sub.toJSON(), kinds } });
}
async function disablePush() {
  const sub = await currentSub();
  if (sub) { await api("/api/push/unsubscribe", { method: "POST", body: { endpoint: sub.endpoint } }); await sub.unsubscribe(); }
}

async function settings() {
  const sub = await currentSub();
  const st = sub ? await api("/api/push/status", { method: "POST", body: { endpoint: sub.endpoint } }) : { subscribed: false, kinds: [] };
  const on = st.subscribed;
  const chosen = st.kinds.length ? st.kinds : allKinds();
  view.innerHTML = `
    <h2>Notifications</h2>
    <div class="card">
      <div class="row"><div><b>${on ? "On for this device" : "Off on this device"}</b><div class="tiny muted">${"Notification" in window ? "Permission: " + Notification.permission : "Not supported here"}</div></div>
        <button class="btn ${on ? "ghost" : ""}" id="tog">${on ? "Turn off" : "Turn on"}</button></div>
      <div style="margin-top:12px">${Object.entries(state.config.kinds).map(([k, v]) => `<label class="check"><input type="checkbox" value="${esc(k)}" ${chosen.includes(k) ? "checked" : ""}> ${esc(v)}</label>`).join("")}</div>
      ${on ? '<button class="btn ghost block" id="test" style="margin-top:10px">Send me a test notification</button>' : ""}
    </div>
    <h2>Install</h2>
    <div class="card small">
      ${isStandalone() ? "Installed and running as an app." : isIOS
        ? `<ol class="steps"><li>Open this page in <b>Safari</b>.</li><li>Tap <b>Share</b>, then <b>Add to Home Screen</b>.</li><li>Open Swing Desk from the new icon and turn on notifications here.</li></ol><span class="muted">Needs iOS 16.4 or newer.</span>`
        : `<ol class="steps"><li>In Chrome, tap the menu ⋮.</li><li>Tap <b>Install app</b> (or <b>Add to Home screen</b>).</li><li>Open Swing Desk from the new icon.</li></ol>`}
    </div>
    <h2>Account</h2>
    <div class="card row"><span>Signed in as <b>${esc(state.me.name)}</b></span><button class="btn ghost" id="out">Sign out</button></div>`;
  const picked = () => [...view.querySelectorAll("label.check input:checked")].map((i) => i.value);
  $("#tog").addEventListener("click", async () => {
    try { on ? await disablePush() : await enablePush(picked()); settings(); } catch (e) { toast(e.message); }
  });
  view.querySelectorAll("label.check input").forEach((i) => i.addEventListener("change", async () => {
    if (on) { await enablePush(picked()); toast("Saved"); }
  }));
  $("#test")?.addEventListener("click", async () => {
    try { const r = await api("/api/push/test", { method: "POST", body: { endpoint: sub.endpoint } }); toast(r.status < 300 ? "Sent. It should arrive in a few seconds." : "Push service answered " + r.status); } catch (e) { toast(e.message); }
  });
  $("#out").addEventListener("click", async () => { await disablePush().catch(() => {}); await api("/api/logout", { method: "POST" }); state.me = null; go("#/login"); });
}

// ---------- boot ----------
(async () => {
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/sw.js").catch(() => {});
    navigator.serviceWorker.addEventListener("message", (e) => { if (e.data?.url) location.href = e.data.url; });
  }
  state.config = await fetch("/api/config").then((r) => r.json()).catch(() => ({ kinds: {} }));
  render();
})();
