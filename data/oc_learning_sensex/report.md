# Sensex option chain pattern log
Updated 2026-11-25 11:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 50 snapshots over 5 trading days
- 97 patterns logged; 44 different patterns so far

## Latest read (2026-11-25 11:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 1.2 | 84473 | 0.966 | 84100 | 83000 | 87000 | ±1.05% (83583-85363) | 23.33 |
| 2026-12-31 (monthly) | 36.2 | 84482 | 1.158 | 84100 | 83000 | 87900 | ±3.89% (81199-87764) | 15.31 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 28 times before; Sensex was up after it 75% of the time, average +0.30%. Too few outcomes (12/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 10 times before; Sensex was up after it 67% of the time, average +0.18%. Too few outcomes (9/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · mid walls`. Seen 2 times before; Sensex was up after it 100% of the time, average +2.48%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 50% of the time, average +0.36%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 0% of the time, average -1.77%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR down · unwinding · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 18 times before; Sensex was up after it 81% of the time, average +0.20%. Too few outcomes (16/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 14 times before; Sensex was up after it 75% of the time, average +0.03%. Too few outcomes (12/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 87000, strongest put writers at 83000; weakest call writers at 84000, weakest put writers at 85500. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83300 | 71840 | 70784 | 573.9 | 83218 | 1398.3 | 83874 | -599 | -824.5 | weak |
| Call | 83400 | 95880 | 93405 | 581.3 | 83300 | 1311.7 | 83981 | -491 | -730.4 | weak |
| Call | 83500 | 427840 | 408610 | 512.9 | 83236 | 1219.2 | 84013 | -460 | -706.4 | weak |
| Call | 83600 | 157700 | 155833 | 511.4 | 83352 | 1141.0 | 84111 | -361 | -629.6 | weak |
| Call | 83700 | 255320 | 253099 | 519.6 | 83684 | 1056.2 | 84220 | -253 | -536.6 | weak |
| Call | 83800 | 449760 | 446388 | 459.1 | 83751 | 972.9 | 84259 | -214 | -513.8 | weak |
| Call | 83900 | 523900 | 521273 | 417.3 | 83754 | 897.0 | 84317 | -155 | -479.6 | weak |
| Call | 84000 | 1105400 | 1059284 | 329.5 | 83437 | 823.5 | 84330 | -143 | -494.0 | weak |
| Call | 84100 | 381680 | 378119 | 333.2 | 83700 | 749.9 | 84433 | -40 | -416.7 | weak |
| Call | 84200 | 664660 | 661230 | 294.4 | 83675 | 681.7 | 84494 | +22 | -387.3 | weak |
| Call | 84300 | 689000 | 681578 | 271.2 | 83688 | 619.6 | 84571 | +98 | -348.5 | weak |
| Call | 84400 | 984440 | 977982 | 335.7 | 83886 | 557.1 | 84736 | +263 | -221.4 | medium |
| Call | 84500 | 1867160 | 1795410 | 277.1 | 83702 | 499.5 | 84777 | +304 | -222.4 | medium |
| Call | 84600 | 757600 | 753015 | 252.0 | 83730 | 447.2 | 84852 | +379 | -195.2 | medium |
| Call | 84700 | 730160 | 722491 | 210.7 | 83711 | 398.9 | 84911 | +438 | -188.2 | strong |
| Call | 84800 | 741220 | 730718 | 166.5 | 83552 | 353.4 | 84966 | +494 | -186.8 | strong |
| Call | 84900 | 657460 | 642504 | 150.8 | 83710 | 311.4 | 85051 | +578 | -160.7 | strong |
| Call | 85000 | 2733160 | 2633718 | 128.6 | 83607 | 273.4 | 85129 | +656 | -144.7 | strong |
| Call | 85100 | 562220 | 557897 | 94.4 | 83721 | 239.2 | 85194 | +722 | -144.7 | strong |
| Call | 85200 | 670320 | 664930 | 108.8 | 83769 | 207.8 | 85309 | +836 | -99.0 | strong |
| Call | 85300 | 607800 | 605888 | 72.9 | 83694 | 180.4 | 85373 | +900 | -107.5 | strong |
| Call | 85400 | 540900 | 536826 | 68.5 | 83513 | 155.8 | 85469 | +996 | -87.3 | strong |
| Call | 85500 | 2206340 | 2170655 | 49.2 | 83351 | 133.8 | 85549 | +1077 | -84.5 | strong |
| Call | 85600 | 615940 | 613269 | 52.5 | 83637 | 114.5 | 85652 | +1180 | -62.0 | strong |
| Call | 85700 | 782700 | 780400 | 50.9 | 83836 | 98.2 | 85751 | +1278 | -47.3 | strong |
| Put | 83300 | 697120 | 695875 | 254.4 | 83839 | 85.5 | 83046 | +1427 | +168.9 | strong |
| Put | 83400 | 776820 | 775574 | 277.4 | 83879 | 97.8 | 83123 | +1350 | +179.7 | strong |
| Put | 83500 | 2282680 | 2275681 | 312.9 | 83844 | 112.2 | 83187 | +1286 | +200.7 | strong |
| Put | 83600 | 835280 | 834524 | 331.1 | 83859 | 127.6 | 83269 | +1204 | +203.5 | strong |
| Put | 83700 | 1245160 | 1244025 | 387.0 | 83810 | 144.8 | 83313 | +1160 | +242.2 | strong |
| Put | 83800 | 1967080 | 1965622 | 424.8 | 83826 | 164.4 | 83375 | +1098 | +260.4 | strong |
| Put | 83900 | 1491920 | 1490266 | 425.6 | 83925 | 187.3 | 83474 | +998 | +238.2 | strong |
| Put | 84000 | 2687300 | 2680231 | 400.9 | 84058 | 213.1 | 83599 | +874 | +187.8 | strong |
| Put | 84100 | 1019740 | 1019546 | 374.0 | 84183 | 241.8 | 83726 | +747 | +132.2 | strong |
| Put | 84200 | 898280 | 898216 | 401.7 | 84222 | 273.6 | 83798 | +674 | +128.2 | strong |
| Put | 84300 | 877340 | 876597 | 405.1 | 84304 | 307.7 | 83895 | +578 | +97.5 | strong |
| Put | 84400 | 993500 | 993490 | 438.3 | 84332 | 347.2 | 83962 | +511 | +91.1 | strong |
| Put | 84500 | 1004620 | 1004406 | 533.2 | 84281 | 390.6 | 83967 | +506 | +142.7 | strong |
| Put | 84600 | 253540 | 253540 | 615.7 | 84268 | 436.8 | 83984 | +488 | +178.9 | strong |
| Put | 84700 | 86880 | 86880 | 860.6 | 84059 | 487.6 | 83839 | +633 | +373.0 | strong |
| Put | 84800 | 77020 | 77020 | 703.7 | 84268 | 542.1 | 84096 | +376 | +161.6 | medium |
| Put | 84900 | 42620 | 42620 | 867.4 | 84174 | 601.5 | 84033 | +440 | +266.0 | strong |
| Put | 85000 | 230320 | 228530 | 926.5 | 84182 | 663.9 | 84074 | +399 | +262.6 | strong |
| Put | 85100 | 10500 | 10500 | 983.8 | 84222 | 730.2 | 84116 | +357 | +253.6 | medium |
| Put | 85200 | 10640 | 10640 | 1098.4 | 84162 | 796.3 | 84102 | +371 | +302.1 | medium |
| Put | 85300 | 17460 | 5173 | 1278.4 | 84062 | 867.9 | 84022 | +451 | +410.5 | strong |
| Put | 85400 | 5520 | 5520 | 1245.7 | 84186 | 946.0 | 84154 | +318 | +299.7 | medium |
| Put | 85500 | 37280 | 37280 | 1143.6 | 84344 | 1025.8 | 84356 | +116 | +117.8 | weak |
| Put | 85600 | 3200 | 3200 | 1337.0 | 84265 | 1090.2 | 84263 | +210 | +246.7 | medium |
| Put | 85700 | 900 | 900 | 2088.3 | 83700 | 1183.3 | 83612 | +861 | +905.0 | strong |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 87000, strongest put writers at 83000; weakest call writers at 82800, weakest put writers at -. Covers 96% of near-money call OI and 96% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +598 | -335.1 | strong |
| Call | 83400 | 540 | 530 | 1578.4 | 83222 | 2069.7 | 84978 | +497 | -491.2 | strong |
| Call | 83500 | 1400 | 1174 | 1631.0 | 83095 | 2487.8 | 85131 | +649 | -856.8 | strong |
| Call | 83600 | 540 | 540 | 1550.3 | 83212 | 1273.7 | 85150 | +668 | +276.6 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1880.9 | 85310 | +828 | -271.0 | strong |
| Call | 83800 | 240 | 240 | 1548.8 | 83298 | 1792.1 | 85349 | +867 | -243.3 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +876 | +287.6 | strong |
| Call | 84000 | 2340 | 2340 | 1478.4 | 83338 | 2159.9 | 85478 | +997 | -681.5 | strong |
| Call | 84100 | 380 | 380 | 1602.8 | 83682 | 2100.0 | 85703 | +1221 | -497.2 | strong |
| Call | 84200 | 480 | 471 | 1260.8 | 83137 | 2041.7 | 85461 | +979 | -780.9 | strong |
| Call | 84300 | 60 | 60 | 1278.0 | 83161 | 1000.1 | 85578 | +1096 | +277.9 | strong |
| Call | 84400 | 280 | 280 | 1192.8 | 82934 | 963.2 | 85593 | +1111 | +229.6 | strong |
| Call | 84500 | 1380 | 1380 | 1438.4 | 83581 | 1883.0 | 85938 | +1457 | -444.6 | strong |
| Call | 84600 | 180 | 180 | 1198.9 | 83250 | 899.0 | 85799 | +1317 | +299.9 | strong |
| Call | 84700 | 560 | 560 | 1029.4 | 82892 | 853.5 | 85729 | +1248 | +175.8 | strong |
| Call | 84800 | 380 | 380 | 997.6 | 82976 | 831.0 | 85798 | +1316 | +166.6 | strong |
| Call | 84900 | 1080 | 1080 | 1049.3 | 83164 | 798.2 | 85949 | +1467 | +251.1 | strong |
| Call | 85000 | 4000 | 4000 | 1069.1 | 83357 | 1602.5 | 86069 | +1587 | -533.4 | strong |
| Call | 85100 | 320 | 320 | 929.9 | 83140 | 741.5 | 86030 | +1548 | +188.4 | strong |
| Call | 85200 | 460 | 460 | 816.9 | 82858 | 718.1 | 86017 | +1535 | +98.8 | strong |
| Call | 85300 | 260 | 260 | 978.7 | 83594 | 1030.2 | 86279 | +1797 | -51.4 | strong |
| Call | 85400 | 800 | 800 | 892.6 | 83194 | 670.7 | 86293 | +1811 | +221.9 | strong |
| Call | 85500 | 1440 | 1440 | 957.6 | 83556 | 1352.1 | 86458 | +1976 | -394.5 | strong |
| Call | 85600 | 400 | 400 | 992.1 | 83815 | 1251.8 | 86592 | +2110 | -259.8 | strong |
| Call | 85700 | 1640 | 1640 | 822.6 | 83328 | 586.5 | 86523 | +2041 | +236.1 | strong |
| Put | 83300 | 720 | 720 | 1488.2 | 83082 | 977.6 | 81812 | +2670 | +510.6 | strong |
| Put | 83400 | 960 | 960 | 1401.2 | 83381 | 1006.6 | 81999 | +2483 | +394.6 | strong |
| Put | 83500 | 2160 | 1862 | 1402.2 | 83497 | 1012.0 | 82098 | +2384 | +390.2 | strong |
| Put | 83600 | 1240 | 1240 | 1521.0 | 83328 | 1942.0 | 82079 | +2403 | -421.0 | strong |
| Put | 83700 | 840 | 840 | 1566.8 | 83306 | 1177.0 | 82133 | +2349 | +389.8 | strong |
| Put | 83800 | 820 | 820 | 1503.2 | 83531 | 1150.0 | 82297 | +2185 | +353.2 | strong |
| Put | 83900 | 440 | 425 | 1519.5 | 83554 | 1325.8 | 82381 | +2101 | +193.6 | strong |
| Put | 84000 | 4280 | 4280 | 1430.1 | 83886 | 1195.6 | 82570 | +1912 | +234.5 | strong |
| Put | 84100 | 1340 | 1340 | 1564.0 | 83685 | 1353.7 | 82536 | +1946 | +210.4 | strong |
| Put | 84200 | 520 | 520 | 1522.9 | 83839 | 1400.0 | 82677 | +1805 | +122.9 | strong |
| Put | 84300 | 720 | 720 | 1627.6 | 83780 | 1311.9 | 82672 | +1809 | +315.7 | strong |
| Put | 84400 | 1460 | 1460 | 1806.0 | 83550 | 1352.1 | 82594 | +1888 | +453.9 | strong |
| Put | 84500 | 8920 | 8920 | 1480.4 | 84239 | 1399.5 | 83020 | +1462 | +81.0 | strong |
| Put | 84600 | 780 | 780 | 1696.2 | 83907 | 1481.0 | 82904 | +1578 | +215.2 | strong |
| Put | 84700 | 560 | 560 | 1672.2 | 84036 | 1515.0 | 83028 | +1454 | +157.1 | strong |
| Put | 84800 | 420 | 420 | 1701.5 | 84137 | 1547.0 | 83098 | +1383 | +154.5 | strong |
| Put | 84900 | 720 | 720 | 2447.0 | 82913 | 1882.1 | 82453 | +2029 | +564.9 | strong |
| Put | 85000 | 2320 | 2320 | 2143.9 | 83474 | 1583.0 | 82856 | +1626 | +561.0 | strong |
| Put | 85100 | 340 | 340 | 2020.7 | 83734 | 1636.3 | 83079 | +1403 | +384.4 | strong |
| Put | 85200 | 620 | 620 | 2141.7 | 83689 | 2120.6 | 83058 | +1424 | +21.1 | strong |
| Put | 85300 | 1080 | 1080 | 2085.3 | 83780 | 2085.3 | 83215 | +1267 | +0.0 | strong |
| Put | 85500 | 2420 | 2420 | 2432.6 | 83462 | 1842.5 | 83067 | +1414 | +590.0 | strong |
| Put | 85700 | 800 | 800 | 2001.8 | 84360 | 2001.8 | 83698 | +784 | +0.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 10 | 33% | -0.34% | -1.29 to +0.43% |  | too few (9/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 5 | 60% | +0.13% | -0.22 to +0.74% |  | too few (5/10) |
| monthly | PCR down · call writing · walls same · near put wall | 4 | 50% | +0.03% | -0.70 to +0.84% |  | too few (4/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 33% | -0.15% | -0.64 to +0.42% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 2 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 50% | -0.33% | -0.80 to +0.13% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.14% | -1.14 to +0.86% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 0% | -1.14% | -1.14 to -1.14% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.83% | +0.83 to +0.83% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.73% | +0.73 to +0.73% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +2.48% | +2.48 to +2.48% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +2.48% | +2.48 to +2.48% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 29 | 75% | +0.30% | no clear direction |
| intraday | monthly | writers even · few weak writers | 19 | 81% | +0.20% | up |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 30% | -0.38% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 4 | 0% | -0.82% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.73% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 100% | +0.13% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers | 4 | 50% | +0.36% | too few (2/10) |
| day | monthly | writers even · few weak writers | 3 | 50% | -0.34% | too few (2/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +2.48% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 100% | +0.66% | too few (3/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 15 | 75% | +0.03% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 11 | 67% | +0.18% | too few (9/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.22% | too few (7/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 4 | 100% | +0.69% | too few (4/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 4 | 0% | -0.82% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 100% | +0.14% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.73% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.13% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | -0.34% | too few (2/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +2.48% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +2.48% | too few (1/10) |
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
