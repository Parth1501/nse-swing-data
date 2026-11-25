# Sensex option chain pattern log
Updated 2026-11-25 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 48 snapshots over 5 trading days
- 93 patterns logged; 42 different patterns so far

## Latest read (2026-11-25 10:45:00)

Sensex trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 1.2 | 84116 | 0.94 | 83900 | 83000 | 85000 | ±1.01% (83266-84967) | 21.99 |
| 2026-12-31 (monthly) | 36.2 | 84119 | 1.277 | 83600 | 83000 | 87900 | ±3.59% (81103-87135) | 14.12 |

- **Weekly, last 30 min**: `PCR up · put writing · walls same · mid walls`. Seen 2 times before; Sensex was up after it 0% of the time, average -0.43%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 27 times before; Sensex was up after it 73% of the time, average +0.21%. Too few outcomes (11/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 17 times before; Sensex was up after it 100% of the time, average +0.35%. Too few outcomes (2/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 50% of the time, average +0.14%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 2 times before; Sensex was up after it 100% of the time, average +2.04%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR up · put writing · walls same · near put wall`. Seen 9 times before; Sensex was up after it 25% of the time, average -0.43%. Too few outcomes (8/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 17 times before; Sensex was up after it 80% of the time, average +0.10%. Too few outcomes (15/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 3 times before; Sensex was up after it 100% of the time, average +0.34%. Too few outcomes (3/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 83000; weakest call writers at 83800, weakest put writers at -. Covers 97% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82900 | 103560 | 95574 | 622.4 | 82936 | 1375.7 | 83522 | -594 | -753.3 | weak |
| Call | 83000 | 266400 | 235733 | 577.6 | 82924 | 1272.4 | 83578 | -539 | -694.8 | weak |
| Call | 83100 | 104560 | 101038 | 619.3 | 83112 | 1192.2 | 83719 | -397 | -572.8 | weak |
| Call | 83200 | 106760 | 105167 | 618.8 | 83207 | 1103.0 | 83819 | -298 | -484.2 | weak |
| Call | 83300 | 102320 | 100816 | 573.9 | 83218 | 1021.7 | 83874 | -243 | -447.9 | weak |
| Call | 83400 | 132260 | 128846 | 581.3 | 83300 | 942.9 | 83981 | -135 | -361.6 | weak |
| Call | 83500 | 495440 | 473172 | 512.9 | 83236 | 863.1 | 84013 | -104 | -350.2 | weak |
| Call | 83600 | 223120 | 220479 | 511.4 | 83352 | 791.5 | 84111 | -5 | -280.0 | weak |
| Call | 83700 | 455380 | 451418 | 519.6 | 83684 | 719.0 | 84220 | +103 | -199.4 | weak |
| Call | 83800 | 936160 | 929141 | 459.1 | 83751 | 650.9 | 84259 | +143 | -191.8 | weak |
| Call | 83900 | 942120 | 937397 | 417.3 | 83754 | 586.1 | 84317 | +201 | -168.8 | medium |
| Call | 84000 | 2020240 | 1935957 | 329.5 | 83437 | 527.3 | 84330 | +213 | -197.8 | medium |
| Call | 84100 | 971140 | 962079 | 333.2 | 83700 | 470.2 | 84433 | +317 | -137.0 | medium |
| Call | 84200 | 1121100 | 1115315 | 294.4 | 83675 | 419.1 | 84494 | +378 | -124.7 | medium |
| Call | 84300 | 769960 | 761665 | 271.2 | 83688 | 368.9 | 84571 | +455 | -97.7 | strong |
| Call | 84400 | 666440 | 659982 | 242.4 | 83635 | 324.1 | 84642 | +526 | -81.6 | strong |
| Call | 84500 | 1707580 | 1628909 | 230.7 | 83541 | 283.9 | 84731 | +614 | -53.3 | strong |
| Call | 84600 | 595080 | 590495 | 200.7 | 83532 | 247.2 | 84801 | +684 | -46.5 | strong |
| Call | 84700 | 583700 | 576031 | 165.1 | 83525 | 213.7 | 84865 | +749 | -48.5 | strong |
| Call | 84800 | 614940 | 604438 | 128.7 | 83364 | 184.3 | 84929 | +812 | -55.6 | strong |
| Call | 84900 | 574220 | 557745 | 107.6 | 83505 | 157.6 | 85008 | +891 | -50.0 | strong |
| Call | 85000 | 2607740 | 2499199 | 106.9 | 83477 | 133.8 | 85107 | +990 | -27.0 | strong |
| Call | 85100 | 599400 | 594491 | 84.9 | 83671 | 113.9 | 85185 | +1068 | -29.0 | strong |
| Call | 85200 | 643280 | 636713 | 81.9 | 83578 | 95.8 | 85282 | +1165 | -14.0 | strong |
| Call | 85300 | 672460 | 670141 | 62.5 | 83618 | 80.0 | 85362 | +1246 | -17.6 | strong |
| Put | 82900 | 511300 | 500225 | 215.3 | 83714 | 76.0 | 82685 | +1432 | +139.3 | strong |
| Put | 83000 | 2885260 | 2769300 | 190.8 | 83778 | 88.0 | 82809 | +1307 | +102.7 | strong |
| Put | 83100 | 541020 | 538413 | 232.6 | 83721 | 101.4 | 82867 | +1249 | +131.2 | strong |
| Put | 83200 | 711480 | 709510 | 242.4 | 83791 | 116.2 | 82958 | +1159 | +126.2 | strong |
| Put | 83300 | 662960 | 661688 | 265.8 | 83800 | 133.9 | 83034 | +1082 | +131.9 | strong |
| Put | 83400 | 637960 | 636714 | 315.6 | 83755 | 154.2 | 83084 | +1032 | +161.4 | strong |
| Put | 83500 | 2136760 | 2129761 | 325.8 | 83805 | 177.1 | 83174 | +942 | +148.7 | strong |
| Put | 83600 | 983520 | 982615 | 334.4 | 83849 | 202.2 | 83266 | +851 | +132.2 | strong |
| Put | 83700 | 1481900 | 1480549 | 387.0 | 83810 | 230.3 | 83313 | +803 | +156.7 | strong |
| Put | 83800 | 2022300 | 2020750 | 432.8 | 83808 | 262.4 | 83367 | +749 | +170.3 | strong |
| Put | 83900 | 1468240 | 1466401 | 452.1 | 83869 | 297.9 | 83448 | +669 | +154.2 | strong |
| Put | 84000 | 1955840 | 1948771 | 457.5 | 83944 | 337.1 | 83542 | +574 | +120.4 | strong |
| Put | 84100 | 578120 | 577926 | 449.6 | 84032 | 380.2 | 83650 | +466 | +69.4 | strong |
| Put | 84200 | 327140 | 327076 | 551.3 | 83971 | 428.4 | 83649 | +468 | +122.9 | strong |
| Put | 84300 | 154620 | 153877 | 672.7 | 83929 | 478.9 | 83627 | +489 | +193.8 | strong |
| Put | 84400 | 133880 | 133870 | 829.9 | 83837 | 534.3 | 83570 | +546 | +295.6 | strong |
| Put | 84500 | 221060 | 220846 | 916.1 | 83836 | 594.2 | 83584 | +533 | +321.9 | strong |
| Put | 84600 | 54360 | 54360 | 1195.7 | 83651 | 658.2 | 83404 | +712 | +537.4 | strong |
| Put | 84700 | 40700 | 40700 | 1240.8 | 83662 | 723.1 | 83459 | +657 | +517.6 | strong |
| Put | 84800 | 26280 | 26280 | 946.6 | 83986 | 790.0 | 83853 | +263 | +156.6 | medium |
| Put | 84900 | 16960 | 16960 | 1226.5 | 83785 | 866.2 | 83673 | +443 | +360.3 | strong |
| Put | 85000 | 74320 | 72530 | 1413.3 | 83670 | 945.4 | 83587 | +530 | +467.9 | strong |
| Put | 85100 | 4100 | 4100 | 1357.8 | 83860 | 1032.0 | 83742 | +374 | +325.9 | medium |
| Put | 85200 | 4220 | 4220 | 1452.9 | 83840 | 1103.7 | 83747 | +369 | +349.2 | medium |
| Put | 85300 | 14580 | 1462 | 2168.5 | 83235 | 1194.0 | 83131 | +985 | +974.5 | strong |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 86000, strongest put writers at 83000; weakest call writers at -, weakest put writers at -. Covers 95% of near-money call OI and 95% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82900 | 260 | 220 | 1609.0 | 82444 | 1609.0 | 84509 | +390 | +0.0 | strong |
| Call | 83000 | 2460 | 2314 | 1922.9 | 83128 | 2519.8 | 84923 | +804 | -596.9 | strong |
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2304.1 | 84702 | +583 | -702.1 | strong |
| Call | 83200 | 560 | 455 | 1599.7 | 82751 | 1444.6 | 84800 | +681 | +155.1 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +961 | -335.1 | strong |
| Call | 83400 | 540 | 530 | 1578.4 | 83222 | 2069.7 | 84978 | +859 | -491.2 | strong |
| Call | 83500 | 1320 | 1094 | 1570.0 | 82996 | 1962.3 | 85070 | +951 | -392.3 | strong |
| Call | 83600 | 540 | 540 | 1550.3 | 83212 | 1273.7 | 85150 | +1031 | +276.6 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1880.9 | 85310 | +1191 | -271.0 | strong |
| Call | 83800 | 240 | 240 | 1548.8 | 83298 | 1792.1 | 85349 | +1230 | -243.3 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +1238 | +287.6 | strong |
| Call | 84000 | 2420 | 2420 | 1473.3 | 83330 | 1870.2 | 85473 | +1354 | -397.0 | strong |
| Call | 84100 | 360 | 360 | 1575.2 | 83638 | 1653.4 | 85675 | +1556 | -78.2 | strong |
| Call | 84200 | 480 | 471 | 1260.8 | 83137 | 1575.0 | 85461 | +1342 | -314.2 | strong |
| Call | 84300 | 60 | 60 | 1278.0 | 83161 | 1000.1 | 85578 | +1459 | +277.9 | strong |
| Call | 84400 | 280 | 280 | 1192.8 | 82934 | 963.2 | 85593 | +1474 | +229.6 | strong |
| Call | 84500 | 740 | 740 | 1074.1 | 82831 | 1605.8 | 85574 | +1455 | -531.7 | strong |
| Call | 84600 | 180 | 180 | 1198.9 | 83250 | 899.0 | 85799 | +1680 | +299.9 | strong |
| Call | 84700 | 560 | 560 | 1029.4 | 82892 | 853.5 | 85729 | +1610 | +175.8 | strong |
| Call | 84800 | 380 | 380 | 997.6 | 82976 | 831.0 | 85798 | +1679 | +166.6 | strong |
| Call | 84900 | 1080 | 1080 | 1049.3 | 83164 | 798.2 | 85949 | +1830 | +251.1 | strong |
| Call | 85000 | 3900 | 3900 | 1042.5 | 83295 | 1335.5 | 86042 | +1923 | -293.0 | strong |
| Call | 85100 | 320 | 320 | 929.9 | 83140 | 741.5 | 86030 | +1911 | +188.4 | strong |
| Call | 85200 | 460 | 460 | 816.9 | 82858 | 718.1 | 86017 | +1898 | +98.8 | strong |
| Call | 85300 | 260 | 260 | 978.7 | 83594 | 1030.2 | 86279 | +2160 | -51.4 | strong |
| Put | 82900 | 500 | 500 | 1295.1 | 83129 | 951.0 | 81605 | +2514 | +344.0 | strong |
| Put | 83000 | 15260 | 14464 | 1150.9 | 83602 | 940.0 | 81849 | +2270 | +210.9 | strong |
| Put | 83100 | 480 | 480 | 1300.9 | 83335 | 1012.2 | 81799 | +2320 | +288.7 | strong |
| Put | 83200 | 920 | 920 | 1379.9 | 83227 | 1053.8 | 81820 | +2299 | +326.1 | strong |
| Put | 83300 | 880 | 880 | 1488.2 | 83082 | 1143.5 | 81812 | +2307 | +344.7 | strong |
| Put | 83400 | 1000 | 1000 | 1401.2 | 83381 | 1165.3 | 81999 | +2120 | +235.9 | strong |
| Put | 83500 | 2380 | 2049 | 1405.4 | 83488 | 1100.0 | 82095 | +2024 | +305.4 | strong |
| Put | 83600 | 1240 | 1240 | 1521.0 | 83328 | 1942.0 | 82079 | +2040 | -421.0 | strong |
| Put | 83700 | 840 | 840 | 1566.8 | 83306 | 1177.0 | 82133 | +1986 | +389.8 | strong |
| Put | 83800 | 780 | 780 | 1521.3 | 83488 | 1342.9 | 82279 | +1840 | +178.4 | strong |
| Put | 83900 | 440 | 425 | 1519.5 | 83554 | 1325.8 | 82381 | +1739 | +193.6 | strong |
| Put | 84000 | 3300 | 3300 | 1496.9 | 83737 | 1288.0 | 82503 | +1616 | +208.9 | strong |
| Put | 84100 | 1320 | 1320 | 1567.2 | 83675 | 1362.5 | 82533 | +1586 | +204.8 | strong |
| Put | 84200 | 520 | 520 | 1522.9 | 83839 | 1400.0 | 82677 | +1442 | +122.9 | strong |
| Put | 84300 | 720 | 720 | 1627.6 | 83780 | 1427.5 | 82672 | +1447 | +200.1 | strong |
| Put | 84400 | 1240 | 1240 | 1880.1 | 83402 | 1538.7 | 82520 | +1599 | +341.5 | strong |
| Put | 84500 | 1240 | 1240 | 1940.3 | 83396 | 1515.2 | 82560 | +1559 | +425.1 | strong |
| Put | 84600 | 780 | 780 | 1696.2 | 83907 | 1565.7 | 82904 | +1215 | +130.5 | strong |
| Put | 84700 | 500 | 500 | 1688.0 | 83988 | 1602.2 | 83012 | +1107 | +85.9 | strong |
| Put | 84800 | 100 | 100 | 2170.5 | 83203 | 2170.5 | 82630 | +1490 | +0.0 | strong |
| Put | 84900 | 720 | 720 | 2447.0 | 82913 | 1882.1 | 82453 | +1666 | +564.9 | strong |
| Put | 85000 | 2160 | 2160 | 2220.9 | 83335 | 1772.3 | 82779 | +1340 | +448.6 | strong |
| Put | 85100 | 340 | 340 | 2020.7 | 83734 | 1932.0 | 83079 | +1040 | +88.7 | strong |
| Put | 85200 | 620 | 620 | 2141.7 | 83689 | 2120.6 | 83058 | +1061 | +21.1 | strong |
| Put | 85300 | 1080 | 1080 | 2085.3 | 83780 | 2085.3 | 83215 | +904 | +0.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 10 | 25% | -0.43% | -1.29 to +0.22% |  | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 5 | 60% | +0.04% | -0.22 to +0.30% |  | too few (5/10) |
| monthly | PCR down · call writing · walls same · near put wall | 4 | 50% | -0.08% | -0.70 to +0.40% |  | too few (4/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.43% | -0.64 to -0.22% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 2 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.14% | -1.14 to +0.86% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 0% | -1.14% | -1.14 to -1.14% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 0% | -0.80% | -0.80 to -0.80% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +2.04% | +2.04 to +2.04% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +2.04% | +2.04 to +2.04% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 28 | 73% | +0.21% | no clear direction |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | writers even · few weak writers | 18 | 80% | +0.10% | up |
| intraday | monthly | put writers stronger · few weak writers | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 4 | 0% | -0.82% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.31% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers | 4 | 50% | +0.14% | too few (2/10) |
| day | monthly | writers even · few weak writers | 3 | 50% | -0.34% | too few (2/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +2.04% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 100% | +0.35% | too few (2/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 14 | 75% | +0.03% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 10 | 67% | +0.18% | too few (9/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.22% | too few (7/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 4 | 100% | +0.34% | too few (3/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 4 | 0% | -0.82% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.31% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 3 | 100% | +2.04% | too few (1/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +2.04% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.34% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 | 0% | -1.77% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
