# Sensex option chain pattern log
Updated 2026-11-26 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 71 snapshots over 6 trading days
- 139 patterns logged; 66 different patterns so far

## Latest read (2026-11-26 15:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 0.0 | 84329 | 0.925 | 84300 | 84200 | 84400 | ±0.03% (84300-84357) | 125.0 |
| 2026-12-31 (monthly) | 35.0 | 84329 | 1.078 | 84000 | 84000 | 86000 | ±3.69% (81217-87441) | 14.77 |

- **Weekly, last 30 min**: `PCR up · unwinding · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak on both sides`. Seen 2 times before; Sensex was up after it 100% of the time, average +0.04%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 100% of the time, average +0.04%. Too few outcomes (2/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak on both sides`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls same · near put wall`. Seen 8 times before; Sensex was up after it 75% of the time, average +0.01%. Too few outcomes (8/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 39 times before; Sensex was up after it 72% of the time, average +0.08%. History points to a bull call debit spread, ATM to about the call wall 86000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 35 times before; Sensex was up after it 72% of the time, average +0.08%. History points to a bull call debit spread, ATM to about the call wall 86000.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 67% of the time, average -0.07%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Sensex was up after it 67% of the time, average -0.07%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 84000; weakest call writers at 84300, weakest put writers at 84300. Covers 99% of near-money call OI and 100% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83100 | 40680 | 39695 | 670.9 | 83323 | 1225.8 | 83771 | -558 | -554.9 | weak |
| Call | 83200 | 39940 | 39489 | 618.3 | 83300 | 1131.2 | 83818 | -510 | -512.8 | weak |
| Call | 83300 | 23500 | 23343 | 595.5 | 83522 | 1026.9 | 83896 | -433 | -431.4 | weak |
| Call | 83400 | 43200 | 42840 | 561.2 | 83615 | 927.0 | 83961 | -367 | -365.8 | weak |
| Call | 83500 | 114200 | 113113 | 443.6 | 83670 | 826.5 | 83944 | -385 | -382.9 | weak |
| Call | 83600 | 123480 | 123323 | 384.3 | 83716 | 729.2 | 83984 | -344 | -344.9 | weak |
| Call | 83700 | 98840 | 98800 | 308.9 | 83850 | 628.1 | 84009 | -320 | -319.3 | weak |
| Call | 83800 | 357840 | 357745 | 214.8 | 83867 | 528.6 | 84015 | -314 | -313.8 | weak |
| Call | 83900 | 580180 | 580079 | 176.4 | 83894 | 427.6 | 84076 | -252 | -251.2 | weak |
| Call | 84000 | 1066840 | 1065239 | 150.7 | 83936 | 327.8 | 84151 | -178 | -177.1 | weak |
| Call | 84100 | 521440 | 521392 | 140.4 | 84039 | 228.1 | 84240 | -88 | -87.6 | weak |
| Call | 84200 | 1055220 | 1055113 | 118.6 | 84063 | 128.2 | 84319 | -10 | -9.7 | weak |
| Call | 84300 | 2633980 | 2632999 | 115.8 | 84101 | 28.5 | 84416 | +87 | +87.3 | weak |
| Call | 84400 | 4699860 | 4698004 | 129.7 | 84187 | 0.1 | 84530 | +201 | +129.6 | medium |
| Call | 84500 | 4591840 | 4568046 | 107.3 | 84035 | 0.1 | 84607 | +279 | +107.3 | medium |
| Call | 84600 | 2441760 | 2440671 | 84.4 | 84165 | 0.1 | 84684 | +356 | +84.3 | medium |
| Call | 84700 | 2031540 | 2029446 | 65.7 | 84136 | 0.1 | 84766 | +437 | +65.7 | strong |
| Call | 84800 | 1689580 | 1686988 | 69.0 | 84117 | 0.1 | 84869 | +540 | +69.0 | strong |
| Call | 84900 | 803860 | 802158 | 55.9 | 84125 | 0.1 | 84956 | +627 | +55.8 | strong |
| Call | 85000 | 2635600 | 2619744 | 51.4 | 83995 | 0.1 | 85051 | +723 | +51.4 | strong |
| Call | 85100 | 804720 | 804126 | 33.0 | 83987 | 0.1 | 85133 | +804 | +33.0 | strong |
| Call | 85200 | 927240 | 926032 | 41.7 | 84007 | 0.1 | 85242 | +913 | +41.6 | strong |
| Call | 85300 | 1009340 | 1009012 | 23.6 | 84044 | 0.1 | 85324 | +995 | +23.6 | strong |
| Call | 85400 | 691720 | 690706 | 25.2 | 83925 | 0.1 | 85425 | +1097 | +25.2 | strong |
| Call | 85500 | 1752140 | 1741539 | 28.9 | 83753 | 0.1 | 85529 | +1200 | +28.8 | strong |
| Put | 83100 | 649080 | 648698 | 77.3 | 83923 | 0.1 | 83023 | +1306 | +77.2 | strong |
| Put | 83200 | 708140 | 707964 | 81.2 | 83931 | 0.1 | 83119 | +1210 | +81.2 | strong |
| Put | 83300 | 656900 | 656764 | 104.7 | 83925 | 0.1 | 83195 | +1133 | +104.6 | strong |
| Put | 83400 | 792360 | 792246 | 95.0 | 83964 | 0.1 | 83305 | +1024 | +95.0 | strong |
| Put | 83500 | 1851500 | 1850662 | 118.1 | 84021 | 0.1 | 83382 | +947 | +118.1 | strong |
| Put | 83600 | 1105200 | 1105126 | 105.4 | 84049 | 0.1 | 83495 | +834 | +105.3 | strong |
| Put | 83700 | 1093660 | 1093594 | 129.3 | 84065 | 0.1 | 83571 | +758 | +129.3 | strong |
| Put | 83800 | 2270800 | 2270647 | 188.0 | 84035 | 0.1 | 83612 | +717 | +188.0 | strong |
| Put | 83900 | 1552280 | 1552137 | 194.1 | 84080 | 0.1 | 83706 | +623 | +194.0 | strong |
| Put | 84000 | 3042480 | 3042088 | 122.8 | 84262 | 0.1 | 83877 | +451 | +122.7 | strong |
| Put | 84100 | 3292460 | 3292451 | 80.7 | 84294 | 0.1 | 84019 | +309 | +80.6 | medium |
| Put | 84200 | 4935300 | 4935297 | 59.8 | 84327 | 0.1 | 84140 | +188 | +59.8 | medium |
| Put | 84300 | 4522320 | 4522299 | 69.6 | 84336 | 0.1 | 84230 | +98 | +69.6 | weak |
| Put | 84400 | 907580 | 907580 | 140.4 | 84348 | 71.3 | 84260 | +69 | +69.1 | weak |
| Put | 84500 | 1025620 | 1025611 | 267.7 | 84345 | 171.0 | 84232 | +96 | +96.7 | weak |
| Put | 84600 | 371040 | 371040 | 350.9 | 84365 | 270.8 | 84249 | +79 | +80.1 | weak |
| Put | 84700 | 133060 | 133060 | 426.1 | 84329 | 371.5 | 84274 | +55 | +54.6 | weak |
| Put | 84800 | 27980 | 27980 | 476.2 | 84368 | 470.4 | 84324 | +5 | +5.9 | weak |
| Put | 84900 | 17640 | 17640 | 622.2 | 84348 | 570.2 | 84278 | +51 | +52.0 | weak |
| Put | 85000 | 125340 | 125287 | 665.8 | 84322 | 670.2 | 84334 | -6 | -4.5 | weak |
| Put | 85100 | 11980 | 11980 | 843.2 | 84294 | 770.1 | 84257 | +72 | +73.1 | weak |
| Put | 85200 | 7720 | 7720 | 926.6 | 84294 | 869.9 | 84273 | +55 | +56.7 | weak |
| Put | 85300 | 6000 | 3244 | 1080.4 | 84225 | 970.5 | 84220 | +109 | +109.9 | weak |
| Put | 85400 | 6240 | 6240 | 1183.7 | 84222 | 1069.8 | 84216 | +112 | +113.8 | weak |
| Put | 85500 | 27160 | 27160 | 1148.0 | 84331 | 1170.5 | 84352 | -23 | -22.4 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 86000, strongest put writers at 84000; weakest call writers at 82900, weakest put writers at -. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2100.0 | 84702 | +373 | -498.0 | medium |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +471 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +751 | -335.1 | strong |
| Call | 83400 | 520 | 511 | 1612.7 | 83261 | 2330.0 | 85013 | +684 | -717.3 | strong |
| Call | 83500 | 8340 | 8269 | 2097.4 | 83850 | 2322.9 | 85597 | +1269 | -225.6 | strong |
| Call | 83600 | 700 | 700 | 1823.9 | 83677 | 2151.3 | 85424 | +1095 | -327.4 | strong |
| Call | 83700 | 900 | 900 | 1622.0 | 83351 | 2154.7 | 85322 | +993 | -532.6 | strong |
| Call | 83800 | 300 | 300 | 1665.5 | 83527 | 2059.2 | 85465 | +1137 | -393.8 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +1029 | +287.6 | strong |
| Call | 84000 | 14700 | 14700 | 1802.8 | 83926 | 1984.0 | 85803 | +1474 | -181.2 | strong |
| Call | 84100 | 540 | 540 | 1647.6 | 83817 | 1863.9 | 85748 | +1419 | -216.3 | strong |
| Call | 84200 | 460 | 456 | 1485.4 | 83584 | 1566.0 | 85685 | +1357 | -80.7 | strong |
| Call | 84300 | 480 | 480 | 1628.6 | 84001 | 1807.0 | 85929 | +1600 | -178.3 | strong |
| Call | 84400 | 560 | 560 | 1436.4 | 83630 | 1494.5 | 85836 | +1508 | -58.1 | strong |
| Call | 84500 | 11420 | 11420 | 1588.4 | 84043 | 1707.5 | 86088 | +1760 | -119.1 | strong |
| Call | 84600 | 500 | 500 | 1353.9 | 83701 | 1503.6 | 85954 | +1625 | -149.7 | strong |
| Call | 84700 | 360 | 360 | 1205.3 | 83377 | 1342.4 | 85905 | +1577 | -137.1 | strong |
| Call | 84800 | 340 | 340 | 1243.1 | 83586 | 1548.1 | 86043 | +1714 | -305.0 | strong |
| Call | 84900 | 500 | 500 | 1161.1 | 83466 | 1472.5 | 86061 | +1733 | -311.3 | strong |
| Call | 85000 | 10780 | 10780 | 1284.6 | 83923 | 1438.2 | 86285 | +1956 | -153.6 | strong |
| Call | 85100 | 300 | 300 | 972.0 | 83276 | 1251.6 | 86072 | +1743 | -279.6 | strong |
| Call | 85200 | 420 | 420 | 978.6 | 83380 | 1305.8 | 86179 | +1850 | -327.2 | strong |
| Call | 85300 | 140 | 140 | 1067.3 | 83937 | 1260.4 | 86367 | +2039 | -193.1 | strong |
| Call | 85400 | 400 | 400 | 892.6 | 83194 | 1063.2 | 86293 | +1964 | -170.6 | strong |
| Call | 85500 | 3000 | 3000 | 1140.5 | 84098 | 1185.0 | 86641 | +2312 | -44.5 | strong |
| Put | 83100 | 160 | 160 | 1163.5 | 83622 | 846.0 | 81936 | +2392 | +317.6 | strong |
| Put | 83200 | 520 | 520 | 1379.9 | 83227 | 828.2 | 81820 | +2508 | +551.6 | strong |
| Put | 83300 | 460 | 460 | 1470.7 | 83125 | 910.5 | 81829 | +2499 | +560.2 | strong |
| Put | 83400 | 800 | 800 | 1387.1 | 83414 | 1097.0 | 82013 | +2316 | +290.0 | strong |
| Put | 83500 | 8300 | 8034 | 1214.7 | 83863 | 973.9 | 82285 | +2043 | +240.8 | strong |
| Put | 83600 | 1060 | 1060 | 1510.0 | 83349 | 1094.2 | 82090 | +2239 | +415.9 | strong |
| Put | 83700 | 640 | 640 | 1552.3 | 83332 | 1061.0 | 82148 | +2181 | +491.4 | strong |
| Put | 83800 | 800 | 800 | 1494.5 | 83550 | 1034.7 | 82306 | +2023 | +459.8 | strong |
| Put | 83900 | 520 | 506 | 1497.6 | 83620 | 1219.0 | 82402 | +1926 | +278.6 | strong |
| Put | 84000 | 19460 | 19460 | 1286.4 | 84125 | 1145.3 | 82714 | +1615 | +141.0 | strong |
| Put | 84100 | 1600 | 1600 | 1472.5 | 83860 | 1195.8 | 82628 | +1701 | +276.7 | strong |
| Put | 84200 | 1200 | 1200 | 1426.8 | 83983 | 1206.3 | 82773 | +1555 | +220.4 | strong |
| Put | 84300 | 980 | 980 | 1595.2 | 83826 | 1305.1 | 82705 | +1624 | +290.1 | strong |
| Put | 84400 | 1600 | 1600 | 1736.0 | 83669 | 1313.5 | 82664 | +1665 | +422.4 | strong |
| Put | 84500 | 10820 | 10820 | 1501.7 | 84148 | 1369.8 | 82998 | +1330 | +131.9 | strong |
| Put | 84600 | 960 | 960 | 1691.8 | 83913 | 1378.3 | 82908 | +1420 | +313.4 | strong |
| Put | 84700 | 720 | 720 | 1651.0 | 84077 | 1656.6 | 83049 | +1280 | -5.6 | strong |
| Put | 84800 | 760 | 760 | 1641.4 | 84218 | 1490.0 | 83159 | +1170 | +151.4 | strong |
| Put | 84900 | 780 | 780 | 2253.9 | 83187 | 1582.0 | 82646 | +1683 | +672.0 | strong |
| Put | 85000 | 9760 | 9760 | 1806.0 | 84018 | 1603.8 | 83194 | +1135 | +202.2 | strong |
| Put | 85100 | 420 | 420 | 1949.1 | 83844 | 1640.1 | 83151 | +1178 | +309.0 | strong |
| Put | 85200 | 620 | 620 | 2141.7 | 83689 | 2120.6 | 83058 | +1270 | +21.1 | strong |
| Put | 85300 | 1080 | 1080 | 2085.3 | 83780 | 1779.7 | 83215 | +1114 | +305.6 | strong |
| Put | 85400 | 140 | 140 | 2041.0 | 83938 | 2041.0 | 83359 | +970 | +0.0 | strong |
| Put | 85500 | 2620 | 2620 | 2369.2 | 83558 | 1875.2 | 83131 | +1198 | +494.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 12 | 36% | -0.30% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 9 | 75% | +0.01% | -0.22 to +0.16% |  | too few (8/10) |
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
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 1 | 100% | +0.66% | +0.66 to +0.66% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR flat · quiet OI · walls down · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
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
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
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
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.82% | +1.82 to +1.82% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.46% | +0.46 to +0.46% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.46% | +0.46 to +0.46% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 44 | 67% | +0.11% | no clear direction |
| intraday | monthly | writers even · few weak writers | 40 | 72% | +0.08% | up |
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
| day | monthly | writers even · few weak writers | 4 | 67% | -0.07% | too few (3/10) |
| day | weekly | writers even · few weak writers | 4 | 67% | +0.17% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak on both sides | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 36 | 72% | +0.08% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 26 | 67% | +0.13% | no clear direction |
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
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 67% | -0.07% | too few (3/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.65% | too few (2/10) |
| day | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
