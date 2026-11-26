# Sensex option chain pattern log
Updated 2026-11-26 11:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 64 snapshots over 6 trading days
- 125 patterns logged; 58 different patterns so far

## Latest read (2026-11-26 11:47:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 0.1 | 84237 | 1.011 | 84300 | 84000 | 85000 | ±0.48% (83834-84641) | 29.12 |
| 2026-12-31 (monthly) | 35.1 | 84238 | 1.066 | 84000 | 84000 | 86000 | ±3.8% (81037-87439) | 15.21 |

- **Weekly, last 30 min**: `PCR flat · put and call writing · walls same · near put wall`. Seen 2 times before; Sensex was up after it 100% of the time, average +0.91%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 40 times before; Sensex was up after it 61% of the time, average +0.06%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 22 times before; Sensex was up after it 60% of the time, average +0.07%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 67% of the time, average +0.14%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 50% of the time, average -0.71%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls up · near put wall`. Seen 2 times before; Sensex was up after it 50% of the time, average -0.14%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 32 times before; Sensex was up after it 69% of the time, average +0.04%. History points to a bull call debit spread, ATM to about the call wall 86000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 28 times before; Sensex was up after it 68% of the time, average +0.03%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 67% of the time, average -0.11%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Sensex was up after it 67% of the time, average -0.11%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 84000; weakest call writers at 84200, weakest put writers at 84300. Covers 99% of near-money call OI and 100% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83000 | 172040 | 155554 | 626.8 | 83062 | 1274.0 | 83627 | -611 | -647.2 | weak |
| Call | 83100 | 40320 | 39095 | 622.4 | 83150 | 1153.0 | 83722 | -515 | -530.7 | weak |
| Call | 83200 | 55620 | 54958 | 616.6 | 83268 | 1067.5 | 83817 | -421 | -450.9 | weak |
| Call | 83300 | 34460 | 34136 | 577.9 | 83339 | 978.0 | 83878 | -360 | -400.1 | weak |
| Call | 83400 | 78460 | 77559 | 576.9 | 83491 | 865.0 | 83977 | -261 | -288.1 | weak |
| Call | 83500 | 193080 | 189857 | 476.9 | 83488 | 774.1 | 83977 | -261 | -297.2 | weak |
| Call | 83600 | 145240 | 144917 | 420.3 | 83559 | 679.7 | 84020 | -217 | -259.4 | weak |
| Call | 83700 | 177920 | 177725 | 400.7 | 83713 | 592.6 | 84101 | -137 | -191.9 | weak |
| Call | 83800 | 389540 | 389161 | 333.4 | 83751 | 503.4 | 84133 | -104 | -170.0 | weak |
| Call | 83900 | 560100 | 559694 | 291.5 | 83757 | 422.9 | 84192 | -46 | -131.3 | weak |
| Call | 84000 | 1251100 | 1242781 | 257.6 | 83773 | 351.2 | 84258 | +20 | -93.6 | weak |
| Call | 84100 | 975240 | 974822 | 224.5 | 83920 | 282.9 | 84324 | +87 | -58.4 | weak |
| Call | 84200 | 1780420 | 1779754 | 205.4 | 84017 | 223.6 | 84405 | +168 | -18.1 | weak |
| Call | 84300 | 3095560 | 3093217 | 177.6 | 84059 | 174.2 | 84478 | +240 | +3.4 | medium |
| Call | 84400 | 2938920 | 2936150 | 194.6 | 84112 | 133.8 | 84595 | +357 | +60.8 | medium |
| Call | 84500 | 4871800 | 4829493 | 149.3 | 83918 | 102.5 | 84649 | +412 | +46.8 | strong |
| Call | 84600 | 2965020 | 2962585 | 136.8 | 84086 | 77.6 | 84737 | +499 | +59.2 | strong |
| Call | 84700 | 2505440 | 2500615 | 99.2 | 83982 | 59.0 | 84799 | +562 | +40.1 | strong |
| Call | 84800 | 2875540 | 2869314 | 86.3 | 84034 | 44.5 | 84886 | +649 | +41.9 | strong |
| Call | 84900 | 2984820 | 2976570 | 63.7 | 84065 | 33.6 | 84964 | +726 | +30.1 | strong |
| Call | 85000 | 7587160 | 7534567 | 56.8 | 83943 | 25.4 | 85057 | +819 | +31.4 | strong |
| Call | 85100 | 2435720 | 2433623 | 36.5 | 83930 | 18.3 | 85137 | +899 | +18.2 | strong |
| Call | 85200 | 2717860 | 2714320 | 41.7 | 84007 | 13.4 | 85242 | +1004 | +28.3 | strong |
| Call | 85300 | 3111960 | 3110828 | 26.2 | 84007 | 9.9 | 85326 | +1089 | +16.3 | strong |
| Call | 85400 | 1690400 | 1687535 | 28.1 | 83863 | 7.8 | 85428 | +1191 | +20.3 | strong |
| Call | 85500 | 4149500 | 4124395 | 28.9 | 83753 | 6.2 | 85529 | +1291 | +22.6 | strong |
| Put | 83000 | 5606140 | 5551130 | 82.4 | 83898 | 9.8 | 82918 | +1320 | +72.6 | strong |
| Put | 83100 | 1506980 | 1505830 | 98.9 | 83899 | 11.3 | 83001 | +1236 | +87.5 | strong |
| Put | 83200 | 2239280 | 2238568 | 102.0 | 83927 | 13.6 | 83098 | +1139 | +88.5 | strong |
| Put | 83300 | 2044840 | 2044372 | 115.0 | 83928 | 17.1 | 83185 | +1052 | +97.9 | strong |
| Put | 83400 | 2179140 | 2178680 | 133.2 | 83966 | 21.6 | 83267 | +971 | +111.6 | strong |
| Put | 83500 | 6374160 | 6370612 | 141.1 | 84015 | 27.6 | 83359 | +879 | +113.5 | strong |
| Put | 83600 | 2357640 | 2357370 | 161.8 | 84029 | 35.2 | 83438 | +799 | +126.6 | strong |
| Put | 83700 | 3011560 | 3011284 | 180.9 | 84037 | 46.1 | 83519 | +718 | +134.8 | strong |
| Put | 83800 | 3622900 | 3622567 | 241.5 | 83988 | 61.1 | 83558 | +679 | +180.3 | strong |
| Put | 83900 | 3155440 | 3155005 | 270.1 | 84001 | 80.5 | 83630 | +608 | +189.6 | strong |
| Put | 84000 | 6730540 | 6728789 | 228.6 | 84171 | 106.5 | 83771 | +466 | +122.1 | strong |
| Put | 84100 | 2658920 | 2658885 | 300.1 | 84098 | 138.4 | 83800 | +437 | +161.7 | strong |
| Put | 84200 | 3352320 | 3352309 | 226.5 | 84265 | 179.8 | 83973 | +264 | +46.8 | medium |
| Put | 84300 | 2794780 | 2794669 | 223.8 | 84344 | 229.7 | 84076 | +161 | -5.8 | weak |
| Put | 84400 | 1830520 | 1830519 | 243.0 | 84398 | 288.2 | 84157 | +80 | -45.3 | weak |
| Put | 84500 | 1374780 | 1374756 | 330.8 | 84355 | 358.4 | 84169 | +68 | -27.6 | weak |
| Put | 84600 | 559340 | 559340 | 371.4 | 84387 | 431.9 | 84229 | +9 | -60.4 | weak |
| Put | 84700 | 199220 | 199220 | 508.0 | 84315 | 514.6 | 84192 | +45 | -6.6 | weak |
| Put | 84800 | 105660 | 105660 | 512.8 | 84381 | 598.4 | 84287 | -50 | -85.6 | weak |
| Put | 84900 | 77080 | 77080 | 627.5 | 84351 | 686.5 | 84273 | -35 | -59.1 | weak |
| Put | 85000 | 237580 | 237025 | 760.3 | 84304 | 780.8 | 84240 | -2 | -20.5 | weak |
| Put | 85100 | 22760 | 22760 | 803.0 | 84342 | 873.3 | 84297 | -60 | -70.3 | weak |
| Put | 85200 | 12340 | 12340 | 953.5 | 84283 | 965.4 | 84247 | -9 | -11.9 | weak |
| Put | 85300 | 11140 | 4701 | 1126.2 | 84202 | 1070.0 | 84174 | +64 | +56.2 | weak |
| Put | 85400 | 5680 | 5680 | 1213.1 | 84201 | 1145.0 | 84187 | +51 | +68.2 | weak |
| Put | 85500 | 12700 | 12700 | 1106.9 | 84388 | 1245.8 | 84393 | -156 | -138.9 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 86000, strongest put writers at 84000; weakest call writers at 82400, weakest put writers at 86500. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83000 | 3300 | 3177 | 2126.9 | 83463 | 2579.7 | 85127 | +889 | -452.8 | strong |
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2100.0 | 84702 | +464 | -498.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +562 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +842 | -335.1 | strong |
| Call | 83400 | 540 | 531 | 1612.7 | 83261 | 2152.9 | 85013 | +775 | -540.2 | strong |
| Call | 83500 | 8080 | 8008 | 2088.6 | 83832 | 2239.6 | 85589 | +1351 | -151.1 | strong |
| Call | 83600 | 940 | 940 | 1823.9 | 83677 | 2151.3 | 85424 | +1186 | -327.4 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1805.5 | 85310 | +1072 | -195.6 | strong |
| Call | 83800 | 340 | 340 | 1665.5 | 83527 | 2210.3 | 85465 | +1227 | -544.9 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +1119 | +287.6 | strong |
| Call | 84000 | 12440 | 12440 | 1777.4 | 83870 | 1924.2 | 85777 | +1539 | -146.9 | strong |
| Call | 84100 | 560 | 560 | 1638.5 | 83796 | 2032.0 | 85739 | +1501 | -393.5 | strong |
| Call | 84200 | 540 | 535 | 1485.4 | 83584 | 1873.2 | 85685 | +1447 | -387.8 | strong |
| Call | 84300 | 320 | 320 | 1632.4 | 83998 | 1820.1 | 85932 | +1694 | -187.7 | strong |
| Call | 84400 | 320 | 320 | 1322.6 | 83340 | 1720.0 | 85723 | +1485 | -397.3 | strong |
| Call | 84500 | 10440 | 10440 | 1552.2 | 83957 | 1690.0 | 86052 | +1814 | -137.8 | strong |
| Call | 84600 | 300 | 300 | 1256.5 | 83457 | 1600.9 | 85856 | +1618 | -344.4 | strong |
| Call | 84700 | 260 | 260 | 1113.5 | 83133 | 1576.0 | 85813 | +1575 | -462.5 | strong |
| Call | 84800 | 280 | 280 | 1175.2 | 83427 | 1495.0 | 85975 | +1737 | -319.7 | strong |
| Call | 84900 | 480 | 480 | 1148.2 | 83432 | 1444.8 | 86048 | +1810 | -296.7 | strong |
| Call | 85000 | 7080 | 7080 | 1220.3 | 83718 | 1403.9 | 86220 | +1982 | -183.6 | strong |
| Call | 85100 | 300 | 300 | 972.0 | 83276 | 1246.0 | 86072 | +1834 | -274.0 | strong |
| Call | 85200 | 340 | 340 | 848.1 | 82939 | 1347.2 | 86048 | +1810 | -499.1 | strong |
| Call | 85300 | 120 | 120 | 1035.2 | 83872 | 1035.5 | 86335 | +2097 | -0.4 | strong |
| Call | 85400 | 460 | 460 | 892.6 | 83194 | 1200.2 | 86293 | +2055 | -307.6 | strong |
| Call | 85500 | 2020 | 2020 | 1109.9 | 84024 | 1171.2 | 86610 | +2372 | -61.3 | strong |
| Put | 83000 | 11780 | 11313 | 1106.5 | 83711 | 900.1 | 81893 | +2345 | +206.4 | strong |
| Put | 83100 | 100 | 100 | 1278.5 | 83394 | 868.2 | 81821 | +2417 | +410.3 | strong |
| Put | 83200 | 540 | 540 | 1379.9 | 83227 | 901.4 | 81820 | +2418 | +478.5 | strong |
| Put | 83300 | 460 | 460 | 1470.7 | 83125 | 930.5 | 81829 | +2409 | +540.2 | strong |
| Put | 83400 | 820 | 820 | 1397.1 | 83392 | 1142.8 | 82003 | +2235 | +254.3 | strong |
| Put | 83500 | 8000 | 7734 | 1223.1 | 83844 | 1059.5 | 82277 | +1961 | +163.7 | strong |
| Put | 83600 | 1060 | 1060 | 1521.0 | 83328 | 1185.7 | 82079 | +2159 | +335.3 | strong |
| Put | 83700 | 680 | 680 | 1566.8 | 83306 | 1219.6 | 82133 | +2105 | +347.2 | strong |
| Put | 83800 | 800 | 800 | 1494.5 | 83550 | 1034.7 | 82306 | +1932 | +459.8 | strong |
| Put | 83900 | 520 | 506 | 1512.2 | 83593 | 1182.7 | 82388 | +1850 | +329.5 | strong |
| Put | 84000 | 12660 | 12660 | 1350.6 | 84034 | 1241.9 | 82649 | +1589 | +108.7 | strong |
| Put | 84100 | 1420 | 1420 | 1545.0 | 83738 | 1219.1 | 82555 | +1683 | +325.9 | strong |
| Put | 84200 | 840 | 840 | 1537.0 | 83811 | 1328.1 | 82663 | +1575 | +208.9 | strong |
| Put | 84300 | 980 | 980 | 1609.2 | 83804 | 1343.0 | 82691 | +1547 | +266.3 | strong |
| Put | 84400 | 1560 | 1560 | 1757.6 | 83636 | 1415.6 | 82642 | +1596 | +342.0 | strong |
| Put | 84500 | 11700 | 11700 | 1548.1 | 84108 | 1457.8 | 82952 | +1286 | +90.3 | strong |
| Put | 84600 | 920 | 920 | 1703.9 | 83894 | 1444.8 | 82896 | +1342 | +259.1 | strong |
| Put | 84700 | 720 | 720 | 1651.0 | 84077 | 1550.5 | 83049 | +1189 | +100.5 | strong |
| Put | 84800 | 760 | 760 | 1641.4 | 84218 | 1564.3 | 83159 | +1079 | +77.0 | strong |
| Put | 84900 | 780 | 780 | 2253.9 | 83187 | 1591.8 | 82646 | +1592 | +662.1 | strong |
| Put | 85000 | 5500 | 5500 | 1915.5 | 83918 | 1700.0 | 83085 | +1153 | +215.4 | strong |
| Put | 85100 | 400 | 400 | 1964.5 | 83821 | 1646.2 | 83135 | +1103 | +318.3 | strong |
| Put | 85200 | 620 | 620 | 2141.7 | 83689 | 2120.6 | 83058 | +1180 | +21.1 | strong |
| Put | 85300 | 1080 | 1080 | 2085.3 | 83780 | 2085.3 | 83215 | +1023 | +0.0 | strong |
| Put | 85400 | 140 | 140 | 2041.0 | 83938 | 2041.0 | 83359 | +879 | +0.0 | strong |
| Put | 85500 | 2600 | 2600 | 2388.7 | 83530 | 1961.2 | 83111 | +1127 | +427.5 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 11 | 30% | -0.34% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 6 | 67% | +0.00% | -0.22 to +0.16% |  | too few (6/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 4 | 67% | +0.21% | -0.05 to +0.48% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 3 | 0% | -0.06% | -0.07 to -0.05% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 100% | +0.91% | +0.86 to +0.97% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 50% | -0.14% | -1.14 to +0.86% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.30% | -1.15 to +0.55% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 0% | -0.50% | -0.80 to -0.19% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.26% | -0.26 to -0.26% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 1 | 100% | +0.55% | +0.55 to +0.55% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.26% | -0.26 to -0.26% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.19% | +0.19 to +0.19% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 0% | -0.44% | -0.44 to -0.44% | 100% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.82% | +1.82 to +1.82% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.36% | +0.36 to +0.36% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.36% | +0.36 to +0.36% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 41 | 61% | +0.06% | no clear direction |
| intraday | monthly | writers even · few weak writers | 33 | 69% | +0.04% | up |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 5 | 20% | -0.61% | too few (5/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| day | weekly | writers even · few weak writers | 5 | 67% | +0.14% | too few (3/10) |
| day | monthly | writers even · few weak writers | 4 | 67% | -0.11% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 29 | 68% | +0.03% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 23 | 60% | +0.07% | no clear direction |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 67% | +0.02% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 5 | 20% | -0.61% | too few (5/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 4 | 75% | +0.04% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 67% | -0.11% | too few (3/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | -0.71% | too few (2/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
