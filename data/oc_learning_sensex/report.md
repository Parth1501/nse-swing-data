# Sensex option chain pattern log
Updated 2026-11-25 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 58 snapshots over 5 trading days
- 113 patterns logged; 50 different patterns so far

## Latest read (2026-11-25 15:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 1.0 | 83938 | 0.798 | 83800 | 81000 | 87000 | ±0.93% (83159-84718) | 22.17 |
| 2026-12-31 (monthly) | 36.0 | 83938 | 1.23 | 84000 | 83000 | 87900 | ±3.12% (81318-86558) | 12.18 |

- **Weekly, last 30 min**: `PCR up · unwinding · walls up · mid walls`. Seen 2 times before; Sensex was up after it 50% of the time, average +0.10%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 34 times before; Sensex was up after it 61% of the time, average +0.05%. Too few outcomes (18/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 16 times before; Sensex was up after it 60% of the time, average +0.05%. Too few outcomes (15/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 50% of the time, average +0.03%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 0% of the time, average -1.77%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR up · put and call writing · walls same · near put wall`. Seen 2 times before; Sensex was up after it 0% of the time, average -0.47%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 26 times before; Sensex was up after it 71% of the time, average +0.02%. History points to a bull call debit spread, ATM to about the call wall 87900.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 22 times before; Sensex was up after it 70% of the time, average +0.02%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 50% of the time, average -0.34%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 86000, strongest put writers at 82000; weakest call writers at 83500, weakest put writers at 84500. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82700 | 138740 | 132138 | 660.9 | 82828 | 1347.6 | 83361 | -577 | -686.8 | weak |
| Call | 82800 | 122660 | 113193 | 630.8 | 82868 | 1259.2 | 83431 | -507 | -628.4 | weak |
| Call | 82900 | 79200 | 73160 | 624.6 | 82943 | 1179.2 | 83525 | -414 | -554.5 | weak |
| Call | 83000 | 190900 | 171759 | 604.8 | 83013 | 1085.0 | 83605 | -333 | -480.2 | weak |
| Call | 83100 | 68760 | 66671 | 622.4 | 83150 | 1005.3 | 83722 | -216 | -382.9 | weak |
| Call | 83200 | 79920 | 78969 | 616.6 | 83268 | 913.6 | 83817 | -122 | -297.1 | weak |
| Call | 83300 | 58760 | 58208 | 577.9 | 83339 | 838.5 | 83878 | -60 | -260.6 | weak |
| Call | 83400 | 96140 | 94950 | 582.5 | 83468 | 766.5 | 83982 | +44 | -184.0 | weak |
| Call | 83500 | 281980 | 275677 | 471.4 | 83364 | 683.2 | 83971 | +33 | -211.9 | weak |
| Call | 83600 | 181440 | 180892 | 426.5 | 83466 | 623.0 | 84027 | +88 | -196.5 | weak |
| Call | 83700 | 309020 | 308416 | 423.4 | 83597 | 554.4 | 84123 | +185 | -131.0 | medium |
| Call | 83800 | 457860 | 456730 | 399.7 | 83651 | 495.0 | 84200 | +261 | -95.3 | medium |
| Call | 83900 | 500620 | 499681 | 390.5 | 83717 | 441.6 | 84291 | +352 | -51.1 | medium |
| Call | 84000 | 1119180 | 1096187 | 334.7 | 83569 | 391.8 | 84335 | +396 | -57.1 | strong |
| Call | 84100 | 423680 | 422290 | 323.7 | 83714 | 346.5 | 84424 | +485 | -22.8 | strong |
| Call | 84200 | 545720 | 544079 | 329.6 | 83786 | 305.2 | 84530 | +591 | +24.4 | strong |
| Call | 84300 | 758100 | 753959 | 314.4 | 83846 | 267.6 | 84614 | +676 | +46.8 | strong |
| Call | 84400 | 677740 | 674150 | 326.1 | 83888 | 232.8 | 84726 | +788 | +93.2 | strong |
| Call | 84500 | 1300780 | 1258369 | 277.2 | 83744 | 205.2 | 84777 | +839 | +72.0 | strong |
| Call | 84600 | 571860 | 569399 | 260.5 | 83828 | 176.9 | 84861 | +922 | +83.6 | strong |
| Call | 84700 | 571860 | 567019 | 202.4 | 83731 | 156.3 | 84902 | +964 | +46.1 | strong |
| Call | 84800 | 579580 | 573267 | 171.8 | 83650 | 131.9 | 84972 | +1034 | +39.9 | strong |
| Call | 84900 | 552800 | 544509 | 141.9 | 83720 | 113.4 | 85042 | +1104 | +28.5 | strong |
| Call | 85000 | 1957940 | 1905195 | 120.2 | 83643 | 98.6 | 85120 | +1182 | +21.6 | strong |
| Call | 85100 | 495620 | 493341 | 96.9 | 83763 | 81.5 | 85197 | +1259 | +15.4 | strong |
| Put | 82700 | 678220 | 670791 | 148.2 | 83801 | 47.4 | 82552 | +1386 | +100.8 | strong |
| Put | 82800 | 535120 | 520832 | 153.7 | 83819 | 56.2 | 82646 | +1292 | +97.4 | strong |
| Put | 82900 | 426120 | 419838 | 176.8 | 83809 | 67.7 | 82723 | +1215 | +109.2 | strong |
| Put | 83000 | 1832400 | 1768501 | 175.1 | 83846 | 81.1 | 82825 | +1113 | +94.0 | strong |
| Put | 83100 | 500880 | 499581 | 201.8 | 83793 | 95.5 | 82898 | +1040 | +106.3 | strong |
| Put | 83200 | 502040 | 501267 | 230.2 | 83800 | 111.0 | 82970 | +968 | +119.2 | strong |
| Put | 83300 | 361820 | 361286 | 278.8 | 83777 | 130.7 | 83021 | +917 | +148.1 | strong |
| Put | 83400 | 440720 | 440236 | 279.7 | 83844 | 155.6 | 83120 | +818 | +124.1 | strong |
| Put | 83500 | 1320220 | 1316642 | 304.3 | 83850 | 182.1 | 83196 | +743 | +122.2 | strong |
| Put | 83600 | 439940 | 439636 | 357.2 | 83808 | 216.9 | 83243 | +695 | +140.2 | strong |
| Put | 83700 | 425060 | 424775 | 379.2 | 83811 | 250.1 | 83321 | +617 | +129.1 | strong |
| Put | 83800 | 676360 | 676026 | 404.6 | 83845 | 292.6 | 83395 | +543 | +112.1 | strong |
| Put | 83900 | 533360 | 532923 | 410.1 | 83929 | 337.6 | 83490 | +448 | +72.5 | strong |
| Put | 84000 | 882580 | 880821 | 404.9 | 84030 | 386.2 | 83595 | +343 | +18.6 | medium |
| Put | 84100 | 255680 | 255643 | 403.6 | 84116 | 436.8 | 83696 | +242 | -33.2 | medium |
| Put | 84200 | 192580 | 192569 | 397.4 | 84221 | 497.9 | 83803 | +136 | -100.4 | weak |
| Put | 84300 | 136100 | 135989 | 409.0 | 84296 | 560.5 | 83891 | +47 | -151.5 | weak |
| Put | 84400 | 133900 | 133899 | 438.3 | 84332 | 628.0 | 83962 | -23 | -189.7 | weak |
| Put | 84500 | 196020 | 195978 | 533.7 | 84280 | 699.9 | 83966 | -28 | -166.1 | weak |
| Put | 84600 | 96020 | 96020 | 616.5 | 84266 | 775.3 | 83984 | -45 | -158.8 | weak |
| Put | 84700 | 38160 | 38160 | 861.2 | 84058 | 851.1 | 83839 | +99 | +10.1 | weak |
| Put | 84800 | 21460 | 21460 | 791.9 | 84151 | 931.0 | 84008 | -70 | -139.1 | weak |
| Put | 84900 | 22320 | 22320 | 865.5 | 84173 | 1003.3 | 84034 | -96 | -137.8 | weak |
| Put | 85000 | 103000 | 102304 | 949.0 | 84153 | 1085.1 | 84051 | -113 | -136.1 | weak |
| Put | 85100 | 5580 | 5580 | 1010.7 | 84190 | 1179.8 | 84089 | -151 | -169.1 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 84000, strongest put writers at 83000; weakest call writers at -, weakest put writers at 86000. Covers 96% of near-money call OI and 97% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +607 | -732.3 | strong |
| Call | 82800 | 1780 | 1692 | 2305.2 | 83514 | 2642.9 | 85105 | +1167 | -337.8 | strong |
| Call | 82900 | 260 | 220 | 1609.0 | 82444 | 1609.0 | 84509 | +571 | +0.0 | strong |
| Call | 83000 | 3040 | 2913 | 2053.9 | 83339 | 2457.0 | 85054 | +1116 | -403.1 | strong |
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2100.0 | 84702 | +764 | -498.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +861 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +1142 | -335.1 | strong |
| Call | 83400 | 540 | 531 | 1612.7 | 83261 | 2152.9 | 85013 | +1074 | -540.2 | strong |
| Call | 83500 | 8100 | 8028 | 2088.4 | 83831 | 2148.6 | 85588 | +1650 | -60.2 | strong |
| Call | 83600 | 540 | 540 | 1550.3 | 83212 | 1273.7 | 85150 | +1212 | +276.6 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1720.5 | 85310 | +1372 | -110.5 | strong |
| Call | 83800 | 260 | 260 | 1570.1 | 83332 | 1919.4 | 85370 | +1432 | -349.3 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +1419 | +287.6 | strong |
| Call | 84000 | 8840 | 8840 | 1729.8 | 83754 | 1858.2 | 85730 | +1792 | -128.4 | strong |
| Call | 84100 | 400 | 400 | 1610.1 | 83709 | 1682.9 | 85710 | +1772 | -72.8 | strong |
| Call | 84200 | 400 | 394 | 1330.2 | 83255 | 1724.8 | 85530 | +1592 | -394.5 | strong |
| Call | 84300 | 120 | 120 | 1460.9 | 83610 | 1671.1 | 85761 | +1823 | -210.2 | strong |
| Call | 84400 | 200 | 200 | 1192.8 | 82934 | 1351.8 | 85593 | +1655 | -159.0 | strong |
| Call | 84500 | 4440 | 4440 | 1509.7 | 83784 | 1594.2 | 86010 | +2071 | -84.5 | strong |
| Call | 84600 | 220 | 220 | 1225.2 | 83341 | 1343.6 | 85825 | +1887 | -118.4 | strong |
| Call | 84700 | 560 | 560 | 1029.4 | 82892 | 853.5 | 85729 | +1791 | +175.8 | strong |
| Call | 84800 | 380 | 380 | 997.6 | 82976 | 831.0 | 85798 | +1859 | +166.6 | strong |
| Call | 84900 | 1080 | 1080 | 1049.3 | 83164 | 798.2 | 85949 | +2011 | +251.1 | strong |
| Call | 85000 | 5220 | 5220 | 1134.6 | 83515 | 1310.0 | 86135 | +2196 | -175.4 | strong |
| Call | 85100 | 320 | 320 | 929.9 | 83140 | 741.5 | 86030 | +2092 | +188.4 | strong |
| Put | 82700 | 300 | 300 | 952.8 | 83868 | 910.0 | 81747 | +2191 | +42.9 | strong |
| Put | 82800 | 220 | 220 | 960.3 | 83798 | 913.0 | 81840 | +2099 | +47.3 | strong |
| Put | 82900 | 100 | 100 | 1103.6 | 83606 | 975.9 | 81796 | +2142 | +127.7 | strong |
| Put | 83000 | 11100 | 10624 | 1127.3 | 83655 | 987.8 | 81873 | +2066 | +139.6 | strong |
| Put | 83100 | 280 | 280 | 1278.5 | 83394 | 1009.0 | 81821 | +2117 | +269.6 | strong |
| Put | 83200 | 560 | 560 | 1379.9 | 83227 | 1111.5 | 81820 | +2118 | +268.4 | strong |
| Put | 83300 | 600 | 600 | 1470.7 | 83125 | 1066.3 | 81829 | +2109 | +404.4 | strong |
| Put | 83400 | 820 | 820 | 1397.1 | 83392 | 1119.4 | 82003 | +1935 | +277.7 | strong |
| Put | 83500 | 8040 | 7770 | 1224.2 | 83841 | 1157.2 | 82276 | +1662 | +67.0 | strong |
| Put | 83600 | 1200 | 1200 | 1521.0 | 83328 | 1268.0 | 82079 | +1859 | +253.0 | strong |
| Put | 83700 | 760 | 760 | 1566.8 | 83306 | 1223.9 | 82133 | +1805 | +342.9 | strong |
| Put | 83800 | 860 | 860 | 1494.5 | 83550 | 1400.0 | 82306 | +1633 | +94.5 | strong |
| Put | 83900 | 520 | 506 | 1512.2 | 83593 | 1450.0 | 82388 | +1550 | +62.2 | strong |
| Put | 84000 | 7240 | 7240 | 1395.4 | 83911 | 1363.1 | 82605 | +1334 | +32.3 | strong |
| Put | 84100 | 1460 | 1460 | 1545.0 | 83738 | 1397.5 | 82555 | +1383 | +147.5 | strong |
| Put | 84200 | 860 | 860 | 1537.0 | 83811 | 1478.3 | 82663 | +1275 | +58.7 | strong |
| Put | 84300 | 1020 | 1020 | 1614.7 | 83792 | 1554.3 | 82685 | +1253 | +60.4 | strong |
| Put | 84400 | 1520 | 1520 | 1796.7 | 83562 | 1535.5 | 82603 | +1335 | +261.2 | strong |
| Put | 84500 | 9160 | 9160 | 1512.1 | 84175 | 1622.5 | 82988 | +950 | -110.4 | strong |
| Put | 84600 | 920 | 920 | 1703.9 | 83894 | 1630.7 | 82896 | +1042 | +73.2 | strong |
| Put | 84700 | 560 | 560 | 1672.2 | 84036 | 1515.0 | 83028 | +910 | +157.1 | strong |
| Put | 84800 | 540 | 540 | 1673.6 | 84175 | 1586.3 | 83126 | +812 | +87.3 | strong |
| Put | 84900 | 680 | 680 | 2351.3 | 83032 | 1633.4 | 82549 | +1390 | +717.9 | strong |
| Put | 85000 | 4100 | 4100 | 2013.0 | 83742 | 1810.7 | 82987 | +951 | +202.3 | strong |
| Put | 85100 | 400 | 400 | 1964.5 | 83821 | 1646.2 | 83135 | +803 | +318.3 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 11 | 30% | -0.34% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 6 | 67% | +0.00% | -0.22 to +0.16% |  | too few (6/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 4 | 67% | +0.21% | -0.05 to +0.48% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 3 | 0% | -0.06% | -0.07 to -0.05% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.14% | -1.14 to +0.86% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 0% | -0.65% | -0.80 to -0.50% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.19% | +0.19 to +0.19% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 0% | -0.44% | -0.44 to -0.44% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 35 | 61% | +0.05% | no clear direction |
| intraday | monthly | writers even · few weak writers | 27 | 71% | +0.02% | up |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 5 | 20% | -0.61% | too few (5/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| day | weekly | writers even · few weak writers | 4 | 50% | +0.03% | too few (2/10) |
| day | monthly | writers even · few weak writers | 3 | 50% | -0.34% | too few (2/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 23 | 70% | +0.02% | no clear direction |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 67% | +0.02% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 17 | 60% | +0.05% | no clear direction |
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
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | -0.34% | too few (2/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
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
