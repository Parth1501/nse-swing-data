# Sensex option chain pattern log
Updated 2026-11-26 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 69 snapshots over 6 trading days
- 135 patterns logged; 64 different patterns so far

## Latest read (2026-11-26 14:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 0.0 | 84358 | 0.943 | 84200 | 84000 | 84500 | ±0.24% (84158-84558) | 32.76 |
| 2026-12-31 (monthly) | 35.0 | 84358 | 1.097 | 84000 | 84000 | 86000 | ±3.3% (81578-87138) | 13.12 |

- **Weekly, last 30 min**: `PCR up · unwinding · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 7 times before; Sensex was up after it 71% of the time, average -0.22%. Too few outcomes (7/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 7 times before; Sensex was up after it 71% of the time, average -0.22%. Too few outcomes (7/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near call wall`. Seen 1 times before; Sensex was up after it 0% of the time, average -1.77%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · unwinding · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 37 times before; Sensex was up after it 74% of the time, average +0.09%. History points to a bull call debit spread, ATM to about the call wall 86000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 33 times before; Sensex was up after it 73% of the time, average +0.10%. History points to a bull call debit spread, ATM to about the call wall 86000.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 67% of the time, average -0.06%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Sensex was up after it 67% of the time, average -0.06%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 84000; weakest call writers at 84400, weakest put writers at 84300. Covers 100% of near-money call OI and 100% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83100 | 44800 | 43715 | 670.9 | 83323 | 1299.7 | 83771 | -587 | -628.8 | weak |
| Call | 83200 | 47520 | 46983 | 618.3 | 83300 | 1202.5 | 83818 | -540 | -584.2 | weak |
| Call | 83300 | 35340 | 35104 | 595.5 | 83522 | 1098.7 | 83896 | -462 | -503.2 | weak |
| Call | 83400 | 67880 | 67314 | 561.2 | 83615 | 998.9 | 83961 | -397 | -437.6 | weak |
| Call | 83500 | 190400 | 188589 | 443.6 | 83670 | 902.1 | 83944 | -414 | -458.5 | weak |
| Call | 83600 | 166780 | 166568 | 384.3 | 83716 | 798.7 | 83984 | -374 | -414.4 | weak |
| Call | 83700 | 220080 | 219992 | 308.9 | 83850 | 707.2 | 84009 | -349 | -398.4 | weak |
| Call | 83800 | 577360 | 577207 | 214.8 | 83867 | 603.0 | 84015 | -343 | -388.2 | weak |
| Call | 83900 | 867080 | 866929 | 176.4 | 83894 | 506.0 | 84076 | -282 | -329.6 | weak |
| Call | 84000 | 1926900 | 1924008 | 150.7 | 83936 | 412.3 | 84151 | -207 | -261.6 | weak |
| Call | 84100 | 1420900 | 1420770 | 140.4 | 84039 | 315.4 | 84240 | -118 | -174.9 | weak |
| Call | 84200 | 2633100 | 2632832 | 118.6 | 84063 | 233.2 | 84319 | -39 | -114.6 | weak |
| Call | 84300 | 3843960 | 3842278 | 126.0 | 84070 | 159.5 | 84426 | +68 | -33.5 | weak |
| Call | 84400 | 4915700 | 4913661 | 135.0 | 84182 | 101.2 | 84535 | +177 | +33.8 | weak |
| Call | 84500 | 7047820 | 7008590 | 114.8 | 84017 | 59.0 | 84615 | +257 | +55.7 | medium |
| Call | 84600 | 3988960 | 3986870 | 98.6 | 84145 | 33.5 | 84699 | +341 | +65.0 | medium |
| Call | 84700 | 2892560 | 2889077 | 76.5 | 84113 | 18.9 | 84776 | +418 | +57.5 | strong |
| Call | 84800 | 2772880 | 2768626 | 69.0 | 84117 | 10.7 | 84869 | +511 | +58.4 | strong |
| Call | 84900 | 1846080 | 1842171 | 55.9 | 84125 | 6.8 | 84956 | +598 | +49.1 | strong |
| Call | 85000 | 5548160 | 5514781 | 51.4 | 83995 | 4.9 | 85051 | +693 | +46.5 | strong |
| Call | 85100 | 1521860 | 1520737 | 33.0 | 83987 | 3.3 | 85133 | +775 | +29.7 | strong |
| Call | 85200 | 1675420 | 1673237 | 41.7 | 84007 | 2.3 | 85242 | +884 | +39.4 | strong |
| Call | 85300 | 1524580 | 1524084 | 23.6 | 84044 | 1.7 | 85324 | +966 | +21.9 | strong |
| Call | 85400 | 975420 | 973990 | 25.2 | 83925 | 1.4 | 85425 | +1067 | +23.8 | strong |
| Call | 85500 | 2719740 | 2703285 | 28.9 | 83753 | 1.1 | 85529 | +1171 | +27.7 | strong |
| Call | 85600 | 1163320 | 1162144 | 23.6 | 83994 | 0.8 | 85624 | +1266 | +22.8 | strong |
| Put | 83100 | 1087300 | 1086660 | 77.3 | 83923 | 1.2 | 83023 | +1335 | +76.0 | strong |
| Put | 83200 | 1507720 | 1507345 | 81.2 | 83931 | 1.4 | 83119 | +1239 | +79.8 | strong |
| Put | 83300 | 1636860 | 1636522 | 104.7 | 83925 | 1.6 | 83195 | +1163 | +103.1 | strong |
| Put | 83400 | 1832060 | 1831797 | 95.0 | 83964 | 1.7 | 83305 | +1053 | +93.3 | strong |
| Put | 83500 | 4636100 | 4634002 | 118.1 | 84021 | 2.1 | 83382 | +976 | +116.0 | strong |
| Put | 83600 | 2159340 | 2159196 | 105.4 | 84049 | 2.5 | 83495 | +863 | +102.8 | strong |
| Put | 83700 | 2628420 | 2628262 | 129.3 | 84065 | 3.1 | 83571 | +787 | +126.2 | strong |
| Put | 83800 | 4945140 | 4944807 | 188.0 | 84035 | 4.0 | 83612 | +746 | +184.0 | strong |
| Put | 83900 | 3825520 | 3825167 | 194.1 | 84080 | 6.0 | 83706 | +652 | +188.0 | strong |
| Put | 84000 | 6203600 | 6202800 | 122.8 | 84262 | 9.8 | 83877 | +481 | +112.9 | strong |
| Put | 84100 | 4336160 | 4336147 | 85.4 | 84295 | 16.7 | 84015 | +343 | +68.7 | medium |
| Put | 84200 | 4387700 | 4387697 | 69.4 | 84340 | 30.4 | 84131 | +227 | +39.0 | medium |
| Put | 84300 | 2979520 | 2979499 | 93.3 | 84353 | 57.7 | 84207 | +151 | +35.6 | weak |
| Put | 84400 | 1384920 | 1384920 | 144.2 | 84360 | 98.5 | 84256 | +102 | +45.7 | weak |
| Put | 84500 | 1297900 | 1297888 | 271.1 | 84349 | 156.8 | 84229 | +129 | +114.3 | weak |
| Put | 84600 | 377220 | 377220 | 354.9 | 84372 | 234.1 | 84245 | +113 | +120.8 | weak |
| Put | 84700 | 161680 | 161680 | 427.1 | 84331 | 317.8 | 84273 | +85 | +109.3 | weak |
| Put | 84800 | 61500 | 61500 | 476.2 | 84368 | 413.2 | 84324 | +34 | +63.0 | weak |
| Put | 84900 | 39080 | 39080 | 622.2 | 84348 | 502.8 | 84278 | +80 | +119.4 | weak |
| Put | 85000 | 256240 | 256089 | 653.7 | 84340 | 606.6 | 84346 | +12 | +47.1 | weak |
| Put | 85100 | 20160 | 20160 | 843.2 | 84294 | 712.1 | 84257 | +101 | +131.1 | weak |
| Put | 85200 | 14520 | 14520 | 926.6 | 84294 | 803.0 | 84273 | +85 | +123.5 | weak |
| Put | 85300 | 9660 | 5224 | 1080.4 | 84225 | 898.5 | 84220 | +138 | +181.9 | weak |
| Put | 85400 | 7060 | 7060 | 1183.9 | 84222 | 1010.5 | 84216 | +142 | +173.4 | weak |
| Put | 85500 | 41060 | 41060 | 1148.0 | 84331 | 1100.5 | 84352 | +6 | +47.6 | weak |
| Put | 85600 | 4020 | 4020 | 1330.7 | 84265 | 1196.7 | 84269 | +89 | +134.0 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 86000, strongest put writers at 84000; weakest call writers at 82900, weakest put writers at -. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2100.0 | 84702 | +344 | -498.0 | medium |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +442 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +722 | -335.1 | strong |
| Call | 83400 | 540 | 531 | 1612.7 | 83261 | 2152.9 | 85013 | +655 | -540.2 | strong |
| Call | 83500 | 8360 | 8289 | 2097.4 | 83850 | 2314.4 | 85597 | +1239 | -217.1 | strong |
| Call | 83600 | 700 | 700 | 1823.9 | 83677 | 2151.3 | 85424 | +1066 | -327.4 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1805.5 | 85310 | +952 | -195.6 | strong |
| Call | 83800 | 300 | 300 | 1665.5 | 83527 | 2059.2 | 85465 | +1107 | -393.8 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +999 | +287.6 | strong |
| Call | 84000 | 13660 | 13660 | 1790.1 | 83899 | 2026.2 | 85790 | +1432 | -236.1 | strong |
| Call | 84100 | 540 | 540 | 1647.6 | 83817 | 1910.0 | 85748 | +1390 | -262.4 | strong |
| Call | 84200 | 460 | 456 | 1485.4 | 83584 | 1566.0 | 85685 | +1327 | -80.7 | strong |
| Call | 84300 | 440 | 440 | 1612.4 | 83974 | 1680.0 | 85912 | +1554 | -67.6 | strong |
| Call | 84400 | 560 | 560 | 1436.4 | 83630 | 1494.5 | 85836 | +1478 | -58.1 | strong |
| Call | 84500 | 9280 | 9280 | 1566.8 | 83986 | 1742.8 | 86067 | +1709 | -176.0 | strong |
| Call | 84600 | 500 | 500 | 1353.9 | 83701 | 1503.6 | 85954 | +1596 | -149.7 | strong |
| Call | 84700 | 360 | 360 | 1205.3 | 83377 | 1342.4 | 85905 | +1547 | -137.1 | strong |
| Call | 84800 | 300 | 300 | 1202.4 | 83487 | 1370.3 | 86002 | +1644 | -167.9 | strong |
| Call | 84900 | 480 | 480 | 1148.2 | 83432 | 1444.8 | 86048 | +1690 | -296.7 | strong |
| Call | 85000 | 9020 | 9020 | 1256.1 | 83852 | 1470.1 | 86256 | +1898 | -214.0 | strong |
| Call | 85100 | 300 | 300 | 972.0 | 83276 | 1251.6 | 86072 | +1714 | -279.6 | strong |
| Call | 85200 | 420 | 420 | 978.6 | 83380 | 1305.8 | 86179 | +1821 | -327.2 | strong |
| Call | 85300 | 120 | 120 | 1035.2 | 83872 | 1077.3 | 86335 | +1977 | -42.1 | strong |
| Call | 85400 | 400 | 400 | 892.6 | 83194 | 1063.2 | 86293 | +1935 | -170.6 | strong |
| Call | 85500 | 2880 | 2880 | 1138.3 | 84089 | 1150.0 | 86638 | +2280 | -11.7 | strong |
| Call | 85600 | 240 | 240 | 991.5 | 83834 | 982.2 | 86592 | +2234 | +9.3 | strong |
| Put | 83100 | 160 | 160 | 1163.5 | 83622 | 1020.0 | 81936 | +2422 | +143.6 | strong |
| Put | 83200 | 520 | 520 | 1379.9 | 83227 | 1062.7 | 81820 | +2538 | +317.2 | strong |
| Put | 83300 | 460 | 460 | 1470.7 | 83125 | 930.5 | 81829 | +2529 | +540.2 | strong |
| Put | 83400 | 800 | 800 | 1387.1 | 83414 | 1097.0 | 82013 | +2345 | +290.0 | strong |
| Put | 83500 | 8280 | 8014 | 1215.3 | 83862 | 1061.3 | 82285 | +2073 | +154.0 | strong |
| Put | 83600 | 1060 | 1060 | 1510.0 | 83349 | 1094.2 | 82090 | +2268 | +415.9 | strong |
| Put | 83700 | 660 | 660 | 1552.3 | 83332 | 1089.1 | 82148 | +2210 | +463.2 | strong |
| Put | 83800 | 800 | 800 | 1494.5 | 83550 | 1034.7 | 82306 | +2052 | +459.8 | strong |
| Put | 83900 | 520 | 506 | 1497.6 | 83620 | 1219.0 | 82402 | +1956 | +278.6 | strong |
| Put | 84000 | 18880 | 18880 | 1290.4 | 84120 | 1135.8 | 82710 | +1648 | +154.6 | strong |
| Put | 84100 | 1360 | 1360 | 1541.6 | 83743 | 1394.6 | 82558 | +1800 | +147.0 | strong |
| Put | 84200 | 800 | 800 | 1537.0 | 83811 | 1429.2 | 82663 | +1695 | +107.8 | strong |
| Put | 84300 | 1000 | 1000 | 1595.2 | 83826 | 1429.5 | 82705 | +1653 | +165.7 | strong |
| Put | 84400 | 1560 | 1560 | 1746.8 | 83653 | 1285.6 | 82653 | +1705 | +461.2 | strong |
| Put | 84500 | 8960 | 8960 | 1531.0 | 84121 | 1329.0 | 82969 | +1389 | +202.1 | strong |
| Put | 84600 | 960 | 960 | 1691.8 | 83913 | 1414.0 | 82908 | +1450 | +277.8 | strong |
| Put | 84700 | 720 | 720 | 1651.0 | 84077 | 1656.6 | 83049 | +1309 | -5.6 | strong |
| Put | 84800 | 760 | 760 | 1641.4 | 84218 | 1490.0 | 83159 | +1199 | +151.4 | strong |
| Put | 84900 | 780 | 780 | 2253.9 | 83187 | 1591.8 | 82646 | +1712 | +662.1 | strong |
| Put | 85000 | 8740 | 8740 | 1830.2 | 83984 | 1578.4 | 83170 | +1188 | +251.8 | strong |
| Put | 85100 | 420 | 420 | 1949.1 | 83844 | 1640.1 | 83151 | +1207 | +309.0 | strong |
| Put | 85200 | 620 | 620 | 2141.7 | 83689 | 2120.6 | 83058 | +1300 | +21.1 | strong |
| Put | 85300 | 1080 | 1080 | 2085.3 | 83780 | 2085.3 | 83215 | +1143 | +0.0 | strong |
| Put | 85400 | 140 | 140 | 2041.0 | 83938 | 2041.0 | 83359 | +999 | +0.0 | strong |
| Put | 85500 | 2540 | 2540 | 2388.7 | 83530 | 2029.1 | 83111 | +1247 | +359.6 | strong |
| Put | 85600 | 1360 | 1360 | 2122.0 | 84202 | 2093.2 | 83478 | +880 | +28.9 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 12 | 36% | -0.29% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 7 | 71% | +0.01% | -0.22 to +0.16% |  | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 5 | 75% | +0.25% | -0.05 to +0.48% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 3 | 0% | -0.06% | -0.07 to -0.05% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | -0.04% | -1.14 to +0.86% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.23% | -1.15 to +0.69% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 0% | -0.45% | -0.80 to -0.04% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 100% | +0.66% | +0.14 to +0.97% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 1 | 100% | +0.69% | +0.69 to +0.69% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near put wall | 1 | 100% | +0.57% | +0.57 to +0.57% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.04% | -0.04 to -0.04% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.12% | -0.12 to -0.12% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.12% | -0.12 to -0.12% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.19% | +0.19 to +0.19% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 0% | -0.44% | -0.44 to -0.44% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put and call writing · walls same · near call wall | 2 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.82% | +1.82 to +1.82% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.50% | +0.50 to +0.50% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 44 | 67% | +0.13% | no clear direction |
| intraday | monthly | writers even · few weak writers | 38 | 74% | +0.09% | up |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 8 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 5 | 20% | -0.61% | too few (5/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides | 1 | 100% | +0.04% | too few (1/10) |
| day | monthly | writers even · few weak writers | 4 | 67% | -0.06% | too few (3/10) |
| day | weekly | writers even · few weak writers | 4 | 67% | +0.18% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 34 | 73% | +0.10% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 26 | 67% | +0.14% | no clear direction |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 67% | +0.02% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 8 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 5 | 20% | -0.61% | too few (5/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 4 | 75% | +0.04% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 100% | +0.04% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 67% | -0.06% | too few (3/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.63% | too few (2/10) |
| day | weekly | writers even · weak calls · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
