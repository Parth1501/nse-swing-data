# Sensex option chain pattern log
Updated 2026-11-26 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 62 snapshots over 6 trading days
- 121 patterns logged; 56 different patterns so far

## Latest read (2026-11-26 10:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 0.2 | 84458 | 0.919 | 84200 | 83000 | 85000 | ±0.55% (83997-84918) | 29.49 |
| 2026-12-31 (monthly) | 35.2 | 84458 | 1.168 | 84000 | 83000 | 84500 | ±3.72% (81313-87603) | 14.89 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 38 times before; Sensex was up after it 67% of the time, average +0.13%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 20 times before; Sensex was up after it 67% of the time, average +0.14%. Too few outcomes (18/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near call wall`. Seen 1 times before; Sensex was up after it 0% of the time, average -1.77%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 67% of the time, average +0.22%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 50% of the time, average -0.57%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 30 times before; Sensex was up after it 74% of the time, average +0.08%. History points to a bull call debit spread, ATM to about the call wall 84500.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 26 times before; Sensex was up after it 74% of the time, average +0.09%. History points to a bull call debit spread, ATM to about the call wall 84500.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 67% of the time, average -0.02%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Sensex was up after it 67% of the time, average -0.02%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 83000; weakest call writers at 84400, weakest put writers at 85500. Covers 99% of near-money call OI and 99% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83200 | 59580 | 58871 | 616.6 | 83268 | 1292.2 | 83817 | -641 | -675.6 | weak |
| Call | 83300 | 39260 | 38891 | 577.9 | 83339 | 1196.8 | 83878 | -580 | -618.9 | weak |
| Call | 83400 | 87840 | 86831 | 576.9 | 83491 | 1098.2 | 83977 | -481 | -521.3 | weak |
| Call | 83500 | 207900 | 204291 | 464.7 | 83458 | 1001.1 | 83965 | -493 | -536.4 | weak |
| Call | 83600 | 156440 | 156084 | 414.3 | 83543 | 908.2 | 84014 | -443 | -493.9 | weak |
| Call | 83700 | 193360 | 193129 | 383.7 | 83667 | 819.9 | 84084 | -374 | -436.2 | weak |
| Call | 83800 | 454140 | 453673 | 324.1 | 83724 | 720.1 | 84124 | -334 | -396.0 | weak |
| Call | 83900 | 639760 | 639292 | 290.3 | 83753 | 635.5 | 84190 | -267 | -345.2 | weak |
| Call | 84000 | 1321720 | 1311571 | 243.0 | 83700 | 552.7 | 84243 | -215 | -309.7 | weak |
| Call | 84100 | 1325720 | 1325065 | 215.5 | 83871 | 471.4 | 84316 | -142 | -255.9 | weak |
| Call | 84200 | 1799100 | 1797914 | 191.7 | 83849 | 397.8 | 84392 | -66 | -206.1 | weak |
| Call | 84300 | 2526440 | 2522299 | 181.5 | 83850 | 330.6 | 84482 | +24 | -149.1 | weak |
| Call | 84400 | 2865100 | 2861514 | 214.5 | 84071 | 274.4 | 84615 | +157 | -59.9 | weak |
| Call | 84500 | 4223080 | 4180773 | 148.6 | 83852 | 220.4 | 84649 | +191 | -71.9 | medium |
| Call | 84600 | 1992580 | 1990145 | 136.1 | 83940 | 176.0 | 84736 | +278 | -39.9 | medium |
| Call | 84700 | 1980520 | 1975695 | 103.0 | 83893 | 139.4 | 84803 | +345 | -36.5 | medium |
| Call | 84800 | 2416280 | 2410054 | 91.7 | 83985 | 109.2 | 84892 | +434 | -17.5 | strong |
| Call | 84900 | 2109660 | 2101410 | 74.3 | 83983 | 84.5 | 84974 | +517 | -10.1 | strong |
| Call | 85000 | 6457500 | 6404907 | 59.3 | 83870 | 64.9 | 85059 | +601 | -5.6 | strong |
| Call | 85100 | 2270600 | 2268364 | 39.2 | 83885 | 49.8 | 85139 | +681 | -10.6 | strong |
| Call | 85200 | 2006400 | 2002860 | 49.3 | 83895 | 37.1 | 85249 | +791 | +12.1 | strong |
| Call | 85300 | 2034500 | 2033368 | 33.1 | 83856 | 28.1 | 85333 | +875 | +5.0 | strong |
| Call | 85400 | 1645380 | 1642195 | 30.1 | 83787 | 21.2 | 85430 | +972 | +8.9 | strong |
| Call | 85500 | 4263140 | 4235970 | 29.8 | 83718 | 15.9 | 85530 | +1072 | +13.9 | strong |
| Call | 85600 | 1797500 | 1795357 | 26.5 | 83922 | 12.0 | 85626 | +1169 | +14.5 | strong |
| Call | 85700 | 1482560 | 1481350 | 27.2 | 83939 | 9.1 | 85727 | +1269 | +18.1 | strong |
| Put | 83200 | 2026460 | 2025691 | 119.1 | 83867 | 13.2 | 83081 | +1377 | +105.9 | strong |
| Put | 83300 | 1850600 | 1850127 | 126.3 | 83892 | 15.8 | 83174 | +1284 | +110.5 | strong |
| Put | 83400 | 1790700 | 1790240 | 157.3 | 83881 | 19.2 | 83243 | +1215 | +138.2 | strong |
| Put | 83500 | 5564240 | 5560662 | 158.7 | 83981 | 23.6 | 83341 | +1117 | +135.1 | strong |
| Put | 83600 | 2332660 | 2332357 | 178.9 | 84001 | 29.4 | 83421 | +1037 | +149.5 | strong |
| Put | 83700 | 2451820 | 2451544 | 212.0 | 83974 | 37.0 | 83488 | +970 | +175.0 | strong |
| Put | 83800 | 2976900 | 2976567 | 281.5 | 83912 | 45.9 | 83518 | +939 | +235.6 | strong |
| Put | 83900 | 2449320 | 2448885 | 325.7 | 83919 | 59.7 | 83574 | +884 | +266.0 | strong |
| Put | 84000 | 4787500 | 4785749 | 284.4 | 84084 | 76.8 | 83716 | +742 | +207.5 | strong |
| Put | 84100 | 2577680 | 2577643 | 316.7 | 84071 | 96.8 | 83783 | +674 | +219.9 | strong |
| Put | 84200 | 2106160 | 2106149 | 259.8 | 84256 | 121.1 | 83940 | +518 | +138.7 | strong |
| Put | 84300 | 2031120 | 2031009 | 225.5 | 84371 | 154.6 | 84074 | +383 | +71.0 | strong |
| Put | 84400 | 1497160 | 1497159 | 251.4 | 84400 | 194.5 | 84149 | +309 | +57.0 | medium |
| Put | 84500 | 995700 | 995661 | 395.0 | 84304 | 240.0 | 84105 | +353 | +155.0 | medium |
| Put | 84600 | 248740 | 248740 | 436.2 | 84369 | 301.1 | 84164 | +294 | +135.2 | medium |
| Put | 84700 | 128860 | 128860 | 614.8 | 84227 | 363.6 | 84085 | +373 | +251.2 | medium |
| Put | 84800 | 82320 | 82320 | 537.8 | 84367 | 434.2 | 84262 | +196 | +103.5 | medium |
| Put | 84900 | 48200 | 48200 | 704.6 | 84293 | 503.8 | 84195 | +262 | +200.9 | medium |
| Put | 85000 | 245620 | 245004 | 768.5 | 84297 | 587.2 | 84231 | +226 | +181.3 | medium |
| Put | 85100 | 10580 | 10580 | 915.9 | 84252 | 670.0 | 84184 | +274 | +245.9 | medium |
| Put | 85200 | 9740 | 9740 | 999.3 | 84243 | 761.1 | 84201 | +257 | +238.2 | medium |
| Put | 85300 | 11820 | 4618 | 1155.2 | 84175 | 852.9 | 84145 | +313 | +302.3 | medium |
| Put | 85400 | 3380 | 3380 | 1313.2 | 84113 | 951.9 | 84087 | +371 | +361.3 | medium |
| Put | 85500 | 11500 | 11500 | 1105.8 | 84386 | 1040.0 | 84394 | +64 | +65.8 | weak |
| Put | 85600 | 2280 | 2280 | 1303.7 | 84298 | 1145.0 | 84296 | +161 | +158.7 | weak |
| Put | 85700 | 1800 | 1800 | 1686.4 | 83997 | 1214.0 | 84014 | +444 | +472.4 | strong |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 84000, strongest put writers at 84000; weakest call writers at 82900, weakest put writers at -. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +342 | -1016.5 | medium |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +622 | -335.1 | strong |
| Call | 83400 | 540 | 531 | 1612.7 | 83261 | 2152.9 | 85013 | +555 | -540.2 | strong |
| Call | 83500 | 8080 | 8008 | 2088.6 | 83832 | 2359.7 | 85589 | +1131 | -271.1 | strong |
| Call | 83600 | 860 | 860 | 1787.7 | 83621 | 2300.0 | 85388 | +930 | -512.3 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1805.5 | 85310 | +852 | -195.6 | strong |
| Call | 83800 | 340 | 340 | 1665.5 | 83527 | 2019.9 | 85465 | +1008 | -354.4 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +900 | +287.6 | strong |
| Call | 84000 | 11420 | 11420 | 1752.5 | 83822 | 2055.9 | 85753 | +1295 | -303.4 | strong |
| Call | 84100 | 560 | 560 | 1638.5 | 83796 | 1887.8 | 85739 | +1281 | -249.2 | strong |
| Call | 84200 | 600 | 594 | 1470.3 | 83559 | 1935.0 | 85670 | +1213 | -464.7 | strong |
| Call | 84300 | 300 | 300 | 1619.9 | 83982 | 1846.3 | 85920 | +1462 | -226.4 | strong |
| Call | 84400 | 320 | 320 | 1291.4 | 83274 | 1774.0 | 85691 | +1234 | -482.6 | strong |
| Call | 84500 | 9280 | 9280 | 1521.9 | 83901 | 1777.2 | 86022 | +1564 | -255.3 | strong |
| Call | 84600 | 300 | 300 | 1256.5 | 83457 | 1342.4 | 85856 | +1399 | -86.0 | strong |
| Call | 84700 | 260 | 260 | 1113.5 | 83133 | 1576.0 | 85813 | +1356 | -462.5 | strong |
| Call | 84800 | 180 | 180 | 997.6 | 82976 | 1237.8 | 85798 | +1340 | -240.2 | strong |
| Call | 84900 | 360 | 360 | 1049.3 | 83164 | 1339.7 | 85949 | +1491 | -290.4 | strong |
| Call | 85000 | 5600 | 5600 | 1140.5 | 83539 | 1495.8 | 86141 | +1683 | -355.3 | strong |
| Call | 85100 | 300 | 300 | 972.0 | 83276 | 1246.0 | 86072 | +1614 | -274.0 | strong |
| Call | 85200 | 320 | 320 | 816.9 | 82858 | 1203.5 | 86017 | +1559 | -386.5 | strong |
| Call | 85300 | 120 | 120 | 1035.2 | 83872 | 1035.5 | 86335 | +1877 | -0.4 | strong |
| Call | 85400 | 800 | 800 | 892.6 | 83194 | 670.7 | 86293 | +1835 | +221.9 | strong |
| Call | 85500 | 1500 | 1500 | 1073.3 | 83907 | 1240.0 | 86573 | +2116 | -166.7 | strong |
| Call | 85600 | 320 | 320 | 991.5 | 83834 | 947.8 | 86592 | +2134 | +43.8 | strong |
| Call | 85700 | 1260 | 1260 | 822.6 | 83328 | 1053.7 | 86523 | +2065 | -231.1 | strong |
| Put | 83200 | 560 | 560 | 1379.9 | 83227 | 1039.0 | 81820 | +2638 | +340.9 | strong |
| Put | 83300 | 560 | 560 | 1470.7 | 83125 | 1095.5 | 81829 | +2629 | +375.2 | strong |
| Put | 83400 | 820 | 820 | 1397.1 | 83392 | 1142.8 | 82003 | +2455 | +254.3 | strong |
| Put | 83500 | 8100 | 7830 | 1223.1 | 83844 | 997.1 | 82277 | +2181 | +226.0 | strong |
| Put | 83600 | 1060 | 1060 | 1521.0 | 83328 | 1185.7 | 82079 | +2379 | +335.3 | strong |
| Put | 83700 | 680 | 680 | 1566.8 | 83306 | 1219.6 | 82133 | +2325 | +347.2 | strong |
| Put | 83800 | 800 | 800 | 1494.5 | 83550 | 1230.5 | 82306 | +2152 | +263.9 | strong |
| Put | 83900 | 520 | 506 | 1512.2 | 83593 | 1182.7 | 82388 | +2070 | +329.5 | strong |
| Put | 84000 | 11020 | 11020 | 1371.4 | 83986 | 1174.4 | 82629 | +1829 | +197.0 | strong |
| Put | 84100 | 1420 | 1420 | 1545.0 | 83738 | 1219.1 | 82555 | +1903 | +325.9 | strong |
| Put | 84200 | 840 | 840 | 1537.0 | 83811 | 1330.0 | 82663 | +1795 | +206.9 | strong |
| Put | 84300 | 1020 | 1020 | 1614.7 | 83792 | 1500.0 | 82685 | +1772 | +114.7 | strong |
| Put | 84400 | 1480 | 1480 | 1790.6 | 83574 | 1350.0 | 82609 | +1848 | +440.6 | strong |
| Put | 84500 | 10660 | 10660 | 1559.1 | 84090 | 1368.0 | 82941 | +1517 | +191.1 | strong |
| Put | 84600 | 920 | 920 | 1703.9 | 83894 | 1630.7 | 82896 | +1562 | +73.2 | strong |
| Put | 84700 | 600 | 600 | 1671.1 | 84044 | 1655.9 | 83029 | +1429 | +15.2 | strong |
| Put | 84800 | 540 | 540 | 1673.6 | 84175 | 1586.3 | 83126 | +1331 | +87.3 | strong |
| Put | 84900 | 680 | 680 | 2351.3 | 83032 | 1633.4 | 82549 | +1909 | +717.9 | strong |
| Put | 85000 | 4400 | 4400 | 1980.2 | 83798 | 1594.6 | 83020 | +1438 | +385.6 | strong |
| Put | 85100 | 400 | 400 | 1964.5 | 83821 | 1646.2 | 83135 | +1322 | +318.3 | strong |
| Put | 85200 | 620 | 620 | 2141.7 | 83689 | 2120.6 | 83058 | +1399 | +21.1 | strong |
| Put | 85300 | 1080 | 1080 | 2085.3 | 83780 | 2085.3 | 83215 | +1243 | +0.0 | strong |
| Put | 85400 | 140 | 140 | 2041.0 | 83938 | 2041.0 | 83359 | +1099 | +0.0 | strong |
| Put | 85500 | 2620 | 2620 | 2392.5 | 83524 | 1855.0 | 83107 | +1350 | +537.6 | strong |
| Put | 85600 | 1220 | 1220 | 2125.3 | 84218 | 2056.3 | 83475 | +983 | +69.0 | strong |
| Put | 85700 | 1160 | 1160 | 2100.3 | 84226 | 2284.1 | 83600 | +858 | -183.8 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 11 | 30% | -0.34% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 6 | 67% | +0.00% | -0.22 to +0.16% |  | too few (6/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 4 | 67% | +0.21% | -0.05 to +0.48% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.17% | -1.15 to +0.81% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 3 | 0% | -0.06% | -0.07 to -0.05% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.14% | -1.14 to +0.86% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 0% | -0.65% | -0.80 to -0.50% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 1 | 100% | +0.81% | +0.81 to +0.81% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
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
| weekly | PCR up · put and call writing · walls same · near call wall | 2 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.82% | +1.82 to +1.82% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 39 | 67% | +0.13% | no clear direction |
| intraday | monthly | writers even · few weak writers | 31 | 74% | +0.08% | up |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 5 | 20% | -0.61% | too few (5/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| day | weekly | writers even · few weak writers | 5 | 67% | +0.22% | too few (3/10) |
| day | monthly | writers even · few weak writers | 4 | 67% | -0.02% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 27 | 74% | +0.09% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 21 | 67% | +0.14% | no clear direction |
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
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 67% | -0.02% | too few (3/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | -0.57% | too few (2/10) |
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
