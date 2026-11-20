# Sensex option chain pattern log
Updated 2026-11-20 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 10 snapshots over 2 trading days
- 17 patterns logged; 15 different patterns so far

## Latest read (2026-11-20 12:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 6.1 | 83712 | 0.934 | 83000 | 82500 | 88000 | ±1.62% (82356-85067) | 15.68 |
| 2026-12-31 (monthly) | 41.1 | 83712 | 0.768 | 83000 | 83000 | 87900 | ±3.92% (80431-86992) | 14.54 |

- **Weekly, last 30 min**: `PCR flat · unwinding · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.23%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 100% of the time, average +0.23%. Too few outcomes (1/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 5 times before; Sensex was up after it 100% of the time, average +0.64%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 5 times before; Sensex was up after it 100% of the time, average +0.64%. Too few outcomes (4/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.83%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 100% of the time, average +0.83%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85500, strongest put writers at 83000; weakest call writers at 83000, weakest put writers at 86000. Covers 72% of near-money call OI and 71% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82500 | 297640 | 113095 | 908.5 | 83022 | 1500.0 | 83408 | -303 | -591.5 | weak |
| Call | 82600 | 65500 | 49392 | 848.4 | 83024 | 1406.8 | 83448 | -263 | -558.5 | weak |
| Call | 82700 | 89220 | 69453 | 791.0 | 83023 | 1341.3 | 83491 | -221 | -550.4 | weak |
| Call | 82800 | 187480 | 136013 | 733.3 | 83023 | 1266.0 | 83533 | -178 | -532.7 | weak |
| Call | 82900 | 134620 | 94966 | 688.0 | 83022 | 1198.9 | 83588 | -124 | -510.9 | weak |
| Call | 83000 | 327500 | 192936 | 662.5 | 83020 | 1127.1 | 83662 | -49 | -464.6 | weak |
| Call | 83100 | 156760 | 138498 | 633.5 | 83044 | 1062.9 | 83734 | +22 | -429.4 | weak |
| Call | 83200 | 114000 | 103698 | 597.4 | 83092 | 996.5 | 83797 | +86 | -399.1 | weak |
| Call | 83300 | 150840 | 136848 | 544.6 | 83072 | 930.9 | 83845 | +133 | -386.3 | weak |
| Call | 83400 | 123400 | 105352 | 574.0 | 83204 | 869.0 | 83974 | +263 | -294.9 | medium |
| Call | 83500 | 240520 | 164952 | 512.5 | 83177 | 810.0 | 84012 | +301 | -297.6 | medium |
| Call | 83600 | 137380 | 121541 | 490.3 | 83210 | 757.2 | 84090 | +379 | -266.9 | strong |
| Call | 83700 | 196780 | 176388 | 536.4 | 83378 | 704.0 | 84236 | +525 | -167.6 | strong |
| Call | 83800 | 170360 | 148898 | 514.8 | 83419 | 654.2 | 84315 | +603 | -139.5 | strong |
| Call | 83900 | 95660 | 84293 | 376.4 | 83186 | 605.0 | 84276 | +565 | -228.7 | strong |
| Call | 84000 | 338720 | 214123 | 309.0 | 83098 | 562.0 | 84309 | +597 | -253.0 | strong |
| Call | 84100 | 96180 | 84753 | 358.6 | 83306 | 519.7 | 84459 | +747 | -161.1 | strong |
| Call | 84200 | 126100 | 113464 | 366.2 | 83405 | 477.2 | 84566 | +855 | -111.0 | strong |
| Call | 84300 | 79900 | 68913 | 225.2 | 83101 | 440.3 | 84525 | +814 | -215.1 | strong |
| Call | 84400 | 78580 | 62530 | 239.7 | 83189 | 402.1 | 84640 | +928 | -162.4 | strong |
| Call | 84500 | 195940 | 111061 | 179.2 | 83056 | 370.1 | 84679 | +968 | -191.0 | strong |
| Call | 84600 | 96480 | 86695 | 242.8 | 83351 | 340.1 | 84843 | +1131 | -97.3 | strong |
| Call | 84700 | 71780 | 58553 | 209.2 | 83321 | 309.4 | 84909 | +1198 | -100.3 | strong |
| Call | 84800 | 94720 | 79087 | 166.9 | 83208 | 282.9 | 84967 | +1255 | -116.1 | strong |
| Call | 84900 | 87800 | 61419 | 123.1 | 83069 | 258.5 | 85023 | +1312 | -135.4 | strong |
| Put | 82500 | 592960 | 311365 | 479.1 | 83025 | 248.4 | 82021 | +1691 | +230.7 | strong |
| Put | 82600 | 174360 | 135706 | 516.1 | 83023 | 269.5 | 82084 | +1628 | +246.6 | strong |
| Put | 82700 | 310920 | 265872 | 485.7 | 83200 | 293.9 | 82214 | +1497 | +191.9 | strong |
| Put | 82800 | 356440 | 263354 | 594.2 | 83031 | 320.8 | 82206 | +1506 | +273.4 | strong |
| Put | 82900 | 215760 | 172658 | 628.5 | 83049 | 346.0 | 82272 | +1440 | +282.5 | strong |
| Put | 83000 | 552820 | 356110 | 627.5 | 83098 | 377.1 | 82372 | +1339 | +250.5 | strong |
| Put | 83100 | 201380 | 188984 | 655.2 | 83111 | 410.6 | 82445 | +1267 | +244.6 | strong |
| Put | 83200 | 190200 | 181563 | 674.0 | 83189 | 444.3 | 82526 | +1186 | +229.7 | strong |
| Put | 83300 | 116100 | 110085 | 674.0 | 83301 | 480.9 | 82626 | +1086 | +193.1 | strong |
| Put | 83400 | 108040 | 103800 | 692.6 | 83381 | 517.9 | 82707 | +1004 | +174.7 | strong |
| Put | 83500 | 275160 | 258720 | 675.4 | 83499 | 562.0 | 82825 | +887 | +113.4 | strong |
| Put | 83600 | 104240 | 100860 | 659.4 | 83621 | 606.8 | 82941 | +771 | +52.6 | strong |
| Put | 83700 | 102000 | 98260 | 699.6 | 83631 | 651.8 | 83000 | +711 | +47.8 | strong |
| Put | 83800 | 67540 | 63980 | 760.9 | 83616 | 700.4 | 83039 | +672 | +60.6 | strong |
| Put | 83900 | 22100 | 18740 | 865.8 | 83543 | 753.9 | 83034 | +677 | +112.0 | strong |
| Put | 84000 | 63120 | 49540 | 942.9 | 83505 | 808.5 | 83057 | +654 | +134.4 | strong |
| Put | 84100 | 9160 | 8640 | 1079.2 | 83445 | 864.9 | 83021 | +691 | +214.4 | strong |
| Put | 84200 | 8420 | 8300 | 1095.7 | 83520 | 921.6 | 83104 | +607 | +174.1 | strong |
| Put | 84300 | 6560 | 5191 | 1038.5 | 83647 | 984.3 | 83261 | +450 | +54.2 | strong |
| Put | 84400 | 4780 | 4761 | 1180.0 | 83582 | 1056.2 | 83220 | +491 | +123.8 | strong |
| Put | 84500 | 10160 | 9740 | 1243.7 | 83575 | 1120.0 | 83256 | +455 | +123.7 | strong |
| Put | 84600 | 1040 | 1040 | 1587.8 | 83354 | 1190.0 | 83012 | +699 | +397.8 | strong |
| Put | 84700 | 640 | 640 | 1764.7 | 83281 | 1213.7 | 82935 | +776 | +551.1 | strong |
| Put | 84800 | 400 | 400 | 2181.0 | 83023 | 1306.0 | 82619 | +1093 | +875.0 | strong |
| Put | 84900 | 1400 | 1400 | 1883.7 | 83216 | 1354.6 | 83016 | +695 | +529.1 | strong |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 83000, strongest put writers at 83000; weakest call writers at -, weakest put writers at -. Covers 75% of near-money call OI and 70% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82800 | 320 | 100 | 1766.7 | 83023 | 1766.7 | 84567 | +855 | +0.0 | strong |
| Call | 83000 | 7580 | 6553 | 2114.3 | 83515 | 2277.6 | 85114 | +1403 | -163.3 | strong |
| Call | 83100 | 80 | 40 | 1607.8 | 83023 | 1786.2 | 84708 | +996 | -178.4 | strong |
| Call | 83300 | 40 | 40 | 1653.3 | 83117 | 1653.3 | 84953 | +1242 | +0.0 | strong |
| Call | 83400 | 120 | 109 | 1484.0 | 83023 | 1973.8 | 84884 | +1172 | -489.9 | strong |
| Call | 83500 | 900 | 455 | 1621.6 | 83190 | 2021.4 | 85122 | +1410 | -399.8 | strong |
| Call | 83600 | 260 | 260 | 1610.9 | 83438 | 1627.2 | 85211 | +1499 | -16.3 | strong |
| Call | 83700 | 420 | 420 | 1620.8 | 83414 | 1657.0 | 85321 | +1609 | -36.2 | strong |
| Call | 83800 | 140 | 140 | 1556.6 | 83380 | 1644.8 | 85357 | +1645 | -88.2 | strong |
| Call | 83900 | 660 | 620 | 1438.5 | 83244 | 1687.3 | 85339 | +1627 | -248.8 | strong |
| Call | 84000 | 1420 | 1420 | 1424.7 | 83297 | 1693.0 | 85425 | +1713 | -268.4 | strong |
| Call | 84100 | 60 | 60 | 1412.8 | 83406 | 1600.0 | 85513 | +1801 | -187.2 | strong |
| Call | 84200 | 640 | 621 | 1247.4 | 83186 | 1429.7 | 85447 | +1736 | -182.3 | strong |
| Call | 84300 | 40 | 40 | 1278.3 | 83117 | 1351.5 | 85578 | +1867 | -73.2 | strong |
| Call | 84500 | 40 | 40 | 1285.3 | 83519 | 1285.3 | 85785 | +2074 | +0.0 | strong |
| Call | 84600 | 40 | 40 | 1052.9 | 83137 | 1153.7 | 85653 | +1941 | -100.8 | strong |
| Call | 84700 | 120 | 120 | 1037.1 | 83172 | 1187.1 | 85737 | +2026 | -150.0 | strong |
| Call | 84800 | 100 | 100 | 1009.5 | 83203 | 1129.5 | 85810 | +2098 | -120.0 | strong |
| Call | 84900 | 120 | 120 | 969.8 | 83203 | 1099.4 | 85870 | +2158 | -129.7 | strong |
| Put | 82500 | 240 | 20 | 1079.0 | 83519 | 1079.0 | 81421 | +2291 | +0.0 | strong |
| Put | 82700 | 60 | 60 | 1291.6 | 83017 | 1282.5 | 81408 | +2303 | +9.1 | strong |
| Put | 82800 | 260 | 260 | 1262.6 | 83210 | 1227.2 | 81537 | +2174 | +35.3 | strong |
| Put | 82900 | 180 | 180 | 1342.9 | 83166 | 1263.3 | 81557 | +2154 | +79.5 | strong |
| Put | 83000 | 6180 | 5296 | 1364.1 | 83110 | 1102.0 | 81636 | +2076 | +262.1 | strong |
| Put | 83100 | 260 | 260 | 1417.8 | 83121 | 1219.2 | 81682 | +2029 | +198.6 | strong |
| Put | 83200 | 480 | 480 | 1428.8 | 83156 | 1266.2 | 81771 | +1940 | +162.6 | strong |
| Put | 83300 | 440 | 440 | 1514.9 | 83101 | 1379.7 | 81785 | +1926 | +135.3 | strong |
| Put | 83400 | 500 | 500 | 1559.6 | 83090 | 1495.8 | 81840 | +1871 | +63.8 | strong |
| Put | 83500 | 1700 | 1220 | 1574.3 | 83164 | 1293.7 | 81926 | +1786 | +280.6 | strong |
| Put | 83600 | 640 | 640 | 1597.4 | 83175 | 1576.8 | 82003 | +1709 | +20.6 | strong |
| Put | 83700 | 480 | 480 | 1627.6 | 83192 | 1623.4 | 82072 | +1639 | +4.2 | strong |
| Put | 83800 | 140 | 140 | 1500.4 | 83547 | 1421.7 | 82300 | +1412 | +78.8 | strong |
| Put | 83900 | 160 | 140 | 1454.0 | 83712 | 1454.0 | 82446 | +1266 | +0.0 | strong |
| Put | 84000 | 260 | 260 | 1713.2 | 83339 | 1498.8 | 82287 | +1425 | +214.5 | strong |
| Put | 84100 | 60 | 60 | 1611.0 | 83583 | 1563.4 | 82489 | +1222 | +47.6 | strong |
| Put | 84200 | 40 | 40 | 1607.9 | 83712 | 1607.9 | 82592 | +1119 | +0.0 | strong |
| Put | 84300 | 100 | 100 | 1889.0 | 83519 | 1623.0 | 82411 | +1300 | +265.9 | strong |
| Put | 84400 | 100 | 100 | 1938.2 | 83519 | 1938.2 | 82462 | +1250 | +0.0 | strong |
| Put | 84500 | 120 | 120 | 1881.5 | 83503 | 1758.1 | 82618 | +1093 | +123.4 | strong |
| Put | 84600 | 100 | 100 | 2090.2 | 83203 | 2090.2 | 82510 | +1202 | +0.0 | strong |
| Put | 84700 | 160 | 160 | 2127.2 | 83322 | 2045.2 | 82573 | +1139 | +82.1 | strong |
| Put | 84800 | 100 | 100 | 2170.5 | 83203 | 2170.5 | 82630 | +1082 | +0.0 | strong |
| Put | 84900 | 180 | 180 | 2229.6 | 83379 | 2181.1 | 82670 | +1041 | +48.5 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.66% | +0.61 to +0.72% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.68% | +0.64 to +0.72% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.61% | +0.61 to +0.61% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.83% | +0.83 to +0.83% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.83% | +0.83 to +0.83% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 6 | 100% | +0.64% | too few (4/10) |
| intraday | weekly | writers even · few weak writers | 5 | 100% | +0.73% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.66% | too few (2/10) |
| intraday | weekly | writers even · weak calls | 2 | 100% | +0.23% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts | 1 | 100% | +1.41% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 2 | 100% | +0.83% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +0.83% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 6 | 100% | +0.64% | too few (4/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 5 | 100% | +0.73% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.66% | too few (2/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 2 | 100% | +0.23% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 | 100% | +1.41% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.83% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +0.83% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
