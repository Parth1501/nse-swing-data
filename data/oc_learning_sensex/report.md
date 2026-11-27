# Sensex option chain pattern log
Updated 2026-11-27 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 81 snapshots over 7 trading days
- 158 patterns logged; 74 different patterns so far

## Latest read (2026-11-27 13:47:00)

Sensex trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-03 (weekly) | 6.1 | 83659 | 0.669 | 83800 | 80000 | 84000 | ±1.69% (82246-85073) | 16.34 |
| 2026-12-31 (monthly) | 34.1 | 83659 | 1.016 | 84200 | 83000 | 84500 | ±3.18% (80998-86320) | 12.91 |

- **Weekly, last 30 min**: `PCR down · call writing · walls same · near call wall`. Seen 3 times before; Sensex was up after it 33% of the time, average -0.06%. Too few outcomes (3/20) to trade on.
  - Writers: `call writers stronger · few weak writers`. Seen 10 times before; Sensex was up after it 30% of the time, average -0.31%. Too few outcomes (10/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 4 times before; Sensex was up after it 50% of the time, average +0.02%. Too few outcomes (4/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls same · mid walls`. Seen 1 times before; Sensex was up after it 0% of the time, average -0.06%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 49 times before; Sensex was up after it 62% of the time, average +0.01%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 8 times before; Sensex was up after it 62% of the time, average +0.03%. Too few outcomes (8/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 50% of the time, average -0.25%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-12-03

Strongest call writers at 84000, strongest put writers at 83500; weakest call writers at 81500, weakest put writers at 84300. Covers 74% of near-money call OI and 64% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82500 | 19800 | 4596 | 1491.6 | 83741 | 1371.0 | 83992 | +332 | +120.6 | medium |
| Call | 82600 | 2860 | 1332 | 1397.8 | 83749 | 1310.0 | 83998 | +338 | +87.8 | medium |
| Call | 82700 | 2680 | 959 | 1293.4 | 83684 | 1265.2 | 83993 | +334 | +28.2 | medium |
| Call | 82800 | 5480 | 3040 | 1242.7 | 83706 | 1174.8 | 84043 | +383 | +67.9 | strong |
| Call | 82900 | 6720 | 4360 | 1185.0 | 83714 | 1108.9 | 84085 | +426 | +76.1 | strong |
| Call | 83000 | 66680 | 25836 | 1222.0 | 83839 | 1043.5 | 84222 | +563 | +178.5 | strong |
| Call | 83100 | 14740 | 11334 | 1086.0 | 83759 | 981.5 | 84186 | +527 | +104.4 | strong |
| Call | 83200 | 30320 | 20379 | 971.9 | 83692 | 921.2 | 84172 | +513 | +50.7 | strong |
| Call | 83300 | 23620 | 20187 | 937.7 | 83726 | 864.4 | 84238 | +578 | +73.3 | strong |
| Call | 83400 | 69160 | 65020 | 899.3 | 83761 | 805.1 | 84299 | +640 | +94.2 | strong |
| Call | 83500 | 253520 | 204720 | 807.9 | 83702 | 756.0 | 84308 | +649 | +52.0 | strong |
| Call | 83600 | 253300 | 245240 | 732.6 | 83661 | 701.8 | 84333 | +673 | +30.8 | strong |
| Call | 83700 | 311420 | 294993 | 718.0 | 83725 | 654.8 | 84418 | +759 | +63.2 | strong |
| Call | 83800 | 273920 | 248900 | 703.5 | 83787 | 608.8 | 84503 | +844 | +94.7 | strong |
| Call | 83900 | 235980 | 196647 | 721.1 | 83895 | 569.0 | 84621 | +962 | +152.1 | strong |
| Call | 84000 | 1015180 | 724360 | 687.1 | 83916 | 529.1 | 84687 | +1028 | +158.0 | strong |
| Call | 84100 | 405180 | 326491 | 719.9 | 84065 | 489.6 | 84820 | +1161 | +230.3 | strong |
| Call | 84200 | 413880 | 351864 | 672.8 | 84061 | 453.2 | 84873 | +1214 | +219.6 | strong |
| Call | 84300 | 314280 | 182440 | 631.0 | 84061 | 417.1 | 84931 | +1272 | +213.9 | strong |
| Call | 84400 | 211180 | 135395 | 509.0 | 83891 | 384.9 | 84909 | +1250 | +124.1 | strong |
| Call | 84500 | 513380 | 291150 | 508.3 | 83987 | 354.9 | 85008 | +1349 | +153.3 | strong |
| Call | 84600 | 163560 | 123801 | 458.9 | 83958 | 328.1 | 85059 | +1400 | +130.8 | strong |
| Call | 84700 | 133600 | 104720 | 424.8 | 83961 | 301.1 | 85125 | +1465 | +123.7 | strong |
| Call | 84800 | 144940 | 121260 | 386.1 | 83956 | 277.4 | 85186 | +1527 | +108.7 | strong |
| Call | 84900 | 129280 | 106011 | 347.0 | 83922 | 253.0 | 85247 | +1588 | +94.0 | strong |
| Put | 82500 | 170320 | 77671 | 218.7 | 84027 | 282.1 | 82281 | +1378 | -63.3 | strong |
| Put | 82600 | 76320 | 58087 | 258.8 | 83944 | 308.9 | 82341 | +1318 | -50.1 | strong |
| Put | 82700 | 79200 | 58778 | 287.6 | 83913 | 338.7 | 82412 | +1247 | -51.1 | strong |
| Put | 82800 | 85040 | 65725 | 295.0 | 83977 | 368.8 | 82505 | +1154 | -73.8 | strong |
| Put | 82900 | 77040 | 65396 | 330.8 | 83941 | 402.2 | 82569 | +1090 | -71.4 | strong |
| Put | 83000 | 293840 | 166809 | 312.3 | 84100 | 437.9 | 82688 | +972 | -125.6 | strong |
| Put | 83100 | 76820 | 57724 | 349.5 | 84066 | 475.6 | 82750 | +909 | -126.0 | strong |
| Put | 83200 | 101120 | 73415 | 431.1 | 83923 | 518.9 | 82769 | +890 | -87.8 | strong |
| Put | 83300 | 87240 | 78699 | 488.4 | 83873 | 558.3 | 82812 | +848 | -69.9 | strong |
| Put | 83400 | 113620 | 91356 | 493.4 | 83937 | 606.9 | 82907 | +753 | -113.5 | strong |
| Put | 83500 | 341700 | 216371 | 563.0 | 83878 | 650.9 | 82937 | +722 | -87.9 | strong |
| Put | 83600 | 209000 | 187201 | 633.2 | 83810 | 706.5 | 82967 | +693 | -73.2 | strong |
| Put | 83700 | 169080 | 144233 | 655.0 | 83870 | 758.9 | 83045 | +614 | -103.9 | strong |
| Put | 83800 | 136420 | 104627 | 644.9 | 83962 | 813.1 | 83155 | +504 | -168.2 | strong |
| Put | 83900 | 117620 | 81641 | 656.5 | 84009 | 863.9 | 83244 | +416 | -207.4 | strong |
| Put | 84000 | 522380 | 270428 | 667.5 | 84102 | 922.2 | 83332 | +327 | -254.7 | medium |
| Put | 84100 | 198800 | 139826 | 740.9 | 84056 | 984.9 | 83359 | +300 | -244.0 | medium |
| Put | 84200 | 110500 | 83122 | 767.9 | 84096 | 1047.2 | 83432 | +227 | -279.2 | medium |
| Put | 84300 | 87840 | 25890 | 818.5 | 84099 | 1113.8 | 83482 | +178 | -295.4 | weak |
| Put | 84400 | 55880 | 14385 | 863.4 | 84106 | 1180.0 | 83537 | +123 | -316.7 | weak |
| Put | 84500 | 103600 | 4873 | 1198.3 | 83733 | 1252.9 | 83302 | +358 | -54.6 | medium |
| Put | 84600 | 19060 | 8209 | 1019.1 | 84063 | 1335.0 | 83581 | +78 | -315.9 | weak |
| Put | 84700 | 10480 | 3867 | 1086.3 | 84045 | 1384.9 | 83614 | +46 | -298.6 | weak |
| Put | 84800 | 12960 | 7342 | 1123.9 | 84088 | 1439.3 | 83676 | -17 | -315.4 | weak |
| Put | 84900 | 7080 | 3066 | 1238.4 | 84014 | 1615.0 | 83662 | -2 | -376.6 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 84500, strongest put writers at 84500; weakest call writers at -, weakest put writers at 86000. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82500 | 820 | 796 | 2523.3 | 83629 | 2292.0 | 85023 | +1364 | +231.3 | strong |
| Call | 82600 | 120 | 120 | 1778.5 | 82439 | 1789.5 | 84378 | +719 | -10.9 | strong |
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +886 | -732.3 | strong |
| Call | 82800 | 1560 | 1487 | 2302.3 | 83528 | 2251.6 | 85102 | +1443 | +50.7 | strong |
| Call | 82900 | 220 | 186 | 1609.0 | 82444 | 2407.8 | 84509 | +850 | -798.9 | strong |
| Call | 83000 | 4660 | 4542 | 2213.6 | 83644 | 2030.0 | 85214 | +1554 | +183.6 | strong |
| Call | 83100 | 600 | 567 | 1626.2 | 82730 | 2289.2 | 84726 | +1067 | -663.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +1140 | -1016.5 | strong |
| Call | 83300 | 440 | 440 | 1780.0 | 83299 | 1924.8 | 85080 | +1421 | -144.8 | strong |
| Call | 83400 | 520 | 511 | 1612.7 | 83261 | 2300.0 | 85013 | +1353 | -687.3 | strong |
| Call | 83500 | 8660 | 8590 | 2086.6 | 83845 | 1708.7 | 85587 | +1927 | +378.0 | strong |
| Call | 83600 | 800 | 800 | 1790.5 | 83671 | 1700.0 | 85390 | +1731 | +90.5 | strong |
| Call | 83700 | 940 | 940 | 1622.6 | 83373 | 1600.0 | 85323 | +1663 | +22.6 | strong |
| Call | 83800 | 280 | 280 | 1697.3 | 83653 | 1713.3 | 85497 | +1838 | -16.1 | strong |
| Call | 83900 | 500 | 483 | 1509.7 | 83446 | 1508.1 | 85410 | +1750 | +1.6 | strong |
| Call | 84000 | 16360 | 16360 | 1780.8 | 83917 | 1518.7 | 85781 | +2122 | +262.1 | strong |
| Call | 84100 | 620 | 620 | 1630.0 | 83814 | 1404.5 | 85730 | +2071 | +225.4 | strong |
| Call | 84200 | 540 | 536 | 1488.9 | 83645 | 1354.8 | 85689 | +2030 | +134.1 | strong |
| Call | 84300 | 560 | 560 | 1607.7 | 83991 | 1399.8 | 85908 | +2248 | +207.9 | strong |
| Call | 84400 | 700 | 700 | 1453.8 | 83745 | 1268.1 | 85854 | +2194 | +185.7 | strong |
| Call | 84500 | 25040 | 25040 | 1450.1 | 83912 | 1199.1 | 85950 | +2291 | +251.0 | strong |
| Call | 84600 | 580 | 580 | 1371.6 | 83791 | 1420.0 | 85972 | +2312 | -48.4 | strong |
| Call | 84700 | 560 | 560 | 1269.8 | 83636 | 1249.2 | 85970 | +2311 | +20.6 | strong |
| Call | 84800 | 320 | 320 | 1243.1 | 83586 | 1330.0 | 86043 | +2384 | -87.0 | strong |
| Call | 84900 | 500 | 500 | 1161.1 | 83466 | 1059.3 | 86061 | +2402 | +101.8 | strong |
| Put | 82500 | 2460 | 2397 | 990.7 | 83571 | 867.1 | 81509 | +2150 | +123.6 | strong |
| Put | 82600 | 800 | 800 | 919.9 | 83832 | 884.0 | 81680 | +1979 | +35.9 | strong |
| Put | 82700 | 420 | 420 | 939.7 | 83833 | 930.0 | 81760 | +1899 | +9.7 | strong |
| Put | 82800 | 520 | 520 | 931.8 | 83810 | 949.7 | 81868 | +1791 | -17.9 | strong |
| Put | 82900 | 160 | 160 | 1015.8 | 83805 | 850.0 | 81884 | +1775 | +165.8 | strong |
| Put | 83000 | 11860 | 11444 | 1075.5 | 83776 | 1060.0 | 81924 | +1735 | +15.6 | strong |
| Put | 83100 | 140 | 140 | 1146.9 | 83627 | 1047.0 | 81953 | +1706 | +99.9 | strong |
| Put | 83200 | 460 | 460 | 1379.9 | 83227 | 984.0 | 81820 | +1839 | +395.9 | strong |
| Put | 83300 | 460 | 460 | 1447.4 | 83169 | 960.5 | 81853 | +1807 | +486.9 | strong |
| Put | 83400 | 720 | 720 | 1380.2 | 83427 | 1206.5 | 82020 | +1640 | +173.8 | strong |
| Put | 83500 | 8420 | 8159 | 1213.7 | 83860 | 1205.7 | 82286 | +1373 | +8.0 | strong |
| Put | 83600 | 1100 | 1100 | 1487.1 | 83378 | 1336.5 | 82113 | +1546 | +150.6 | strong |
| Put | 83700 | 640 | 640 | 1552.3 | 83332 | 1061.0 | 82148 | +1512 | +491.4 | strong |
| Put | 83800 | 840 | 840 | 1483.9 | 83560 | 1273.3 | 82316 | +1343 | +210.6 | strong |
| Put | 83900 | 440 | 429 | 1489.5 | 83625 | 1460.0 | 82411 | +1249 | +29.5 | strong |
| Put | 84000 | 16860 | 16860 | 1286.0 | 84125 | 1456.8 | 82714 | +945 | -170.9 | strong |
| Put | 84100 | 1620 | 1620 | 1465.8 | 83866 | 1503.5 | 82634 | +1025 | -37.6 | strong |
| Put | 84200 | 1240 | 1240 | 1420.0 | 83990 | 1500.0 | 82780 | +879 | -80.0 | strong |
| Put | 84300 | 1080 | 1080 | 1586.5 | 83821 | 1501.3 | 82714 | +946 | +85.1 | strong |
| Put | 84400 | 1740 | 1740 | 1693.5 | 83714 | 1580.5 | 82707 | +953 | +113.0 | strong |
| Put | 84500 | 23720 | 23720 | 1584.2 | 83935 | 1709.5 | 82916 | +743 | -125.4 | strong |
| Put | 84600 | 940 | 940 | 1691.8 | 83913 | 1458.4 | 82908 | +751 | +233.4 | strong |
| Put | 84700 | 780 | 780 | 1645.8 | 84081 | 1584.2 | 83054 | +605 | +61.6 | strong |
| Put | 84800 | 800 | 800 | 1641.3 | 84214 | 1639.6 | 83159 | +501 | +1.7 | strong |
| Put | 84900 | 780 | 780 | 2253.9 | 83187 | 1582.0 | 82646 | +1013 | +672.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 12 | 36% | -0.30% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 11 | 60% | -0.10% | -0.56 to +0.16% |  | no clear direction |
| monthly | PCR down · put and call writing · walls same · near put wall | 5 | 75% | +0.24% | -0.05 to +0.48% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 33% | -0.02% | -0.07 to +0.06% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · near call wall | 4 | 33% | -0.06% | -0.14 to +0.03% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.24% | -1.15 to +0.66% | 100% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 3 | 33% | -0.36% | -0.56 to +0.01% |  | too few (3/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 0% | -0.46% | -0.80 to -0.08% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 100% | +0.65% | +0.11 to +0.97% | 0% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | -0.06% | -1.14 to +0.86% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | +0.05% | -0.02 to +0.12% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 2 | 50% | +0.26% | -0.13 to +0.66% |  | too few (2/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 2 | 0% | -0.06% | -0.06 to -0.06% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.01% | -0.02 to +0.05% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near put wall | 1 | 0% | -0.31% | -0.31 to -0.31% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.32% | +0.32 to +0.32% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls up · near put wall | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 0% | -0.31% | -0.31 to -0.31% |  | too few (1/10) |
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
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.79% | -0.79 to -0.79% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.46% | +0.46 to +0.46% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.46% | +0.46 to +0.46% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.79% | -0.79 to -0.79% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 50 | 62% | +0.01% | no clear direction |
| intraday | weekly | writers even · few weak writers | 47 | 60% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | call writers stronger · few weak writers | 11 | 30% | -0.31% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 8 | 62% | -0.19% | too few (8/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | writers even · weak on both sides | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers | 5 | 50% | -0.25% | too few (4/10) |
| day | weekly | writers even · few weak writers | 4 | 67% | +0.17% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak on both sides | 1 | 0% | -0.79% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 41 | 62% | +0.01% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 29 | 59% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 67% | +0.02% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 9 | 62% | +0.03% | too few (8/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 8 | 62% | -0.19% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 6 | 17% | -0.53% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 5 | 50% | +0.02% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 50% | -0.25% | too few (4/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.65% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 0% | -0.79% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
