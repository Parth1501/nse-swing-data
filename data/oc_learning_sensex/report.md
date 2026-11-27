# Sensex option chain pattern log
Updated 2026-11-27 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 73 snapshots over 7 trading days
- 142 patterns logged; 66 different patterns so far

## Latest read (2026-11-27 09:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-03 (weekly) | 6.2 | 84093 | 0.88 | 84100 | 84000 | 88000 | ±1.74% (82632-85555) | 16.75 |
| 2026-12-31 (monthly) | 34.2 | 84094 | 1.066 | 84000 | 84000 | 86000 | ±3.56% (81104-87085) | 14.37 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls same · near put wall`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.01%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 44 times before; Sensex was up after it 67% of the time, average +0.11%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 26 times before; Sensex was up after it 67% of the time, average +0.13%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 67% of the time, average +0.17%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 50% of the time, average -0.65%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls same · near put wall`. Seen 9 times before; Sensex was up after it 75% of the time, average +0.01%. Too few outcomes (8/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 41 times before; Sensex was up after it 70% of the time, average +0.07%. History points to a bull call debit spread, ATM to about the call wall 86000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 37 times before; Sensex was up after it 70% of the time, average +0.07%. History points to a bull call debit spread, ATM to about the call wall 86000.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · near put wall`. Seen 1 times before; Sensex was up after it 100% of the time, average +1.82%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 50% of the time, average -0.12%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 4 times before; Sensex was up after it 50% of the time, average -0.12%. Too few outcomes (4/20) to trade on.

## Strong vs weak writers, weekly 2026-12-03

Strongest call writers at 84200, strongest put writers at 84000; weakest call writers at -, weakest put writers at 85600. Covers 54% of near-money call OI and 52% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82900 | 2580 | 220 | 1542.6 | 84093 | 1542.6 | 84443 | +349 | +0.0 | medium |
| Call | 83000 | 48520 | 6100 | 1437.5 | 84093 | 1437.5 | 84438 | +344 | +0.0 | medium |
| Call | 83100 | 4260 | 660 | 1455.3 | 84093 | 1455.3 | 84555 | +462 | +0.0 | strong |
| Call | 83200 | 11620 | 1540 | 1360.0 | 84093 | 1360.0 | 84560 | +467 | +0.0 | strong |
| Call | 83300 | 4960 | 920 | 1238.2 | 84093 | 1238.2 | 84538 | +445 | +0.0 | strong |
| Call | 83400 | 10440 | 6300 | 1150.0 | 84093 | 1150.0 | 84550 | +457 | +0.0 | strong |
| Call | 83500 | 60920 | 12120 | 1099.6 | 84093 | 1099.6 | 84600 | +506 | +0.0 | strong |
| Call | 83600 | 12120 | 4060 | 1029.2 | 84093 | 1029.2 | 84629 | +536 | +0.0 | strong |
| Call | 83700 | 27180 | 10460 | 969.6 | 84093 | 969.6 | 84670 | +576 | +0.0 | strong |
| Call | 83800 | 42780 | 17760 | 911.6 | 84093 | 911.6 | 84712 | +618 | +0.0 | strong |
| Call | 83900 | 64920 | 24900 | 852.9 | 84093 | 852.9 | 84753 | +659 | +0.0 | strong |
| Call | 84000 | 536520 | 245700 | 797.4 | 84093 | 797.4 | 84797 | +704 | +0.0 | strong |
| Call | 84100 | 293680 | 210500 | 745.7 | 84093 | 745.7 | 84846 | +752 | +0.0 | strong |
| Call | 84200 | 332800 | 269420 | 696.8 | 84093 | 696.8 | 84897 | +803 | +0.0 | strong |
| Call | 84300 | 279320 | 142840 | 654.9 | 84093 | 654.9 | 84955 | +861 | +0.0 | strong |
| Call | 84400 | 162880 | 67180 | 604.1 | 84093 | 604.1 | 85004 | +911 | +0.0 | strong |
| Call | 84500 | 383100 | 158100 | 565.0 | 84093 | 565.0 | 85065 | +972 | +0.0 | strong |
| Call | 84600 | 105400 | 64700 | 521.5 | 84093 | 521.5 | 85121 | +1028 | +0.0 | strong |
| Call | 84700 | 86960 | 58080 | 482.1 | 84093 | 482.1 | 85182 | +1089 | +0.0 | strong |
| Call | 84800 | 71000 | 47320 | 446.7 | 84093 | 446.7 | 85247 | +1153 | +0.0 | strong |
| Call | 84900 | 64800 | 40560 | 416.9 | 84093 | 416.9 | 85317 | +1223 | +0.0 | strong |
| Call | 85000 | 405520 | 222800 | 384.4 | 84093 | 384.4 | 85384 | +1291 | +0.0 | strong |
| Call | 85100 | 72340 | 49680 | 353.4 | 84093 | 353.4 | 85453 | +1360 | +0.0 | strong |
| Call | 85200 | 97720 | 73700 | 324.6 | 84093 | 324.6 | 85525 | +1431 | +0.0 | strong |
| Call | 85300 | 79320 | 47080 | 295.9 | 84093 | 295.9 | 85596 | +1502 | +0.0 | strong |
| Put | 82900 | 65580 | 50140 | 291.7 | 84093 | 291.7 | 82608 | +1485 | +0.0 | strong |
| Put | 83000 | 360280 | 187960 | 316.9 | 84093 | 316.9 | 82683 | +1410 | +0.0 | strong |
| Put | 83100 | 83460 | 57780 | 344.2 | 84093 | 344.2 | 82756 | +1338 | +0.0 | strong |
| Put | 83200 | 69980 | 40220 | 369.6 | 84093 | 369.6 | 82830 | +1263 | +0.0 | strong |
| Put | 83300 | 67940 | 51720 | 403.9 | 84093 | 403.9 | 82896 | +1197 | +0.0 | strong |
| Put | 83400 | 61440 | 38520 | 434.6 | 84093 | 434.6 | 82965 | +1128 | +0.0 | strong |
| Put | 83500 | 246560 | 115800 | 469.4 | 84093 | 469.4 | 83031 | +1063 | +0.0 | strong |
| Put | 83600 | 92000 | 61640 | 506.4 | 84093 | 506.4 | 83094 | +1000 | +0.0 | strong |
| Put | 83700 | 88200 | 52920 | 543.8 | 84093 | 543.8 | 83156 | +937 | +0.0 | strong |
| Put | 83800 | 128120 | 69660 | 587.1 | 84093 | 587.1 | 83213 | +881 | +0.0 | strong |
| Put | 83900 | 158860 | 77660 | 624.6 | 84093 | 624.6 | 83275 | +818 | +0.0 | strong |
| Put | 84000 | 667040 | 306220 | 674.8 | 84093 | 674.8 | 83325 | +768 | +0.0 | strong |
| Put | 84100 | 328860 | 205800 | 715.9 | 84093 | 715.9 | 83384 | +709 | +0.0 | strong |
| Put | 84200 | 216440 | 159900 | 770.1 | 84093 | 770.1 | 83430 | +664 | +0.0 | strong |
| Put | 84300 | 137420 | 36680 | 822.4 | 84093 | 822.4 | 83478 | +616 | +0.0 | strong |
| Put | 84400 | 71300 | 13780 | 871.0 | 84093 | 871.0 | 83529 | +565 | +0.0 | strong |
| Put | 84600 | 15780 | 3800 | 1003.2 | 84093 | 1003.2 | 83597 | +497 | +0.0 | strong |
| Put | 84700 | 10920 | 2020 | 1046.5 | 84093 | 1046.5 | 83654 | +440 | +0.0 | strong |
| Put | 84800 | 19420 | 10880 | 1119.7 | 84093 | 1119.7 | 83680 | +413 | +0.0 | strong |
| Put | 84900 | 8140 | 2600 | 1184.8 | 84093 | 1184.8 | 83715 | +378 | +0.0 | medium |
| Put | 85000 | 32880 | 5400 | 1256.3 | 84093 | 1256.3 | 83744 | +350 | +0.0 | medium |
| Put | 85100 | 5160 | 160 | 1302.5 | 84093 | 1302.5 | 83797 | +296 | +0.0 | medium |
| Put | 85200 | 5400 | 1100 | 1384.2 | 84093 | 1384.2 | 83816 | +278 | +0.0 | medium |
| Put | 85300 | 19520 | 340 | 1445.0 | 84093 | 1445.0 | 83855 | +238 | +0.0 | medium |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 86000, strongest put writers at 84000; weakest call writers at -, weakest put writers at 86500. Covers 98% of near-money call OI and 99% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82900 | 220 | 186 | 1609.0 | 82444 | 2407.8 | 84509 | +415 | -798.9 | strong |
| Call | 83000 | 4100 | 3978 | 2227.8 | 83623 | 2436.1 | 85228 | +1133 | -208.3 | strong |
| Call | 83100 | 580 | 547 | 1602.0 | 82679 | 2289.2 | 84702 | +608 | -687.3 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +705 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +986 | -335.1 | strong |
| Call | 83400 | 520 | 511 | 1612.7 | 83261 | 2300.0 | 85013 | +918 | -687.3 | strong |
| Call | 83500 | 8380 | 8309 | 2097.9 | 83851 | 2101.2 | 85598 | +1504 | -3.3 | strong |
| Call | 83600 | 700 | 700 | 1823.9 | 83677 | 1988.6 | 85424 | +1330 | -164.7 | strong |
| Call | 83700 | 900 | 900 | 1622.0 | 83351 | 2023.1 | 85322 | +1228 | -401.1 | strong |
| Call | 83800 | 180 | 180 | 1665.5 | 83527 | 1926.5 | 85465 | +1371 | -261.1 | strong |
| Call | 83900 | 360 | 343 | 1457.4 | 83284 | 1831.5 | 85357 | +1263 | -374.1 | strong |
| Call | 84000 | 15260 | 15260 | 1803.2 | 83936 | 1808.8 | 85803 | +1709 | -5.6 | strong |
| Call | 84100 | 560 | 560 | 1650.8 | 83827 | 1735.0 | 85751 | +1656 | -84.2 | strong |
| Call | 84200 | 460 | 456 | 1485.4 | 83584 | 1566.0 | 85685 | +1591 | -80.7 | strong |
| Call | 84300 | 520 | 520 | 1623.7 | 84008 | 1564.7 | 85924 | +1829 | +59.1 | strong |
| Call | 84400 | 600 | 600 | 1467.5 | 83740 | 1532.3 | 85868 | +1773 | -64.8 | strong |
| Call | 84500 | 11420 | 11420 | 1588.4 | 84043 | 1524.7 | 86088 | +1994 | +63.7 | strong |
| Call | 84600 | 440 | 440 | 1353.9 | 83701 | 1484.7 | 85954 | +1859 | -130.8 | strong |
| Call | 84700 | 520 | 520 | 1258.0 | 83598 | 1376.5 | 85958 | +1864 | -118.5 | strong |
| Call | 84800 | 340 | 340 | 1243.1 | 83586 | 1548.1 | 86043 | +1949 | -305.0 | strong |
| Call | 84900 | 500 | 500 | 1161.1 | 83466 | 1472.5 | 86061 | +1967 | -311.3 | strong |
| Call | 85000 | 14680 | 14680 | 1288.3 | 83969 | 1298.0 | 86288 | +2194 | -9.7 | strong |
| Call | 85100 | 300 | 300 | 972.0 | 83276 | 1251.6 | 86072 | +1978 | -279.6 | strong |
| Call | 85200 | 420 | 420 | 978.6 | 83380 | 1305.8 | 86179 | +2084 | -327.2 | strong |
| Call | 85300 | 140 | 140 | 1067.3 | 83937 | 1260.4 | 86367 | +2273 | -193.1 | strong |
| Put | 82900 | 160 | 160 | 1015.8 | 83805 | 803.5 | 81884 | +2210 | +212.4 | strong |
| Put | 83000 | 12280 | 11846 | 1076.2 | 83777 | 847.0 | 81924 | +2171 | +229.2 | strong |
| Put | 83100 | 160 | 160 | 1163.5 | 83622 | 846.0 | 81936 | +2158 | +317.6 | strong |
| Put | 83200 | 460 | 460 | 1379.9 | 83227 | 984.0 | 81820 | +2274 | +395.9 | strong |
| Put | 83300 | 460 | 460 | 1447.4 | 83169 | 960.5 | 81853 | +2242 | +486.9 | strong |
| Put | 83400 | 800 | 800 | 1387.1 | 83414 | 1097.0 | 82013 | +2082 | +290.0 | strong |
| Put | 83500 | 8340 | 8074 | 1214.0 | 83864 | 1075.0 | 82286 | +1808 | +139.0 | strong |
| Put | 83600 | 1060 | 1060 | 1510.0 | 83349 | 1135.7 | 82090 | +2004 | +374.4 | strong |
| Put | 83700 | 640 | 640 | 1552.3 | 83332 | 1061.0 | 82148 | +1947 | +491.4 | strong |
| Put | 83800 | 800 | 800 | 1494.5 | 83550 | 1034.7 | 82306 | +1789 | +459.8 | strong |
| Put | 83900 | 520 | 506 | 1497.6 | 83620 | 1219.0 | 82402 | +1692 | +278.6 | strong |
| Put | 84000 | 19340 | 19340 | 1286.2 | 84125 | 1200.0 | 82714 | +1381 | +86.2 | strong |
| Put | 84100 | 1640 | 1640 | 1467.2 | 83866 | 1255.2 | 82633 | +1462 | +211.9 | strong |
| Put | 84200 | 1220 | 1220 | 1425.1 | 83985 | 1326.5 | 82775 | +1320 | +98.6 | strong |
| Put | 84300 | 980 | 980 | 1595.2 | 83826 | 1305.1 | 82705 | +1390 | +290.1 | strong |
| Put | 84400 | 1640 | 1640 | 1727.4 | 83679 | 1384.3 | 82673 | +1422 | +343.1 | strong |
| Put | 84500 | 10440 | 10440 | 1501.2 | 84148 | 1460.0 | 82999 | +1096 | +41.2 | strong |
| Put | 84600 | 940 | 940 | 1691.8 | 83913 | 1458.4 | 82908 | +1186 | +233.4 | strong |
| Put | 84700 | 720 | 720 | 1651.0 | 84077 | 1656.6 | 83049 | +1045 | -5.6 | strong |
| Put | 84800 | 760 | 760 | 1641.4 | 84218 | 1490.0 | 83159 | +936 | +151.4 | strong |
| Put | 84900 | 780 | 780 | 2253.9 | 83187 | 1582.0 | 82646 | +1448 | +672.0 | strong |
| Put | 85000 | 13300 | 13300 | 1761.8 | 84039 | 1640.0 | 83238 | +856 | +121.8 | strong |
| Put | 85100 | 420 | 420 | 1949.1 | 83844 | 1640.1 | 83151 | +944 | +309.0 | strong |
| Put | 85200 | 620 | 620 | 2141.7 | 83689 | 2120.6 | 83058 | +1036 | +21.1 | strong |
| Put | 85300 | 1080 | 1080 | 2085.3 | 83780 | 1774.8 | 83215 | +880 | +310.6 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 12 | 36% | -0.30% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 10 | 75% | +0.01% | -0.22 to +0.16% |  | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 5 | 75% | +0.24% | -0.05 to +0.48% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 33% | -0.02% | -0.07 to +0.06% | 100% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 100% | +0.65% | +0.11 to +0.97% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | -0.06% | -1.14 to +0.86% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.24% | -1.15 to +0.66% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 0% | -0.46% | -0.80 to -0.08% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 1 | 100% | +0.66% | +0.66 to +0.66% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.32% | +0.32 to +0.32% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls up · near put wall | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% | 0% of 1 | too few (1/10) |
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
| monthly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.82% | +1.82 to +1.82% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.46% | +0.46 to +0.46% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.28% | -0.28 to -0.28% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.46% | +0.46 to +0.46% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 45 | 67% | +0.11% | no clear direction |
| intraday | monthly | writers even · few weak writers | 42 | 70% | +0.07% | up |
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
| day | monthly | writers even · few weak writers | 5 | 50% | -0.12% | too few (4/10) |
| day | weekly | writers even · few weak writers | 5 | 67% | +0.17% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak on both sides | 1 | 0% | -0.28% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 38 | 70% | +0.07% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 27 | 67% | +0.13% | no clear direction |
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
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 5 | 50% | -0.12% | too few (4/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | -0.65% | too few (2/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 0% | -0.28% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
