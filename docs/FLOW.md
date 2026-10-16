# NSE swing system: the full flow, end to end

Snapshot of everything that runs, as of 14 Oct 2026. Use it to rebuild or backtest the system locally.

The system has two halves:

- **Code** (this repo, run by GitHub Actions): downloads prices, scores setups, draws charts,
  tracks every pick, snapshots the Nifty option chain and learns option-chain patterns.
  Deterministic; you can run all of it locally with Python.
- **LLM routines** (Claude scheduled routines): read the code's output files, do web research,
  apply skip rules, write the morning list / evening review emails and refresh the dashboard.
  Their exact prompts are in [`prompts/routines/`](../prompts/routines/), with schedules and
  settings in [`prompts/routines.json`](../prompts/routines.json).

Claude routines only *start* the GitHub workflows (via `workflow_dispatch`); the workflows have no
`schedule:` of their own.

## Daily timeline (IST, Mon–Fri)

| Time | Who | What | Prompt / code |
|---|---|---|---|
| 07:45 | Claude routine "NSE Price Action List" | Starts `daily.yml` in `global_only` mode, reads `latest.csv` + `picks_log.csv` + fresh `global.json`, builds skip list, runs 3 research nodes (fundamentals, events, global), quick screen, sends the morning email + app message | [`01_morning_price_action_list.txt`](../prompts/routines/01_morning_price_action_list.txt) |
| 08:05 | Claude routine | Dashboard refresh | [`05_dashboard_refresh.txt`](../prompts/routines/05_dashboard_refresh.txt) |
| 09:15 … 15:15 hourly | Claude routine | Starts `option_chain.yml` (snapshot now + 30 min later → :15 and :45) | [`02_option_chain_snapshot.txt`](../prompts/routines/02_option_chain_snapshot.txt) |
| 09:50 … 15:50 hourly | Claude routine | Dashboard refresh after the :45 snapshot | [`03_dashboard_refresh_after_snapshot.txt`](../prompts/routines/03_dashboard_refresh_after_snapshot.txt) |
| 09:55 … 15:55 hourly | Claude routine | Starts `oc_learn.yml`; at 15:55 reports any new pattern with a lean and ≥ 20 outcomes | [`04_option_chain_patterns.txt`](../prompts/routines/04_option_chain_patterns.txt) |
| 10:05 … 16:05 hourly | Claude routine | Dashboard refresh | [`05_dashboard_refresh.txt`](../prompts/routines/05_dashboard_refresh.txt) |
| 18:45 | Claude routine | Starts `daily.yml` (full run: global numbers, scan, charts, tracker, feedback) | [`06_daily_data_run.txt`](../prompts/routines/06_daily_data_run.txt) |
| 19:05 | Claude routine | Dashboard refresh | [`05_dashboard_refresh.txt`](../prompts/routines/05_dashboard_refresh.txt) |
| 19:28 | Claude routine "NSE Trade Review" | Reads `feedback.json`, `picks_log.csv`, `pick_features.csv`, past reviews; explains the day's results, keeps lessons, proposes (never applies) rule changes; sends the review email | trigger: [`07_trade_review_trigger.txt`](../prompts/routines/07_trade_review_trigger.txt) → full prompt: [`07_trade_review.txt`](../prompts/routines/07_trade_review.txt) |
| Fri 19:45 | Claude routine "Friday value pick" | Starts `value_scan.yml`, waits for `data/value/`, screens the shortlist for manipulation and promoter quality, emails one Full teardown of a long-term mid/small-cap idea (never feeds the morning list) | [`08_friday_value_pick.txt`](../prompts/routines/08_friday_value_pick.txt) |
| ~~19:45~~ | **Disabled** since 8 Oct 2026 | Evening red-flag screen + one-stock forensic teardown (its emails still feed the morning list's skip rules for 20 trading days) | [`disabled/setup_teardown.txt`](../prompts/routines/disabled/setup_teardown.txt) |

## Code: GitHub workflows and scripts

### `value_scan.yml` — "Weekly value screen" (started Fridays 19:45 by the Friday value pick)

`value_scan.py`: Nifty Midcap 150 + Smallcap 250, ₹2,000–40,000 cr, annual numbers from Yahoo Finance. Passes = ROCE > 15% (ROE for lenders), 3-year sales and profit CAGR > 15%, D/E < 0.5, 3-year CFO ≥ 70% of profit, P/E below its own 4-year-end median or its industry median. Writes `data/value/latest.csv`, `shortlist.csv` and `meta.json`. Never touches the swing data.

### `daily.yml` — "Daily NSE data" (started 18:45, and 07:45 in global-only mode)

1. `global_data.py` → `data/global.json`. S&P 500, Nasdaq, Nikkei, Hang Seng, Brent, USD/INR,
   US 10-yr (yfinance, CNBC quote JSON as a second feed, US Treasury CSV), NSE provisional FII/DII.
   Failures never stop the run.
2. `scan_data.py` (skipped when `global_only`) → `data/latest.csv`, `data/meta.json`,
   `data/picks_log.csv`, `data/charts/<date>/<SYMBOL>.png`, and (newer code, not yet on main's data) `data/sector_map.csv`, `data/near_miss_log.csv`.
   - Universe: NSE F&O + Nifty Midcap 150 + any NSE EQ stock with 20-day avg traded value ≥ ₹50 cr;
     ETFs excluded; stocks with a running bought pick marked not eligible.
   - Prices: Yahoo Finance via yfinance (2 years daily). NSE archives for F&O list, ban list,
     ASM/GSM, price bands, index constituents, sectors.
   - Rules (support trades only since 8 Oct 2026, support from **weekly** candles): A uptrend,
     C pullback to support, D retest, E candle at support (hammer graded 0–100), W weekly reversal,
     F room to run ≥ 6% (required), G relative strength vs Nifty, volume ≥ 1.5× 20-day avg.
     Score → rank. Entry zone, T1 = +3%, T2 = +6% from top of zone, 30-day time exit, no stop-loss.
   - `charts.py` draws the annotated PNG for the top 12 eligible.
   - Tracker: every listed pick is replayed on daily prices (fill in 3 sessions, T1/T2/time exit) in
     `picks_log.csv`; `meta.json.track_record` summarises it.
   - `SCAN_END=YYYY-MM-DD` (workflow input `scan_end`) re-runs a past day with prices up to that date.
3. `feedback.py` (skipped when `global_only`) → `data/pick_features.csv` (listing-day setup of each
   pick), `data/feedback.json` (today's events, group stats, signals, completed trades,
   missed entries, near misses).
4. Commits `data/` to main ("Data update …").

### `option_chain.yml` — "Nifty option chain" (started hourly 09:15–15:15)

`option_chain.py` reads NSE's option chain API for the weekly and monthly Nifty expiry and appends
one row per strike to `data/option_chain/<date>.csv` (spot, CE/PE LTP, OI, ΔOI, IV, volume, with
`nse_time`). Takes a second snapshot after `sleep 1800`. `.github/save_option_chain.sh` commits with
retries on a fresh copy of main.

### `oc_learn.yml` — "Nifty option chain patterns" (started hourly 09:55–15:55)

`oc_learn.py` turns each snapshot into a pattern label (near-money PCR change, put vs call writing,
wall moves, spot between walls, writer strength), records what Nifty did afterwards (intraday close,
next day, to expiry) and writes `data/oc_learning/pattern_log.csv`, `pattern_library.csv`,
`latest.json`, `report.md`, `writers/`. Learns forward only from 14 Oct 2026.

## LLM routines: what each step needs

| Routine | Reads | Uses web / tools | Writes / sends |
|---|---|---|---|
| Morning list | `meta.json`, `latest.csv`, `picks_log.csv`, `global.json` (fresh clone), Gmail search for teardown emails (skip rules), chart PNG URLs | Agent tool for 3 parallel nodes; WebSearch/WebFetch on the trusted-sources list only; Playwright to check email width | Gmail email to 2 recipients, app message |
| Trade review | `meta.json`, `feedback.json`, `picks_log.csv`, `pick_features.csv`, past "Trade review" emails in Gmail | Optional web research (trusted sources) | Email (to you, bcc second recipient), thread reply |
| Option chain / patterns / daily data | — | GitHub `workflow_dispatch` | Starts workflows only |
| Dashboard refresh | Repo checkout + newest lessons file (`/mnt/project-files/nse-swing/reviews/`, written in a project thread; copy in [`docs/lessons/`](lessons/)) | Artifact publish | Runs [`dashboard/build.py`](../dashboard/build.py) with [`dashboard/template.html`](../dashboard/template.html) |
| Friday value pick | `data/value/meta.json`, `shortlist.csv`, `latest.csv`, past "Friday value pick" emails (12-week no-repeat) | Sub-agents, web research (trusted sources), Playwright | Email (to you, bcc second recipient) + app message |
| Teardown (disabled) | `meta.json`, `latest.csv`, Gmail | Sub-agents, web research, Playwright | Email + app message |

## Data files (all in `data/`)

| File | Made by | Overwritten daily? | Notes |
|---|---|---|---|
| `latest.csv` | scan_data.py | yes | 70 columns: patterns, score, rank, eligible, entry/T1/T2, support/resistance, flags, warning, sector, chart path |
| `meta.json` | scan_data.py | yes | data_date, universe stats, Nifty context, ban/ASM lists, track_record |
| `picks_log.csv` | scan_data.py | appended + updated | every pick ever listed and its simulated outcome |
| `pick_features.csv` | feedback.py | appended | listing-day setup per pick |
| `feedback.json` | feedback.py | yes | evening review input |
| `global.json` | global_data.py | yes | morning/evening global numbers |
| `charts/<date>/*.png` | charts.py | new folder per day | |
| `option_chain/<date>.csv` | option_chain.py | new file per day | 30-minute snapshots |
| `oc_learning/*` | oc_learn.py | rebuilt each run | pattern log and library |

Every daily version of `latest.csv`, `meta.json` and `global.json` is in git history, so past days can
be recovered with `git log --format='%h %s' -- data/latest.csv` and `git show <sha>:data/latest.csv`.

## Backtesting locally

1. `pip install yfinance pandas numpy requests matplotlib`
2. Re-create any past day's list: `SCAN_END=2026-10-01 python scan_data.py` (prices up to, not
   including, that date). NSE archive files (F&O list, ban list, ASM/GSM, constituents) are fetched
   *today*, not as of that date, so the universe and warnings are approximate for old days.
   Or use the exact `latest.csv` that was produced that day from git history.
3. Outcomes: `picks_log.csv` + `feedback.py` already simulate fills, T1/T2 and the 30-day exit
   from daily prices. That is the code-only backtest; no LLM is needed.
4. LLM layer: feed the morning prompt the files from step 2. It also depends on things you
   cannot replay exactly: live web research (results dates, SEBI orders, news), Gmail history
   (teardown verdicts and evening red-flag screens drive the skip rules), and the date logic in
   STEP 0. For a local backtest, either stub those (e.g. give each node a saved JSON) or drop the
   skip rules and compare.
5. Option chain: only forward data exists (from 14 Oct 2026); there is no historical backtest of it.

## What was redacted

The repo is public, so in all committed prompts the email addresses are replaced by
`<YOUR_EMAIL>`, `<SECOND_EMAIL>` (second recipient) and `<SENDER_GMAIL>` (connected Gmail
account). Everything else is the exact live text.

## Where the live copies are

- Live prompts: Claude routines (source of truth; exported here on 14 Oct 2026).
- The trade review routine reads `/mnt/project-files/nse-swing/routine-prompts/trade_review.txt`
  at run time; that file is identical to `routine-prompts/current/trade_review.txt` and to
  [`prompts/routines/07_trade_review.txt`](../prompts/routines/07_trade_review.txt).
- The live morning list prompt is identical to `routine-prompts/current/morning_list_*.txt` in the
  project files (only a trailing newline differs). Older versions are in
  [`prompts/history/`](../prompts/history/).
- `dashboard/build.py` reads the newest lessons file from `/mnt/project-files/nse-swing/reviews/`;
  locally, point that glob at `docs/lessons/`.
- The project-files copy of `scan_data.py` is older than the one in this repo; the repo's is the one
  the workflow runs.
- [`docs/runbook_2026-09-30.md`](runbook_2026-09-30.md) is the original setup runbook (rules,
  scoring, issue history). Parts are out of date (breakouts were dropped on 8 Oct, teardown disabled).
