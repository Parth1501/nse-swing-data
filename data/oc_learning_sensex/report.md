# Sensex option chain pattern log
Updated 2026-11-25 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 54 snapshots over 5 trading days
- 105 patterns logged; 49 different patterns so far

## Latest read (2026-11-25 13:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 1.1 | 83748 | 0.708 | 83700 | 80000 | 85000 | ±1.07% (82852-84644) | 24.63 |
| 2026-12-31 (monthly) | 36.1 | 83746 | 1.382 | 84000 | 83000 | 87900 | ±3.86% (80510-86983) | 15.19 |

- **Weekly, last 30 min**: `PCR down · call writing · walls down · near call wall`. Seen 1 times before; Sensex was up after it 0% of the time, average -1.14%. Too few outcomes (1/20) to trade on.
  - Writers: `call writers stronger · few weak writers`. Seen 4 times before; Sensex was up after it 0% of the time, average -0.82%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 4 times before; Sensex was up after it 0% of the time, average -0.82%. Too few outcomes (4/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put writing · walls same · near put wall`. Seen 10 times before; Sensex was up after it 22% of the time, average -0.43%. Too few outcomes (9/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 22 times before; Sensex was up after it 50% of the time, average -0.09%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 18 times before; Sensex was up after it 62% of the time, average -0.06%. Too few outcomes (16/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 83000; weakest call writers at 83000, weakest put writers at 84000. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82500 | 185460 | 155191 | 631.1 | 82581 | 1382.6 | 83131 | -617 | -751.5 | weak |
| Call | 82600 | 79680 | 76169 | 667.7 | 82737 | 1299.6 | 83268 | -480 | -631.9 | weak |
| Call | 82700 | 144520 | 137618 | 658.7 | 82825 | 1187.5 | 83359 | -389 | -528.7 | weak |
| Call | 82800 | 130060 | 119869 | 620.8 | 82850 | 1132.2 | 83421 | -327 | -511.4 | weak |
| Call | 82900 | 91180 | 84217 | 624.0 | 82942 | 1047.8 | 83524 | -224 | -423.8 | weak |
| Call | 83000 | 257200 | 230988 | 598.3 | 82999 | 963.9 | 83598 | -149 | -365.6 | weak |
| Call | 83100 | 96540 | 93606 | 622.4 | 83150 | 888.3 | 83722 | -25 | -265.9 | weak |
| Call | 83200 | 100300 | 99105 | 616.2 | 83268 | 814.5 | 83816 | +69 | -198.3 | weak |
| Call | 83300 | 101100 | 100150 | 577.9 | 83339 | 744.4 | 83878 | +130 | -166.4 | weak |
| Call | 83400 | 199920 | 197445 | 582.5 | 83468 | 679.3 | 83982 | +235 | -96.8 | medium |
| Call | 83500 | 728760 | 712472 | 471.4 | 83364 | 616.3 | 83971 | +224 | -144.9 | medium |
| Call | 83600 | 553980 | 552307 | 426.5 | 83466 | 558.4 | 84027 | +279 | -131.8 | medium |
| Call | 83700 | 926440 | 924539 | 420.2 | 83588 | 502.4 | 84120 | +373 | -82.2 | medium |
| Call | 83800 | 1171760 | 1168744 | 396.3 | 83642 | 452.2 | 84196 | +449 | -55.9 | strong |
| Call | 83900 | 1042000 | 1039652 | 376.8 | 83680 | 404.8 | 84277 | +529 | -28.0 | strong |
| Call | 84000 | 2029460 | 1986055 | 331.6 | 83556 | 362.2 | 84332 | +584 | -30.6 | strong |
| Call | 84100 | 992500 | 989243 | 323.7 | 83714 | 321.2 | 84424 | +676 | +2.5 | strong |
| Call | 84200 | 919980 | 916914 | 330.4 | 83774 | 286.1 | 84530 | +783 | +44.2 | strong |
| Call | 84300 | 994660 | 987538 | 323.5 | 83830 | 253.7 | 84624 | +876 | +69.9 | strong |
| Call | 84400 | 1167600 | 1161416 | 326.1 | 83888 | 223.2 | 84726 | +978 | +102.9 | strong |
| Call | 84500 | 2200640 | 2128890 | 277.2 | 83744 | 197.4 | 84777 | +1030 | +79.8 | strong |
| Call | 84600 | 902820 | 898724 | 265.9 | 83831 | 173.6 | 84866 | +1118 | +92.4 | strong |
| Call | 84700 | 873720 | 866051 | 203.7 | 83724 | 151.2 | 84904 | +1156 | +52.4 | strong |
| Call | 84800 | 903860 | 893643 | 173.3 | 83642 | 132.3 | 84973 | +1226 | +40.9 | strong |
| Call | 84900 | 976840 | 961884 | 142.7 | 83719 | 116.0 | 85043 | +1295 | +26.7 | strong |
| Call | 85000 | 3283480 | 3187714 | 122.3 | 83628 | 101.6 | 85122 | +1375 | +20.7 | strong |
| Put | 82500 | 1692060 | 1572240 | 125.0 | 83784 | 71.2 | 82375 | +1373 | +53.8 | strong |
| Put | 82600 | 480300 | 468059 | 175.2 | 83655 | 83.5 | 82425 | +1323 | +91.7 | strong |
| Put | 82700 | 664000 | 656124 | 155.1 | 83791 | 97.8 | 82545 | +1203 | +57.3 | strong |
| Put | 82800 | 520720 | 503344 | 169.1 | 83812 | 114.5 | 82631 | +1117 | +54.6 | strong |
| Put | 82900 | 443820 | 436227 | 189.2 | 83795 | 133.2 | 82711 | +1037 | +56.0 | strong |
| Put | 83000 | 2211860 | 2131714 | 177.6 | 83844 | 155.2 | 82822 | +925 | +22.4 | strong |
| Put | 83100 | 470900 | 469155 | 231.0 | 83746 | 178.8 | 82869 | +879 | +52.1 | strong |
| Put | 83200 | 611820 | 610630 | 253.5 | 83771 | 205.6 | 82947 | +801 | +47.9 | strong |
| Put | 83300 | 619080 | 618166 | 278.8 | 83777 | 236.6 | 83021 | +726 | +42.2 | strong |
| Put | 83400 | 732200 | 731306 | 287.7 | 83838 | 271.1 | 83112 | +635 | +16.6 | strong |
| Put | 83500 | 1508040 | 1503416 | 312.9 | 83844 | 308.8 | 83187 | +561 | +4.1 | strong |
| Put | 83600 | 778040 | 777448 | 363.8 | 83802 | 349.6 | 83236 | +512 | +14.2 | strong |
| Put | 83700 | 945880 | 945119 | 387.8 | 83802 | 393.7 | 83312 | +435 | -5.9 | strong |
| Put | 83800 | 847360 | 846732 | 424.8 | 83826 | 442.9 | 83375 | +373 | -18.1 | medium |
| Put | 83900 | 671380 | 670636 | 425.6 | 83925 | 496.8 | 83474 | +273 | -71.2 | medium |
| Put | 84000 | 984480 | 981890 | 400.9 | 84058 | 552.8 | 83599 | +149 | -151.9 | weak |
| Put | 84100 | 233340 | 233296 | 374.0 | 84183 | 614.3 | 83726 | +22 | -240.3 | weak |
| Put | 84200 | 261720 | 261704 | 392.5 | 84234 | 676.4 | 83808 | -60 | -283.9 | weak |
| Put | 84300 | 195120 | 194958 | 404.5 | 84304 | 745.2 | 83896 | -148 | -340.7 | weak |
| Put | 84400 | 243320 | 243318 | 438.3 | 84332 | 815.0 | 83962 | -214 | -376.6 | weak |
| Put | 84500 | 353780 | 353705 | 533.2 | 84281 | 889.1 | 83967 | -219 | -355.9 | weak |
| Put | 84600 | 122480 | 122480 | 615.7 | 84268 | 964.5 | 83984 | -237 | -348.8 | weak |
| Put | 84700 | 46980 | 46980 | 861.2 | 84058 | 1043.6 | 83839 | -91 | -182.4 | weak |
| Put | 84800 | 36120 | 36120 | 703.7 | 84268 | 1124.3 | 84096 | -349 | -420.6 | weak |
| Put | 84900 | 31940 | 31940 | 865.5 | 84173 | 1210.0 | 84034 | -287 | -344.5 | weak |
| Put | 85000 | 143820 | 142703 | 926.5 | 84182 | 1296.5 | 84074 | -326 | -370.1 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 85900, strongest put writers at 83000; weakest call writers at -, weakest put writers at 86000. Covers 94% of near-money call OI and 96% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82500 | 960 | 931 | 2515.2 | 83617 | 2493.9 | 85015 | +1269 | +21.3 | strong |
| Call | 82600 | 120 | 120 | 1778.5 | 82439 | 1789.5 | 84378 | +632 | -10.9 | strong |
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +799 | -732.3 | strong |
| Call | 82800 | 720 | 632 | 1854.8 | 82817 | 2500.0 | 84655 | +908 | -645.2 | strong |
| Call | 82900 | 260 | 220 | 1609.0 | 82444 | 1609.0 | 84509 | +763 | +0.0 | strong |
| Call | 83000 | 2900 | 2764 | 2009.3 | 83270 | 2301.1 | 85009 | +1263 | -291.8 | strong |
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2100.0 | 84702 | +956 | -498.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +1053 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +1334 | -335.1 | strong |
| Call | 83400 | 520 | 511 | 1578.4 | 83222 | 2055.2 | 84978 | +1232 | -476.8 | strong |
| Call | 83500 | 2400 | 2328 | 1977.3 | 83561 | 2023.7 | 85477 | +1731 | -46.4 | strong |
| Call | 83600 | 540 | 540 | 1550.3 | 83212 | 1273.7 | 85150 | +1404 | +276.6 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1811.3 | 85310 | +1564 | -201.4 | strong |
| Call | 83800 | 260 | 260 | 1570.1 | 83332 | 1826.3 | 85370 | +1624 | -256.2 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +1611 | +287.6 | strong |
| Call | 84000 | 3600 | 3600 | 1553.0 | 83467 | 1738.6 | 85553 | +1807 | -185.6 | strong |
| Call | 84100 | 360 | 360 | 1602.0 | 83686 | 1588.8 | 85702 | +1956 | +13.2 | strong |
| Call | 84200 | 520 | 512 | 1330.2 | 83255 | 1655.5 | 85530 | +1784 | -325.3 | strong |
| Call | 84300 | 100 | 100 | 1328.1 | 83395 | 1403.2 | 85628 | +1882 | -75.1 | strong |
| Call | 84400 | 200 | 200 | 1192.8 | 82934 | 1351.8 | 85593 | +1846 | -159.0 | strong |
| Call | 84500 | 1360 | 1360 | 1433.0 | 83575 | 1495.8 | 85933 | +2187 | -62.8 | strong |
| Call | 84600 | 220 | 220 | 1225.2 | 83341 | 1343.6 | 85825 | +2079 | -118.4 | strong |
| Call | 84700 | 560 | 560 | 1029.4 | 82892 | 853.5 | 85729 | +1983 | +175.8 | strong |
| Call | 84800 | 380 | 380 | 997.6 | 82976 | 831.0 | 85798 | +2051 | +166.6 | strong |
| Call | 84900 | 1080 | 1080 | 1049.3 | 83164 | 798.2 | 85949 | +2203 | +251.1 | strong |
| Call | 85000 | 3960 | 3960 | 1076.5 | 83376 | 1219.6 | 86077 | +2330 | -143.1 | strong |
| Put | 82500 | 1960 | 1886 | 1078.0 | 83329 | 916.0 | 81422 | +2324 | +162.0 | strong |
| Put | 82600 | 520 | 520 | 945.5 | 83795 | 982.0 | 81654 | +2092 | -36.5 | strong |
| Put | 82700 | 280 | 280 | 955.9 | 83860 | 1008.9 | 81744 | +2002 | -53.0 | strong |
| Put | 82800 | 160 | 160 | 978.1 | 83729 | 1008.9 | 81822 | +1924 | -30.8 | strong |
| Put | 82900 | 100 | 100 | 1103.6 | 83606 | 975.9 | 81796 | +1950 | +127.7 | strong |
| Put | 83000 | 9540 | 9048 | 1149.3 | 83607 | 1137.8 | 81851 | +1896 | +11.5 | strong |
| Put | 83100 | 280 | 280 | 1278.5 | 83394 | 1144.2 | 81821 | +1925 | +134.4 | strong |
| Put | 83200 | 560 | 560 | 1379.9 | 83227 | 1111.5 | 81820 | +1926 | +268.4 | strong |
| Put | 83300 | 620 | 620 | 1470.7 | 83125 | 1217.5 | 81829 | +1917 | +253.3 | strong |
| Put | 83400 | 900 | 900 | 1401.2 | 83381 | 1239.2 | 81999 | +1748 | +162.0 | strong |
| Put | 83500 | 2660 | 2386 | 1366.0 | 83592 | 1337.5 | 82134 | +1612 | +28.5 | strong |
| Put | 83600 | 1240 | 1240 | 1521.0 | 83328 | 1942.0 | 82079 | +1667 | -421.0 | strong |
| Put | 83700 | 760 | 760 | 1566.8 | 83306 | 1425.1 | 82133 | +1613 | +141.7 | strong |
| Put | 83800 | 820 | 820 | 1500.4 | 83536 | 1386.7 | 82300 | +1447 | +113.7 | strong |
| Put | 83900 | 500 | 485 | 1520.5 | 83567 | 1504.2 | 82380 | +1367 | +16.2 | strong |
| Put | 84000 | 2980 | 2980 | 1445.2 | 83851 | 1491.0 | 82555 | +1192 | -45.8 | strong |
| Put | 84100 | 1380 | 1380 | 1560.0 | 83702 | 1564.5 | 82540 | +1206 | -4.5 | strong |
| Put | 84200 | 800 | 800 | 1541.4 | 83804 | 1572.1 | 82659 | +1088 | -30.7 | strong |
| Put | 84300 | 940 | 940 | 1619.8 | 83783 | 1614.1 | 82680 | +1066 | +5.7 | strong |
| Put | 84400 | 1520 | 1520 | 1796.7 | 83562 | 1669.8 | 82603 | +1143 | +126.9 | strong |
| Put | 84500 | 8420 | 8420 | 1502.0 | 84199 | 1737.2 | 82998 | +748 | -235.2 | strong |
| Put | 84600 | 840 | 840 | 1701.1 | 83903 | 1925.5 | 82899 | +847 | -224.4 | strong |
| Put | 84700 | 560 | 560 | 1672.2 | 84036 | 1515.0 | 83028 | +719 | +157.1 | strong |
| Put | 84800 | 540 | 540 | 1673.6 | 84175 | 1586.3 | 83126 | +620 | +87.3 | strong |
| Put | 84900 | 680 | 680 | 2351.3 | 83032 | 1633.4 | 82549 | +1198 | +717.9 | strong |
| Put | 85000 | 3820 | 3820 | 2034.6 | 83695 | 1980.0 | 82965 | +781 | +54.6 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 11 | 22% | -0.43% | -1.29 to +0.22% |  | too few (9/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 5 | 40% | -0.05% | -0.22 to +0.16% |  | too few (5/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 20% | -0.20% | -0.70 to +0.25% |  | too few (5/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.43% | -0.64 to -0.22% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 2 | 0% | -0.70% | -0.73 to -0.67% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.14% | -1.14 to +0.86% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 2 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 0% | -0.76% | -0.80 to -0.73% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 0% | -1.14% | -1.14 to -1.14% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.87% | -0.87 to -0.87% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 0% | -0.21% | -0.21 to -0.21% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.86% | -0.86 to -0.86% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.04% | -0.04 to -0.04% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 0% | -0.67% | -0.67 to -0.67% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.59% | +1.59 to +1.59% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.59% | +1.59 to +1.59% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 31 | 40% | -0.05% | no clear direction |
| intraday | monthly | writers even · few weak writers | 23 | 50% | -0.09% | no clear direction |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.47% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 5 | 0% | -0.82% | too few (4/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.31% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 0% | -0.13% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.73% | too few (1/10) |
| day | monthly | writers even · few weak writers | 3 | 50% | -0.34% | too few (2/10) |
| day | weekly | writers even · few weak writers | 3 | 50% | -0.09% | too few (2/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.59% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 19 | 62% | -0.06% | no clear direction |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 0% | -0.20% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 13 | 50% | -0.01% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 5 | 0% | -0.82% | too few (4/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 4 | 0% | -0.19% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 100% | +0.31% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.73% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.13% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.73% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | -0.34% | too few (2/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.59% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.59% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 | 0% | -1.77% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
