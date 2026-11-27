# Sensex option chain pattern log
Updated 2026-11-27 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 83 snapshots over 7 trading days
- 162 patterns logged; 76 different patterns so far

## Latest read (2026-11-27 14:46:00)

Sensex trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-03 (weekly) | 6.0 | 83422 | 0.766 | 83800 | 80000 | 84000 | ±1.65% (82042-84802) | 16.07 |
| 2026-12-31 (monthly) | 34.0 | 83422 | 1.185 | 84200 | 83000 | 84500 | ±3.53% (80474-86371) | 14.32 |

- **Weekly, last 30 min**: `PCR up · put writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 12 times before; Sensex was up after it 8% of the time, average -0.42%. Too few outcomes (12/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 6 times before; Sensex was up after it 0% of the time, average -0.26%. Too few outcomes (6/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · unwinding · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 51 times before; Sensex was up after it 55% of the time, average -0.05%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 10 times before; Sensex was up after it 30% of the time, average -0.14%. Too few outcomes (10/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls down · near put wall`. Seen 1 times before. Too few outcomes (0/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 50% of the time, average -0.32%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-12-03

Strongest call writers at 84000, strongest put writers at 83500; weakest call writers at 81000, weakest put writers at 84000. Covers 76% of near-money call OI and 65% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82200 | 1740 | 333 | 1696.2 | 83684 | 1515.0 | 83896 | +474 | +181.1 | strong |
| Call | 82300 | 1540 | 431 | 1574.4 | 83593 | 1440.0 | 83874 | +452 | +134.4 | strong |
| Call | 82400 | 1860 | 1181 | 1658.9 | 83855 | 1453.5 | 84059 | +637 | +205.3 | strong |
| Call | 82500 | 22560 | 7356 | 1422.0 | 83649 | 1251.8 | 83922 | +500 | +170.2 | strong |
| Call | 82600 | 3200 | 1710 | 1377.2 | 83715 | 1170.0 | 83977 | +555 | +207.2 | strong |
| Call | 82700 | 3400 | 1679 | 1252.0 | 83618 | 1130.9 | 83952 | +530 | +121.1 | strong |
| Call | 82800 | 6860 | 4420 | 1207.5 | 83655 | 1042.8 | 84008 | +585 | +164.7 | strong |
| Call | 82900 | 7840 | 5480 | 1159.6 | 83675 | 985.5 | 84060 | +637 | +174.1 | strong |
| Call | 83000 | 64780 | 25100 | 1222.0 | 83839 | 915.1 | 84222 | +800 | +306.9 | strong |
| Call | 83100 | 15280 | 11930 | 1071.2 | 83737 | 860.0 | 84171 | +749 | +211.2 | strong |
| Call | 83200 | 28940 | 19510 | 970.3 | 83690 | 799.9 | 84170 | +748 | +170.4 | strong |
| Call | 83300 | 31820 | 28387 | 886.5 | 83644 | 748.9 | 84186 | +764 | +137.6 | strong |
| Call | 83400 | 98540 | 94558 | 831.1 | 83646 | 698.0 | 84231 | +809 | +133.2 | strong |
| Call | 83500 | 300060 | 251260 | 791.6 | 83672 | 650.1 | 84292 | +869 | +141.4 | strong |
| Call | 83600 | 255280 | 247744 | 722.9 | 83643 | 602.0 | 84323 | +901 | +120.9 | strong |
| Call | 83700 | 305500 | 289656 | 715.2 | 83719 | 561.6 | 84415 | +993 | +153.6 | strong |
| Call | 83800 | 265460 | 241213 | 703.5 | 83787 | 518.5 | 84503 | +1081 | +184.9 | strong |
| Call | 83900 | 229200 | 191305 | 719.7 | 83892 | 480.9 | 84620 | +1197 | +238.7 | strong |
| Call | 84000 | 934120 | 666521 | 687.1 | 83916 | 444.9 | 84687 | +1265 | +242.3 | strong |
| Call | 84100 | 388540 | 313082 | 719.9 | 84065 | 410.0 | 84820 | +1398 | +309.9 | strong |
| Call | 84200 | 391520 | 332854 | 672.8 | 84061 | 377.3 | 84873 | +1451 | +295.5 | strong |
| Call | 84300 | 303740 | 176322 | 631.0 | 84061 | 347.4 | 84931 | +1509 | +283.7 | strong |
| Call | 84400 | 210920 | 136671 | 503.4 | 83877 | 321.3 | 84903 | +1481 | +182.2 | strong |
| Call | 84500 | 531060 | 311566 | 491.9 | 83943 | 295.2 | 84992 | +1570 | +196.6 | strong |
| Call | 84600 | 169960 | 130201 | 450.1 | 83933 | 269.8 | 85050 | +1628 | +180.3 | strong |
| Put | 82200 | 72120 | 50326 | 186.6 | 83908 | 242.7 | 82013 | +1409 | -56.1 | strong |
| Put | 82300 | 65720 | 52216 | 209.2 | 83841 | 268.2 | 82091 | +1331 | -59.0 | strong |
| Put | 82400 | 68760 | 47989 | 221.3 | 83881 | 295.0 | 82179 | +1244 | -73.7 | strong |
| Put | 82500 | 164700 | 78401 | 223.4 | 83995 | 323.1 | 82277 | +1146 | -99.6 | strong |
| Put | 82600 | 73100 | 55636 | 258.8 | 83944 | 352.4 | 82341 | +1081 | -93.6 | strong |
| Put | 82700 | 81160 | 61012 | 292.6 | 83889 | 387.1 | 82407 | +1015 | -94.5 | strong |
| Put | 82800 | 78800 | 60902 | 295.0 | 83977 | 421.2 | 82505 | +917 | -126.3 | strong |
| Put | 82900 | 78840 | 67196 | 333.1 | 83930 | 458.9 | 82567 | +855 | -125.8 | strong |
| Put | 83000 | 293220 | 166492 | 312.4 | 84100 | 497.6 | 82688 | +735 | -185.2 | strong |
| Put | 83100 | 74380 | 56231 | 352.4 | 84055 | 540.6 | 82748 | +675 | -188.2 | strong |
| Put | 83200 | 91940 | 66750 | 431.1 | 83923 | 584.4 | 82769 | +653 | -153.3 | strong |
| Put | 83300 | 91240 | 82724 | 495.7 | 83850 | 630.0 | 82804 | +618 | -134.4 | strong |
| Put | 83400 | 143720 | 121738 | 542.2 | 83804 | 681.9 | 82858 | +564 | -139.7 | strong |
| Put | 83500 | 371720 | 246391 | 578.8 | 83832 | 728.6 | 82921 | +501 | -149.8 | strong |
| Put | 83600 | 254160 | 232361 | 657.4 | 83747 | 787.1 | 82943 | +480 | -129.7 | strong |
| Put | 83700 | 161440 | 137716 | 655.0 | 83870 | 841.6 | 83045 | +377 | -186.7 | strong |
| Put | 83800 | 134180 | 103268 | 648.7 | 83954 | 900.2 | 83151 | +271 | -251.5 | medium |
| Put | 83900 | 110100 | 76421 | 656.5 | 84009 | 965.3 | 83244 | +179 | -308.9 | weak |
| Put | 84000 | 431640 | 223453 | 667.5 | 84102 | 1027.4 | 83332 | +90 | -359.9 | weak |
| Put | 84100 | 191500 | 134691 | 740.9 | 84056 | 1090.2 | 83359 | +63 | -349.3 | weak |
| Put | 84200 | 104020 | 78247 | 767.9 | 84096 | 1157.5 | 83432 | -10 | -389.6 | weak |
| Put | 84300 | 85840 | 26223 | 832.7 | 84074 | 1225.8 | 83467 | -45 | -393.1 | weak |
| Put | 84400 | 52720 | 13571 | 863.4 | 84106 | 1295.0 | 83537 | -114 | -431.6 | weak |
| Put | 84500 | 97520 | 4587 | 1198.3 | 83733 | 1380.0 | 83302 | +121 | -181.7 | weak |
| Put | 84600 | 18400 | 7925 | 1019.1 | 84063 | 1449.9 | 83581 | -159 | -430.8 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 84500, strongest put writers at 84500; weakest call writers at -, weakest put writers at 85900. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82200 | 160 | 120 | 2106.2 | 82925 | 2016.4 | 84306 | +884 | +89.8 | strong |
| Call | 82300 | 100 | 100 | 2104.6 | 82925 | 2300.0 | 84405 | +982 | -195.4 | strong |
| Call | 82400 | 120 | 120 | 1994.6 | 82762 | 2765.2 | 84395 | +972 | -770.6 | strong |
| Call | 82500 | 840 | 816 | 2518.2 | 83629 | 2244.9 | 85018 | +1596 | +273.3 | strong |
| Call | 82600 | 120 | 120 | 1778.5 | 82439 | 1789.5 | 84378 | +956 | -10.9 | strong |
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +1123 | -732.3 | strong |
| Call | 82800 | 1560 | 1487 | 2302.3 | 83528 | 2251.6 | 85102 | +1680 | +50.7 | strong |
| Call | 82900 | 220 | 186 | 1609.0 | 82444 | 2407.8 | 84509 | +1087 | -798.9 | strong |
| Call | 83000 | 4800 | 4683 | 2204.7 | 83636 | 1953.4 | 85205 | +1782 | +251.3 | strong |
| Call | 83100 | 600 | 567 | 1626.2 | 82730 | 2289.2 | 84726 | +1304 | -663.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +1377 | -1016.5 | strong |
| Call | 83300 | 440 | 440 | 1780.0 | 83299 | 1924.8 | 85080 | +1658 | -144.8 | strong |
| Call | 83400 | 500 | 492 | 1612.7 | 83261 | 1741.8 | 85013 | +1590 | -129.2 | strong |
| Call | 83500 | 8800 | 8730 | 2080.6 | 83840 | 1654.0 | 85581 | +2158 | +426.6 | strong |
| Call | 83600 | 740 | 740 | 1790.5 | 83671 | 1618.8 | 85390 | +1968 | +171.7 | strong |
| Call | 83700 | 960 | 960 | 1622.7 | 83374 | 1630.0 | 85323 | +1900 | -7.3 | strong |
| Call | 83800 | 280 | 280 | 1686.5 | 83650 | 1528.8 | 85487 | +2064 | +157.8 | strong |
| Call | 83900 | 600 | 583 | 1506.8 | 83461 | 1505.8 | 85407 | +1985 | +0.9 | strong |
| Call | 84000 | 16720 | 16720 | 1773.0 | 83908 | 1392.5 | 85773 | +2351 | +380.5 | strong |
| Call | 84100 | 620 | 620 | 1630.0 | 83814 | 1404.5 | 85730 | +2308 | +225.4 | strong |
| Call | 84200 | 540 | 536 | 1488.9 | 83645 | 1354.8 | 85689 | +2267 | +134.1 | strong |
| Call | 84300 | 560 | 560 | 1598.0 | 83971 | 1334.3 | 85898 | +2476 | +263.6 | strong |
| Call | 84400 | 700 | 700 | 1453.8 | 83745 | 1268.1 | 85854 | +2432 | +185.7 | strong |
| Call | 84500 | 25380 | 25380 | 1447.1 | 83908 | 1182.1 | 85947 | +2525 | +265.0 | strong |
| Call | 84600 | 580 | 580 | 1371.6 | 83791 | 1420.0 | 85972 | +2549 | -48.4 | strong |
| Put | 82200 | 280 | 280 | 774.9 | 83703 | 788.3 | 81425 | +1997 | -13.4 | strong |
| Put | 82300 | 820 | 820 | 940.3 | 83524 | 767.6 | 81360 | +2063 | +172.6 | strong |
| Put | 82400 | 1400 | 1400 | 950.8 | 83582 | 879.9 | 81449 | +1973 | +70.9 | strong |
| Put | 82500 | 2460 | 2397 | 990.7 | 83571 | 867.1 | 81509 | +1913 | +123.6 | strong |
| Put | 82600 | 800 | 800 | 919.9 | 83832 | 884.0 | 81680 | +1742 | +35.9 | strong |
| Put | 82700 | 540 | 540 | 939.7 | 83782 | 940.0 | 81760 | +1662 | -0.3 | strong |
| Put | 82800 | 520 | 520 | 931.8 | 83810 | 949.7 | 81868 | +1554 | -17.9 | strong |
| Put | 82900 | 160 | 160 | 1015.8 | 83805 | 1034.0 | 81884 | +1538 | -18.1 | strong |
| Put | 83000 | 11680 | 11271 | 1075.5 | 83776 | 1080.0 | 81924 | +1498 | -4.5 | strong |
| Put | 83100 | 140 | 140 | 1134.3 | 83624 | 1046.5 | 81966 | +1457 | +87.8 | strong |
| Put | 83200 | 460 | 460 | 1379.9 | 83227 | 984.0 | 81820 | +1602 | +395.9 | strong |
| Put | 83300 | 460 | 460 | 1447.4 | 83169 | 960.5 | 81853 | +1570 | +486.9 | strong |
| Put | 83400 | 720 | 720 | 1380.2 | 83427 | 1206.5 | 82020 | +1403 | +173.8 | strong |
| Put | 83500 | 8400 | 8140 | 1213.6 | 83859 | 1291.8 | 82286 | +1136 | -78.2 | strong |
| Put | 83600 | 1080 | 1080 | 1487.1 | 83378 | 1279.3 | 82113 | +1309 | +207.7 | strong |
| Put | 83700 | 640 | 640 | 1552.3 | 83332 | 1363.3 | 82148 | +1275 | +189.0 | strong |
| Put | 83800 | 840 | 840 | 1483.9 | 83560 | 1390.0 | 82316 | +1106 | +93.9 | strong |
| Put | 83900 | 440 | 430 | 1486.8 | 83624 | 1477.0 | 82413 | +1009 | +9.8 | strong |
| Put | 84000 | 16720 | 16720 | 1286.5 | 84123 | 1522.0 | 82713 | +709 | -235.5 | strong |
| Put | 84100 | 1460 | 1460 | 1465.8 | 83866 | 1520.5 | 82634 | +788 | -54.6 | strong |
| Put | 84200 | 1240 | 1240 | 1420.0 | 83990 | 1500.0 | 82780 | +642 | -80.0 | strong |
| Put | 84300 | 1080 | 1080 | 1586.5 | 83821 | 1501.3 | 82714 | +709 | +85.1 | strong |
| Put | 84400 | 1740 | 1740 | 1693.5 | 83714 | 1580.5 | 82707 | +716 | +113.0 | strong |
| Put | 84500 | 24020 | 24020 | 1585.7 | 83930 | 1763.2 | 82914 | +508 | -177.5 | strong |
| Put | 84600 | 940 | 940 | 1691.8 | 83913 | 1458.4 | 82908 | +514 | +233.4 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 12 | 36% | -0.30% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 11 | 60% | -0.15% | -0.85 to +0.16% |  | no clear direction |
| monthly | PCR down · put and call writing · walls same · near put wall | 5 | 75% | +0.24% | -0.05 to +0.48% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 33% | -0.02% | -0.07 to +0.06% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · near call wall | 4 | 0% | -0.32% | -0.42 to -0.25% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 3 | 33% | -0.55% | -0.85 to +0.01% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.24% | -1.15 to +0.66% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 100% | +0.65% | +0.11 to +0.97% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 3 | 0% | -0.28% | -0.35 to -0.22% |  | too few (3/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 0% | -0.46% | -0.80 to -0.08% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | -0.06% | -1.14 to +0.86% |  | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.13% | -0.30 to +0.05% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 2 | 50% | +0.12% | -0.42 to +0.66% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 0% | -0.23% | -0.30 to -0.16% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.25% | -0.25 to -0.25% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls up · near put wall | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near put wall | 1 | 0% | -0.59% | -0.59 to -0.59% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.32% | +0.32 to +0.32% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near call wall | 1 | 0% | -0.16% | -0.16 to -0.16% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near call wall | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.19% | +0.19 to +0.19% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 0% | -0.59% | -0.59 to -0.59% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
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
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -1.07% | -1.07 to -1.07% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.46% | +0.46 to +0.46% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -1.07% | -1.07 to -1.07% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 52 | 55% | -0.05% | no clear direction |
| intraday | weekly | writers even · few weak writers | 47 | 60% | +0.03% | no clear direction |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | call writers stronger · few weak writers | 13 | 8% | -0.42% | down |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 8 | 62% | -0.19% | too few (8/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | writers even · weak on both sides | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers | 5 | 50% | -0.32% | too few (4/10) |
| day | weekly | writers even · few weak writers | 4 | 67% | +0.17% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak on both sides | 1 | 0% | -1.07% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 41 | 62% | -0.03% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 29 | 59% | +0.03% | no clear direction |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 67% | +0.02% | too few (3/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 11 | 30% | -0.14% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 8 | 62% | -0.19% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 7 | 0% | -0.26% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 6 | 17% | -0.58% | too few (6/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 50% | -0.32% | too few (4/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.65% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 0% | -1.07% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
