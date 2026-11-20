# Sensex option chain pattern log
Updated 2026-11-20 11:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 8 snapshots over 2 trading days
- 13 patterns logged; 11 different patterns so far

## Latest read (2026-11-20 11:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 6.2 | 83203 | 0.924 | 82800 | 82500 | 86000 | ±1.55% (81916-84490) | 14.92 |
| 2026-12-31 (monthly) | 41.2 | 83203 | 1.257 | 83000 | 83000 | 87900 | ±3.71% (80116-86291) | 13.72 |

- **Weekly, last 30 min**: `PCR flat · put and call writing · walls same · near put wall`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.10%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 100% of the time, average +0.15%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 4 times before; Sensex was up after it 100% of the time, average +0.15%. Too few outcomes (4/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.10%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 100% of the time, average +0.10%. Too few outcomes (1/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `put writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 83200, strongest put writers at 82500; weakest call writers at 82000, weakest put writers at 85000. Covers 68% of near-money call OI and 65% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82000 | 137860 | 32398 | 1269.2 | 83038 | 1424.6 | 83269 | +66 | -155.3 | weak |
| Call | 82100 | 19000 | 4921 | 1170.8 | 83027 | 1355.0 | 83271 | +68 | -184.2 | weak |
| Call | 82200 | 27600 | 2016 | 1110.0 | 83023 | 1273.0 | 83310 | +107 | -163.0 | weak |
| Call | 82300 | 35420 | 2524 | 1038.4 | 83023 | 1193.3 | 83338 | +135 | -154.9 | weak |
| Call | 82400 | 41600 | 8514 | 976.5 | 83023 | 1124.7 | 83376 | +173 | -148.2 | weak |
| Call | 82500 | 398060 | 151251 | 908.5 | 83022 | 1058.1 | 83408 | +205 | -149.6 | medium |
| Call | 82600 | 92400 | 69677 | 848.4 | 83024 | 985.7 | 83448 | +245 | -137.3 | medium |
| Call | 82700 | 116320 | 90548 | 791.0 | 83023 | 922.2 | 83491 | +288 | -131.2 | medium |
| Call | 82800 | 275760 | 200058 | 733.3 | 83023 | 861.0 | 83533 | +330 | -127.6 | medium |
| Call | 82900 | 211020 | 148861 | 688.0 | 83022 | 799.9 | 83588 | +385 | -111.8 | strong |
| Call | 83000 | 518780 | 305622 | 662.5 | 83020 | 743.0 | 83662 | +459 | -80.5 | strong |
| Call | 83100 | 310400 | 274240 | 633.5 | 83044 | 689.6 | 83734 | +530 | -56.0 | strong |
| Call | 83200 | 340240 | 309493 | 597.4 | 83092 | 639.5 | 83797 | +594 | -42.1 | strong |
| Call | 83300 | 216600 | 196206 | 540.8 | 83064 | 591.1 | 83841 | +638 | -50.3 | strong |
| Call | 83400 | 133360 | 106104 | 501.7 | 83048 | 543.0 | 83902 | +699 | -41.2 | strong |
| Call | 83500 | 286460 | 176640 | 458.5 | 83055 | 501.3 | 83958 | +755 | -42.8 | strong |
| Call | 83600 | 103360 | 87521 | 424.1 | 83067 | 460.9 | 84024 | +821 | -36.9 | strong |
| Call | 83700 | 108980 | 88588 | 373.9 | 83052 | 421.2 | 84074 | +871 | -47.4 | strong |
| Call | 83800 | 101540 | 76713 | 341.0 | 83054 | 386.3 | 84141 | +938 | -45.3 | strong |
| Call | 83900 | 85620 | 73000 | 311.9 | 83038 | 353.4 | 84212 | +1009 | -41.5 | strong |
| Call | 84000 | 354100 | 217345 | 288.4 | 83048 | 322.2 | 84288 | +1085 | -33.9 | strong |
| Call | 84100 | 78240 | 64540 | 266.0 | 83073 | 292.9 | 84366 | +1163 | -26.9 | strong |
| Call | 84200 | 72680 | 58560 | 237.0 | 83048 | 266.4 | 84437 | +1234 | -29.4 | strong |
| Call | 84300 | 108740 | 93787 | 225.2 | 83101 | 242.2 | 84525 | +1322 | -17.0 | strong |
| Call | 84400 | 62780 | 46730 | 193.9 | 83032 | 219.7 | 84594 | +1391 | -25.8 | strong |
| Put | 82000 | 503440 | 254900 | 303.9 | 83046 | 233.2 | 81696 | +1507 | +70.7 | strong |
| Put | 82100 | 101580 | 52642 | 328.8 | 83045 | 255.2 | 81771 | +1432 | +73.5 | strong |
| Put | 82200 | 158640 | 65380 | 347.4 | 83066 | 279.2 | 81853 | +1351 | +68.2 | strong |
| Put | 82300 | 140220 | 80700 | 384.9 | 83064 | 305.0 | 81915 | +1288 | +79.9 | strong |
| Put | 82400 | 183440 | 123231 | 440.4 | 83025 | 333.9 | 81960 | +1244 | +106.4 | strong |
| Put | 82500 | 673860 | 353846 | 479.1 | 83025 | 363.9 | 82021 | +1182 | +115.2 | strong |
| Put | 82600 | 187120 | 145637 | 516.1 | 83023 | 395.6 | 82084 | +1119 | +120.4 | strong |
| Put | 82700 | 251980 | 199418 | 560.0 | 83023 | 431.8 | 82140 | +1063 | +128.2 | strong |
| Put | 82800 | 403620 | 298213 | 594.2 | 83031 | 470.6 | 82206 | +997 | +123.6 | strong |
| Put | 82900 | 228380 | 181291 | 637.2 | 83030 | 509.6 | 82263 | +940 | +127.5 | strong |
| Put | 83000 | 544420 | 340316 | 642.7 | 83062 | 554.0 | 82357 | +846 | +88.7 | strong |
| Put | 83100 | 218020 | 203900 | 664.6 | 83089 | 596.2 | 82435 | +768 | +68.4 | strong |
| Put | 83200 | 172020 | 162760 | 702.7 | 83124 | 647.6 | 82497 | +706 | +55.1 | strong |
| Put | 83300 | 71920 | 65360 | 762.7 | 83119 | 697.2 | 82537 | +666 | +65.5 | strong |
| Put | 83400 | 38860 | 34260 | 872.5 | 83070 | 752.0 | 82528 | +676 | +120.5 | strong |
| Put | 83500 | 64940 | 48500 | 900.2 | 83101 | 805.9 | 82600 | +603 | +94.3 | strong |
| Put | 83600 | 12560 | 9180 | 1012.3 | 83038 | 868.1 | 82588 | +616 | +144.2 | strong |
| Put | 83700 | 14120 | 10380 | 1009.4 | 83115 | 926.8 | 82691 | +513 | +82.6 | strong |
| Put | 83800 | 13520 | 9960 | 1076.5 | 83117 | 992.8 | 82723 | +480 | +83.8 | strong |
| Put | 83900 | 7740 | 4380 | 1150.2 | 83117 | 1059.3 | 82750 | +453 | +90.9 | strong |
| Put | 84000 | 27480 | 13900 | 1215.6 | 83082 | 1131.8 | 82784 | +419 | +83.8 | strong |
| Put | 84100 | 3700 | 3180 | 1375.9 | 83090 | 1174.0 | 82724 | +479 | +201.9 | strong |
| Put | 84200 | 2100 | 1980 | 1527.6 | 83062 | 1270.0 | 82672 | +531 | +257.6 | strong |
| Put | 84300 | 1520 | 151 | 1644.4 | 83057 | 1325.2 | 82656 | +548 | +319.3 | strong |
| Put | 84400 | 720 | 701 | 1745.3 | 83038 | 1424.0 | 82655 | +548 | +321.3 | strong |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 83000, strongest put writers at 83000; weakest call writers at -, weakest put writers at -. Covers 58% of near-money call OI and 65% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82000 | 3340 | 380 | 2400.4 | 83014 | 2584.4 | 84400 | +1197 | -184.0 | strong |
| Call | 82200 | 140 | 100 | 2124.2 | 83023 | 2124.2 | 84324 | +1121 | +0.0 | strong |
| Call | 82300 | 100 | 100 | 2134.5 | 83023 | 2134.5 | 84434 | +1231 | +0.0 | strong |
| Call | 82400 | 100 | 100 | 2074.4 | 83023 | 2074.4 | 84474 | +1271 | +0.0 | strong |
| Call | 82800 | 320 | 100 | 1766.7 | 83023 | 1766.7 | 84567 | +1363 | +0.0 | strong |
| Call | 83000 | 2360 | 1333 | 1828.4 | 83118 | 1938.8 | 84828 | +1625 | -110.4 | strong |
| Call | 83100 | 80 | 40 | 1607.8 | 83023 | 1786.2 | 84708 | +1505 | -178.4 | strong |
| Call | 83300 | 40 | 40 | 1653.3 | 83117 | 1653.3 | 84953 | +1750 | +0.0 | strong |
| Call | 83400 | 140 | 127 | 1484.0 | 83023 | 1678.0 | 84884 | +1681 | -194.1 | strong |
| Call | 83500 | 1040 | 496 | 1597.5 | 83150 | 1651.5 | 85098 | +1894 | -54.0 | strong |
| Call | 83600 | 60 | 60 | 1556.7 | 83166 | 1615.7 | 85157 | +1953 | -59.0 | strong |
| Call | 83700 | 140 | 140 | 1548.3 | 83203 | 1548.3 | 85248 | +2045 | +0.0 | strong |
| Call | 83800 | 60 | 60 | 1439.0 | 83195 | 1451.0 | 85239 | +2036 | -12.1 | strong |
| Call | 83900 | 540 | 500 | 1403.7 | 83178 | 1407.8 | 85304 | +2101 | -4.0 | strong |
| Call | 84000 | 1000 | 1000 | 1347.6 | 83157 | 1354.8 | 85348 | +2144 | -7.2 | strong |
| Call | 84100 | 20 | 20 | 1280.8 | 83178 | 1379.7 | 85381 | +2178 | -98.8 | strong |
| Call | 84200 | 660 | 640 | 1247.4 | 83186 | 1250.9 | 85447 | +2244 | -3.5 | strong |
| Call | 84300 | 40 | 40 | 1278.3 | 83117 | 1278.3 | 85578 | +2375 | +0.0 | strong |
| Put | 82000 | 3800 | 700 | 1073.8 | 83032 | 921.6 | 80926 | +2277 | +152.2 | strong |
| Put | 82100 | 40 | 40 | 985.9 | 83203 | 985.9 | 81114 | +2089 | +0.0 | strong |
| Put | 82300 | 40 | 40 | 1049.8 | 83203 | 1049.8 | 81250 | +1953 | +0.0 | strong |
| Put | 82400 | 40 | 40 | 1086.2 | 83203 | 1086.2 | 81314 | +1889 | +0.0 | strong |
| Put | 82700 | 60 | 60 | 1291.6 | 83017 | 1282.5 | 81408 | +1795 | +9.1 | strong |
| Put | 82800 | 240 | 240 | 1265.5 | 83184 | 1243.9 | 81534 | +1669 | +21.6 | strong |
| Put | 82900 | 160 | 160 | 1352.8 | 83122 | 1308.0 | 81547 | +1656 | +44.8 | strong |
| Put | 83000 | 6220 | 5327 | 1364.8 | 83109 | 1279.1 | 81635 | +1568 | +85.7 | strong |
| Put | 83100 | 240 | 240 | 1434.3 | 83088 | 1413.5 | 81666 | +1538 | +20.9 | strong |
| Put | 83200 | 440 | 440 | 1443.6 | 83123 | 1350.0 | 81756 | +1447 | +93.6 | strong |
| Put | 83300 | 420 | 420 | 1521.4 | 83082 | 1431.6 | 81779 | +1425 | +89.8 | strong |
| Put | 83400 | 500 | 500 | 1559.6 | 83090 | 1495.8 | 81840 | +1363 | +63.8 | strong |
| Put | 83500 | 1580 | 1100 | 1602.9 | 83108 | 1455.7 | 81897 | +1306 | +147.3 | strong |
| Put | 83600 | 640 | 640 | 1597.4 | 83175 | 1576.8 | 82003 | +1201 | +20.6 | strong |
| Put | 83700 | 480 | 480 | 1627.6 | 83192 | 1623.4 | 82072 | +1131 | +4.2 | strong |
| Put | 84000 | 160 | 160 | 1800.0 | 83203 | 1800.0 | 82200 | +1003 | +0.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.10% | +0.10 to +0.10% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.07% | +0.03 to +0.10% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 5 | 100% | +0.15% | too few (4/10) |
| intraday | monthly | writers even · few weak writers | 4 | 100% | +0.16% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.10% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts | 1 | 100% | +0.79% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | put writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 1 | 100% | +0.22% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +0.22% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 5 | 100% | +0.15% | too few (4/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 100% | +0.16% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.10% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 | 100% | +0.79% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.22% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +0.22% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
