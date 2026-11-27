# Sensex option chain pattern log
Updated 2026-11-27 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 75 snapshots over 7 trading days
- 146 patterns logged; 69 different patterns so far

## Latest read (2026-11-27 10:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-03 (weekly) | 6.2 | 83921 | 0.868 | 84000 | 80000 | 84000 | ±1.7% (82497-85345) | 16.31 |
| 2026-12-31 (monthly) | 34.2 | 83921 | 1.063 | 84000 | 83000 | 86000 | ±3.46% (81021-86821) | 14.0 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 46 times before; Sensex was up after it 62% of the time, average +0.09%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 28 times before; Sensex was up after it 62% of the time, average +0.10%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 67% of the time, average +0.17%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 50% of the time, average -0.65%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls down · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 43 times before; Sensex was up after it 67% of the time, average +0.05%. History points to a bull call debit spread, ATM to about the call wall 86000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 39 times before; Sensex was up after it 66% of the time, average +0.05%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls down · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 50% of the time, average -0.18%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 4 times before; Sensex was up after it 50% of the time, average -0.18%. Too few outcomes (4/20) to trade on.

## Strong vs weak writers, weekly 2026-12-03

Strongest call writers at 84000, strongest put writers at 84000; weakest call writers at -, weakest put writers at 86000. Covers 63% of near-money call OI and 56% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82700 | 1820 | 99 | 1578.4 | 83989 | 1494.0 | 84278 | +357 | +84.4 | medium |
| Call | 82800 | 2660 | 220 | 1598.2 | 84096 | 1434.3 | 84398 | +477 | +163.9 | strong |
| Call | 82900 | 2900 | 540 | 1483.0 | 84086 | 1360.0 | 84383 | +462 | +123.0 | strong |
| Call | 83000 | 52480 | 10060 | 1395.2 | 84049 | 1290.8 | 84395 | +474 | +104.4 | strong |
| Call | 83100 | 4740 | 1140 | 1389.0 | 84069 | 1218.0 | 84489 | +568 | +171.0 | strong |
| Call | 83200 | 11760 | 1819 | 1324.3 | 84065 | 1143.2 | 84524 | +603 | +181.0 | strong |
| Call | 83300 | 7940 | 3910 | 1229.2 | 84125 | 1089.5 | 84529 | +608 | +139.7 | strong |
| Call | 83400 | 20180 | 16040 | 1104.0 | 84036 | 1025.4 | 84504 | +583 | +78.6 | strong |
| Call | 83500 | 79700 | 30900 | 1067.3 | 84079 | 962.8 | 84567 | +646 | +104.5 | strong |
| Call | 83600 | 20960 | 12900 | 961.1 | 84006 | 903.4 | 84561 | +640 | +57.7 | strong |
| Call | 83700 | 57840 | 41120 | 886.5 | 83981 | 847.2 | 84587 | +666 | +39.3 | strong |
| Call | 83800 | 100360 | 75340 | 828.3 | 83983 | 788.5 | 84628 | +707 | +39.8 | strong |
| Call | 83900 | 180260 | 140240 | 763.4 | 83963 | 737.6 | 84663 | +742 | +25.8 | strong |
| Call | 84000 | 744560 | 453740 | 767.1 | 84057 | 688.8 | 84767 | +846 | +78.3 | strong |
| Call | 84100 | 407820 | 324640 | 734.3 | 84091 | 640.4 | 84834 | +913 | +94.0 | strong |
| Call | 84200 | 392160 | 328780 | 694.2 | 84101 | 595.3 | 84894 | +973 | +99.0 | strong |
| Call | 84300 | 309100 | 172620 | 650.7 | 84099 | 552.7 | 84951 | +1030 | +98.0 | strong |
| Call | 84400 | 190580 | 94880 | 593.5 | 84088 | 512.8 | 84993 | +1072 | +80.7 | strong |
| Call | 84500 | 449620 | 224620 | 552.4 | 84084 | 474.1 | 85052 | +1131 | +78.4 | strong |
| Call | 84600 | 136220 | 95520 | 504.9 | 84069 | 438.4 | 85105 | +1184 | +66.5 | strong |
| Call | 84700 | 103620 | 74740 | 473.3 | 84083 | 404.1 | 85173 | +1252 | +69.2 | strong |
| Call | 84800 | 106540 | 82860 | 427.9 | 84066 | 371.6 | 85228 | +1307 | +56.4 | strong |
| Call | 84900 | 89100 | 64860 | 398.7 | 84064 | 343.6 | 85299 | +1378 | +55.1 | strong |
| Call | 85000 | 470640 | 287920 | 376.0 | 84084 | 314.9 | 85376 | +1455 | +61.1 | strong |
| Call | 85100 | 90480 | 67820 | 346.2 | 84091 | 288.8 | 85446 | +1525 | +57.4 | strong |
| Put | 82700 | 71380 | 46200 | 248.8 | 84065 | 264.9 | 82451 | +1470 | -16.1 | strong |
| Put | 82800 | 76260 | 53638 | 261.8 | 84100 | 288.5 | 82538 | +1383 | -26.7 | strong |
| Put | 82900 | 75080 | 59640 | 295.3 | 84066 | 314.9 | 82605 | +1316 | -19.6 | strong |
| Put | 83000 | 326360 | 185270 | 312.3 | 84100 | 342.8 | 82688 | +1233 | -30.5 | strong |
| Put | 83100 | 99500 | 73820 | 342.6 | 84085 | 371.1 | 82757 | +1164 | -28.6 | strong |
| Put | 83200 | 74340 | 44580 | 369.2 | 84090 | 404.0 | 82831 | +1090 | -34.8 | strong |
| Put | 83300 | 51220 | 41660 | 395.9 | 84104 | 437.1 | 82904 | +1017 | -41.1 | strong |
| Put | 83400 | 86280 | 63360 | 436.3 | 84070 | 475.8 | 82964 | +957 | -39.4 | strong |
| Put | 83500 | 255580 | 126273 | 473.7 | 84077 | 515.1 | 83026 | +895 | -41.4 | strong |
| Put | 83600 | 120800 | 91790 | 494.9 | 84108 | 556.1 | 83105 | +816 | -61.2 | strong |
| Put | 83700 | 113240 | 79616 | 562.9 | 84030 | 596.0 | 83137 | +784 | -33.1 | strong |
| Put | 83800 | 209880 | 151420 | 608.1 | 84021 | 642.0 | 83192 | +729 | -33.9 | strong |
| Put | 83900 | 256680 | 175480 | 647.0 | 84026 | 686.6 | 83253 | +668 | -39.6 | strong |
| Put | 84000 | 694980 | 359781 | 667.5 | 84102 | 741.0 | 83332 | +589 | -73.5 | strong |
| Put | 84100 | 310920 | 210421 | 709.9 | 84102 | 790.6 | 83390 | +531 | -80.8 | strong |
| Put | 84200 | 188980 | 142157 | 767.9 | 84096 | 847.5 | 83432 | +489 | -79.6 | strong |
| Put | 84300 | 128680 | 37927 | 818.5 | 84099 | 907.9 | 83482 | +439 | -89.5 | strong |
| Put | 84400 | 68000 | 17505 | 863.4 | 84106 | 960.6 | 83537 | +384 | -97.3 | strong |
| Put | 84500 | 124000 | 1484 | 901.1 | 84134 | 1026.6 | 83599 | +322 | -125.5 | medium |
| Put | 84600 | 20260 | 8280 | 988.1 | 84105 | 1105.0 | 83612 | +309 | -117.0 | medium |
| Put | 84700 | 13540 | 4640 | 1049.9 | 84093 | 1155.8 | 83650 | +271 | -105.9 | medium |
| Put | 84800 | 16100 | 9090 | 1121.5 | 84090 | 1224.2 | 83678 | +243 | -102.7 | medium |
| Put | 84900 | 9060 | 3779 | 1220.0 | 84034 | 1287.1 | 83680 | +241 | -67.1 | medium |
| Put | 85000 | 33920 | 6440 | 1271.2 | 84070 | 1369.3 | 83729 | +192 | -98.2 | medium |
| Put | 85100 | 5220 | 239 | 1305.8 | 84107 | 1454.2 | 83794 | +127 | -148.4 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 86000, strongest put writers at 84000; weakest call writers at -, weakest put writers at 86000. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +625 | -732.3 | strong |
| Call | 82800 | 1480 | 1407 | 2305.2 | 83514 | 2999.5 | 85105 | +1184 | -694.3 | strong |
| Call | 82900 | 220 | 186 | 1609.0 | 82444 | 2407.8 | 84509 | +588 | -798.9 | strong |
| Call | 83000 | 4380 | 4258 | 2227.9 | 83644 | 2229.2 | 85228 | +1307 | -1.3 | strong |
| Call | 83100 | 600 | 567 | 1626.2 | 82730 | 2289.2 | 84726 | +805 | -663.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +879 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +1159 | -335.1 | strong |
| Call | 83400 | 520 | 511 | 1612.7 | 83261 | 2300.0 | 85013 | +1092 | -687.3 | strong |
| Call | 83500 | 8440 | 8369 | 2096.9 | 83852 | 1955.0 | 85597 | +1676 | +141.9 | strong |
| Call | 83600 | 620 | 620 | 1823.9 | 83677 | 1966.8 | 85424 | +1503 | -142.9 | strong |
| Call | 83700 | 900 | 900 | 1622.0 | 83351 | 2035.6 | 85322 | +1401 | -413.6 | strong |
| Call | 83800 | 260 | 260 | 1696.0 | 83648 | 1764.9 | 85496 | +1575 | -68.8 | strong |
| Call | 83900 | 460 | 443 | 1507.9 | 83428 | 1680.9 | 85408 | +1487 | -173.0 | strong |
| Call | 84000 | 15640 | 15640 | 1800.6 | 83936 | 1681.7 | 85801 | +1880 | +118.9 | strong |
| Call | 84100 | 580 | 580 | 1648.0 | 83831 | 1570.8 | 85748 | +1827 | +77.2 | strong |
| Call | 84200 | 560 | 556 | 1488.9 | 83645 | 1505.0 | 85689 | +1768 | -16.1 | strong |
| Call | 84300 | 520 | 520 | 1623.7 | 84008 | 1564.7 | 85924 | +2003 | +59.1 | strong |
| Call | 84400 | 660 | 660 | 1465.0 | 83756 | 1440.0 | 85865 | +1944 | +25.0 | strong |
| Call | 84500 | 15400 | 15400 | 1557.4 | 84050 | 1408.7 | 86057 | +2136 | +148.7 | strong |
| Call | 84600 | 580 | 580 | 1371.6 | 83791 | 1420.0 | 85972 | +2051 | -48.4 | strong |
| Call | 84700 | 560 | 560 | 1269.8 | 83636 | 1424.0 | 85970 | +2049 | -154.2 | strong |
| Call | 84800 | 320 | 320 | 1243.1 | 83586 | 1330.0 | 86043 | +2122 | -87.0 | strong |
| Call | 84900 | 500 | 500 | 1161.1 | 83466 | 1472.5 | 86061 | +2140 | -311.3 | strong |
| Call | 85000 | 15320 | 15320 | 1283.6 | 83967 | 1170.0 | 86284 | +2363 | +113.6 | strong |
| Call | 85100 | 300 | 300 | 972.0 | 83276 | 1251.6 | 86072 | +2151 | -279.6 | strong |
| Put | 82700 | 360 | 360 | 951.9 | 83853 | 751.6 | 81748 | +2173 | +200.3 | strong |
| Put | 82800 | 360 | 360 | 923.9 | 83853 | 839.0 | 81876 | +2045 | +84.8 | strong |
| Put | 82900 | 160 | 160 | 1015.8 | 83805 | 850.0 | 81884 | +2037 | +165.8 | strong |
| Put | 83000 | 12240 | 11809 | 1075.6 | 83777 | 911.6 | 81924 | +1997 | +164.0 | strong |
| Put | 83100 | 160 | 160 | 1163.5 | 83622 | 846.0 | 81936 | +1985 | +317.6 | strong |
| Put | 83200 | 460 | 460 | 1379.9 | 83227 | 984.0 | 81820 | +2101 | +395.9 | strong |
| Put | 83300 | 460 | 460 | 1447.4 | 83169 | 960.5 | 81853 | +2068 | +486.9 | strong |
| Put | 83400 | 820 | 820 | 1380.2 | 83427 | 1107.2 | 82020 | +1901 | +273.0 | strong |
| Put | 83500 | 8360 | 8094 | 1213.7 | 83864 | 1100.0 | 82286 | +1635 | +113.7 | strong |
| Put | 83600 | 1080 | 1080 | 1504.1 | 83359 | 1187.9 | 82096 | +1825 | +316.2 | strong |
| Put | 83700 | 640 | 640 | 1552.3 | 83332 | 1061.0 | 82148 | +1773 | +491.4 | strong |
| Put | 83800 | 800 | 800 | 1494.5 | 83550 | 1034.7 | 82306 | +1615 | +459.8 | strong |
| Put | 83900 | 520 | 506 | 1497.6 | 83620 | 1219.0 | 82402 | +1519 | +278.6 | strong |
| Put | 84000 | 19140 | 19140 | 1286.0 | 84125 | 1284.1 | 82714 | +1207 | +1.9 | strong |
| Put | 84100 | 1640 | 1640 | 1465.8 | 83866 | 1360.0 | 82634 | +1287 | +105.8 | strong |
| Put | 84200 | 1260 | 1260 | 1420.0 | 83990 | 1410.0 | 82780 | +1141 | +10.0 | strong |
| Put | 84300 | 980 | 980 | 1595.2 | 83826 | 1435.5 | 82705 | +1216 | +159.7 | strong |
| Put | 84400 | 1820 | 1820 | 1693.5 | 83714 | 1490.1 | 82707 | +1215 | +203.4 | strong |
| Put | 84500 | 13140 | 13140 | 1496.4 | 84128 | 1530.5 | 83004 | +917 | -34.1 | strong |
| Put | 84600 | 940 | 940 | 1691.8 | 83913 | 1458.4 | 82908 | +1013 | +233.4 | strong |
| Put | 84700 | 780 | 780 | 1645.8 | 84081 | 1584.2 | 83054 | +867 | +61.6 | strong |
| Put | 84800 | 800 | 800 | 1641.3 | 84214 | 1639.6 | 83159 | +762 | +1.7 | strong |
| Put | 84900 | 780 | 780 | 2253.9 | 83187 | 1582.0 | 82646 | +1275 | +672.0 | strong |
| Put | 85000 | 13340 | 13340 | 1761.4 | 84039 | 1805.7 | 83239 | +682 | -44.2 | strong |
| Put | 85100 | 420 | 420 | 1949.1 | 83844 | 1640.1 | 83151 | +770 | +309.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 12 | 36% | -0.30% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 11 | 60% | -0.04% | -0.25 to +0.16% |  | no clear direction |
| monthly | PCR down · put and call writing · walls same · near put wall | 5 | 75% | +0.24% | -0.05 to +0.48% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 33% | -0.02% | -0.07 to +0.06% | 100% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 3 | 33% | -0.15% | -0.25 to +0.01% |  | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 100% | +0.65% | +0.11 to +0.97% | 0% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | -0.06% | -1.14 to +0.86% |  | too few (3/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.24% | -1.15 to +0.66% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 0% | -0.46% | -0.80 to -0.08% | 100% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls down · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 1 | 100% | +0.66% | +0.66 to +0.66% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.32% | +0.32 to +0.32% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls up · near put wall | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.19% | +0.19 to +0.19% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 0% | -0.44% | -0.44 to -0.44% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.82% | +1.82 to +1.82% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.48% | -0.48 to -0.48% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.46% | +0.46 to +0.46% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.46% | +0.46 to +0.46% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.48% | -0.48 to -0.48% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 47 | 62% | +0.09% | no clear direction |
| intraday | monthly | writers even · few weak writers | 44 | 67% | +0.05% | up |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 8 | 62% | -0.19% | too few (8/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 5 | 20% | -0.61% | too few (5/10) |
| intraday | weekly | writers even · weak on both sides | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers | 5 | 50% | -0.18% | too few (4/10) |
| day | weekly | writers even · few weak writers | 5 | 67% | +0.17% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak on both sides | 1 | 0% | -0.48% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 40 | 66% | +0.05% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 29 | 62% | +0.10% | no clear direction |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 67% | +0.02% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 8 | 62% | -0.19% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 5 | 20% | -0.61% | too few (5/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 4 | 75% | +0.04% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 5 | 50% | -0.18% | too few (4/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | -0.65% | too few (2/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 0% | -0.48% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
