# Sensex option chain pattern log
Updated 2026-11-25 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 52 snapshots over 5 trading days
- 101 patterns logged; 47 different patterns so far

## Latest read (2026-11-25 12:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 1.1 | 83923 | 0.954 | 84000 | 83000 | 85000 | ±1.12% (82982-84864) | 25.41 |
| 2026-12-31 (monthly) | 36.1 | 83923 | 1.291 | 84000 | 83000 | 87900 | ±2.97% (81427-86419) | 11.73 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 30 times before; Sensex was up after it 57% of the time, average +0.04%. Too few outcomes (14/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 12 times before; Sensex was up after it 55% of the time, average +0.05%. Too few outcomes (11/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 50% of the time, average +0.02%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 0% of the time, average -1.77%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR down · call writing · walls same · near put wall`. Seen 4 times before; Sensex was up after it 50% of the time, average -0.14%. Too few outcomes (4/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 20 times before; Sensex was up after it 67% of the time, average -0.03%. Too few outcomes (18/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 16 times before; Sensex was up after it 64% of the time, average -0.05%. Too few outcomes (14/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 83000; weakest call writers at 83500, weakest put writers at 84200. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82700 | 138640 | 131676 | 644.2 | 82789 | 1361.9 | 83344 | -579 | -717.7 | weak |
| Call | 82800 | 132120 | 121642 | 617.7 | 82842 | 1259.9 | 83418 | -505 | -642.2 | weak |
| Call | 82900 | 96020 | 88616 | 622.4 | 82936 | 1179.5 | 83522 | -401 | -557.1 | weak |
| Call | 83000 | 228100 | 201888 | 578.7 | 82926 | 1110.5 | 83579 | -344 | -531.8 | weak |
| Call | 83100 | 89020 | 86021 | 619.3 | 83112 | 1021.5 | 83719 | -204 | -402.2 | weak |
| Call | 83200 | 86760 | 85480 | 622.6 | 83215 | 956.9 | 83823 | -101 | -334.2 | weak |
| Call | 83300 | 73180 | 72187 | 597.6 | 83273 | 879.1 | 83898 | -26 | -281.5 | weak |
| Call | 83400 | 104140 | 101665 | 607.6 | 83359 | 808.9 | 84008 | +85 | -201.2 | weak |
| Call | 83500 | 364080 | 347716 | 512.9 | 83236 | 741.2 | 84013 | +90 | -228.3 | weak |
| Call | 83600 | 141360 | 139687 | 511.4 | 83352 | 677.4 | 84111 | +188 | -166.0 | medium |
| Call | 83700 | 248380 | 246479 | 531.5 | 83713 | 617.9 | 84232 | +308 | -86.3 | medium |
| Call | 83800 | 469880 | 466864 | 473.4 | 83776 | 557.5 | 84273 | +350 | -84.1 | medium |
| Call | 83900 | 619220 | 616872 | 438.9 | 83795 | 505.4 | 84339 | +416 | -66.5 | strong |
| Call | 84000 | 1513260 | 1468556 | 366.9 | 83583 | 453.6 | 84367 | +444 | -86.8 | strong |
| Call | 84100 | 754380 | 750819 | 372.2 | 83814 | 407.0 | 84472 | +549 | -34.8 | strong |
| Call | 84200 | 962740 | 959310 | 340.1 | 83794 | 361.9 | 84540 | +617 | -21.8 | strong |
| Call | 84300 | 1018880 | 1011458 | 326.3 | 83836 | 325.3 | 84626 | +703 | +1.0 | strong |
| Call | 84400 | 1098500 | 1092042 | 337.5 | 83904 | 288.0 | 84737 | +814 | +49.5 | strong |
| Call | 84500 | 2160140 | 2088390 | 279.2 | 83745 | 251.8 | 84779 | +856 | +27.4 | strong |
| Call | 84600 | 1010740 | 1006155 | 265.9 | 83831 | 223.4 | 84866 | +943 | +42.5 | strong |
| Call | 84700 | 789160 | 781491 | 211.4 | 83732 | 194.6 | 84911 | +988 | +16.9 | strong |
| Call | 84800 | 875220 | 864718 | 175.8 | 83636 | 171.1 | 84976 | +1053 | +4.8 | strong |
| Call | 84900 | 727660 | 712704 | 161.4 | 83768 | 148.3 | 85061 | +1138 | +13.1 | strong |
| Call | 85000 | 2832340 | 2736574 | 128.8 | 83630 | 130.3 | 85129 | +1206 | -1.5 | strong |
| Call | 85100 | 703140 | 698817 | 102.9 | 83784 | 111.4 | 85203 | +1280 | -8.5 | strong |
| Put | 82700 | 606300 | 596524 | 176.1 | 83807 | 95.7 | 82524 | +1399 | +80.4 | strong |
| Put | 82800 | 597360 | 577426 | 169.1 | 83812 | 111.1 | 82631 | +1292 | +58.0 | strong |
| Put | 82900 | 421740 | 413674 | 195.9 | 83801 | 127.6 | 82704 | +1219 | +68.3 | strong |
| Put | 83000 | 2521540 | 2430173 | 177.6 | 83844 | 145.8 | 82822 | +1101 | +31.8 | strong |
| Put | 83100 | 443960 | 442025 | 216.7 | 83793 | 165.4 | 82883 | +1040 | +51.2 | strong |
| Put | 83200 | 554140 | 552765 | 226.5 | 83850 | 190.0 | 82974 | +950 | +36.5 | strong |
| Put | 83300 | 552600 | 551613 | 254.4 | 83839 | 215.6 | 83046 | +878 | +38.8 | strong |
| Put | 83400 | 576960 | 576066 | 271.9 | 83893 | 243.0 | 83128 | +795 | +28.9 | strong |
| Put | 83500 | 1760180 | 1754783 | 312.9 | 83844 | 276.6 | 83187 | +736 | +36.3 | strong |
| Put | 83600 | 654040 | 653448 | 331.1 | 83859 | 312.4 | 83269 | +654 | +18.7 | strong |
| Put | 83700 | 995700 | 994792 | 387.0 | 83810 | 350.1 | 83313 | +610 | +36.9 | strong |
| Put | 83800 | 1381340 | 1380316 | 424.8 | 83826 | 391.2 | 83375 | +548 | +33.6 | strong |
| Put | 83900 | 1253860 | 1252470 | 425.6 | 83925 | 435.9 | 83474 | +449 | -10.3 | strong |
| Put | 84000 | 1922080 | 1917024 | 400.9 | 84058 | 486.8 | 83599 | +324 | -85.9 | medium |
| Put | 84100 | 609100 | 608984 | 374.0 | 84183 | 537.5 | 83726 | +197 | -163.6 | medium |
| Put | 84200 | 571900 | 571865 | 392.5 | 84234 | 595.6 | 83808 | +116 | -203.1 | weak |
| Put | 84300 | 411740 | 411398 | 404.5 | 84304 | 655.4 | 83896 | +28 | -250.9 | weak |
| Put | 84400 | 445340 | 445335 | 438.3 | 84332 | 721.4 | 83962 | -39 | -283.0 | weak |
| Put | 84500 | 543140 | 543024 | 533.2 | 84281 | 784.8 | 83967 | -44 | -251.5 | weak |
| Put | 84600 | 186780 | 186780 | 615.7 | 84268 | 855.0 | 83984 | -61 | -239.3 | weak |
| Put | 84700 | 63340 | 63340 | 860.6 | 84059 | 929.0 | 83839 | +84 | -68.4 | weak |
| Put | 84800 | 65180 | 65180 | 703.7 | 84268 | 1006.8 | 84096 | -173 | -303.1 | weak |
| Put | 84900 | 34080 | 34080 | 859.6 | 84180 | 1095.0 | 84040 | -117 | -235.4 | weak |
| Put | 85000 | 182760 | 181340 | 926.5 | 84182 | 1164.5 | 84074 | -150 | -238.0 | weak |
| Put | 85100 | 8020 | 8020 | 983.8 | 84222 | 1246.5 | 84116 | -193 | -262.7 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 86000, strongest put writers at 83000; weakest call writers at -, weakest put writers at 86000. Covers 94% of near-money call OI and 95% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +622 | -732.3 | strong |
| Call | 82800 | 1460 | 1282 | 1854.8 | 82817 | 2861.0 | 84655 | +732 | -1006.2 | strong |
| Call | 82900 | 260 | 220 | 1609.0 | 82444 | 1609.0 | 84509 | +586 | +0.0 | strong |
| Call | 83000 | 2660 | 2516 | 1994.9 | 83236 | 2416.4 | 84995 | +1072 | -421.5 | strong |
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2304.1 | 84702 | +779 | -702.1 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +877 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +1157 | -335.1 | strong |
| Call | 83400 | 540 | 530 | 1578.4 | 83222 | 2450.2 | 84978 | +1055 | -871.7 | strong |
| Call | 83500 | 3680 | 3454 | 2075.5 | 83646 | 2301.4 | 85576 | +1652 | -225.9 | strong |
| Call | 83600 | 540 | 540 | 1550.3 | 83212 | 1273.7 | 85150 | +1227 | +276.6 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1880.9 | 85310 | +1387 | -271.0 | strong |
| Call | 83800 | 240 | 240 | 1548.8 | 83298 | 1792.1 | 85349 | +1426 | -243.3 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +1434 | +287.6 | strong |
| Call | 84000 | 2820 | 2820 | 1537.2 | 83442 | 1810.0 | 85537 | +1614 | -272.8 | strong |
| Call | 84100 | 380 | 380 | 1602.8 | 83682 | 2100.0 | 85703 | +1780 | -497.2 | strong |
| Call | 84200 | 520 | 511 | 1302.7 | 83213 | 1701.3 | 85503 | +1580 | -398.6 | strong |
| Call | 84300 | 60 | 60 | 1278.0 | 83161 | 1000.1 | 85578 | +1655 | +277.9 | strong |
| Call | 84400 | 280 | 280 | 1192.8 | 82934 | 963.2 | 85593 | +1670 | +229.6 | strong |
| Call | 84500 | 1320 | 1320 | 1438.4 | 83581 | 1577.7 | 85938 | +2015 | -139.3 | strong |
| Call | 84600 | 180 | 180 | 1198.9 | 83250 | 899.0 | 85799 | +1876 | +299.9 | strong |
| Call | 84700 | 560 | 560 | 1029.4 | 82892 | 853.5 | 85729 | +1806 | +175.8 | strong |
| Call | 84800 | 380 | 380 | 997.6 | 82976 | 831.0 | 85798 | +1874 | +166.6 | strong |
| Call | 84900 | 1080 | 1080 | 1049.3 | 83164 | 798.2 | 85949 | +2026 | +251.1 | strong |
| Call | 85000 | 3900 | 3900 | 1075.8 | 83374 | 1286.0 | 86076 | +2153 | -210.2 | strong |
| Call | 85100 | 320 | 320 | 929.9 | 83140 | 741.5 | 86030 | +2107 | +188.4 | strong |
| Put | 82700 | 320 | 320 | 955.9 | 83860 | 913.3 | 81744 | +2179 | +42.6 | strong |
| Put | 82800 | 120 | 120 | 967.8 | 83811 | 920.4 | 81832 | +2091 | +47.5 | strong |
| Put | 82900 | 100 | 100 | 1103.6 | 83606 | 975.9 | 81796 | +2127 | +127.7 | strong |
| Put | 83000 | 9480 | 8988 | 1149.4 | 83606 | 1067.7 | 81851 | +2073 | +81.7 | strong |
| Put | 83100 | 240 | 240 | 1300.9 | 83335 | 1109.8 | 81799 | +2124 | +191.1 | strong |
| Put | 83200 | 560 | 560 | 1379.9 | 83227 | 1111.5 | 81820 | +2103 | +268.4 | strong |
| Put | 83300 | 580 | 580 | 1488.2 | 83082 | 1000.9 | 81812 | +2111 | +487.4 | strong |
| Put | 83400 | 920 | 920 | 1401.2 | 83381 | 1127.0 | 81999 | +1924 | +274.3 | strong |
| Put | 83500 | 2360 | 2081 | 1370.7 | 83566 | 1209.5 | 82129 | +1794 | +161.3 | strong |
| Put | 83600 | 1240 | 1240 | 1521.0 | 83328 | 1942.0 | 82079 | +1844 | -421.0 | strong |
| Put | 83700 | 840 | 840 | 1566.8 | 83306 | 1177.0 | 82133 | +1790 | +389.8 | strong |
| Put | 83800 | 820 | 820 | 1503.2 | 83531 | 1150.0 | 82297 | +1626 | +353.2 | strong |
| Put | 83900 | 440 | 425 | 1519.5 | 83554 | 1325.8 | 82381 | +1543 | +193.6 | strong |
| Put | 84000 | 2940 | 2940 | 1430.1 | 83886 | 1420.0 | 82570 | +1353 | +10.1 | strong |
| Put | 84100 | 1160 | 1160 | 1559.2 | 83693 | 1422.8 | 82541 | +1382 | +136.4 | strong |
| Put | 84200 | 500 | 500 | 1522.9 | 83839 | 1515.7 | 82677 | +1246 | +7.2 | strong |
| Put | 84300 | 720 | 720 | 1621.6 | 83794 | 1486.2 | 82678 | +1245 | +135.3 | strong |
| Put | 84400 | 1500 | 1500 | 1798.4 | 83560 | 1520.0 | 82602 | +1322 | +278.4 | strong |
| Put | 84500 | 8640 | 8640 | 1481.1 | 84240 | 1640.3 | 83019 | +904 | -159.2 | strong |
| Put | 84600 | 800 | 800 | 1691.7 | 83917 | 1634.8 | 82908 | +1015 | +56.8 | strong |
| Put | 84700 | 560 | 560 | 1672.2 | 84036 | 1515.0 | 83028 | +895 | +157.1 | strong |
| Put | 84800 | 540 | 540 | 1673.6 | 84175 | 1586.3 | 83126 | +797 | +87.3 | strong |
| Put | 84900 | 680 | 680 | 2351.3 | 83032 | 1633.4 | 82549 | +1374 | +717.9 | strong |
| Put | 85000 | 3320 | 3320 | 2027.1 | 83711 | 1800.0 | 82973 | +950 | +227.1 | strong |
| Put | 85100 | 400 | 400 | 1964.5 | 83821 | 1646.2 | 83135 | +788 | +318.3 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 10 | 22% | -0.41% | -1.29 to +0.22% |  | too few (9/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 5 | 60% | -0.01% | -0.22 to +0.16% |  | too few (5/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 50% | -0.14% | -0.70 to +0.25% |  | too few (4/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.22% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 2 | 0% | -0.49% | -0.52 to -0.46% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.14% | -1.14 to +0.86% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 2 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 0% | -0.66% | -0.80 to -0.52% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.66% | -0.66 to -0.66% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 0% | -1.14% | -1.14 to -1.14% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.65% | -0.65 to -0.65% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 0% | -0.46% | -0.46 to -0.46% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.80% | +1.80 to +1.80% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.80% | +1.80 to +1.80% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 31 | 57% | +0.04% | no clear direction |
| intraday | monthly | writers even · few weak writers | 21 | 67% | -0.03% | no clear direction |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 4 | 0% | -0.82% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.08% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.52% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers | 4 | 50% | +0.02% | too few (2/10) |
| day | monthly | writers even · few weak writers | 3 | 50% | -0.34% | too few (2/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.80% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 67% | +0.00% | too few (3/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 17 | 64% | -0.05% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 13 | 55% | +0.05% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.22% | too few (7/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 4 | 75% | +0.02% | too few (4/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 4 | 0% | -0.82% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.52% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.08% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.52% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | -0.34% | too few (2/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.80% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.80% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 0% | -1.77% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
