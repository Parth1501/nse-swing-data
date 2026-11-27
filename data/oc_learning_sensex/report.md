# Sensex option chain pattern log
Updated 2026-11-27 11:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 77 snapshots over 7 trading days
- 150 patterns logged; 71 different patterns so far

## Latest read (2026-11-27 11:46:00)

Sensex trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-03 (weekly) | 6.2 | 83633 | 0.77 | 84000 | 80000 | 84000 | ±1.75% (82173-85093) | 16.8 |
| 2026-12-31 (monthly) | 34.2 | 83631 | 1.014 | 84000 | 83000 | 84500 | ±3.52% (80685-86577) | 14.27 |

- **Weekly, last 30 min**: `PCR down · call writing · walls same · near call wall`. Seen 1 times before; Sensex was up after it 0% of the time, average -0.17%. Too few outcomes (1/20) to trade on.
  - Writers: `call writers stronger · few weak writers`. Seen 6 times before; Sensex was up after it 17% of the time, average -0.54%. Too few outcomes (6/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 45 times before; Sensex was up after it 63% of the time, average +0.01%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 4 times before; Sensex was up after it 75% of the time, average +0.04%. Too few outcomes (4/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 50% of the time, average -0.26%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-12-03

Strongest call writers at 84000, strongest put writers at 83600; weakest call writers at -, weakest put writers at 84300. Covers 70% of near-money call OI and 61% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82400 | 1420 | 710 | 1807.3 | 84013 | 1471.5 | 84207 | +574 | +335.7 | strong |
| Call | 82500 | 18660 | 3456 | 1526.4 | 83768 | 1430.0 | 84026 | +393 | +96.4 | strong |
| Call | 82600 | 1880 | 352 | 1669.3 | 84049 | 1363.0 | 84269 | +636 | +306.3 | strong |
| Call | 82700 | 2140 | 419 | 1376.9 | 83757 | 1281.1 | 84077 | +444 | +95.8 | strong |
| Call | 82800 | 3680 | 1240 | 1296.8 | 83758 | 1204.7 | 84097 | +464 | +92.2 | strong |
| Call | 82900 | 4840 | 2480 | 1244.3 | 83758 | 1151.7 | 84144 | +511 | +92.6 | strong |
| Call | 83000 | 67140 | 24720 | 1234.9 | 83853 | 1086.5 | 84235 | +602 | +148.4 | strong |
| Call | 83100 | 13760 | 10160 | 1103.9 | 83779 | 1021.2 | 84204 | +571 | +82.7 | strong |
| Call | 83200 | 19040 | 9099 | 1050.5 | 83772 | 956.5 | 84250 | +617 | +94.0 | strong |
| Call | 83300 | 17560 | 13530 | 1006.6 | 83805 | 900.5 | 84307 | +674 | +106.2 | strong |
| Call | 83400 | 40160 | 36020 | 978.4 | 83856 | 848.0 | 84378 | +745 | +130.4 | strong |
| Call | 83500 | 148120 | 99320 | 883.8 | 83789 | 791.5 | 84384 | +751 | +92.3 | strong |
| Call | 83600 | 133360 | 125300 | 773.9 | 83697 | 743.0 | 84374 | +741 | +30.9 | strong |
| Call | 83700 | 194880 | 178160 | 750.8 | 83762 | 690.9 | 84451 | +818 | +59.9 | strong |
| Call | 83800 | 210360 | 185340 | 738.1 | 83841 | 645.0 | 84538 | +905 | +93.1 | strong |
| Call | 83900 | 229040 | 189020 | 728.3 | 83906 | 598.0 | 84628 | +995 | +130.3 | strong |
| Call | 84000 | 905760 | 614940 | 717.5 | 83968 | 557.0 | 84717 | +1084 | +160.5 | strong |
| Call | 84100 | 392480 | 313218 | 732.0 | 84087 | 516.4 | 84832 | +1199 | +215.6 | strong |
| Call | 84200 | 383720 | 321704 | 694.2 | 84101 | 476.3 | 84894 | +1261 | +217.9 | strong |
| Call | 84300 | 310580 | 175543 | 645.8 | 84090 | 441.0 | 84946 | +1313 | +204.8 | strong |
| Call | 84400 | 250680 | 154980 | 522.2 | 83917 | 406.5 | 84922 | +1289 | +115.7 | strong |
| Call | 84500 | 479260 | 254260 | 534.3 | 84045 | 376.6 | 85034 | +1401 | +157.7 | strong |
| Call | 84600 | 139860 | 99160 | 499.8 | 84058 | 345.7 | 85100 | +1467 | +154.1 | strong |
| Call | 84700 | 110920 | 82040 | 460.9 | 84053 | 317.4 | 85161 | +1528 | +143.5 | strong |
| Call | 84800 | 127080 | 103400 | 404.2 | 84005 | 292.9 | 85204 | +1571 | +111.3 | strong |
| Put | 82400 | 60460 | 37378 | 196.7 | 84023 | 284.2 | 82203 | +1430 | -87.5 | strong |
| Put | 82500 | 181760 | 74902 | 205.6 | 84095 | 308.9 | 82294 | +1339 | -103.3 | strong |
| Put | 82600 | 79640 | 59951 | 254.7 | 83962 | 336.0 | 82345 | +1288 | -81.3 | strong |
| Put | 82700 | 74700 | 52236 | 273.9 | 83974 | 367.4 | 82426 | +1207 | -93.5 | strong |
| Put | 82800 | 91460 | 68838 | 286.2 | 84014 | 395.0 | 82514 | +1119 | -108.8 | strong |
| Put | 82900 | 67660 | 55013 | 310.1 | 84018 | 427.2 | 82590 | +1043 | -117.1 | strong |
| Put | 83000 | 318500 | 180808 | 312.3 | 84100 | 462.9 | 82688 | +945 | -150.6 | strong |
| Put | 83100 | 83120 | 61668 | 342.6 | 84085 | 500.0 | 82757 | +876 | -157.4 | strong |
| Put | 83200 | 99040 | 69280 | 418.9 | 83960 | 539.5 | 82781 | +852 | -120.6 | strong |
| Put | 83300 | 87760 | 78200 | 472.3 | 83912 | 580.0 | 82828 | +805 | -107.7 | strong |
| Put | 83400 | 103480 | 80560 | 472.8 | 83986 | 624.0 | 82927 | +706 | -151.2 | strong |
| Put | 83500 | 291160 | 161853 | 516.1 | 83981 | 669.0 | 82984 | +649 | -152.9 | strong |
| Put | 83600 | 233460 | 204450 | 617.1 | 83847 | 717.4 | 82983 | +650 | -100.2 | strong |
| Put | 83700 | 195280 | 162804 | 639.9 | 83894 | 767.7 | 83060 | +573 | -127.8 | strong |
| Put | 83800 | 166020 | 123884 | 626.0 | 83992 | 820.0 | 83174 | +459 | -194.0 | strong |
| Put | 83900 | 150200 | 102685 | 647.0 | 84026 | 875.0 | 83253 | +380 | -228.0 | strong |
| Put | 84000 | 569140 | 294635 | 667.5 | 84102 | 932.0 | 83332 | +301 | -264.5 | medium |
| Put | 84100 | 208720 | 141256 | 709.9 | 84102 | 990.0 | 83390 | +243 | -280.1 | medium |
| Put | 84200 | 129100 | 97114 | 767.9 | 84096 | 1054.3 | 83432 | +201 | -286.4 | medium |
| Put | 84300 | 103140 | 30399 | 818.5 | 84099 | 1118.5 | 83482 | +152 | -300.1 | weak |
| Put | 84400 | 61200 | 15754 | 863.4 | 84106 | 1187.0 | 83537 | +96 | -323.7 | weak |
| Put | 84500 | 106740 | 1277 | 901.1 | 84134 | 1258.2 | 83599 | +34 | -357.1 | weak |
| Put | 84600 | 19900 | 8523 | 1015.1 | 84068 | 1337.2 | 83585 | +48 | -322.0 | weak |
| Put | 84700 | 11580 | 3968 | 1049.9 | 84093 | 1407.0 | 83650 | -17 | -357.1 | weak |
| Put | 84800 | 13940 | 7871 | 1121.5 | 84090 | 1470.0 | 83678 | -45 | -348.5 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 84500, strongest put writers at 84500; weakest call writers at -, weakest put writers at 86000. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82400 | 120 | 120 | 1994.6 | 82762 | 2765.2 | 84395 | +764 | -770.6 | strong |
| Call | 82500 | 980 | 951 | 2523.3 | 83629 | 2900.9 | 85023 | +1392 | -377.6 | strong |
| Call | 82600 | 120 | 120 | 1778.5 | 82439 | 1789.5 | 84378 | +747 | -10.9 | strong |
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +915 | -732.3 | strong |
| Call | 82800 | 1560 | 1487 | 2302.3 | 83528 | 2251.6 | 85102 | +1471 | +50.7 | strong |
| Call | 82900 | 220 | 186 | 1609.0 | 82444 | 2407.8 | 84509 | +878 | -798.9 | strong |
| Call | 83000 | 4680 | 4558 | 2219.5 | 83644 | 2100.0 | 85219 | +1588 | +119.5 | strong |
| Call | 83100 | 600 | 567 | 1626.2 | 82730 | 2289.2 | 84726 | +1095 | -663.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +1169 | -1016.5 | strong |
| Call | 83300 | 440 | 440 | 1780.0 | 83299 | 1924.8 | 85080 | +1449 | -144.8 | strong |
| Call | 83400 | 520 | 511 | 1612.7 | 83261 | 2300.0 | 85013 | +1382 | -687.3 | strong |
| Call | 83500 | 8640 | 8569 | 2090.0 | 83847 | 1787.7 | 85590 | +1959 | +302.4 | strong |
| Call | 83600 | 580 | 580 | 1823.9 | 83677 | 1715.0 | 85424 | +1793 | +108.9 | strong |
| Call | 83700 | 920 | 920 | 1623.9 | 83360 | 1707.5 | 85324 | +1693 | -83.7 | strong |
| Call | 83800 | 260 | 260 | 1696.0 | 83648 | 1705.0 | 85496 | +1865 | -8.9 | strong |
| Call | 83900 | 480 | 463 | 1509.7 | 83437 | 1550.8 | 85410 | +1779 | -41.1 | strong |
| Call | 84000 | 16560 | 16560 | 1786.1 | 83922 | 1520.0 | 85786 | +2155 | +266.1 | strong |
| Call | 84100 | 560 | 560 | 1648.0 | 83831 | 1450.0 | 85748 | +2117 | +198.0 | strong |
| Call | 84200 | 540 | 536 | 1488.9 | 83645 | 1475.0 | 85689 | +2058 | +13.9 | strong |
| Call | 84300 | 560 | 560 | 1607.7 | 83991 | 1399.8 | 85908 | +2277 | +207.9 | strong |
| Call | 84400 | 660 | 660 | 1465.0 | 83756 | 1440.0 | 85865 | +2234 | +25.0 | strong |
| Call | 84500 | 21280 | 21280 | 1488.4 | 83961 | 1266.3 | 85988 | +2357 | +222.1 | strong |
| Call | 84600 | 580 | 580 | 1371.6 | 83791 | 1420.0 | 85972 | +2341 | -48.4 | strong |
| Call | 84700 | 560 | 560 | 1269.8 | 83636 | 1249.2 | 85970 | +2339 | +20.6 | strong |
| Call | 84800 | 320 | 320 | 1243.1 | 83586 | 1330.0 | 86043 | +2412 | -87.0 | strong |
| Put | 82400 | 1220 | 1220 | 963.4 | 83581 | 855.5 | 81437 | +2194 | +108.0 | strong |
| Put | 82500 | 2620 | 2552 | 992.5 | 83571 | 873.7 | 81508 | +2124 | +118.8 | strong |
| Put | 82600 | 760 | 760 | 921.8 | 83840 | 745.3 | 81678 | +1953 | +176.5 | strong |
| Put | 82700 | 360 | 360 | 951.9 | 83853 | 751.6 | 81748 | +1883 | +200.3 | strong |
| Put | 82800 | 360 | 360 | 923.9 | 83853 | 839.0 | 81876 | +1755 | +84.8 | strong |
| Put | 82900 | 160 | 160 | 1015.8 | 83805 | 850.0 | 81884 | +1747 | +165.8 | strong |
| Put | 83000 | 12080 | 11655 | 1075.6 | 83777 | 1039.8 | 81924 | +1707 | +35.9 | strong |
| Put | 83100 | 120 | 120 | 1163.5 | 83622 | 1085.4 | 81936 | +1695 | +78.2 | strong |
| Put | 83200 | 460 | 460 | 1379.9 | 83227 | 984.0 | 81820 | +1811 | +395.9 | strong |
| Put | 83300 | 460 | 460 | 1447.4 | 83169 | 960.5 | 81853 | +1778 | +486.9 | strong |
| Put | 83400 | 720 | 720 | 1380.2 | 83427 | 1206.5 | 82020 | +1611 | +173.8 | strong |
| Put | 83500 | 8420 | 8154 | 1213.9 | 83863 | 1243.7 | 82286 | +1345 | -29.7 | strong |
| Put | 83600 | 1080 | 1080 | 1504.1 | 83359 | 1231.0 | 82096 | +1535 | +273.0 | strong |
| Put | 83700 | 640 | 640 | 1552.3 | 83332 | 1061.0 | 82148 | +1483 | +491.4 | strong |
| Put | 83800 | 840 | 840 | 1483.9 | 83560 | 1273.3 | 82316 | +1315 | +210.6 | strong |
| Put | 83900 | 420 | 409 | 1497.6 | 83620 | 1355.0 | 82402 | +1229 | +142.6 | strong |
| Put | 84000 | 17200 | 17200 | 1286.0 | 84125 | 1493.9 | 82714 | +917 | -207.9 | strong |
| Put | 84100 | 1620 | 1620 | 1465.8 | 83866 | 1506.2 | 82634 | +997 | -40.4 | strong |
| Put | 84200 | 1240 | 1240 | 1420.0 | 83990 | 1500.0 | 82780 | +851 | -80.0 | strong |
| Put | 84300 | 1080 | 1080 | 1586.5 | 83821 | 1501.3 | 82714 | +918 | +85.1 | strong |
| Put | 84400 | 1820 | 1820 | 1693.5 | 83714 | 1490.1 | 82707 | +925 | +203.4 | strong |
| Put | 84500 | 18940 | 18940 | 1539.2 | 84013 | 1728.0 | 82961 | +670 | -188.8 | strong |
| Put | 84600 | 940 | 940 | 1691.8 | 83913 | 1458.4 | 82908 | +723 | +233.4 | strong |
| Put | 84700 | 780 | 780 | 1645.8 | 84081 | 1584.2 | 83054 | +577 | +61.6 | strong |
| Put | 84800 | 800 | 800 | 1641.3 | 84214 | 1639.6 | 83159 | +472 | +1.7 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 12 | 36% | -0.30% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 11 | 60% | -0.10% | -0.60 to +0.16% |  | no clear direction |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 5 | 75% | +0.24% | -0.05 to +0.48% |  | too few (4/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 33% | -0.02% | -0.07 to +0.06% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 3 | 33% | -0.38% | -0.60 to +0.01% |  | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 100% | +0.65% | +0.11 to +0.97% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 0% | -0.46% | -0.80 to -0.08% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | -0.06% | -1.14 to +0.86% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.24% | -1.15 to +0.66% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 0% | -0.17% | -0.17 to -0.17% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 2 | 50% | +0.25% | -0.17 to +0.66% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near put wall | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.32% | +0.32 to +0.32% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls up · near put wall | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
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
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
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
| monthly | PCR down · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.83% | -0.83 to -0.83% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.46% | +0.46 to +0.46% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.46% | +0.46 to +0.46% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.83% | -0.83 to -0.83% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 47 | 60% | +0.05% | no clear direction |
| intraday | monthly | writers even · few weak writers | 46 | 63% | +0.01% | no clear direction |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 8 | 62% | -0.19% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers | 7 | 17% | -0.54% | too few (6/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | writers even · weak on both sides | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers | 5 | 50% | -0.26% | too few (4/10) |
| day | weekly | writers even · few weak writers | 4 | 67% | +0.17% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak on both sides | 1 | 0% | -0.83% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 41 | 62% | +0.01% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 29 | 59% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 67% | +0.02% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 8 | 62% | -0.19% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 6 | 17% | -0.54% | too few (6/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 5 | 75% | +0.04% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 50% | -0.26% | too few (4/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.65% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 0% | -0.83% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
