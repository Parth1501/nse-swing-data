# Sensex option chain pattern log
Updated 2026-11-27 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 85 snapshots over 7 trading days
- 166 patterns logged; 77 different patterns so far

## Latest read (2026-11-27 15:47:00)

Sensex trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-03 (weekly) | 6.0 | 83339 | 0.611 | 83600 | 80000 | 84000 | ±1.67% (81943-84735) | 16.41 |
| 2026-12-31 (monthly) | 34.0 | 83339 | 1.157 | 84300 | 83000 | 84500 | ±3.53% (80396-86282) | 14.33 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls same · near call wall`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.02%. Too few outcomes (1/20) to trade on.
  - Writers: `call writers stronger · few weak writers`. Seen 14 times before; Sensex was up after it 14% of the time, average -0.42%. Too few outcomes (14/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 8 times before; Sensex was up after it 12% of the time, average -0.28%. Too few outcomes (8/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · near put wall`. Seen 5 times before; Sensex was up after it 75% of the time, average +0.24%. Too few outcomes (4/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 53 times before; Sensex was up after it 55% of the time, average -0.07%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 12 times before; Sensex was up after it 33% of the time, average -0.17%. Too few outcomes (12/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls down · near put wall`. Seen 1 times before. Too few outcomes (0/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 50% of the time, average -0.35%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-12-03

Strongest call writers at 84000, strongest put writers at 81500; weakest call writers at 81000, weakest put writers at 84000. Covers 76% of near-money call OI and 64% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82100 | 2180 | 220 | 1524.5 | 83547 | 1448.7 | 83624 | +285 | +75.8 | medium |
| Call | 82200 | 1900 | 493 | 1596.1 | 83572 | 1388.0 | 83796 | +457 | +208.1 | strong |
| Call | 82300 | 1460 | 435 | 1551.3 | 83570 | 1285.5 | 83851 | +512 | +265.8 | strong |
| Call | 82400 | 2020 | 1356 | 1596.7 | 83779 | 1237.1 | 83997 | +657 | +359.6 | strong |
| Call | 82500 | 21360 | 6964 | 1422.0 | 83649 | 1170.3 | 83922 | +583 | +251.7 | strong |
| Call | 82600 | 5440 | 3950 | 1224.6 | 83498 | 1104.2 | 83825 | +485 | +120.4 | strong |
| Call | 82700 | 4520 | 2799 | 1168.9 | 83503 | 1040.9 | 83869 | +530 | +128.0 | strong |
| Call | 82800 | 7580 | 5140 | 1176.5 | 83609 | 985.0 | 83976 | +637 | +191.5 | strong |
| Call | 82900 | 9260 | 6955 | 1105.1 | 83593 | 924.0 | 84005 | +666 | +181.1 | strong |
| Call | 83000 | 77600 | 37920 | 1103.0 | 83665 | 867.9 | 84103 | +764 | +235.1 | strong |
| Call | 83100 | 19400 | 16751 | 958.1 | 83556 | 814.5 | 84058 | +719 | +143.6 | strong |
| Call | 83200 | 46140 | 37887 | 853.5 | 83488 | 765.0 | 84054 | +714 | +88.5 | strong |
| Call | 83300 | 108000 | 104567 | 755.2 | 83413 | 708.9 | 84055 | +716 | +46.3 | strong |
| Call | 83400 | 144880 | 141352 | 761.2 | 83514 | 663.0 | 84161 | +822 | +98.1 | strong |
| Call | 83500 | 294840 | 249986 | 777.9 | 83646 | 617.2 | 84278 | +939 | +160.7 | strong |
| Call | 83600 | 198660 | 192796 | 722.9 | 83643 | 577.8 | 84323 | +984 | +145.1 | strong |
| Call | 83700 | 253640 | 240485 | 715.2 | 83719 | 534.1 | 84415 | +1076 | +181.1 | strong |
| Call | 83800 | 201120 | 182750 | 703.5 | 83787 | 504.3 | 84503 | +1164 | +199.2 | strong |
| Call | 83900 | 179220 | 149589 | 719.7 | 83892 | 465.1 | 84620 | +1280 | +254.6 | strong |
| Call | 84000 | 775160 | 553099 | 687.1 | 83916 | 436.0 | 84687 | +1348 | +251.1 | strong |
| Call | 84100 | 274720 | 221367 | 719.9 | 84065 | 399.9 | 84820 | +1481 | +320.0 | strong |
| Call | 84200 | 333600 | 283613 | 672.8 | 84061 | 373.5 | 84873 | +1534 | +299.3 | strong |
| Call | 84300 | 327680 | 201503 | 593.0 | 83964 | 346.1 | 84893 | +1554 | +246.9 | strong |
| Call | 84400 | 204820 | 134541 | 496.3 | 83856 | 318.0 | 84896 | +1557 | +178.3 | strong |
| Call | 84500 | 519640 | 314927 | 475.4 | 83895 | 292.5 | 84975 | +1636 | +182.9 | strong |
| Put | 82100 | 66160 | 58526 | 180.9 | 83802 | 237.4 | 81919 | +1420 | -56.5 | strong |
| Put | 82200 | 47720 | 33300 | 186.6 | 83908 | 265.8 | 82013 | +1326 | -79.2 | strong |
| Put | 82300 | 44660 | 35483 | 209.2 | 83841 | 295.4 | 82091 | +1248 | -86.2 | strong |
| Put | 82400 | 60260 | 42056 | 221.3 | 83881 | 321.2 | 82179 | +1161 | -99.9 | strong |
| Put | 82500 | 197300 | 111001 | 257.5 | 83800 | 349.2 | 82242 | +1097 | -91.7 | strong |
| Put | 82600 | 49940 | 38009 | 258.8 | 83944 | 381.1 | 82341 | +998 | -122.3 | strong |
| Put | 82700 | 47340 | 35588 | 292.6 | 83889 | 422.9 | 82407 | +932 | -130.4 | strong |
| Put | 82800 | 51800 | 40035 | 295.0 | 83977 | 456.0 | 82505 | +834 | -161.0 | strong |
| Put | 82900 | 53560 | 45650 | 333.1 | 83930 | 498.8 | 82567 | +772 | -165.7 | strong |
| Put | 83000 | 206280 | 117127 | 312.4 | 84100 | 542.0 | 82688 | +652 | -229.6 | strong |
| Put | 83100 | 44260 | 33460 | 352.4 | 84055 | 588.0 | 82748 | +592 | -235.6 | strong |
| Put | 83200 | 65680 | 49244 | 450.8 | 83854 | 631.6 | 82749 | +590 | -180.9 | strong |
| Put | 83300 | 104060 | 95991 | 524.4 | 83753 | 687.0 | 82776 | +564 | -162.6 | strong |
| Put | 83400 | 78100 | 66154 | 542.2 | 83804 | 738.9 | 82858 | +481 | -196.7 | strong |
| Put | 83500 | 195100 | 129320 | 578.8 | 83832 | 791.9 | 82921 | +418 | -213.1 | strong |
| Put | 83600 | 121740 | 111298 | 657.4 | 83747 | 853.2 | 82943 | +397 | -195.8 | strong |
| Put | 83700 | 89140 | 76041 | 655.0 | 83870 | 910.4 | 83045 | +294 | -255.4 | medium |
| Put | 83800 | 66180 | 50934 | 648.7 | 83954 | 970.8 | 83151 | +188 | -322.0 | medium |
| Put | 83900 | 90940 | 63122 | 656.5 | 84009 | 1038.2 | 83244 | +96 | -381.8 | weak |
| Put | 84000 | 326000 | 168765 | 667.5 | 84102 | 1106.8 | 83332 | +7 | -439.3 | weak |
| Put | 84100 | 88420 | 62190 | 740.9 | 84056 | 1173.2 | 83359 | -20 | -432.3 | weak |
| Put | 84200 | 78700 | 59201 | 767.9 | 84096 | 1232.4 | 83432 | -93 | -464.5 | weak |
| Put | 84300 | 62860 | 19203 | 832.7 | 84074 | 1312.2 | 83467 | -128 | -479.4 | weak |
| Put | 84400 | 47600 | 12253 | 863.4 | 84106 | 1382.4 | 83537 | -197 | -519.0 | weak |
| Put | 84500 | 86080 | 4049 | 1198.3 | 83733 | 1458.5 | 83302 | +38 | -260.2 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 84500, strongest put writers at 84500; weakest call writers at -, weakest put writers at 85000. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82200 | 160 | 120 | 2106.2 | 82925 | 2016.4 | 84306 | +967 | +89.8 | strong |
| Call | 82300 | 100 | 100 | 2104.6 | 82925 | 2300.0 | 84405 | +1065 | -195.4 | strong |
| Call | 82400 | 120 | 120 | 1994.6 | 82762 | 2765.2 | 84395 | +1055 | -770.6 | strong |
| Call | 82500 | 820 | 797 | 2518.2 | 83629 | 2173.0 | 85018 | +1679 | +345.2 | strong |
| Call | 82600 | 120 | 120 | 1778.5 | 82439 | 1789.5 | 84378 | +1039 | -10.9 | strong |
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +1206 | -732.3 | strong |
| Call | 82800 | 1560 | 1487 | 2302.3 | 83528 | 2251.6 | 85102 | +1763 | +50.7 | strong |
| Call | 82900 | 220 | 186 | 1609.0 | 82444 | 2407.8 | 84509 | +1170 | -798.9 | strong |
| Call | 83000 | 5160 | 5043 | 2180.2 | 83615 | 1877.5 | 85180 | +1841 | +302.8 | strong |
| Call | 83100 | 600 | 567 | 1626.2 | 82730 | 2289.2 | 84726 | +1387 | -663.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +1460 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1771.3 | 83302 | 1706.0 | 85071 | +1732 | +65.3 | strong |
| Call | 83400 | 600 | 592 | 1621.0 | 83275 | 1662.0 | 85021 | +1682 | -41.0 | strong |
| Call | 83500 | 8940 | 8870 | 2067.1 | 83826 | 1598.0 | 85567 | +2228 | +469.0 | strong |
| Call | 83600 | 740 | 740 | 1790.5 | 83671 | 1533.2 | 85390 | +2051 | +257.3 | strong |
| Call | 83700 | 960 | 960 | 1622.7 | 83374 | 1630.0 | 85323 | +1983 | -7.3 | strong |
| Call | 83800 | 640 | 640 | 1540.0 | 83472 | 1429.5 | 85340 | +2001 | +110.5 | strong |
| Call | 83900 | 680 | 663 | 1490.7 | 83446 | 1373.4 | 85391 | +2051 | +117.3 | strong |
| Call | 84000 | 22720 | 22720 | 1662.8 | 83755 | 1349.5 | 85663 | +2324 | +313.3 | strong |
| Call | 84100 | 740 | 740 | 1578.7 | 83736 | 1287.5 | 85679 | +2339 | +291.2 | strong |
| Call | 84200 | 540 | 536 | 1488.9 | 83645 | 1241.3 | 85689 | +2350 | +247.6 | strong |
| Call | 84300 | 580 | 580 | 1584.1 | 83949 | 1195.0 | 85884 | +2545 | +389.1 | strong |
| Call | 84400 | 720 | 720 | 1446.4 | 83733 | 1189.0 | 85846 | +2507 | +257.4 | strong |
| Call | 84500 | 33660 | 33660 | 1366.9 | 83765 | 1122.5 | 85867 | +2528 | +244.3 | strong |
| Put | 82100 | 380 | 380 | 742.7 | 83699 | 759.1 | 81357 | +1982 | -16.4 | strong |
| Put | 82200 | 460 | 460 | 797.9 | 83561 | 833.5 | 81402 | +1937 | -35.6 | strong |
| Put | 82300 | 820 | 820 | 940.3 | 83524 | 767.6 | 81360 | +1980 | +172.6 | strong |
| Put | 82400 | 1280 | 1280 | 950.8 | 83582 | 899.0 | 81449 | +1890 | +51.9 | strong |
| Put | 82500 | 2660 | 2597 | 986.6 | 83552 | 940.2 | 81513 | +1826 | +46.4 | strong |
| Put | 82600 | 820 | 820 | 920.8 | 83819 | 955.9 | 81679 | +1660 | -35.1 | strong |
| Put | 82700 | 540 | 540 | 939.7 | 83782 | 940.0 | 81760 | +1579 | -0.3 | strong |
| Put | 82800 | 520 | 520 | 931.8 | 83810 | 949.7 | 81868 | +1471 | -17.9 | strong |
| Put | 82900 | 160 | 160 | 1015.8 | 83805 | 1034.0 | 81884 | +1455 | -18.1 | strong |
| Put | 83000 | 11800 | 11392 | 1075.8 | 83770 | 1115.2 | 81924 | +1415 | -39.4 | strong |
| Put | 83100 | 140 | 140 | 1134.3 | 83624 | 1164.0 | 81966 | +1374 | -29.6 | strong |
| Put | 83200 | 460 | 460 | 1379.9 | 83227 | 984.0 | 81820 | +1519 | +395.9 | strong |
| Put | 83300 | 340 | 340 | 1447.4 | 83169 | 1236.8 | 81853 | +1487 | +210.6 | strong |
| Put | 83400 | 720 | 720 | 1380.2 | 83427 | 1206.5 | 82020 | +1320 | +173.8 | strong |
| Put | 83500 | 8460 | 8202 | 1215.2 | 83851 | 1309.3 | 82285 | +1055 | -94.1 | strong |
| Put | 83600 | 1080 | 1080 | 1487.1 | 83378 | 1344.9 | 82113 | +1226 | +142.2 | strong |
| Put | 83700 | 620 | 620 | 1552.3 | 83332 | 1392.7 | 82148 | +1192 | +159.7 | strong |
| Put | 83800 | 840 | 840 | 1483.9 | 83560 | 1402.7 | 82316 | +1023 | +81.3 | strong |
| Put | 83900 | 420 | 410 | 1486.8 | 83624 | 1521.7 | 82413 | +926 | -34.8 | strong |
| Put | 84000 | 21280 | 21280 | 1343.8 | 83953 | 1571.4 | 82656 | +683 | -227.6 | strong |
| Put | 84100 | 1460 | 1460 | 1465.8 | 83866 | 1520.5 | 82634 | +705 | -54.6 | strong |
| Put | 84200 | 1240 | 1240 | 1420.0 | 83990 | 1500.0 | 82780 | +559 | -80.0 | strong |
| Put | 84300 | 1080 | 1080 | 1586.5 | 83821 | 1717.7 | 82714 | +626 | -131.2 | strong |
| Put | 84400 | 1720 | 1720 | 1693.5 | 83714 | 1784.3 | 82707 | +633 | -90.8 | strong |
| Put | 84500 | 32560 | 32560 | 1653.5 | 83772 | 1859.8 | 82847 | +493 | -206.4 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 12 | 36% | -0.30% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 12 | 64% | -0.16% | -0.94 to +0.16% |  | no clear direction |
| monthly | PCR down · put and call writing · walls same · near put wall | 6 | 75% | +0.24% | -0.05 to +0.48% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| weekly | PCR down · call writing · walls same · near call wall | 4 | 0% | -0.42% | -0.52 to -0.35% |  | too few (4/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 33% | -0.02% | -0.07 to +0.06% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 0% | -0.46% | -0.80 to -0.08% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 3 | 33% | -0.61% | -0.94 to +0.01% |  | too few (3/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.24% | -1.15 to +0.66% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 100% | +0.65% | +0.11 to +0.97% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 3 | 0% | -0.38% | -0.44 to -0.32% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | -0.06% | -1.14 to +0.86% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 0% | -0.33% | -0.40 to -0.26% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 2 | 50% | +0.07% | -0.52 to +0.66% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.18% | -0.40 to +0.05% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls up · near put wall | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.32% | +0.32 to +0.32% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near put wall | 1 | 0% | -0.10% | -0.10 to -0.10% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near call wall | 1 | 0% | -0.26% | -0.26 to -0.26% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near call wall | 1 | 0% | -0.32% | -0.32 to -0.32% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.19% | +0.19 to +0.19% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.10% | -0.10 to -0.10% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 0% | -0.44% | -0.44 to -0.44% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put and call writing · walls down · near put wall | 2 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.82% | +1.82 to +1.82% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.46% | +0.46 to +0.46% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -1.17% | -1.17 to -1.17% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.46% | +0.46 to +0.46% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -1.17% | -1.17 to -1.17% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 54 | 55% | -0.07% | no clear direction |
| intraday | weekly | writers even · few weak writers | 47 | 60% | +0.02% | no clear direction |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | call writers stronger · few weak writers | 15 | 14% | -0.42% | down |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 8 | 62% | -0.19% | too few (8/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | writers even · weak on both sides | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers | 5 | 50% | -0.35% | too few (4/10) |
| day | weekly | writers even · few weak writers | 4 | 67% | +0.17% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak on both sides | 1 | 0% | -1.17% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 41 | 62% | -0.04% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 29 | 59% | +0.02% | no clear direction |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 67% | +0.02% | too few (3/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 13 | 33% | -0.17% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 9 | 12% | -0.28% | too few (8/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 8 | 62% | -0.19% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 6 | 17% | -0.60% | too few (6/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 50% | -0.35% | too few (4/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.65% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 0% | -1.17% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
