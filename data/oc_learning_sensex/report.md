# Sensex option chain pattern log
Updated 2026-11-23 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 20 snapshots over 3 trading days
- 37 patterns logged; 27 different patterns so far

## Latest read (2026-11-23 10:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 3.2 | 83229 | 0.903 | 83300 | 80000 | 85000 | ±1.51% (81970-84487) | 20.2 |
| 2026-12-31 (monthly) | 38.2 | 83229 | 2.226 | 83300 | 83000 | 85900 | ±4.15% (79774-86683) | 15.96 |

- **Weekly, last 30 min**: `PCR down · call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 9 times before; Sensex was up after it 75% of the time, average +0.56%. Too few outcomes (8/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 9 times before; Sensex was up after it 75% of the time, average +0.56%. Too few outcomes (8/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Sensex was up after it 0% of the time, average -0.82%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 0% of the time, average -0.82%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR up · put writing · walls same · near put wall`. Seen 4 times before; Sensex was up after it 67% of the time, average +0.02%. Too few outcomes (3/20) to trade on.
  - Writers: `put writers stronger · few weak writers`. Seen 3 times before; Sensex was up after it 67% of the time, average +0.54%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Sensex was up after it 67% of the time, average +0.54%. Too few outcomes (3/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put writing · walls down · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 81500; weakest call writers at 82500, weakest put writers at 84000. Covers 87% of near-money call OI and 82% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82000 | 94220 | 22142 | 1269.2 | 83038 | 1347.6 | 83269 | +41 | -78.3 | weak |
| Call | 82100 | 10140 | 2664 | 1183.9 | 83042 | 1330.0 | 83284 | +55 | -146.1 | weak |
| Call | 82200 | 19860 | 1450 | 1110.0 | 83023 | 1213.5 | 83310 | +81 | -103.5 | weak |
| Call | 82300 | 26860 | 2286 | 1054.8 | 83059 | 1132.0 | 83355 | +126 | -77.2 | weak |
| Call | 82400 | 22740 | 5704 | 1010.9 | 83086 | 1070.0 | 83411 | +182 | -59.1 | weak |
| Call | 82500 | 125020 | 47504 | 908.5 | 83022 | 984.8 | 83408 | +180 | -76.3 | weak |
| Call | 82600 | 35420 | 27560 | 868.3 | 83062 | 919.1 | 83468 | +240 | -50.8 | medium |
| Call | 82700 | 69080 | 54829 | 811.4 | 83054 | 857.0 | 83511 | +283 | -45.6 | medium |
| Call | 82800 | 100700 | 74193 | 744.0 | 83043 | 801.0 | 83544 | +315 | -57.0 | medium |
| Call | 82900 | 82380 | 61166 | 718.5 | 83083 | 743.9 | 83619 | +390 | -25.4 | strong |
| Call | 83000 | 253820 | 169926 | 693.0 | 83112 | 689.0 | 83693 | +464 | +3.9 | strong |
| Call | 83100 | 101240 | 92899 | 647.1 | 83120 | 636.6 | 83747 | +518 | +10.4 | strong |
| Call | 83200 | 154260 | 148975 | 677.8 | 83280 | 591.0 | 83878 | +649 | +86.8 | strong |
| Call | 83300 | 240300 | 235540 | 601.3 | 83272 | 544.4 | 83901 | +673 | +56.9 | strong |
| Call | 83400 | 305360 | 296009 | 608.8 | 83355 | 501.9 | 84009 | +780 | +106.9 | strong |
| Call | 83500 | 482060 | 440264 | 592.1 | 83383 | 461.2 | 84092 | +863 | +130.9 | strong |
| Call | 83600 | 290880 | 285402 | 563.6 | 83412 | 423.9 | 84164 | +935 | +139.8 | strong |
| Call | 83700 | 233880 | 226460 | 569.6 | 83481 | 389.8 | 84270 | +1041 | +179.8 | strong |
| Call | 83800 | 228740 | 213832 | 542.1 | 83498 | 356.3 | 84342 | +1113 | +185.8 | strong |
| Call | 83900 | 215820 | 206902 | 508.9 | 83514 | 327.3 | 84409 | +1180 | +181.6 | strong |
| Call | 84000 | 713060 | 601079 | 402.8 | 83365 | 299.9 | 84403 | +1174 | +102.9 | strong |
| Call | 84100 | 171760 | 162470 | 399.6 | 83433 | 274.8 | 84500 | +1271 | +124.8 | strong |
| Call | 84200 | 197440 | 191319 | 398.7 | 83495 | 251.2 | 84599 | +1370 | +147.6 | strong |
| Call | 84300 | 232400 | 222996 | 346.6 | 83450 | 229.6 | 84647 | +1418 | +117.0 | strong |
| Call | 84400 | 247260 | 238714 | 331.2 | 83470 | 208.8 | 84731 | +1502 | +122.4 | strong |
| Put | 82000 | 453860 | 272932 | 264.3 | 83209 | 221.6 | 81736 | +1493 | +42.7 | strong |
| Put | 82100 | 102120 | 63056 | 293.0 | 83158 | 246.1 | 81807 | +1422 | +46.9 | strong |
| Put | 82200 | 129560 | 66129 | 308.9 | 83205 | 271.6 | 81891 | +1338 | +37.3 | strong |
| Put | 82300 | 131800 | 97867 | 290.2 | 83408 | 300.0 | 82010 | +1219 | -9.8 | strong |
| Put | 82400 | 142980 | 103340 | 399.4 | 83141 | 331.2 | 82001 | +1228 | +68.2 | strong |
| Put | 82500 | 409400 | 225785 | 461.5 | 83065 | 364.4 | 82038 | +1190 | +97.1 | strong |
| Put | 82600 | 128300 | 103150 | 487.1 | 83104 | 398.4 | 82113 | +1116 | +88.7 | strong |
| Put | 82700 | 209800 | 183724 | 459.6 | 83262 | 436.4 | 82240 | +988 | +23.3 | strong |
| Put | 82800 | 284560 | 217271 | 573.0 | 83073 | 478.1 | 82227 | +1002 | +95.0 | strong |
| Put | 82900 | 157260 | 133224 | 585.2 | 83136 | 520.0 | 82315 | +914 | +65.2 | strong |
| Put | 83000 | 442720 | 291165 | 622.0 | 83111 | 565.4 | 82378 | +851 | +56.6 | strong |
| Put | 83100 | 158440 | 150922 | 606.7 | 83241 | 615.4 | 82493 | +735 | -8.6 | strong |
| Put | 83200 | 223060 | 217093 | 623.5 | 83321 | 667.4 | 82576 | +652 | -43.8 | strong |
| Put | 83300 | 239100 | 234297 | 648.0 | 83370 | 721.1 | 82652 | +577 | -73.1 | strong |
| Put | 83400 | 201920 | 198514 | 666.1 | 83435 | 774.7 | 82734 | +495 | -108.5 | strong |
| Put | 83500 | 336720 | 324531 | 654.0 | 83547 | 836.5 | 82846 | +383 | -182.4 | strong |
| Put | 83600 | 152400 | 150307 | 681.6 | 83597 | 897.8 | 82918 | +310 | -216.2 | medium |
| Put | 83700 | 130000 | 127579 | 653.8 | 83699 | 967.0 | 83046 | +182 | -313.3 | weak |
| Put | 83800 | 164540 | 162058 | 650.0 | 83771 | 1032.0 | 83150 | +79 | -382.0 | weak |
| Put | 83900 | 140700 | 138342 | 682.1 | 83798 | 1101.0 | 83218 | +11 | -418.9 | weak |
| Put | 84000 | 225320 | 212707 | 798.6 | 83727 | 1177.0 | 83201 | +27 | -378.4 | weak |
| Put | 84100 | 51840 | 51429 | 945.9 | 83614 | 1245.3 | 83154 | +75 | -299.5 | weak |
| Put | 84200 | 42300 | 42204 | 1005.7 | 83630 | 1326.3 | 83194 | +34 | -320.6 | weak |
| Put | 84300 | 49720 | 48704 | 1083.0 | 83615 | 1396.7 | 83217 | +12 | -313.7 | weak |
| Put | 84400 | 62600 | 62586 | 1199.7 | 83553 | 1477.5 | 83200 | +28 | -277.7 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 84000, strongest put writers at 83000; weakest call writers at -, weakest put writers at 85500. Covers 77% of near-money call OI and 88% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82000 | 3080 | 492 | 2571.6 | 83246 | 3032.2 | 84572 | +1343 | -460.7 | strong |
| Call | 82200 | 140 | 100 | 2124.2 | 83023 | 2124.2 | 84324 | +1096 | +0.0 | strong |
| Call | 82300 | 100 | 100 | 2134.5 | 83023 | 2134.5 | 84434 | +1206 | +0.0 | strong |
| Call | 82400 | 100 | 100 | 2074.4 | 83023 | 2074.4 | 84474 | +1246 | +0.0 | strong |
| Call | 82800 | 320 | 100 | 1766.7 | 83023 | 1766.7 | 84567 | +1338 | +0.0 | strong |
| Call | 83000 | 1820 | 1622 | 2176.3 | 83599 | 1941.1 | 85176 | +1948 | +235.2 | strong |
| Call | 83100 | 80 | 40 | 1607.8 | 83023 | 1786.2 | 84708 | +1479 | -178.4 | strong |
| Call | 83200 | 120 | 15 | 2180.4 | 83732 | 2129.1 | 85380 | +2152 | +51.4 | strong |
| Call | 83300 | 40 | 40 | 1653.3 | 83117 | 1653.3 | 84953 | +1725 | +0.0 | strong |
| Call | 83400 | 140 | 129 | 1550.5 | 83080 | 1913.5 | 84950 | +1722 | -363.0 | strong |
| Call | 83500 | 860 | 523 | 1679.1 | 83289 | 1670.0 | 85179 | +1950 | +9.1 | strong |
| Call | 83600 | 340 | 340 | 1613.5 | 83408 | 1607.0 | 85214 | +1985 | +6.5 | strong |
| Call | 83700 | 880 | 880 | 1628.7 | 83376 | 1568.0 | 85329 | +2100 | +60.7 | strong |
| Call | 83800 | 220 | 220 | 1588.2 | 83423 | 1575.0 | 85388 | +2160 | +13.2 | strong |
| Call | 83900 | 760 | 724 | 1457.4 | 83284 | 1524.2 | 85357 | +2129 | -66.9 | strong |
| Call | 84000 | 2380 | 2380 | 1520.5 | 83441 | 1424.5 | 85520 | +2292 | +96.0 | strong |
| Call | 84100 | 160 | 160 | 1477.4 | 83460 | 1392.3 | 85577 | +2349 | +85.0 | strong |
| Call | 84200 | 600 | 586 | 1320.8 | 83321 | 1381.2 | 85521 | +2292 | -60.5 | strong |
| Call | 84300 | 100 | 100 | 1286.6 | 83184 | 1292.2 | 85587 | +2358 | -5.5 | strong |
| Call | 84400 | 320 | 320 | 1461.7 | 83517 | 1263.5 | 85862 | +2633 | +198.2 | strong |
| Put | 82000 | 6360 | 3400 | 946.6 | 83328 | 970.0 | 81053 | +2175 | -23.4 | strong |
| Put | 82100 | 160 | 160 | 965.4 | 83303 | 978.6 | 81135 | +2094 | -13.2 | strong |
| Put | 82300 | 2120 | 2120 | 979.1 | 83457 | 1025.0 | 81321 | +1908 | -45.9 | strong |
| Put | 82400 | 1960 | 1960 | 975.4 | 83594 | 1054.6 | 81425 | +1804 | -79.2 | strong |
| Put | 82500 | 1440 | 1272 | 1031.3 | 83504 | 1121.7 | 81469 | +1760 | -90.3 | strong |
| Put | 82600 | 180 | 180 | 900.6 | 83867 | 1049.8 | 81699 | +1529 | -149.1 | strong |
| Put | 82700 | 200 | 200 | 1132.9 | 83395 | 1082.0 | 81567 | +1662 | +51.0 | strong |
| Put | 82800 | 580 | 580 | 1186.0 | 83335 | 1200.3 | 81614 | +1615 | -14.2 | strong |
| Put | 82900 | 400 | 400 | 1278.4 | 83200 | 1225.7 | 81622 | +1607 | +52.8 | strong |
| Put | 83000 | 9960 | 9085 | 1266.6 | 83348 | 1319.1 | 81733 | +1495 | -52.5 | strong |
| Put | 83100 | 500 | 500 | 1312.8 | 83310 | 1281.8 | 81787 | +1442 | +31.0 | strong |
| Put | 83200 | 800 | 800 | 1382.7 | 83247 | 1325.3 | 81817 | +1411 | +57.4 | strong |
| Put | 83300 | 480 | 480 | 1502.4 | 83112 | 1365.2 | 81798 | +1431 | +137.2 | strong |
| Put | 83400 | 980 | 980 | 1459.8 | 83287 | 1411.0 | 81940 | +1288 | +48.8 | strong |
| Put | 83500 | 1940 | 1522 | 1496.5 | 83334 | 1546.6 | 82004 | +1225 | -50.1 | strong |
| Put | 83600 | 1140 | 1140 | 1518.3 | 83332 | 1583.7 | 82082 | +1147 | -65.4 | strong |
| Put | 83700 | 700 | 700 | 1560.9 | 83317 | 1563.8 | 82139 | +1090 | -2.9 | strong |
| Put | 83800 | 760 | 760 | 1526.0 | 83478 | 1655.7 | 82274 | +955 | -129.6 | strong |
| Put | 83900 | 440 | 425 | 1519.5 | 83554 | 1658.2 | 82381 | +848 | -138.7 | strong |
| Put | 84000 | 1520 | 1520 | 1634.2 | 83552 | 1775.5 | 82366 | +863 | -141.3 | strong |
| Put | 84100 | 1140 | 1140 | 1593.2 | 83618 | 1673.3 | 82507 | +722 | -80.1 | strong |
| Put | 84200 | 440 | 440 | 1541.5 | 83800 | 1625.6 | 82659 | +570 | -84.1 | strong |
| Put | 84300 | 540 | 540 | 1618.0 | 83777 | 1673.5 | 82682 | +547 | -55.6 | strong |
| Put | 84400 | 1020 | 1020 | 1672.9 | 83776 | 1917.2 | 82727 | +502 | -244.3 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls same · near put wall | 5 | 67% | +0.02% | -0.35 to +0.22% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 3 | 67% | +0.04% | -0.07 to +0.16% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.86% | +0.86 to +0.86% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.82% | -0.82 to -0.82% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 14 | 75% | +0.19% | no clear direction |
| intraday | weekly | writers even · few weak writers | 10 | 75% | +0.56% | too few (8/10) |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.08% | too few (7/10) |
| intraday | monthly | put writers stronger · few weak writers | 4 | 67% | +0.54% | too few (3/10) |
| intraday | weekly | call writers stronger · weak puts | 1 | 100% | +1.66% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 2 | 50% | +0.13% | too few (2/10) |
| day | weekly | writers even · few weak writers | 2 | 0% | -0.82% | too few (1/10) |
| day | monthly | put writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 14 | 75% | +0.19% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 10 | 75% | +0.56% | too few (8/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.08% | too few (7/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 4 | 67% | +0.54% | too few (3/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | +0.13% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 0% | -0.82% | too few (1/10) |
| day | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
