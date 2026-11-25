# Sensex option chain pattern log
Updated 2026-11-25 09:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 46 snapshots over 5 trading days
- 89 patterns logged; 41 different patterns so far

## Latest read (2026-11-25 09:46:00)

Sensex trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 1.2 | 83780 | 0.842 | 83800 | 83000 | 84000 | ±1.05% (82897-84663) | 22.74 |
| 2026-12-31 (monthly) | 36.2 | 83780 | 1.144 | 83500 | 83000 | 87900 | ±4.12% (80332-87228) | 16.18 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 25 times before; Sensex was up after it 67% of the time, average +0.18%. Too few outcomes (9/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 15 times before. Too few outcomes (0/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 50% of the time, average -0.07%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 2 times before; Sensex was up after it 100% of the time, average +1.63%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR down · call writing · walls same · near put wall`. Seen 3 times before; Sensex was up after it 33% of the time, average -0.24%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 15 times before; Sensex was up after it 69% of the time, average +0.02%. Too few outcomes (13/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 1 times before; Sensex was up after it 0% of the time, average -0.10%. Too few outcomes (1/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 84000, strongest put writers at 83000; weakest call writers at 83000, weakest put writers at 85500. Covers 97% of near-money call OI and 96% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82600 | 91080 | 86986 | 653.7 | 82715 | 1327.2 | 83254 | -526 | -673.5 | weak |
| Call | 82700 | 158340 | 150386 | 644.2 | 82789 | 1260.0 | 83344 | -436 | -615.8 | weak |
| Call | 82800 | 155280 | 142965 | 617.7 | 82842 | 1150.0 | 83418 | -362 | -532.3 | weak |
| Call | 82900 | 109360 | 100927 | 622.4 | 82936 | 1047.8 | 83522 | -258 | -425.5 | weak |
| Call | 83000 | 312880 | 276862 | 577.6 | 82924 | 968.5 | 83578 | -202 | -390.9 | weak |
| Call | 83100 | 106960 | 103319 | 615.8 | 83104 | 907.4 | 83716 | -64 | -291.6 | weak |
| Call | 83200 | 132720 | 130740 | 618.8 | 83207 | 828.4 | 83819 | +39 | -209.6 | weak |
| Call | 83300 | 144360 | 142238 | 573.9 | 83218 | 749.1 | 83874 | +94 | -175.3 | weak |
| Call | 83400 | 195080 | 190045 | 581.3 | 83300 | 680.0 | 83981 | +201 | -98.7 | medium |
| Call | 83500 | 609580 | 581418 | 508.9 | 83217 | 616.5 | 84009 | +229 | -107.6 | medium |
| Call | 83600 | 282760 | 278844 | 498.0 | 83264 | 558.2 | 84098 | +318 | -60.2 | medium |
| Call | 83700 | 553580 | 547716 | 517.2 | 83644 | 500.7 | 84217 | +437 | +16.5 | strong |
| Call | 83800 | 1360860 | 1348511 | 456.0 | 83728 | 446.1 | 84256 | +476 | +9.9 | strong |
| Call | 83900 | 1159580 | 1151869 | 415.6 | 83718 | 402.6 | 84316 | +536 | +13.0 | strong |
| Call | 84000 | 2629860 | 2519676 | 329.3 | 83435 | 355.5 | 84329 | +549 | -26.2 | strong |
| Call | 84100 | 741880 | 732819 | 322.8 | 83628 | 314.5 | 84423 | +643 | +8.3 | strong |
| Call | 84200 | 980820 | 975035 | 290.0 | 83638 | 276.8 | 84490 | +710 | +13.2 | strong |
| Call | 84300 | 714400 | 705440 | 273.7 | 83659 | 244.6 | 84574 | +794 | +29.1 | strong |
| Call | 84400 | 688920 | 680660 | 247.4 | 83581 | 212.2 | 84647 | +867 | +35.1 | strong |
| Call | 84500 | 1539680 | 1460398 | 235.3 | 83501 | 184.8 | 84735 | +955 | +50.5 | strong |
| Call | 84600 | 573720 | 568631 | 205.8 | 83482 | 161.1 | 84806 | +1026 | +44.8 | strong |
| Call | 84700 | 549660 | 541953 | 166.6 | 83502 | 138.9 | 84867 | +1087 | +27.7 | strong |
| Call | 84800 | 559300 | 547907 | 129.9 | 83266 | 118.2 | 84930 | +1150 | +11.8 | strong |
| Call | 84900 | 521660 | 501859 | 108.7 | 83385 | 101.7 | 85009 | +1229 | +7.1 | strong |
| Call | 85000 | 2382880 | 2269774 | 109.5 | 83420 | 87.0 | 85110 | +1330 | +22.5 | strong |
| Put | 82600 | 674720 | 655386 | 192.0 | 83577 | 90.2 | 82408 | +1372 | +101.9 | strong |
| Put | 82700 | 493980 | 480268 | 265.1 | 83488 | 104.9 | 82435 | +1345 | +160.2 | strong |
| Put | 82800 | 599100 | 571259 | 214.9 | 83621 | 119.0 | 82585 | +1195 | +95.9 | strong |
| Put | 82900 | 370220 | 359145 | 265.9 | 83580 | 138.4 | 82634 | +1146 | +127.5 | strong |
| Put | 83000 | 2080220 | 1964260 | 223.7 | 83684 | 159.4 | 82776 | +1004 | +64.2 | strong |
| Put | 83100 | 558360 | 555442 | 238.9 | 83709 | 182.3 | 82861 | +919 | +56.5 | strong |
| Put | 83200 | 473500 | 471530 | 290.4 | 83686 | 208.8 | 82910 | +870 | +81.6 | strong |
| Put | 83300 | 428820 | 427548 | 317.1 | 83696 | 238.9 | 82983 | +797 | +78.2 | strong |
| Put | 83400 | 565160 | 563914 | 330.1 | 83728 | 273.0 | 83070 | +710 | +57.1 | strong |
| Put | 83500 | 1549800 | 1542801 | 363.2 | 83737 | 305.4 | 83137 | +643 | +57.9 | strong |
| Put | 83600 | 654980 | 654075 | 381.4 | 83761 | 346.9 | 83219 | +561 | +34.4 | strong |
| Put | 83700 | 1134540 | 1133189 | 406.8 | 83775 | 390.2 | 83293 | +487 | +16.6 | strong |
| Put | 83800 | 1644400 | 1642850 | 450.7 | 83779 | 436.8 | 83349 | +431 | +13.9 | strong |
| Put | 83900 | 938520 | 936681 | 509.6 | 83782 | 486.9 | 83390 | +390 | +22.8 | strong |
| Put | 84000 | 978520 | 971451 | 577.3 | 83774 | 546.3 | 83423 | +357 | +31.0 | medium |
| Put | 84100 | 112900 | 112706 | 731.1 | 83689 | 603.6 | 83369 | +411 | +127.5 | strong |
| Put | 84200 | 117100 | 117036 | 750.2 | 83739 | 662.0 | 83450 | +330 | +88.2 | medium |
| Put | 84300 | 60260 | 59517 | 942.9 | 83680 | 732.1 | 83357 | +423 | +210.8 | strong |
| Put | 84400 | 79700 | 79690 | 1026.5 | 83651 | 801.0 | 83374 | +407 | +225.5 | strong |
| Put | 84500 | 113740 | 113526 | 1208.4 | 83585 | 849.0 | 83292 | +488 | +359.4 | strong |
| Put | 84600 | 46740 | 46740 | 1281.0 | 83578 | 899.7 | 83319 | +461 | +381.2 | strong |
| Put | 84700 | 33400 | 33400 | 1342.8 | 83574 | 1022.5 | 83357 | +423 | +320.3 | strong |
| Put | 84800 | 6400 | 6400 | 1433.1 | 83579 | 2348.8 | 83367 | +413 | -915.8 | strong |
| Put | 84900 | 8400 | 8400 | 1453.1 | 83586 | 1136.0 | 83447 | +333 | +317.1 | medium |
| Put | 85000 | 49420 | 47630 | 1620.1 | 83473 | 1269.0 | 83380 | +400 | +351.1 | strong |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 86000, strongest put writers at 83000; weakest call writers at -, weakest put writers at -. Covers 93% of near-money call OI and 93% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82600 | 120 | 120 | 1778.5 | 82439 | 1789.5 | 84378 | +598 | -10.9 | strong |
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +766 | -732.3 | strong |
| Call | 82800 | 1600 | 1383 | 1729.5 | 82627 | 2532.8 | 84530 | +750 | -803.2 | strong |
| Call | 82900 | 260 | 220 | 1609.0 | 82444 | 1609.0 | 84509 | +729 | +0.0 | strong |
| Call | 83000 | 2800 | 2633 | 1922.9 | 83128 | 2352.1 | 84923 | +1143 | -429.2 | strong |
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2194.7 | 84702 | +922 | -592.7 | strong |
| Call | 83200 | 560 | 455 | 1599.7 | 82751 | 1444.6 | 84800 | +1020 | +155.1 | strong |
| Call | 83300 | 320 | 320 | 1633.4 | 83053 | 1999.0 | 84933 | +1153 | -365.6 | strong |
| Call | 83400 | 540 | 530 | 1578.4 | 83222 | 2069.7 | 84978 | +1198 | -491.2 | strong |
| Call | 83500 | 1260 | 1034 | 1547.2 | 82945 | 2022.8 | 85047 | +1267 | -475.6 | strong |
| Call | 83600 | 540 | 540 | 1550.3 | 83212 | 1273.7 | 85150 | +1370 | +276.6 | strong |
| Call | 83700 | 940 | 940 | 1609.9 | 83329 | 1228.9 | 85310 | +1530 | +381.0 | strong |
| Call | 83800 | 240 | 240 | 1548.8 | 83298 | 1792.1 | 85349 | +1569 | -243.3 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +1577 | +287.6 | strong |
| Call | 84000 | 2340 | 2340 | 1465.1 | 83307 | 1674.4 | 85465 | +1685 | -209.3 | strong |
| Call | 84100 | 360 | 360 | 1575.2 | 83638 | 1653.4 | 85675 | +1895 | -78.2 | strong |
| Call | 84200 | 520 | 510 | 1260.8 | 83137 | 1564.5 | 85461 | +1681 | -303.7 | strong |
| Call | 84300 | 60 | 60 | 1278.0 | 83161 | 1000.1 | 85578 | +1798 | +277.9 | strong |
| Call | 84400 | 280 | 280 | 1192.8 | 82934 | 963.2 | 85593 | +1813 | +229.6 | strong |
| Call | 84500 | 1040 | 1040 | 1074.1 | 82831 | 1408.0 | 85574 | +1794 | -333.9 | strong |
| Call | 84600 | 180 | 180 | 1198.9 | 83250 | 899.0 | 85799 | +2019 | +299.9 | strong |
| Call | 84700 | 560 | 560 | 1029.4 | 82892 | 853.5 | 85729 | +1949 | +175.8 | strong |
| Call | 84800 | 380 | 380 | 997.6 | 82976 | 831.0 | 85798 | +2018 | +166.6 | strong |
| Call | 84900 | 1080 | 1080 | 1049.3 | 83164 | 798.2 | 85949 | +2169 | +251.1 | strong |
| Call | 85000 | 2720 | 2720 | 940.2 | 83002 | 1158.9 | 85940 | +2160 | -218.7 | strong |
| Put | 82600 | 540 | 540 | 1057.4 | 83368 | 1292.2 | 81543 | +2237 | -234.9 | strong |
| Put | 82700 | 480 | 480 | 1198.0 | 83200 | 883.5 | 81502 | +2278 | +314.6 | strong |
| Put | 82800 | 640 | 640 | 1205.1 | 83249 | 939.5 | 81595 | +2185 | +265.6 | strong |
| Put | 82900 | 520 | 520 | 1295.1 | 83129 | 1486.2 | 81605 | +2175 | -191.1 | strong |
| Put | 83000 | 10200 | 9404 | 1243.3 | 83387 | 1025.0 | 81757 | +2023 | +218.3 | strong |
| Put | 83100 | 460 | 460 | 1313.5 | 83301 | 1069.0 | 81787 | +1993 | +244.5 | strong |
| Put | 83200 | 920 | 920 | 1379.9 | 83227 | 1056.8 | 81820 | +1960 | +323.1 | strong |
| Put | 83300 | 880 | 880 | 1488.2 | 83082 | 1143.5 | 81812 | +1968 | +344.7 | strong |
| Put | 83400 | 1360 | 1360 | 1401.2 | 83381 | 1179.9 | 81999 | +1781 | +221.3 | strong |
| Put | 83500 | 2120 | 1789 | 1436.6 | 83425 | 1224.5 | 82063 | +1717 | +212.1 | strong |
| Put | 83600 | 1240 | 1240 | 1521.0 | 83328 | 1942.0 | 82079 | +1701 | -421.0 | strong |
| Put | 83700 | 780 | 780 | 1590.5 | 83256 | 1281.5 | 82109 | +1671 | +309.1 | strong |
| Put | 83800 | 760 | 760 | 1526.0 | 83478 | 1655.7 | 82274 | +1506 | -129.6 | strong |
| Put | 83900 | 440 | 425 | 1519.5 | 83554 | 1325.8 | 82381 | +1399 | +193.6 | strong |
| Put | 84000 | 2240 | 2240 | 1579.8 | 83585 | 1421.3 | 82420 | +1360 | +158.5 | strong |
| Put | 84100 | 1100 | 1100 | 1608.2 | 83586 | 1386.8 | 82492 | +1288 | +221.4 | strong |
| Put | 84200 | 440 | 440 | 1541.5 | 83800 | 1625.6 | 82659 | +1121 | -84.1 | strong |
| Put | 84300 | 600 | 600 | 1651.7 | 83738 | 1954.8 | 82648 | +1132 | -303.1 | strong |
| Put | 84400 | 1240 | 1240 | 1880.1 | 83402 | 1569.4 | 82520 | +1260 | +310.7 | strong |
| Put | 84500 | 1080 | 1080 | 2003.2 | 83289 | 1590.0 | 82497 | +1283 | +413.2 | strong |
| Put | 84600 | 400 | 400 | 1820.1 | 83706 | 1656.2 | 82780 | +1000 | +164.0 | strong |
| Put | 84700 | 120 | 120 | 1959.9 | 83572 | 1775.1 | 82740 | +1040 | +184.8 | strong |
| Put | 84800 | 100 | 100 | 2170.5 | 83203 | 2170.5 | 82630 | +1151 | +0.0 | strong |
| Put | 84900 | 720 | 720 | 2447.0 | 82913 | 1882.1 | 82453 | +1327 | +564.9 | strong |
| Put | 85000 | 2080 | 2080 | 2235.5 | 83310 | 1843.8 | 82764 | +1016 | +391.8 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 9 | 25% | -0.43% | -1.29 to +0.22% |  | too few (8/10) |
| monthly | PCR down · call writing · walls same · near put wall | 4 | 33% | -0.24% | -0.70 to +0.25% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 4 | 50% | -0.03% | -0.22 to +0.16% |  | too few (4/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 2 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.14% | -1.14 to +0.86% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 2 | 0% | -0.43% | -0.64 to -0.22% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 0% | -1.14% | -1.14 to -1.14% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 0% | -0.80% | -0.80 to -0.80% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.63% | +1.63 to +1.63% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.63% | +1.63 to +1.63% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 26 | 67% | +0.18% | too few (9/10) |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | writers even · few weak writers | 16 | 69% | +0.02% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 4 | 0% | -0.82% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 0% | -0.10% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers | 4 | 50% | -0.07% | too few (2/10) |
| day | monthly | writers even · few weak writers | 3 | 50% | -0.34% | too few (2/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.63% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 16 |  |  | too few (0/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 14 | 75% | +0.03% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 10 | 67% | +0.18% | too few (9/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 4 | 0% | -0.82% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 0% | -0.10% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.10% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 3 | 100% | +1.63% | too few (1/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.63% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.34% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
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
