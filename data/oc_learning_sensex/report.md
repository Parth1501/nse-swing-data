# Sensex option chain pattern log
Updated 2026-11-25 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 56 snapshots over 5 trading days
- 109 patterns logged; 50 different patterns so far

## Latest read (2026-11-25 14:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 1.0 | 83768 | 0.746 | 83800 | 82000 | 85000 | ±1.03% (82901-84635) | 24.3 |
| 2026-12-31 (monthly) | 36.0 | 83768 | 1.295 | 84000 | 83000 | 87900 | ±3.96% (80449-87087) | 15.68 |

- **Weekly, last 30 min**: `PCR up · unwinding · walls up · mid walls`. Seen 1 times before; Sensex was up after it 0% of the time, average -0.01%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 32 times before; Sensex was up after it 38% of the time, average -0.04%. Too few outcomes (16/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 14 times before; Sensex was up after it 46% of the time, average -0.01%. Too few outcomes (13/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 50% of the time, average -0.08%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 0% of the time, average -1.77%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · near put wall`. Seen 2 times before; Sensex was up after it 100% of the time, average +0.48%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 24 times before; Sensex was up after it 50% of the time, average -0.08%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 20 times before; Sensex was up after it 61% of the time, average -0.06%. Too few outcomes (18/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 82000; weakest call writers at 83000, weakest put writers at 84000. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82600 | 78560 | 75099 | 667.7 | 82737 | 1292.8 | 83268 | -500 | -625.0 | weak |
| Call | 82700 | 142120 | 135357 | 660.9 | 82828 | 1210.0 | 83361 | -407 | -549.1 | weak |
| Call | 82800 | 130140 | 120095 | 630.8 | 82868 | 1117.3 | 83431 | -337 | -486.5 | weak |
| Call | 82900 | 88740 | 81973 | 624.6 | 82943 | 1039.8 | 83525 | -243 | -415.2 | weak |
| Call | 83000 | 249700 | 224664 | 604.8 | 83013 | 959.5 | 83605 | -163 | -354.7 | weak |
| Call | 83100 | 94480 | 91609 | 622.4 | 83150 | 884.8 | 83722 | -46 | -262.4 | weak |
| Call | 83200 | 97980 | 96815 | 616.6 | 83268 | 807.5 | 83817 | +49 | -190.9 | weak |
| Call | 83300 | 93240 | 92364 | 577.9 | 83339 | 735.2 | 83878 | +110 | -157.3 | weak |
| Call | 83400 | 162320 | 160311 | 582.5 | 83468 | 668.1 | 83982 | +215 | -85.6 | medium |
| Call | 83500 | 576180 | 563302 | 471.4 | 83364 | 599.9 | 83971 | +203 | -128.5 | medium |
| Call | 83600 | 393820 | 392630 | 426.5 | 83466 | 542.0 | 84027 | +259 | -115.5 | medium |
| Call | 83700 | 832340 | 830714 | 423.4 | 83597 | 486.1 | 84123 | +355 | -62.7 | medium |
| Call | 83800 | 1221520 | 1218504 | 399.7 | 83651 | 437.8 | 84200 | +432 | -38.0 | strong |
| Call | 83900 | 1205200 | 1202940 | 390.5 | 83717 | 384.8 | 84291 | +523 | +5.7 | strong |
| Call | 84000 | 2093860 | 2050843 | 334.7 | 83569 | 345.0 | 84335 | +567 | -10.3 | strong |
| Call | 84100 | 786480 | 783899 | 323.7 | 83714 | 302.1 | 84424 | +656 | +21.5 | strong |
| Call | 84200 | 965420 | 962517 | 329.6 | 83786 | 266.1 | 84530 | +762 | +63.5 | strong |
| Call | 84300 | 1185860 | 1179382 | 314.4 | 83846 | 235.1 | 84614 | +846 | +79.2 | strong |
| Call | 84400 | 1129100 | 1123120 | 326.1 | 83888 | 207.0 | 84726 | +958 | +119.1 | strong |
| Call | 84500 | 1994340 | 1929316 | 277.2 | 83744 | 181.8 | 84777 | +1009 | +95.4 | strong |
| Call | 84600 | 951660 | 947564 | 260.5 | 83828 | 156.2 | 84861 | +1093 | +104.3 | strong |
| Call | 84700 | 853480 | 846256 | 202.4 | 83731 | 137.2 | 84902 | +1134 | +65.2 | strong |
| Call | 84800 | 937920 | 927703 | 171.8 | 83650 | 117.2 | 84972 | +1204 | +54.6 | strong |
| Call | 84900 | 985580 | 970798 | 141.9 | 83720 | 101.3 | 85042 | +1274 | +40.5 | strong |
| Call | 85000 | 3554920 | 3459154 | 120.2 | 83643 | 87.6 | 85120 | +1352 | +32.6 | strong |
| Put | 82600 | 640900 | 628659 | 147.1 | 83710 | 78.5 | 82453 | +1315 | +68.6 | strong |
| Put | 82700 | 669300 | 661801 | 150.5 | 83797 | 91.7 | 82550 | +1218 | +58.8 | strong |
| Put | 82800 | 650800 | 633424 | 153.7 | 83819 | 107.0 | 82646 | +1122 | +46.7 | strong |
| Put | 82900 | 515060 | 507467 | 176.8 | 83809 | 126.6 | 82723 | +1045 | +50.2 | strong |
| Put | 83000 | 2195820 | 2119248 | 175.1 | 83846 | 147.6 | 82825 | +943 | +27.5 | strong |
| Put | 83100 | 660940 | 659225 | 201.8 | 83793 | 168.8 | 82898 | +870 | +33.0 | strong |
| Put | 83200 | 597900 | 596833 | 248.7 | 83771 | 195.7 | 82951 | +817 | +53.0 | strong |
| Put | 83300 | 523100 | 522328 | 278.8 | 83777 | 223.9 | 83021 | +747 | +54.8 | strong |
| Put | 83400 | 798160 | 797284 | 279.7 | 83844 | 257.4 | 83120 | +648 | +22.2 | strong |
| Put | 83500 | 1697100 | 1692501 | 304.3 | 83850 | 293.5 | 83196 | +572 | +10.8 | strong |
| Put | 83600 | 857940 | 857348 | 357.2 | 83808 | 336.2 | 83243 | +525 | +20.9 | strong |
| Put | 83700 | 1136780 | 1136019 | 379.2 | 83811 | 382.0 | 83321 | +447 | -2.8 | strong |
| Put | 83800 | 1270740 | 1270112 | 404.6 | 83845 | 429.0 | 83395 | +373 | -24.4 | medium |
| Put | 83900 | 697900 | 697246 | 421.2 | 83921 | 481.1 | 83479 | +289 | -59.8 | medium |
| Put | 84000 | 1084140 | 1081679 | 408.1 | 84036 | 534.8 | 83592 | +176 | -126.6 | weak |
| Put | 84100 | 281140 | 281096 | 400.3 | 84130 | 595.2 | 83700 | +68 | -194.9 | weak |
| Put | 84200 | 234380 | 234365 | 392.5 | 84234 | 658.8 | 83808 | -40 | -266.3 | weak |
| Put | 84300 | 189740 | 189586 | 409.0 | 84296 | 724.0 | 83891 | -123 | -315.0 | weak |
| Put | 84400 | 199320 | 199318 | 438.3 | 84332 | 793.8 | 83962 | -194 | -355.5 | weak |
| Put | 84500 | 317820 | 317752 | 533.7 | 84280 | 869.8 | 83966 | -198 | -336.0 | weak |
| Put | 84600 | 108840 | 108840 | 615.7 | 84268 | 949.9 | 83984 | -216 | -334.2 | weak |
| Put | 84700 | 42740 | 42740 | 861.2 | 84058 | 1025.7 | 83839 | -71 | -164.5 | weak |
| Put | 84800 | 23040 | 23040 | 703.7 | 84268 | 1104.2 | 84096 | -328 | -400.4 | weak |
| Put | 84900 | 30700 | 30700 | 865.5 | 84173 | 1210.3 | 84034 | -266 | -344.8 | weak |
| Put | 85000 | 135760 | 134746 | 935.4 | 84171 | 1282.8 | 84065 | -297 | -347.4 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 86000, strongest put writers at 83000; weakest call writers at -, weakest put writers at 86000. Covers 95% of near-money call OI and 96% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82600 | 120 | 120 | 1778.5 | 82439 | 1789.5 | 84378 | +611 | -10.9 | strong |
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +778 | -732.3 | strong |
| Call | 82800 | 1220 | 1132 | 2157.1 | 83288 | 2450.0 | 84957 | +1189 | -292.9 | strong |
| Call | 82900 | 260 | 220 | 1609.0 | 82444 | 1609.0 | 84509 | +741 | +0.0 | strong |
| Call | 83000 | 3260 | 3124 | 2053.9 | 83339 | 2300.0 | 85054 | +1286 | -246.1 | strong |
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2100.0 | 84702 | +934 | -498.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +1032 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +1312 | -335.1 | strong |
| Call | 83400 | 560 | 551 | 1612.7 | 83261 | 2050.0 | 85013 | +1245 | -437.3 | strong |
| Call | 83500 | 3360 | 3288 | 1986.9 | 83622 | 2010.0 | 85487 | +1719 | -23.1 | strong |
| Call | 83600 | 540 | 540 | 1550.3 | 83212 | 1273.7 | 85150 | +1382 | +276.6 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1811.3 | 85310 | +1542 | -201.4 | strong |
| Call | 83800 | 260 | 260 | 1570.1 | 83332 | 1919.4 | 85370 | +1602 | -349.3 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +1589 | +287.6 | strong |
| Call | 84000 | 4540 | 4540 | 1605.0 | 83551 | 1740.3 | 85605 | +1837 | -135.4 | strong |
| Call | 84100 | 380 | 380 | 1606.2 | 83694 | 1642.2 | 85706 | +1938 | -35.9 | strong |
| Call | 84200 | 440 | 433 | 1330.2 | 83255 | 1601.5 | 85530 | +1762 | -271.3 | strong |
| Call | 84300 | 100 | 100 | 1418.9 | 83544 | 1555.2 | 85719 | +1951 | -136.2 | strong |
| Call | 84400 | 200 | 200 | 1192.8 | 82934 | 1351.8 | 85593 | +1825 | -159.0 | strong |
| Call | 84500 | 2880 | 2880 | 1460.5 | 83677 | 1485.1 | 85960 | +2193 | -24.6 | strong |
| Call | 84600 | 220 | 220 | 1225.2 | 83341 | 1343.6 | 85825 | +2057 | -118.4 | strong |
| Call | 84700 | 560 | 560 | 1029.4 | 82892 | 853.5 | 85729 | +1961 | +175.8 | strong |
| Call | 84800 | 380 | 380 | 997.6 | 82976 | 831.0 | 85798 | +2030 | +166.6 | strong |
| Call | 84900 | 1080 | 1080 | 1049.3 | 83164 | 798.2 | 85949 | +2181 | +251.1 | strong |
| Call | 85000 | 4040 | 4040 | 1079.7 | 83384 | 1234.7 | 86080 | +2312 | -155.0 | strong |
| Put | 82600 | 640 | 640 | 934.4 | 83815 | 944.9 | 81666 | +2102 | -10.4 | strong |
| Put | 82700 | 280 | 280 | 955.9 | 83860 | 1008.9 | 81744 | +2024 | -53.0 | strong |
| Put | 82800 | 160 | 160 | 978.1 | 83729 | 1008.9 | 81822 | +1946 | -30.8 | strong |
| Put | 82900 | 100 | 100 | 1103.6 | 83606 | 975.9 | 81796 | +1972 | +127.7 | strong |
| Put | 83000 | 11480 | 10988 | 1127.3 | 83655 | 1081.0 | 81873 | +1895 | +46.3 | strong |
| Put | 83100 | 280 | 280 | 1278.5 | 83394 | 1144.2 | 81821 | +1946 | +134.4 | strong |
| Put | 83200 | 560 | 560 | 1379.9 | 83227 | 1111.5 | 81820 | +1948 | +268.4 | strong |
| Put | 83300 | 620 | 620 | 1470.7 | 83125 | 1217.5 | 81829 | +1939 | +253.3 | strong |
| Put | 83400 | 900 | 900 | 1397.1 | 83392 | 1239.4 | 82003 | +1765 | +157.7 | strong |
| Put | 83500 | 3320 | 3050 | 1342.4 | 83632 | 1263.2 | 82158 | +1610 | +79.2 | strong |
| Put | 83600 | 1200 | 1200 | 1521.0 | 83328 | 1268.0 | 82079 | +1689 | +253.0 | strong |
| Put | 83700 | 760 | 760 | 1566.8 | 83306 | 1425.1 | 82133 | +1635 | +141.7 | strong |
| Put | 83800 | 860 | 860 | 1494.5 | 83550 | 1400.0 | 82306 | +1462 | +94.5 | strong |
| Put | 83900 | 520 | 506 | 1512.2 | 83593 | 1450.0 | 82388 | +1380 | +62.2 | strong |
| Put | 84000 | 3380 | 3380 | 1445.4 | 83846 | 1458.0 | 82555 | +1213 | -12.7 | strong |
| Put | 84100 | 1380 | 1380 | 1552.7 | 83724 | 1492.0 | 82547 | +1221 | +60.7 | strong |
| Put | 84200 | 860 | 860 | 1537.0 | 83811 | 1478.3 | 82663 | +1105 | +58.7 | strong |
| Put | 84300 | 1020 | 1020 | 1614.7 | 83792 | 1554.3 | 82685 | +1083 | +60.4 | strong |
| Put | 84400 | 1520 | 1520 | 1796.7 | 83562 | 1669.8 | 82603 | +1165 | +126.9 | strong |
| Put | 84500 | 8280 | 8280 | 1502.0 | 84199 | 1704.7 | 82998 | +770 | -202.7 | strong |
| Put | 84600 | 920 | 920 | 1703.9 | 83894 | 1756.2 | 82896 | +872 | -52.4 | strong |
| Put | 84700 | 560 | 560 | 1672.2 | 84036 | 1515.0 | 83028 | +740 | +157.1 | strong |
| Put | 84800 | 540 | 540 | 1673.6 | 84175 | 1586.3 | 83126 | +642 | +87.3 | strong |
| Put | 84900 | 680 | 680 | 2351.3 | 83032 | 1633.4 | 82549 | +1219 | +717.9 | strong |
| Put | 85000 | 3440 | 3440 | 2034.6 | 83695 | 1949.3 | 82965 | +803 | +85.3 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 11 | 30% | -0.38% | -1.29 to +0.22% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 6 | 33% | -0.06% | -0.22 to +0.16% |  | too few (6/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 20% | -0.18% | -0.70 to +0.25% |  | too few (5/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.43% | -0.64 to -0.22% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 3 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 2 | 0% | -0.67% | -0.70 to -0.64% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.14% | -1.14 to +0.86% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 0% | -0.75% | -0.80 to -0.70% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.56% | -1.14 to +0.02% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.85% | -0.85 to -0.85% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.83% | -0.83 to -0.83% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.16% | -0.16 to -0.16% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 0% | -0.18% | -0.18 to -0.18% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.62% | +1.62 to +1.62% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.62% | +1.62 to +1.62% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 33 | 38% | -0.04% | no clear direction |
| intraday | monthly | writers even · few weak writers | 25 | 50% | -0.08% | no clear direction |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.47% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 5 | 20% | -0.65% | too few (5/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.34% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 0% | -0.11% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.70% | too few (1/10) |
| day | weekly | writers even · few weak writers | 4 | 50% | -0.08% | too few (2/10) |
| day | monthly | writers even · few weak writers | 3 | 50% | -0.34% | too few (2/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.62% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 21 | 61% | -0.06% | no clear direction |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 0% | -0.18% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 15 | 46% | -0.01% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 5 | 20% | -0.65% | too few (5/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 4 | 0% | -0.16% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 100% | +0.34% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.70% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.11% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.70% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | -0.34% | too few (2/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.62% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.62% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 0% | -1.77% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
