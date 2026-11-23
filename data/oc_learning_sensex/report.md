# Sensex option chain pattern log
Updated 2026-11-23 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 24 snapshots over 3 trading days
- 45 patterns logged; 32 different patterns so far

## Latest read (2026-11-23 12:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 3.1 | 82967 | 0.869 | 83100 | 79000 | 88000 | ±1.49% (81733-84200) | 20.01 |
| 2026-12-31 (monthly) | 38.1 | 82967 | 1.944 | 83200 | 82000 | 87900 | ±3.89% (79741-86192) | 14.97 |

- **Weekly, last 30 min**: `PCR up · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 3 times before; Sensex was up after it 0% of the time, average -0.24%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Sensex was up after it 0% of the time, average -0.24%. Too few outcomes (3/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · call writing · walls down · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. Seen 7 times before; Sensex was up after it 29% of the time, average +0.04%. Too few outcomes (7/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 7 times before; Sensex was up after it 29% of the time, average +0.04%. Too few outcomes (7/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put writing · walls down · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 81000; weakest call writers at 81900, weakest put writers at 83500. Covers 89% of near-money call OI and 84% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 81800 | 6120 | 851 | 1434.1 | 83061 | 1330.0 | 83234 | +268 | +104.1 | medium |
| Call | 81900 | 12680 | 4431 | 1228.7 | 82999 | 1188.1 | 83129 | +162 | +40.6 | weak |
| Call | 82000 | 97800 | 25767 | 1275.3 | 83053 | 1180.0 | 83275 | +309 | +95.3 | medium |
| Call | 82100 | 10560 | 3707 | 1174.7 | 83059 | 1098.4 | 83275 | +308 | +76.3 | medium |
| Call | 82200 | 19600 | 1486 | 1111.2 | 83026 | 1053.5 | 83311 | +345 | +57.7 | medium |
| Call | 82300 | 30200 | 5922 | 1076.2 | 83110 | 971.4 | 83376 | +410 | +104.8 | strong |
| Call | 82400 | 25720 | 9592 | 998.5 | 83082 | 919.9 | 83399 | +432 | +78.7 | strong |
| Call | 82500 | 128320 | 57641 | 906.9 | 83028 | 857.2 | 83407 | +440 | +49.6 | strong |
| Call | 82600 | 49800 | 41977 | 885.0 | 83103 | 797.0 | 83485 | +519 | +88.1 | strong |
| Call | 82700 | 84680 | 71277 | 824.0 | 83091 | 740.0 | 83524 | +558 | +84.0 | strong |
| Call | 82800 | 126240 | 99970 | 741.2 | 83047 | 688.9 | 83541 | +575 | +52.3 | strong |
| Call | 82900 | 173080 | 152691 | 683.3 | 83047 | 636.1 | 83583 | +617 | +47.1 | strong |
| Call | 83000 | 468780 | 387744 | 663.6 | 83097 | 590.9 | 83664 | +697 | +72.7 | strong |
| Call | 83100 | 225760 | 217419 | 631.0 | 83134 | 543.0 | 83731 | +764 | +88.0 | strong |
| Call | 83200 | 327200 | 321915 | 637.0 | 83244 | 502.6 | 83837 | +870 | +134.4 | strong |
| Call | 83300 | 297520 | 292791 | 592.4 | 83260 | 461.4 | 83892 | +926 | +131.1 | strong |
| Call | 83400 | 336640 | 327826 | 584.8 | 83308 | 424.8 | 83985 | +1018 | +160.0 | strong |
| Call | 83500 | 760480 | 718684 | 556.6 | 83345 | 390.2 | 84057 | +1090 | +166.4 | strong |
| Call | 83600 | 323540 | 318319 | 535.0 | 83353 | 357.5 | 84135 | +1168 | +177.5 | strong |
| Call | 83700 | 262140 | 255243 | 546.7 | 83453 | 326.4 | 84247 | +1280 | +220.3 | strong |
| Call | 83800 | 246260 | 231786 | 519.3 | 83453 | 298.9 | 84319 | +1353 | +220.5 | strong |
| Call | 83900 | 223860 | 215441 | 488.0 | 83468 | 274.1 | 84388 | +1421 | +213.9 | strong |
| Call | 84000 | 820540 | 708559 | 388.1 | 83340 | 252.1 | 84388 | +1422 | +136.1 | strong |
| Call | 84100 | 179460 | 170324 | 389.8 | 83408 | 230.3 | 84490 | +1523 | +159.4 | strong |
| Call | 84200 | 215980 | 209957 | 382.5 | 83457 | 209.7 | 84582 | +1616 | +172.8 | strong |
| Put | 81800 | 115680 | 96203 | 205.5 | 83172 | 196.5 | 81594 | +1372 | +9.0 | strong |
| Put | 81900 | 100500 | 74567 | 215.2 | 83296 | 220.9 | 81685 | +1282 | -5.7 | strong |
| Put | 82000 | 459300 | 294025 | 254.1 | 83219 | 246.2 | 81746 | +1221 | +7.9 | strong |
| Put | 82100 | 108460 | 74767 | 286.2 | 83119 | 273.7 | 81814 | +1153 | +12.5 | strong |
| Put | 82200 | 132740 | 75781 | 305.0 | 83174 | 304.2 | 81895 | +1072 | +0.8 | strong |
| Put | 82300 | 135820 | 103870 | 293.5 | 83370 | 338.3 | 82007 | +960 | -44.8 | strong |
| Put | 82400 | 170780 | 134968 | 383.1 | 83124 | 371.4 | 82017 | +950 | +11.7 | strong |
| Put | 82500 | 339600 | 191999 | 458.8 | 83060 | 410.6 | 82041 | +925 | +48.1 | strong |
| Put | 82600 | 139980 | 114991 | 482.8 | 83092 | 451.9 | 82117 | +849 | +30.9 | strong |
| Put | 82700 | 210980 | 185877 | 460.6 | 83251 | 495.6 | 82239 | +727 | -35.0 | strong |
| Put | 82800 | 252080 | 194755 | 570.1 | 83073 | 538.3 | 82230 | +737 | +31.8 | strong |
| Put | 82900 | 228780 | 205031 | 584.5 | 83088 | 589.0 | 82316 | +651 | -4.5 | strong |
| Put | 83000 | 451540 | 305373 | 622.8 | 83103 | 642.1 | 82377 | +589 | -19.4 | strong |
| Put | 83100 | 146740 | 141296 | 597.0 | 83256 | 695.8 | 82503 | +464 | -98.8 | strong |
| Put | 83200 | 206620 | 202232 | 632.3 | 83294 | 753.0 | 82568 | +399 | -120.7 | strong |
| Put | 83300 | 151220 | 148776 | 670.8 | 83317 | 813.2 | 82629 | +337 | -142.5 | medium |
| Put | 83400 | 129940 | 127930 | 679.1 | 83407 | 876.1 | 82721 | +246 | -197.1 | medium |
| Put | 83500 | 400920 | 389665 | 673.8 | 83507 | 937.6 | 82826 | +140 | -263.8 | weak |
| Put | 83600 | 95080 | 93799 | 686.8 | 83587 | 1009.0 | 82913 | +53 | -322.2 | weak |
| Put | 83700 | 100500 | 98629 | 653.8 | 83699 | 1079.7 | 83046 | -80 | -425.9 | weak |
| Put | 83800 | 129300 | 127386 | 658.2 | 83759 | 1149.9 | 83142 | -175 | -491.7 | weak |
| Put | 83900 | 126920 | 124793 | 682.1 | 83798 | 1224.0 | 83218 | -251 | -541.9 | weak |
| Put | 84000 | 170520 | 160975 | 798.6 | 83727 | 1300.0 | 83201 | -235 | -501.4 | weak |
| Put | 84100 | 42000 | 41713 | 996.3 | 83544 | 1412.8 | 83104 | -137 | -416.6 | weak |
| Put | 84200 | 36640 | 36559 | 1017.1 | 83614 | 1472.8 | 83183 | -216 | -455.7 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 84000, strongest put writers at 83000; weakest call writers at -, weakest put writers at 85000. Covers 80% of near-money call OI and 88% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82000 | 2820 | 450 | 2571.6 | 83246 | 2355.4 | 84572 | +1605 | +216.2 | strong |
| Call | 82200 | 140 | 100 | 2124.2 | 83023 | 2124.2 | 84324 | +1358 | +0.0 | strong |
| Call | 82300 | 100 | 100 | 2134.5 | 83023 | 2134.5 | 84434 | +1468 | +0.0 | strong |
| Call | 82400 | 100 | 100 | 2074.4 | 83023 | 2074.4 | 84474 | +1508 | +0.0 | strong |
| Call | 82500 | 580 | 536 | 2250.0 | 83384 | 2250.1 | 84750 | +1783 | -0.1 | strong |
| Call | 82800 | 420 | 200 | 1834.1 | 83020 | 1901.5 | 84634 | +1668 | -67.5 | strong |
| Call | 83000 | 1900 | 1721 | 2135.6 | 83516 | 1800.0 | 85136 | +2169 | +335.6 | strong |
| Call | 83100 | 80 | 40 | 1607.8 | 83023 | 1786.2 | 84708 | +1741 | -178.4 | strong |
| Call | 83200 | 200 | 95 | 1755.9 | 83087 | 1676.3 | 84956 | +1989 | +79.6 | strong |
| Call | 83300 | 320 | 320 | 1643.5 | 83093 | 1640.9 | 84944 | +1977 | +2.6 | strong |
| Call | 83400 | 600 | 589 | 1578.4 | 83222 | 1556.7 | 84978 | +2012 | +21.8 | strong |
| Call | 83500 | 1260 | 923 | 1674.3 | 83254 | 1543.7 | 85174 | +2208 | +130.7 | strong |
| Call | 83600 | 500 | 500 | 1587.1 | 83322 | 1491.8 | 85187 | +2221 | +95.3 | strong |
| Call | 83700 | 1060 | 1060 | 1614.9 | 83340 | 1532.2 | 85315 | +2348 | +82.6 | strong |
| Call | 83800 | 320 | 320 | 1548.8 | 83298 | 1399.0 | 85349 | +2382 | +149.8 | strong |
| Call | 83900 | 580 | 552 | 1457.4 | 83284 | 1379.2 | 85357 | +2391 | +78.2 | strong |
| Call | 84000 | 2760 | 2760 | 1500.7 | 83391 | 1320.0 | 85501 | +2534 | +180.7 | strong |
| Call | 84100 | 160 | 160 | 1477.4 | 83460 | 1392.3 | 85577 | +2611 | +85.0 | strong |
| Call | 84200 | 600 | 586 | 1320.8 | 83321 | 1248.3 | 85521 | +2554 | +72.5 | strong |
| Put | 81900 | 600 | 600 | 920.2 | 83350 | 954.4 | 80980 | +1987 | -34.2 | strong |
| Put | 82000 | 5960 | 3342 | 950.9 | 83302 | 1033.2 | 81049 | +1917 | -82.3 | strong |
| Put | 82100 | 200 | 200 | 962.1 | 83263 | 949.2 | 81138 | +1829 | +12.9 | strong |
| Put | 82300 | 2020 | 2020 | 979.1 | 83457 | 1150.4 | 81321 | +1646 | -171.3 | strong |
| Put | 82400 | 1980 | 1980 | 976.8 | 83589 | 1116.6 | 81423 | +1543 | -139.8 | strong |
| Put | 82500 | 1740 | 1572 | 1059.8 | 83416 | 1219.8 | 81440 | +1526 | -160.0 | strong |
| Put | 82600 | 480 | 480 | 1029.1 | 83460 | 1111.6 | 81571 | +1396 | -82.5 | strong |
| Put | 82700 | 420 | 420 | 1159.7 | 83349 | 1192.3 | 81540 | +1426 | -32.6 | strong |
| Put | 82800 | 620 | 620 | 1182.8 | 83320 | 1135.8 | 81617 | +1349 | +47.0 | strong |
| Put | 82900 | 460 | 460 | 1277.4 | 83200 | 1272.0 | 81623 | +1344 | +5.4 | strong |
| Put | 83000 | 9620 | 8777 | 1266.9 | 83347 | 1425.5 | 81733 | +1233 | -158.6 | strong |
| Put | 83100 | 580 | 580 | 1313.5 | 83301 | 1265.2 | 81787 | +1180 | +48.3 | strong |
| Put | 83200 | 880 | 880 | 1380.6 | 83241 | 1349.7 | 81819 | +1147 | +31.0 | strong |
| Put | 83300 | 660 | 660 | 1480.5 | 83127 | 1585.0 | 81819 | +1147 | -104.5 | strong |
| Put | 83400 | 1000 | 1000 | 1462.7 | 83282 | 1607.2 | 81937 | +1029 | -144.5 | strong |
| Put | 83500 | 2040 | 1638 | 1505.7 | 83309 | 1681.1 | 81994 | +972 | -175.4 | strong |
| Put | 83600 | 1260 | 1260 | 1521.0 | 83328 | 1462.5 | 82079 | +887 | +58.5 | strong |
| Put | 83700 | 740 | 740 | 1565.1 | 83321 | 1661.2 | 82135 | +832 | -96.1 | strong |
| Put | 83800 | 760 | 760 | 1526.0 | 83478 | 1655.7 | 82274 | +693 | -129.6 | strong |
| Put | 83900 | 440 | 425 | 1519.5 | 83554 | 1658.2 | 82381 | +586 | -138.7 | strong |
| Put | 84000 | 1340 | 1340 | 1636.6 | 83546 | 1945.0 | 82363 | +603 | -308.4 | strong |
| Put | 84100 | 1140 | 1140 | 1593.2 | 83618 | 1673.3 | 82507 | +460 | -80.1 | strong |
| Put | 84200 | 440 | 440 | 1541.5 | 83800 | 1625.6 | 82659 | +308 | -84.1 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls same · near put wall | 6 | 40% | -0.15% | -0.66 to +0.22% |  | too few (5/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 3 | 67% | +0.04% | -0.07 to +0.16% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | +0.18% | -0.50 to +0.86% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near put wall | 2 | 50% | +0.09% | -0.06 to +0.25% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.50% | -0.50 to -0.50% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.31% | -0.31 to -0.31% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -0.51% | -0.51 to -0.51% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.06% | -0.06 to -0.06% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.66% | -0.66 to -0.66% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.51% | -0.51 to -0.51% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 0% | -0.17% | -0.17 to -0.17% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.14% | -1.14 to -1.14% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 14 | 75% | +0.14% | no clear direction |
| intraday | weekly | writers even · few weak writers | 10 | 67% | +0.40% | too few (9/10) |
| intraday | monthly | put writers stronger · few weak writers | 8 | 29% | +0.04% | too few (7/10) |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.13% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers | 4 | 0% | -0.24% | too few (3/10) |
| intraday | weekly | call writers stronger · weak puts | 1 | 100% | +1.66% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 2 | 50% | -0.03% | too few (2/10) |
| day | monthly | put writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -1.14% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 14 | 75% | +0.14% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 10 | 67% | +0.40% | too few (9/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 8 | 29% | +0.04% | too few (7/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.13% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 4 | 0% | -0.24% | too few (3/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.03% | too few (2/10) |
| day | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 | 0% | -1.14% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
