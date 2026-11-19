# Sensex option chain pattern log
Updated 2026-11-19 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 2 snapshots over 1 trading days
- 2 patterns logged; 2 different patterns so far

## Latest read (2026-11-19 15:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-19 (weekly) | 0.0 | 83022 | 1.196 | 82900 | 82900 | 83100 | ±0.03% (83000-83044) | 62.5 |
| 2026-11-26 (monthly) | 7.0 | 83022 | 0.92 | 82500 | 80000 | 85000 | ±1.61% (81682-84361) | 14.4 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-19

Strongest call writers at -, strongest put writers at -; weakest call writers at -, weakest put writers at 85000. Covers 0% of near-money call OI and 5% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Put | 83700 | 16400 | 560 | 676.6 | 83022 | 676.6 | 83023 | -2 | +0.0 | weak |
| Put | 83800 | 10060 | 380 | 776.5 | 83022 | 776.5 | 83024 | -2 | +0.0 | weak |

## Strong vs weak writers, monthly 2026-11-26

Strongest call writers at 83000, strongest put writers at 81000; weakest call writers at 80800, weakest put writers at 85000. Covers 19% of near-money call OI and 17% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82400 | 47520 | 500 | 1145.8 | 83022 | 1145.8 | 83546 | +524 | +0.0 | strong |
| Call | 82800 | 102720 | 300 | 860.8 | 83022 | 860.8 | 83661 | +639 | +0.0 | strong |
| Call | 82900 | 79620 | 5400 | 800.0 | 83022 | 800.0 | 83700 | +678 | +0.0 | strong |
| Call | 83000 | 311320 | 54640 | 764.4 | 83022 | 764.4 | 83764 | +743 | +0.0 | strong |
| Call | 83100 | 82840 | 46680 | 707.0 | 83022 | 707.0 | 83807 | +785 | +0.0 | strong |
| Call | 83200 | 48520 | 17760 | 646.0 | 83022 | 646.0 | 83846 | +824 | +0.0 | strong |
| Call | 83300 | 31580 | 9120 | 595.9 | 83022 | 595.9 | 83896 | +874 | +0.0 | strong |
| Call | 83400 | 54960 | 27300 | 560.0 | 83022 | 560.0 | 83960 | +938 | +0.0 | strong |
| Call | 83500 | 133380 | 23560 | 519.6 | 83022 | 519.6 | 84020 | +998 | +0.0 | strong |
| Call | 83600 | 28620 | 10920 | 466.0 | 83022 | 466.0 | 84066 | +1044 | +0.0 | strong |
| Call | 83700 | 25640 | 3260 | 432.6 | 83022 | 432.6 | 84133 | +1111 | +0.0 | strong |
| Call | 83900 | 16660 | 920 | 363.1 | 83022 | 363.1 | 84263 | +1241 | +0.0 | strong |
| Call | 84000 | 175940 | 32260 | 328.0 | 83022 | 328.0 | 84328 | +1306 | +0.0 | strong |
| Call | 84100 | 15020 | 1320 | 306.9 | 83022 | 306.9 | 84407 | +1385 | +0.0 | strong |
| Call | 84200 | 14440 | 320 | 267.1 | 83022 | 267.1 | 84467 | +1445 | +0.0 | strong |
| Put | 82500 | 326540 | 2480 | 383.2 | 83022 | 383.2 | 82117 | +905 | +0.0 | strong |
| Put | 82600 | 44000 | 1580 | 404.6 | 83022 | 404.6 | 82195 | +826 | +0.0 | strong |
| Put | 82700 | 58640 | 4220 | 444.1 | 83022 | 444.1 | 82256 | +766 | +0.0 | strong |
| Put | 82800 | 129940 | 15500 | 493.2 | 83022 | 493.2 | 82307 | +715 | +0.0 | strong |
| Put | 82900 | 53960 | 6100 | 522.5 | 83022 | 522.5 | 82378 | +644 | +0.0 | strong |
| Put | 83000 | 261660 | 56820 | 575.0 | 83022 | 575.0 | 82425 | +597 | +0.0 | strong |
| Put | 83100 | 49260 | 35140 | 611.0 | 83022 | 611.0 | 82489 | +533 | +0.0 | strong |
| Put | 83200 | 20360 | 11100 | 671.0 | 83022 | 671.0 | 82529 | +493 | +0.0 | strong |
| Put | 83300 | 9060 | 2500 | 714.9 | 83022 | 714.9 | 82585 | +437 | +0.0 | strong |
| Put | 83400 | 5740 | 1140 | 771.8 | 83022 | 771.8 | 82628 | +394 | +0.0 | strong |
| Put | 83500 | 19160 | 2720 | 814.5 | 83022 | 814.5 | 82685 | +336 | +0.0 | medium |
| Put | 83600 | 4380 | 1000 | 882.7 | 83022 | 882.7 | 82717 | +304 | +0.0 | medium |
| Put | 83700 | 4620 | 880 | 953.4 | 83022 | 953.4 | 82747 | +275 | +0.0 | medium |
| Put | 83800 | 3720 | 160 | 1063.0 | 83022 | 1063.0 | 82737 | +285 | +0.0 | medium |
| Put | 83900 | 3680 | 320 | 1102.8 | 83022 | 1102.8 | 82797 | +225 | +0.0 | medium |
| Put | 84000 | 16740 | 3160 | 1140.0 | 83022 | 1140.0 | 82860 | +162 | +0.0 | weak |
| Put | 84100 | 620 | 100 | 1270.0 | 83022 | 1270.0 | 82830 | +192 | +0.0 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
