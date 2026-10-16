# Prompts

Exact text of every Claude routine that drives this system, exported from the live routines on
14 Oct 2026. Schedules, models and connectors are in [`routines.json`](routines.json). How it all
fits together: [`docs/FLOW.md`](../docs/FLOW.md).

| File | Schedule (IST, Mon–Fri) | What it does |
|---|---|---|
| `routines/01_morning_price_action_list.txt` | 07:45 | Morning list: research nodes, skip rules, email |
| `routines/02_option_chain_snapshot.txt` | 09:15–15:15 hourly | Starts `option_chain.yml` |
| `routines/03_dashboard_refresh_after_snapshot.txt` | 09:50–15:50 hourly | Rebuilds the dashboard |
| `routines/04_option_chain_patterns.txt` | 09:55–15:55 hourly | Starts `oc_learn.yml`, reports new leans at 15:55 |
| `routines/05_dashboard_refresh.txt` | 08:05, 10:05–16:05 hourly, 19:05 | Rebuilds the dashboard |
| `routines/06_daily_data_run.txt` | 18:45 | Starts `daily.yml` |
| `routines/07_trade_review_trigger.txt` | 19:28 | Tells the run to read the trade review file |
| `routines/07_trade_review.txt` | (read by the 19:28 run) | Full evening trade review prompt |
| `routines/08_friday_value_pick.txt` | Fri 19:45 | Starts `value_scan.yml`, screens for manipulation and promoter quality, one Full teardown |
| `routines/disabled/setup_teardown.txt` | was 19:45, disabled 8 Oct | Red-flag screen + one-stock teardown |
| `routines/disabled/one_time_*.txt` | one-off, already fired | Test and check-in runs from 30 Sep |
| `history/morning_list_*.txt` | — | Earlier versions of the morning prompt |

Email addresses are replaced with `<YOUR_EMAIL>`, `<SECOND_EMAIL>` and `<SENDER_GMAIL>` because
the repo is public. Put your own back before running a prompt.
