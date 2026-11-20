# Sensex option chain pattern log
Updated 2026-11-20 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 14 snapshots over 2 trading days
- 25 patterns logged; 20 different patterns so far

## Latest read (2026-11-20 14:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 6.0 | 83784 | 1.055 | 83100 | 81500 | 88000 | ±1.58% (82462-85105) | 15.28 |
| 2026-12-31 (monthly) | 41.0 | 83786 | 1.074 | 83000 | 83000 | 87900 | ±3.76% (80639-86933) | 13.88 |

- **Weekly, last 30 min**: `PCR up · put writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 5 times before; Sensex was up after it 100% of the time, average +0.82%. Too few outcomes (5/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 5 times before; Sensex was up after it 100% of the time, average +0.82%. Too few outcomes (5/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls same · near put wall`. Seen 1 times before; Sensex was up after it 0% of the time, average -0.13%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 9 times before; Sensex was up after it 88% of the time, average +0.37%. Too few outcomes (8/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 9 times before; Sensex was up after it 88% of the time, average +0.37%. Too few outcomes (8/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.92%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 100% of the time, average +0.92%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85500, strongest put writers at 81500; weakest call writers at 83000, weakest put writers at -. Covers 76% of near-money call OI and 77% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82600 | 47280 | 35653 | 848.4 | 83024 | 1508.2 | 83448 | -335 | -659.8 | weak |
| Call | 82700 | 72860 | 56717 | 791.0 | 83023 | 1429.1 | 83491 | -293 | -638.1 | weak |
| Call | 82800 | 153720 | 111520 | 733.3 | 83023 | 1353.5 | 83533 | -251 | -620.1 | weak |
| Call | 82900 | 109040 | 76921 | 688.0 | 83022 | 1276.1 | 83588 | -196 | -588.1 | weak |
| Call | 83000 | 263660 | 155327 | 662.5 | 83020 | 1203.7 | 83662 | -121 | -541.2 | weak |
| Call | 83100 | 120480 | 106445 | 633.5 | 83044 | 1130.1 | 83734 | -50 | -496.6 | weak |
| Call | 83200 | 84660 | 77027 | 598.5 | 83094 | 1065.0 | 83799 | +15 | -466.4 | weak |
| Call | 83300 | 74880 | 67934 | 544.6 | 83072 | 1003.5 | 83845 | +61 | -458.9 | weak |
| Call | 83400 | 90660 | 77401 | 574.0 | 83204 | 935.2 | 83974 | +190 | -361.1 | medium |
| Call | 83500 | 216400 | 153538 | 554.8 | 83253 | 873.2 | 84055 | +271 | -318.5 | medium |
| Call | 83600 | 96520 | 86321 | 518.2 | 83264 | 810.4 | 84118 | +334 | -292.2 | medium |
| Call | 83700 | 186420 | 172837 | 597.5 | 83502 | 755.9 | 84298 | +514 | -158.3 | strong |
| Call | 83800 | 228240 | 207775 | 562.8 | 83523 | 702.6 | 84363 | +579 | -139.8 | strong |
| Call | 83900 | 222800 | 211433 | 537.8 | 83553 | 649.0 | 84438 | +654 | -111.2 | strong |
| Call | 84000 | 419520 | 294923 | 385.4 | 83286 | 599.2 | 84385 | +602 | -213.8 | strong |
| Call | 84100 | 116100 | 104685 | 395.4 | 83401 | 551.0 | 84495 | +712 | -155.6 | strong |
| Call | 84200 | 109000 | 99639 | 386.6 | 83464 | 504.8 | 84587 | +803 | -118.1 | strong |
| Call | 84300 | 98320 | 87891 | 286.7 | 83281 | 464.1 | 84587 | +803 | -177.4 | strong |
| Call | 84400 | 78260 | 65750 | 285.9 | 83339 | 425.0 | 84686 | +902 | -139.1 | strong |
| Call | 84500 | 212760 | 127881 | 207.2 | 83157 | 387.9 | 84707 | +923 | -180.8 | strong |
| Call | 84600 | 69720 | 63386 | 254.9 | 83400 | 354.0 | 84855 | +1071 | -99.1 | strong |
| Call | 84700 | 79000 | 67773 | 236.0 | 83431 | 322.9 | 84936 | +1152 | -86.8 | strong |
| Call | 84800 | 110140 | 95635 | 194.6 | 83333 | 291.8 | 84995 | +1211 | -97.2 | strong |
| Call | 84900 | 87300 | 66436 | 161.4 | 83262 | 265.5 | 85061 | +1278 | -104.1 | strong |
| Call | 85000 | 371980 | 234778 | 141.0 | 83224 | 241.3 | 85141 | +1357 | -100.3 | strong |
| Put | 82600 | 147700 | 116262 | 503.0 | 83059 | 236.6 | 82097 | +1687 | +266.4 | strong |
| Put | 82700 | 291460 | 252861 | 465.6 | 83253 | 256.9 | 82234 | +1549 | +208.6 | strong |
| Put | 82800 | 344160 | 254517 | 593.2 | 83034 | 278.4 | 82207 | +1577 | +314.7 | strong |
| Put | 82900 | 173160 | 138569 | 628.5 | 83049 | 302.6 | 82272 | +1512 | +325.8 | strong |
| Put | 83000 | 507800 | 327109 | 627.5 | 83098 | 328.6 | 82372 | +1411 | +298.9 | strong |
| Put | 83100 | 189900 | 178417 | 649.5 | 83124 | 356.6 | 82450 | +1333 | +292.9 | strong |
| Put | 83200 | 178940 | 170884 | 671.4 | 83195 | 387.7 | 82529 | +1255 | +283.6 | strong |
| Put | 83300 | 122740 | 116794 | 658.4 | 83332 | 420.2 | 82642 | +1142 | +238.2 | strong |
| Put | 83400 | 118900 | 114660 | 673.3 | 83417 | 454.4 | 82727 | +1057 | +218.9 | strong |
| Put | 83500 | 292080 | 277221 | 638.5 | 83561 | 492.0 | 82862 | +922 | +146.5 | strong |
| Put | 83600 | 127620 | 124481 | 635.3 | 83658 | 531.6 | 82965 | +819 | +103.7 | strong |
| Put | 83700 | 199840 | 196119 | 653.8 | 83699 | 573.5 | 83046 | +738 | +80.2 | strong |
| Put | 83800 | 229660 | 226100 | 653.8 | 83763 | 618.9 | 83146 | +638 | +34.9 | strong |
| Put | 83900 | 166960 | 163600 | 690.9 | 83767 | 665.5 | 83209 | +575 | +25.4 | strong |
| Put | 84000 | 147300 | 133720 | 798.3 | 83697 | 716.2 | 83202 | +582 | +82.1 | strong |
| Put | 84100 | 28300 | 27780 | 870.1 | 83689 | 769.5 | 83230 | +554 | +100.6 | strong |
| Put | 84200 | 22260 | 22140 | 937.8 | 83690 | 826.0 | 83262 | +522 | +111.8 | strong |
| Put | 84300 | 17220 | 15851 | 929.3 | 83760 | 883.8 | 83371 | +413 | +45.5 | strong |
| Put | 84400 | 11540 | 11521 | 1039.7 | 83713 | 932.7 | 83360 | +424 | +107.0 | strong |
| Put | 84500 | 16280 | 15864 | 1173.5 | 83645 | 1008.4 | 83327 | +457 | +165.1 | strong |
| Put | 84600 | 6680 | 6680 | 1171.8 | 83716 | 1060.7 | 83428 | +356 | +111.1 | medium |
| Put | 84700 | 3840 | 3840 | 1250.8 | 83710 | 1146.6 | 83449 | +335 | +104.2 | medium |
| Put | 84800 | 1940 | 1940 | 1336.4 | 83714 | 1210.2 | 83464 | +320 | +126.2 | medium |
| Put | 84900 | 1660 | 1660 | 1788.9 | 83306 | 1277.4 | 83111 | +673 | +511.5 | strong |
| Put | 85000 | 16660 | 14476 | 1692.4 | 83396 | 1355.0 | 83308 | +476 | +337.4 | strong |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 83000, strongest put writers at 83000; weakest call writers at -, weakest put writers at -. Covers 79% of near-money call OI and 82% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82800 | 320 | 100 | 1766.7 | 83023 | 1766.7 | 84567 | +781 | +0.0 | strong |
| Call | 83000 | 9120 | 8096 | 2170.1 | 83587 | 2330.0 | 85170 | +1384 | -159.9 | strong |
| Call | 83100 | 80 | 40 | 1607.8 | 83023 | 1786.2 | 84708 | +922 | -178.4 | strong |
| Call | 83200 | 120 | 15 | 2180.4 | 83732 | 2129.1 | 85380 | +1594 | +51.4 | strong |
| Call | 83300 | 40 | 40 | 1653.3 | 83117 | 1653.3 | 84953 | +1167 | +0.0 | strong |
| Call | 83400 | 120 | 109 | 1484.0 | 83023 | 2050.1 | 84884 | +1098 | -566.1 | strong |
| Call | 83500 | 740 | 394 | 1662.1 | 83261 | 2020.0 | 85162 | +1376 | -357.9 | strong |
| Call | 83600 | 260 | 260 | 1610.9 | 83438 | 1627.2 | 85211 | +1425 | -16.3 | strong |
| Call | 83700 | 420 | 420 | 1620.8 | 83414 | 1885.0 | 85321 | +1535 | -264.2 | strong |
| Call | 83800 | 160 | 160 | 1589.6 | 83424 | 1788.5 | 85390 | +1604 | -198.8 | strong |
| Call | 83900 | 660 | 620 | 1438.5 | 83244 | 1764.6 | 85339 | +1553 | -326.1 | strong |
| Call | 84000 | 1380 | 1380 | 1462.7 | 83353 | 1763.3 | 85463 | +1677 | -300.6 | strong |
| Call | 84100 | 60 | 60 | 1412.8 | 83406 | 1600.0 | 85513 | +1727 | -187.2 | strong |
| Call | 84200 | 720 | 703 | 1320.8 | 83321 | 1569.8 | 85521 | +1735 | -249.0 | strong |
| Call | 84300 | 40 | 40 | 1278.3 | 83117 | 1351.5 | 85578 | +1792 | -73.2 | strong |
| Call | 84500 | 240 | 240 | 1478.0 | 83773 | 1500.0 | 85978 | +2192 | -22.1 | strong |
| Call | 84600 | 20 | 20 | 1052.9 | 83137 | 1437.2 | 85653 | +1867 | -384.4 | strong |
| Call | 84700 | 120 | 120 | 1037.1 | 83172 | 1187.1 | 85737 | +1951 | -150.0 | strong |
| Call | 84800 | 100 | 100 | 1009.5 | 83203 | 1129.5 | 85810 | +2024 | -120.0 | strong |
| Call | 84900 | 80 | 80 | 969.8 | 83203 | 1249.2 | 85870 | +2084 | -279.4 | strong |
| Call | 85000 | 540 | 540 | 1075.6 | 83478 | 1217.5 | 86076 | +2290 | -141.9 | strong |
| Put | 82600 | 160 | 160 | 897.5 | 83853 | 897.5 | 81703 | +2083 | +0.0 | strong |
| Put | 82700 | 100 | 100 | 1182.2 | 83322 | 1018.2 | 81518 | +2268 | +164.0 | strong |
| Put | 82800 | 260 | 260 | 1262.6 | 83210 | 1227.2 | 81537 | +2249 | +35.3 | strong |
| Put | 82900 | 180 | 180 | 1342.9 | 83166 | 1263.3 | 81557 | +2229 | +79.5 | strong |
| Put | 83000 | 9080 | 8196 | 1270.8 | 83332 | 1055.2 | 81729 | +2057 | +215.7 | strong |
| Put | 83100 | 280 | 280 | 1392.0 | 83168 | 1057.5 | 81708 | +2078 | +334.6 | strong |
| Put | 83200 | 480 | 480 | 1428.8 | 83156 | 1266.2 | 81771 | +2015 | +162.6 | strong |
| Put | 83300 | 440 | 440 | 1514.9 | 83101 | 1379.7 | 81785 | +2001 | +135.3 | strong |
| Put | 83400 | 600 | 600 | 1508.2 | 83205 | 1251.2 | 81892 | +1894 | +257.0 | strong |
| Put | 83500 | 1860 | 1391 | 1534.8 | 83252 | 1225.0 | 81965 | +1821 | +309.8 | strong |
| Put | 83600 | 740 | 740 | 1561.4 | 83257 | 1331.0 | 82039 | +1747 | +230.5 | strong |
| Put | 83700 | 660 | 660 | 1559.8 | 83353 | 1378.9 | 82140 | +1646 | +180.9 | strong |
| Put | 83800 | 260 | 260 | 1445.6 | 83657 | 1358.5 | 82354 | +1432 | +87.1 | strong |
| Put | 83900 | 380 | 360 | 1435.8 | 83751 | 1392.2 | 82464 | +1322 | +43.6 | strong |
| Put | 84000 | 900 | 900 | 1522.7 | 83663 | 1364.7 | 82477 | +1309 | +158.0 | strong |
| Put | 84100 | 620 | 620 | 1528.8 | 83779 | 1470.7 | 82571 | +1215 | +58.1 | strong |
| Put | 84200 | 760 | 760 | 1543.4 | 83792 | 1519.2 | 82657 | +1129 | +24.2 | strong |
| Put | 84300 | 920 | 920 | 1619.5 | 83773 | 1565.7 | 82681 | +1105 | +53.8 | strong |
| Put | 84400 | 920 | 920 | 1662.5 | 83800 | 1612.5 | 82737 | +1049 | +50.0 | strong |
| Put | 84500 | 540 | 540 | 1719.5 | 83724 | 1650.2 | 82780 | +1005 | +69.2 | strong |
| Put | 84600 | 260 | 260 | 1910.0 | 83558 | 1644.2 | 82690 | +1096 | +265.9 | strong |
| Put | 84700 | 220 | 220 | 1959.9 | 83572 | 1820.5 | 82740 | +1046 | +139.4 | strong |
| Put | 84800 | 100 | 100 | 2170.5 | 83203 | 2170.5 | 82630 | +1156 | +0.0 | strong |
| Put | 84900 | 140 | 140 | 2229.6 | 83379 | 1947.0 | 82670 | +1116 | +282.5 | strong |
| Put | 85000 | 1320 | 1320 | 1991.6 | 83702 | 1916.6 | 83008 | +778 | +75.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.04% | +0.01 to +0.06% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.77% | +0.73 to +0.81% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 50% | -0.04% | -0.13 to +0.06% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.75% | +0.70 to +0.80% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.32% | +0.32 to +0.32% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.93% | +0.93 to +0.93% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.92% | +0.92 to +0.92% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.70% | +0.70 to +0.70% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.92% | +0.92 to +0.92% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.32% | +0.32 to +0.32% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.00% | +0.00 to +0.00% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.73% | +0.73 to +0.73% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.93% | +0.93 to +0.93% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put and call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 10 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · few weak writers | 6 | 100% | +0.82% | too few (5/10) |
| intraday | weekly | writers even · weak calls | 5 | 80% | +0.07% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.75% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts | 1 | 100% | +1.50% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 2 | 100% | +0.92% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +0.92% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 10 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 6 | 100% | +0.82% | too few (5/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 5 | 80% | +0.07% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.75% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 | 100% | +1.50% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.92% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +0.92% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
