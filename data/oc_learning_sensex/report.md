# Sensex option chain pattern log
Updated 2026-11-23 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 26 snapshots over 3 trading days
- 49 patterns logged; 33 different patterns so far

## Latest read (2026-11-23 13:46:00)

Sensex trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 3.1 | 82724 | 0.88 | 83000 | 79000 | 88000 | ±1.45% (81524-83925) | 19.86 |
| 2026-12-31 (monthly) | 38.1 | 82730 | 2.164 | 83500 | 82000 | 87900 | ±3.79% (79591-85868) | 14.54 |

- **Weekly, last 30 min**: `PCR down · call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 2 times before; Sensex was up after it 50% of the time, average +0.79%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put writing · walls same · near put wall`. Seen 7 times before; Sensex was up after it 33% of the time, average -0.28%. Too few outcomes (6/20) to trade on.
  - Writers: `put writers stronger · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, today vs previous day**: `PCR up · put writing · walls down · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 81000; weakest call writers at 80700, weakest put writers at 83500. Covers 90% of near-money call OI and 85% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 81500 | 39580 | 15909 | 2033.3 | 83450 | 1370.0 | 83533 | +809 | +663.4 | strong |
| Call | 81600 | 3900 | 486 | 1620.2 | 83074 | 1280.0 | 83220 | +496 | +340.2 | strong |
| Call | 81700 | 5880 | 1392 | 1553.5 | 83194 | 1229.2 | 83254 | +529 | +324.3 | strong |
| Call | 81800 | 6420 | 1203 | 1346.2 | 82960 | 1140.4 | 83146 | +422 | +205.8 | strong |
| Call | 81900 | 12620 | 4612 | 1221.7 | 82985 | 1063.2 | 83122 | +398 | +158.5 | strong |
| Call | 82000 | 104900 | 32867 | 1222.0 | 82989 | 1008.2 | 83222 | +498 | +213.8 | strong |
| Call | 82100 | 12960 | 6107 | 1093.4 | 82946 | 933.8 | 83193 | +469 | +159.6 | strong |
| Call | 82200 | 25500 | 7386 | 952.6 | 82828 | 869.9 | 83153 | +428 | +82.7 | strong |
| Call | 82300 | 33180 | 8902 | 995.6 | 82993 | 815.3 | 83296 | +571 | +180.3 | strong |
| Call | 82400 | 30440 | 14312 | 928.9 | 82981 | 757.0 | 83329 | +605 | +171.9 | strong |
| Call | 82500 | 149040 | 78361 | 855.6 | 82954 | 700.6 | 83356 | +631 | +155.0 | strong |
| Call | 82600 | 58720 | 50897 | 846.9 | 83043 | 650.0 | 83447 | +723 | +196.8 | strong |
| Call | 82700 | 154880 | 141477 | 715.7 | 82913 | 602.1 | 83416 | +692 | +113.6 | strong |
| Call | 82800 | 290440 | 264170 | 633.6 | 82870 | 553.9 | 83434 | +709 | +79.8 | strong |
| Call | 82900 | 246340 | 225951 | 634.1 | 82959 | 510.7 | 83534 | +810 | +123.5 | strong |
| Call | 83000 | 573400 | 492364 | 625.0 | 83025 | 468.7 | 83625 | +901 | +156.3 | strong |
| Call | 83100 | 245060 | 236719 | 615.8 | 83104 | 431.1 | 83716 | +992 | +184.7 | strong |
| Call | 83200 | 348900 | 343615 | 622.7 | 83215 | 395.1 | 83823 | +1099 | +227.7 | strong |
| Call | 83300 | 304940 | 300226 | 586.5 | 83247 | 363.6 | 83887 | +1162 | +223.0 | strong |
| Call | 83400 | 341460 | 332646 | 581.3 | 83300 | 331.9 | 83981 | +1257 | +249.4 | strong |
| Call | 83500 | 780300 | 738856 | 547.6 | 83323 | 303.3 | 84048 | +1323 | +244.3 | strong |
| Call | 83600 | 370720 | 365499 | 502.2 | 83274 | 278.2 | 84102 | +1378 | +224.0 | strong |
| Call | 83700 | 265060 | 258201 | 541.9 | 83442 | 254.1 | 84242 | +1518 | +287.9 | strong |
| Call | 83800 | 233940 | 220190 | 519.3 | 83453 | 232.0 | 84319 | +1595 | +287.3 | strong |
| Call | 83900 | 218620 | 210435 | 486.7 | 83465 | 213.1 | 84387 | +1663 | +273.6 | strong |
| Put | 81500 | 490420 | 426856 | 133.4 | 83355 | 170.3 | 81367 | +1358 | -36.9 | strong |
| Put | 81600 | 91640 | 82902 | 156.3 | 83324 | 194.3 | 81444 | +1280 | -38.1 | strong |
| Put | 81700 | 124580 | 99422 | 202.8 | 83144 | 216.7 | 81497 | +1227 | -13.8 | strong |
| Put | 81800 | 120760 | 102586 | 209.2 | 83124 | 242.7 | 81591 | +1133 | -33.5 | strong |
| Put | 81900 | 104800 | 79097 | 218.4 | 83263 | 271.6 | 81682 | +1043 | -53.3 | strong |
| Put | 82000 | 431540 | 276254 | 254.1 | 83219 | 302.8 | 81746 | +978 | -48.7 | strong |
| Put | 82100 | 100260 | 69114 | 286.2 | 83119 | 336.6 | 81814 | +910 | -50.5 | strong |
| Put | 82200 | 141420 | 86399 | 313.3 | 83115 | 373.5 | 81887 | +838 | -60.2 | strong |
| Put | 82300 | 140140 | 108792 | 300.9 | 83330 | 411.2 | 81999 | +725 | -110.3 | strong |
| Put | 82400 | 161680 | 129001 | 386.3 | 83106 | 454.2 | 82014 | +711 | -67.9 | strong |
| Put | 82500 | 363540 | 215939 | 462.7 | 83025 | 499.2 | 82037 | +687 | -36.5 | strong |
| Put | 82600 | 138420 | 114217 | 483.9 | 83084 | 549.6 | 82116 | +608 | -65.8 | strong |
| Put | 82700 | 272040 | 247358 | 496.7 | 83114 | 598.6 | 82203 | +521 | -101.9 | strong |
| Put | 82800 | 280500 | 227136 | 581.3 | 83016 | 652.1 | 82219 | +506 | -70.9 | strong |
| Put | 82900 | 201060 | 181264 | 590.0 | 83071 | 709.0 | 82310 | +414 | -119.0 | strong |
| Put | 83000 | 403400 | 272816 | 622.8 | 83103 | 767.7 | 82377 | +347 | -144.9 | medium |
| Put | 83100 | 128780 | 124002 | 597.0 | 83256 | 826.4 | 82503 | +221 | -229.3 | medium |
| Put | 83200 | 182160 | 178292 | 632.3 | 83294 | 892.8 | 82568 | +156 | -260.5 | weak |
| Put | 83300 | 128940 | 126856 | 670.8 | 83317 | 960.0 | 82629 | +95 | -289.2 | weak |
| Put | 83400 | 113300 | 111547 | 679.1 | 83407 | 1030.3 | 82721 | +3 | -351.2 | weak |
| Put | 83500 | 342840 | 333215 | 673.8 | 83507 | 1094.7 | 82826 | -102 | -420.9 | weak |
| Put | 83600 | 86700 | 85532 | 686.8 | 83587 | 1173.8 | 82913 | -189 | -487.0 | weak |
| Put | 83700 | 93140 | 91406 | 653.8 | 83699 | 1260.0 | 83046 | -322 | -606.3 | weak |
| Put | 83800 | 121900 | 120096 | 658.2 | 83759 | 1339.2 | 83142 | -418 | -681.0 | weak |
| Put | 83900 | 122280 | 120231 | 682.1 | 83798 | 1416.2 | 83218 | -494 | -734.1 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 85000, strongest put writers at 83000; weakest call writers at -, weakest put writers at 85000. Covers 84% of near-money call OI and 89% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 81500 | 1040 | 50 | 2953.1 | 83415 | 2875.0 | 84453 | +1723 | +78.1 | strong |
| Call | 82000 | 1520 | 243 | 2571.6 | 83246 | 2240.5 | 84572 | +1842 | +331.1 | strong |
| Call | 82200 | 140 | 100 | 2124.2 | 83023 | 2124.2 | 84324 | +1594 | +0.0 | strong |
| Call | 82300 | 100 | 100 | 2134.5 | 83023 | 2134.5 | 84434 | +1705 | +0.0 | strong |
| Call | 82400 | 100 | 100 | 2074.4 | 83023 | 2074.4 | 84474 | +1745 | +0.0 | strong |
| Call | 82500 | 580 | 538 | 2243.9 | 83363 | 2000.0 | 84744 | +2014 | +243.9 | strong |
| Call | 82800 | 880 | 660 | 1808.8 | 82818 | 1797.8 | 84609 | +1879 | +11.0 | strong |
| Call | 83000 | 1840 | 1666 | 2135.6 | 83516 | 1684.2 | 85136 | +2406 | +451.4 | strong |
| Call | 83100 | 220 | 180 | 1630.5 | 82802 | 1630.3 | 84731 | +2001 | +0.2 | strong |
| Call | 83200 | 300 | 195 | 1677.5 | 82904 | 1603.0 | 84877 | +2148 | +74.5 | strong |
| Call | 83300 | 360 | 360 | 1633.4 | 83053 | 1552.0 | 84933 | +2204 | +81.3 | strong |
| Call | 83400 | 600 | 589 | 1578.4 | 83222 | 1556.7 | 84978 | +2249 | +21.8 | strong |
| Call | 83500 | 1340 | 1003 | 1657.0 | 83216 | 1434.6 | 85157 | +2427 | +222.4 | strong |
| Call | 83600 | 500 | 500 | 1587.1 | 83322 | 1491.8 | 85187 | +2457 | +95.3 | strong |
| Call | 83700 | 1080 | 1080 | 1609.9 | 83329 | 1347.0 | 85310 | +2580 | +263.0 | strong |
| Call | 83800 | 320 | 320 | 1548.8 | 83298 | 1301.4 | 85349 | +2619 | +247.4 | strong |
| Call | 83900 | 580 | 552 | 1457.4 | 83284 | 1256.7 | 85357 | +2628 | +200.7 | strong |
| Put | 81500 | 1160 | 111 | 804.5 | 83267 | 879.9 | 80696 | +2034 | -75.4 | strong |
| Put | 81600 | 100 | 100 | 901.8 | 83055 | 880.3 | 80698 | +2032 | +21.5 | strong |
| Put | 81700 | 660 | 660 | 877.3 | 83342 | 870.6 | 80823 | +1907 | +6.6 | strong |
| Put | 81900 | 600 | 600 | 920.2 | 83350 | 1010.7 | 80980 | +1750 | -90.5 | strong |
| Put | 82000 | 6640 | 4022 | 967.5 | 83216 | 1076.5 | 81033 | +1697 | -109.1 | strong |
| Put | 82100 | 200 | 200 | 962.1 | 83263 | 949.2 | 81138 | +1592 | +12.9 | strong |
| Put | 82300 | 2020 | 2020 | 979.1 | 83457 | 1150.4 | 81321 | +1409 | -171.3 | strong |
| Put | 82400 | 1940 | 1940 | 976.8 | 83589 | 1191.8 | 81423 | +1307 | -214.9 | strong |
| Put | 82500 | 1980 | 1812 | 1085.1 | 83329 | 1262.2 | 81415 | +1315 | -177.1 | strong |
| Put | 82600 | 480 | 480 | 1029.1 | 83460 | 1111.6 | 81571 | +1159 | -82.5 | strong |
| Put | 82700 | 460 | 460 | 1172.8 | 83295 | 1309.9 | 81527 | +1203 | -137.1 | strong |
| Put | 82800 | 620 | 620 | 1182.8 | 83320 | 1135.8 | 81617 | +1113 | +47.0 | strong |
| Put | 82900 | 460 | 460 | 1277.4 | 83200 | 1272.0 | 81623 | +1107 | +5.4 | strong |
| Put | 83000 | 9500 | 8669 | 1267.4 | 83346 | 1452.3 | 81733 | +997 | -185.0 | strong |
| Put | 83100 | 580 | 580 | 1313.5 | 83301 | 1265.2 | 81787 | +943 | +48.3 | strong |
| Put | 83200 | 960 | 960 | 1394.6 | 83202 | 1547.8 | 81805 | +924 | -153.3 | strong |
| Put | 83300 | 840 | 840 | 1504.6 | 83049 | 1593.0 | 81795 | +934 | -88.3 | strong |
| Put | 83400 | 1000 | 1000 | 1462.7 | 83282 | 1643.0 | 81937 | +793 | -180.3 | strong |
| Put | 83500 | 1880 | 1510 | 1505.7 | 83309 | 1700.5 | 81994 | +736 | -194.8 | strong |
| Put | 83600 | 1260 | 1260 | 1521.0 | 83328 | 1462.5 | 82079 | +651 | +58.5 | strong |
| Put | 83700 | 740 | 740 | 1565.1 | 83321 | 1661.2 | 82135 | +595 | -96.1 | strong |
| Put | 83800 | 760 | 760 | 1526.0 | 83478 | 1655.7 | 82274 | +456 | -129.6 | strong |
| Put | 83900 | 440 | 425 | 1519.5 | 83554 | 1658.2 | 82381 | +349 | -138.7 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls same · near put wall | 8 | 33% | -0.28% | -0.94 to +0.22% |  | too few (6/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 3 | 67% | +0.04% | -0.07 to +0.16% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | +0.04% | -0.78 to +0.86% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near put wall | 2 | 50% | -0.05% | -0.35 to +0.25% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.52% | -0.95 to -0.08% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.29% | -0.29 to -0.29% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.79% | -0.79 to -0.79% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -0.80% | -0.80 to -0.80% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.80% | -0.80 to -0.80% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.29% | -0.29 to -0.29% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 0% | -0.46% | -0.46 to -0.46% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.42% | -1.42 to -1.42% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 14 | 75% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers | 10 | 67% | +0.30% | too few (9/10) |
| intraday | monthly | put writers stronger · few weak writers | 9 | 22% | -0.17% | too few (9/10) |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.17% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers | 4 | 0% | -0.47% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts | 3 | 50% | +0.79% | too few (2/10) |
| intraday | monthly | put writers stronger · weak puts | 1 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 2 | 50% | -0.17% | too few (2/10) |
| day | monthly | put writers stronger · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -1.42% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 14 | 75% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 10 | 67% | +0.30% | too few (9/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.17% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.17% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 4 | 0% | -0.47% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.79% | too few (2/10) |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.17% | too few (2/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 | 0% | -1.42% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
