# Sensex option chain pattern log
Updated 2026-11-20 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 16 snapshots over 2 trading days
- 29 patterns logged; 21 different patterns so far

## Latest read (2026-11-20 15:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 6.0 | 83920 | 1.052 | 83200 | 81500 | 84500 | ±1.55% (82621-85218) | 15.12 |
| 2026-12-31 (monthly) | 41.0 | 83920 | 1.102 | 83000 | 83000 | 87900 | ±3.85% (80687-87152) | 14.29 |

- **Weekly, last 30 min**: `PCR up · unwinding · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 6 times before; Sensex was up after it 100% of the time, average +0.84%. Too few outcomes (6/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 6 times before; Sensex was up after it 100% of the time, average +0.84%. Too few outcomes (6/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put writing · walls same · near put wall`. Seen 2 times before; Sensex was up after it 100% of the time, average +0.20%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 11 times before; Sensex was up after it 90% of the time, average +0.43%. Too few outcomes (10/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 11 times before; Sensex was up after it 90% of the time, average +0.43%. Too few outcomes (10/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 1 times before; Sensex was up after it 100% of the time, average +1.08%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 100% of the time, average +1.08%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 84500, strongest put writers at 81500; weakest call writers at 83000, weakest put writers at 85400. Covers 77% of near-money call OI and 78% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82700 | 64500 | 50209 | 791.0 | 83023 | 1380.8 | 83491 | -429 | -589.9 | weak |
| Call | 82800 | 139760 | 101393 | 733.3 | 83023 | 1312.5 | 83533 | -386 | -579.2 | weak |
| Call | 82900 | 82240 | 58015 | 688.0 | 83022 | 1253.2 | 83588 | -332 | -565.2 | weak |
| Call | 83000 | 215180 | 126766 | 662.5 | 83020 | 1180.0 | 83662 | -257 | -517.5 | weak |
| Call | 83100 | 83280 | 73578 | 633.5 | 83044 | 1117.3 | 83734 | -186 | -483.8 | weak |
| Call | 83200 | 58620 | 53335 | 598.5 | 83094 | 1030.0 | 83799 | -121 | -431.5 | weak |
| Call | 83300 | 51320 | 46560 | 544.6 | 83072 | 970.5 | 83845 | -75 | -425.8 | weak |
| Call | 83400 | 63940 | 54589 | 574.0 | 83204 | 911.2 | 83974 | +54 | -337.1 | weak |
| Call | 83500 | 144060 | 102212 | 554.8 | 83253 | 835.9 | 84055 | +135 | -281.1 | weak |
| Call | 83600 | 51900 | 46416 | 518.2 | 83264 | 785.1 | 84118 | +199 | -266.9 | medium |
| Call | 83700 | 101840 | 94420 | 597.5 | 83502 | 720.0 | 84298 | +378 | -122.5 | strong |
| Call | 83800 | 166260 | 151352 | 562.8 | 83523 | 675.6 | 84363 | +443 | -112.8 | strong |
| Call | 83900 | 174800 | 165882 | 537.8 | 83553 | 618.3 | 84438 | +518 | -80.5 | strong |
| Call | 84000 | 381760 | 268378 | 385.4 | 83286 | 575.5 | 84385 | +466 | -190.1 | strong |
| Call | 84100 | 95680 | 86272 | 395.4 | 83401 | 522.9 | 84495 | +576 | -127.5 | strong |
| Call | 84200 | 75080 | 68632 | 386.6 | 83464 | 491.8 | 84587 | +667 | -105.1 | strong |
| Call | 84300 | 100600 | 91196 | 306.8 | 83364 | 440.2 | 84607 | +687 | -133.4 | strong |
| Call | 84400 | 53460 | 44914 | 285.9 | 83339 | 405.9 | 84686 | +766 | -120.0 | strong |
| Call | 84500 | 563000 | 478121 | 361.8 | 83748 | 377.1 | 84862 | +942 | -15.3 | strong |
| Call | 84600 | 60440 | 54949 | 254.9 | 83400 | 347.5 | 84855 | +935 | -92.6 | strong |
| Call | 84700 | 61700 | 52932 | 236.0 | 83431 | 318.2 | 84936 | +1016 | -82.2 | strong |
| Call | 84800 | 139320 | 127415 | 228.9 | 83558 | 283.9 | 85029 | +1109 | -55.0 | strong |
| Call | 84900 | 104840 | 83976 | 182.3 | 83399 | 261.2 | 85082 | +1163 | -79.0 | strong |
| Call | 85000 | 310420 | 195924 | 141.0 | 83224 | 234.2 | 85141 | +1221 | -93.2 | strong |
| Call | 85100 | 56700 | 49163 | 126.3 | 83198 | 215.8 | 85226 | +1307 | -89.5 | strong |
| Put | 82700 | 223640 | 194023 | 465.6 | 83253 | 255.0 | 82234 | +1685 | +210.6 | strong |
| Put | 82800 | 264360 | 195503 | 593.2 | 83034 | 281.0 | 82207 | +1713 | +312.2 | strong |
| Put | 82900 | 120420 | 96364 | 628.5 | 83049 | 307.4 | 82272 | +1648 | +321.1 | strong |
| Put | 83000 | 428080 | 275756 | 627.5 | 83098 | 331.7 | 82372 | +1547 | +295.8 | strong |
| Put | 83100 | 195000 | 184781 | 609.1 | 83236 | 362.3 | 82491 | +1429 | +246.8 | strong |
| Put | 83200 | 132860 | 126879 | 671.4 | 83195 | 388.0 | 82529 | +1391 | +283.4 | strong |
| Put | 83300 | 99380 | 94566 | 658.4 | 83332 | 424.4 | 82642 | +1278 | +234.0 | strong |
| Put | 83400 | 97360 | 93888 | 673.3 | 83417 | 449.4 | 82727 | +1193 | +223.8 | strong |
| Put | 83500 | 267200 | 253607 | 638.5 | 83561 | 498.0 | 82862 | +1058 | +140.5 | strong |
| Put | 83600 | 100720 | 98243 | 635.3 | 83658 | 539.5 | 82965 | +955 | +95.8 | strong |
| Put | 83700 | 171200 | 168012 | 653.8 | 83699 | 585.0 | 83046 | +873 | +68.8 | strong |
| Put | 83800 | 198700 | 195692 | 651.5 | 83768 | 625.0 | 83149 | +771 | +26.5 | strong |
| Put | 83900 | 200480 | 197120 | 682.1 | 83798 | 680.0 | 83218 | +702 | +2.1 | strong |
| Put | 84000 | 200020 | 186440 | 759.0 | 83774 | 721.5 | 83241 | +679 | +37.5 | strong |
| Put | 84100 | 26480 | 26041 | 852.6 | 83718 | 815.5 | 83247 | +672 | +37.2 | strong |
| Put | 84200 | 20760 | 20654 | 927.7 | 83705 | 846.9 | 83272 | +647 | +80.8 | strong |
| Put | 84300 | 17000 | 15932 | 901.4 | 83809 | 905.9 | 83399 | +521 | -4.5 | strong |
| Put | 84400 | 11740 | 11722 | 1028.4 | 83730 | 969.5 | 83372 | +548 | +58.9 | strong |
| Put | 84500 | 22980 | 22564 | 1122.7 | 83732 | 1039.8 | 83377 | +542 | +82.8 | strong |
| Put | 84600 | 6480 | 6480 | 1169.6 | 83719 | 1063.0 | 83430 | +489 | +106.6 | strong |
| Put | 84700 | 3960 | 3960 | 1245.7 | 83717 | 1135.6 | 83454 | +465 | +110.1 | strong |
| Put | 84800 | 2600 | 2600 | 1287.0 | 83778 | 1214.5 | 83513 | +407 | +72.5 | strong |
| Put | 84900 | 1940 | 1940 | 1716.0 | 83396 | 1300.0 | 83184 | +736 | +416.0 | strong |
| Put | 85000 | 16280 | 14229 | 1673.4 | 83423 | 1375.0 | 83327 | +593 | +298.4 | strong |
| Put | 85100 | 940 | 940 | 1777.3 | 83549 | 1399.6 | 83323 | +597 | +377.7 | strong |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 83000, strongest put writers at 83000; weakest call writers at -, weakest put writers at -. Covers 81% of near-money call OI and 83% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82800 | 320 | 100 | 1766.7 | 83023 | 1766.7 | 84567 | +647 | +0.0 | strong |
| Call | 83000 | 9360 | 8342 | 2176.3 | 83599 | 2340.3 | 85176 | +1257 | -164.0 | strong |
| Call | 83100 | 80 | 40 | 1607.8 | 83023 | 1786.2 | 84708 | +788 | -178.4 | strong |
| Call | 83200 | 120 | 15 | 2180.4 | 83732 | 2129.1 | 85380 | +1461 | +51.4 | strong |
| Call | 83300 | 40 | 40 | 1653.3 | 83117 | 1653.3 | 84953 | +1034 | +0.0 | strong |
| Call | 83400 | 120 | 109 | 1484.0 | 83023 | 2050.1 | 84884 | +964 | -566.1 | strong |
| Call | 83500 | 720 | 383 | 1662.1 | 83261 | 2060.7 | 85162 | +1242 | -398.6 | strong |
| Call | 83600 | 260 | 260 | 1610.9 | 83438 | 1627.2 | 85211 | +1291 | -16.3 | strong |
| Call | 83700 | 360 | 360 | 1620.8 | 83414 | 1957.8 | 85321 | +1401 | -337.0 | strong |
| Call | 83800 | 160 | 160 | 1589.6 | 83424 | 1788.5 | 85390 | +1470 | -198.8 | strong |
| Call | 83900 | 600 | 564 | 1438.5 | 83244 | 1840.2 | 85339 | +1419 | -401.7 | strong |
| Call | 84000 | 1680 | 1680 | 1515.7 | 83454 | 1759.6 | 85516 | +1596 | -243.9 | strong |
| Call | 84100 | 60 | 60 | 1412.8 | 83406 | 1600.0 | 85513 | +1593 | -187.2 | strong |
| Call | 84200 | 720 | 703 | 1320.8 | 83321 | 1692.3 | 85521 | +1601 | -371.5 | strong |
| Call | 84300 | 40 | 40 | 1278.3 | 83117 | 1619.8 | 85578 | +1659 | -341.4 | strong |
| Call | 84500 | 660 | 660 | 1507.9 | 83905 | 1525.0 | 86008 | +2088 | -17.1 | strong |
| Call | 84600 | 20 | 20 | 1052.9 | 83137 | 1437.2 | 85653 | +1733 | -384.4 | strong |
| Call | 84700 | 120 | 120 | 1037.1 | 83172 | 1401.1 | 85737 | +1817 | -364.0 | strong |
| Call | 84800 | 100 | 100 | 1009.5 | 83203 | 1129.5 | 85810 | +1890 | -120.0 | strong |
| Call | 84900 | 80 | 80 | 969.8 | 83203 | 1309.3 | 85870 | +1950 | -339.6 | strong |
| Call | 85000 | 580 | 580 | 1087.9 | 83513 | 1237.8 | 86088 | +2168 | -149.9 | strong |
| Put | 82700 | 100 | 100 | 1182.2 | 83322 | 903.0 | 81518 | +2402 | +279.3 | strong |
| Put | 82800 | 240 | 240 | 1262.6 | 83210 | 986.2 | 81537 | +2382 | +276.4 | strong |
| Put | 82900 | 180 | 180 | 1342.9 | 83166 | 1263.3 | 81557 | +2363 | +79.5 | strong |
| Put | 83000 | 9040 | 8165 | 1269.0 | 83336 | 1035.0 | 81731 | +2189 | +234.0 | strong |
| Put | 83100 | 280 | 280 | 1392.0 | 83168 | 1057.5 | 81708 | +2212 | +334.6 | strong |
| Put | 83200 | 480 | 480 | 1428.8 | 83156 | 1266.2 | 81771 | +2149 | +162.6 | strong |
| Put | 83300 | 440 | 440 | 1514.9 | 83101 | 1379.7 | 81785 | +2135 | +135.3 | strong |
| Put | 83400 | 600 | 600 | 1508.2 | 83205 | 1251.2 | 81892 | +2028 | +257.0 | strong |
| Put | 83500 | 2040 | 1571 | 1498.2 | 83329 | 1215.3 | 82002 | +1918 | +282.9 | strong |
| Put | 83600 | 740 | 740 | 1561.4 | 83257 | 1331.0 | 82039 | +1881 | +230.5 | strong |
| Put | 83700 | 660 | 660 | 1559.8 | 83353 | 1378.9 | 82140 | +1779 | +180.9 | strong |
| Put | 83800 | 260 | 260 | 1445.6 | 83657 | 1358.5 | 82354 | +1565 | +87.1 | strong |
| Put | 83900 | 380 | 360 | 1435.8 | 83751 | 1392.2 | 82464 | +1455 | +43.6 | strong |
| Put | 84000 | 920 | 920 | 1520.7 | 83670 | 1432.0 | 82479 | +1440 | +88.7 | strong |
| Put | 84100 | 620 | 620 | 1528.8 | 83779 | 1470.7 | 82571 | +1348 | +58.1 | strong |
| Put | 84200 | 800 | 800 | 1541.5 | 83800 | 1505.9 | 82659 | +1261 | +35.6 | strong |
| Put | 84300 | 940 | 940 | 1618.0 | 83777 | 1550.5 | 82682 | +1238 | +67.4 | strong |
| Put | 84400 | 980 | 980 | 1657.6 | 83810 | 1588.0 | 82742 | +1177 | +69.6 | strong |
| Put | 84500 | 820 | 820 | 1683.1 | 83808 | 1650.8 | 82817 | +1103 | +32.3 | strong |
| Put | 84600 | 400 | 400 | 1820.1 | 83706 | 1648.8 | 82780 | +1140 | +171.3 | strong |
| Put | 84700 | 220 | 220 | 1959.9 | 83572 | 1820.5 | 82740 | +1180 | +139.4 | strong |
| Put | 84800 | 100 | 100 | 2170.5 | 83203 | 2170.5 | 82630 | +1290 | +0.0 | strong |
| Put | 84900 | 140 | 140 | 2229.6 | 83379 | 1947.0 | 82670 | +1249 | +282.5 | strong |
| Put | 85000 | 1600 | 1600 | 1966.4 | 83751 | 1848.0 | 83034 | +886 | +118.4 | strong |
| Put | 85100 | 100 | 100 | 2157.7 | 83558 | 2157.7 | 82942 | +977 | +0.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls same · near put wall | 3 | 100% | +0.20% | +0.17 to +0.22% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 3 | 67% | +0.04% | -0.07 to +0.16% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.86% | +0.86 to +0.86% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 12 | 90% | +0.43% | up |
| intraday | weekly | writers even · few weak writers | 7 | 100% | +0.84% | too few (6/10) |
| intraday | weekly | writers even · weak calls | 6 | 83% | +0.18% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.91% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts | 1 | 100% | +1.66% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 2 | 100% | +1.08% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 12 | 90% | +0.43% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 7 | 100% | +0.84% | too few (6/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 6 | 83% | +0.18% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.91% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 100% | +1.08% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
