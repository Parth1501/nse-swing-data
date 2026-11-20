# Sensex option chain pattern log
Updated 2026-11-20 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 4 snapshots over 2 trading days
- 5 patterns logged; 5 different patterns so far

## Latest read (2026-11-20 09:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 6.2 | 83023 | 0.874 | 82600 | 82500 | 85000 | ±1.62% (81679-84366) | 15.46 |
| 2026-12-31 (monthly) | 41.2 | 83023 | 0.839 | 82000 | 82000 | 83500 | ±3.75% (79911-86134) | 13.91 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put and call writing · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before. Too few outcomes (0/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before. Too few outcomes (0/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.00%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 100% of the time, average +0.00%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 82800, strongest put writers at 82500; weakest call writers at 81800, weakest put writers at 85000. Covers 58% of near-money call OI and 55% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 81800 | 9640 | 900 | 1398.0 | 83023 | 1398.0 | 83198 | +175 | +0.0 | weak |
| Call | 81900 | 11840 | 620 | 1310.0 | 83023 | 1310.0 | 83210 | +187 | +0.0 | medium |
| Call | 82000 | 136960 | 27700 | 1250.0 | 83023 | 1250.0 | 83250 | +227 | +0.0 | medium |
| Call | 82100 | 20600 | 5140 | 1167.0 | 83023 | 1167.0 | 83267 | +244 | +0.0 | medium |
| Call | 82200 | 30400 | 2220 | 1110.0 | 83023 | 1110.0 | 83310 | +287 | +0.0 | medium |
| Call | 82300 | 42940 | 3060 | 1038.4 | 83023 | 1038.4 | 83338 | +316 | +0.0 | medium |
| Call | 82400 | 59120 | 12100 | 976.5 | 83023 | 969.1 | 83376 | +354 | +7.3 | medium |
| Call | 82500 | 468720 | 178100 | 908.5 | 83022 | 908.7 | 83408 | +386 | -0.2 | strong |
| Call | 82600 | 112020 | 84340 | 847.5 | 83023 | 847.5 | 83448 | +425 | +0.0 | strong |
| Call | 82700 | 160680 | 125080 | 791.0 | 83023 | 791.0 | 83491 | +468 | +0.0 | strong |
| Call | 82800 | 371180 | 269239 | 733.2 | 83023 | 733.1 | 83533 | +511 | +0.1 | strong |
| Call | 82900 | 241640 | 167457 | 686.8 | 83023 | 683.0 | 83587 | +564 | +3.8 | strong |
| Call | 83000 | 504680 | 248445 | 663.3 | 83022 | 634.9 | 83663 | +641 | +28.4 | strong |
| Call | 83100 | 147940 | 111780 | 636.7 | 83020 | 587.5 | 83737 | +714 | +49.3 | strong |
| Call | 83200 | 113640 | 82893 | 563.7 | 83022 | 541.3 | 83764 | +741 | +22.4 | strong |
| Call | 83300 | 89780 | 67320 | 513.7 | 83020 | 501.6 | 83814 | +791 | +12.1 | strong |
| Call | 83400 | 110860 | 83200 | 493.1 | 83020 | 461.5 | 83893 | +871 | +31.6 | strong |
| Call | 83500 | 210300 | 100480 | 446.2 | 83017 | 425.4 | 83946 | +924 | +20.8 | strong |
| Call | 83600 | 61920 | 44245 | 409.5 | 83022 | 391.0 | 84009 | +987 | +18.5 | strong |
| Call | 83700 | 95900 | 74079 | 363.1 | 83023 | 360.0 | 84063 | +1041 | +3.1 | strong |
| Call | 83800 | 81300 | 55200 | 326.3 | 83022 | 326.5 | 84126 | +1104 | -0.2 | strong |
| Call | 83900 | 61580 | 45840 | 300.9 | 83021 | 299.9 | 84201 | +1178 | +1.0 | strong |
| Call | 84000 | 332640 | 188960 | 281.6 | 83017 | 273.2 | 84282 | +1259 | +8.4 | strong |
| Call | 84100 | 47860 | 34160 | 248.8 | 83016 | 247.6 | 84349 | +1326 | +1.3 | strong |
| Call | 84200 | 52640 | 38520 | 226.8 | 83015 | 227.4 | 84427 | +1404 | -0.6 | strong |
| Put | 81800 | 79900 | 46460 | 265.1 | 83023 | 265.1 | 81535 | +1488 | +0.0 | strong |
| Put | 81900 | 59740 | 26660 | 289.9 | 83023 | 289.9 | 81610 | +1412 | +0.0 | strong |
| Put | 82000 | 430660 | 182120 | 317.0 | 83023 | 317.0 | 81683 | +1340 | +0.0 | strong |
| Put | 82100 | 84060 | 33320 | 344.5 | 83023 | 344.5 | 81756 | +1267 | +0.0 | strong |
| Put | 82200 | 124020 | 30760 | 374.4 | 83023 | 374.4 | 81826 | +1197 | +0.0 | strong |
| Put | 82300 | 113180 | 53660 | 409.8 | 83023 | 409.8 | 81890 | +1132 | +0.0 | strong |
| Put | 82400 | 178580 | 117580 | 442.6 | 83023 | 442.6 | 81957 | +1065 | +0.0 | strong |
| Put | 82500 | 662360 | 338300 | 481.5 | 83022 | 481.9 | 82018 | +1004 | -0.4 | strong |
| Put | 82600 | 181380 | 139365 | 517.2 | 83023 | 518.5 | 82083 | +940 | -1.3 | strong |
| Put | 82700 | 245980 | 192154 | 561.4 | 83023 | 564.0 | 82139 | +884 | -2.6 | strong |
| Put | 82800 | 374600 | 266572 | 601.2 | 83023 | 607.5 | 82199 | +824 | -6.3 | strong |
| Put | 82900 | 153500 | 105640 | 648.8 | 83022 | 656.3 | 82251 | +771 | -7.5 | strong |
| Put | 83000 | 327400 | 123296 | 647.2 | 83022 | 708.5 | 82353 | +670 | -61.4 | strong |
| Put | 83100 | 56600 | 42480 | 641.1 | 83015 | 762.5 | 82459 | +564 | -121.4 | strong |
| Put | 83200 | 27780 | 18520 | 726.7 | 83021 | 808.6 | 82473 | +549 | -81.9 | strong |
| Put | 83300 | 13980 | 7420 | 824.1 | 83015 | 873.9 | 82476 | +547 | -49.7 | strong |
| Put | 83400 | 19860 | 15260 | 924.3 | 83023 | 936.6 | 82476 | +547 | -12.3 | strong |
| Put | 83500 | 33740 | 17300 | 965.9 | 83019 | 991.8 | 82534 | +488 | -25.9 | strong |
| Put | 83600 | 7860 | 4480 | 1039.8 | 83005 | 1074.5 | 82560 | +462 | -34.8 | strong |
| Put | 83700 | 5860 | 2120 | 1061.9 | 83018 | 1134.3 | 82638 | +384 | -72.4 | strong |
| Put | 83800 | 5320 | 1760 | 1189.1 | 83022 | 1201.8 | 82611 | +412 | -12.6 | strong |
| Put | 83900 | 4540 | 1180 | 1232.9 | 83022 | 1281.3 | 82667 | +355 | -48.4 | medium |
| Put | 84000 | 17980 | 4400 | 1199.5 | 83016 | 1335.0 | 82801 | +222 | -135.5 | medium |
| Put | 84100 | 1720 | 1200 | 1524.3 | 83023 | 1547.4 | 82576 | +447 | -23.1 | strong |
| Put | 84200 | 1340 | 1220 | 1624.0 | 83023 | 1624.0 | 82576 | +447 | +0.0 | strong |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 83000, strongest put writers at 82000; weakest call writers at -, weakest put writers at -. Covers 23% of near-money call OI and 24% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82000 | 2980 | 20 | 2100.0 | 83023 | 2100.0 | 84100 | +1077 | +0.0 | strong |
| Call | 82200 | 140 | 100 | 2124.2 | 83023 | 2124.2 | 84324 | +1302 | +0.0 | strong |
| Call | 82300 | 100 | 100 | 2134.5 | 83023 | 2134.5 | 84434 | +1412 | +0.0 | strong |
| Call | 82400 | 100 | 100 | 2074.4 | 83023 | 2074.4 | 84474 | +1452 | +0.0 | strong |
| Call | 82800 | 320 | 100 | 1766.7 | 83023 | 1766.7 | 84567 | +1544 | +0.0 | strong |
| Call | 83000 | 1600 | 560 | 1711.9 | 83023 | 1711.9 | 84712 | +1689 | +0.0 | strong |
| Call | 83100 | 200 | 100 | 1607.8 | 83023 | 1607.8 | 84708 | +1685 | +0.0 | strong |
| Call | 83400 | 220 | 200 | 1484.0 | 83023 | 1484.0 | 84884 | +1861 | +0.0 | strong |
| Call | 83500 | 700 | 140 | 1462.5 | 83023 | 1462.5 | 84962 | +1940 | +0.0 | strong |
| Call | 84000 | 20 | 20 | 1219.0 | 83023 | 1219.0 | 85219 | +2196 | +0.0 | strong |
| Call | 84200 | 40 | 20 | 1132.7 | 83023 | 1132.7 | 85333 | +2310 | +0.0 | strong |
| Put | 82000 | 3540 | 440 | 1100.2 | 83023 | 1100.2 | 80900 | +2123 | +0.0 | strong |
| Put | 82700 | 20 | 20 | 1309.8 | 83023 | 1309.8 | 81390 | +1632 | +0.0 | strong |
| Put | 82800 | 20 | 20 | 1354.2 | 83023 | 1354.2 | 81446 | +1577 | +0.0 | strong |
| Put | 82900 | 60 | 60 | 1400.3 | 83023 | 1400.3 | 81500 | +1523 | +0.0 | strong |
| Put | 83000 | 940 | 20 | 1400.0 | 83023 | 1400.0 | 81600 | +1423 | +0.0 | strong |
| Put | 83100 | 100 | 100 | 1467.3 | 83023 | 1467.3 | 81633 | +1390 | +0.0 | strong |
| Put | 83200 | 160 | 160 | 1540.9 | 83023 | 1540.9 | 81659 | +1363 | +0.0 | strong |
| Put | 83300 | 200 | 200 | 1565.7 | 83023 | 1565.7 | 81734 | +1288 | +0.0 | strong |
| Put | 83400 | 40 | 40 | 1607.4 | 83023 | 1607.4 | 81793 | +1230 | +0.0 | strong |
| Put | 83500 | 880 | 400 | 1720.0 | 83023 | 1720.0 | 81780 | +1243 | +0.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 2 |  |  | too few (0/10) |
| intraday | weekly | call writers stronger · weak puts | 1 | 100% | +0.57% | too few (1/10) |
| intraday | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 2 | 100% | +0.00% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +0.00% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 |  |  | too few (0/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 | 100% | +0.57% | too few (1/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.00% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +0.00% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
