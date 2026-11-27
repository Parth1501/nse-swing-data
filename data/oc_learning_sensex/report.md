# Sensex option chain pattern log
Updated 2026-11-27 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 79 snapshots over 7 trading days
- 154 patterns logged; 73 different patterns so far

## Latest read (2026-11-27 12:47:00)

Sensex trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-03 (weekly) | 6.1 | 83673 | 0.737 | 83900 | 80000 | 84000 | ±1.69% (82257-85089) | 16.37 |
| 2026-12-31 (monthly) | 34.1 | 83673 | 1.013 | 84100 | 83000 | 84500 | ±3.17% (81020-86327) | 12.86 |

- **Weekly, last 30 min**: `PCR flat · put and call writing · walls same · near call wall`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.05%. Too few outcomes (1/20) to trade on.
  - Writers: `call writers stronger · few weak writers`. Seen 8 times before; Sensex was up after it 25% of the time, average -0.40%. Too few outcomes (8/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 2 times before; Sensex was up after it 50% of the time, average +0.00%. Too few outcomes (2/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 47 times before; Sensex was up after it 63% of the time, average +0.02%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 6 times before; Sensex was up after it 67% of the time, average +0.03%. Too few outcomes (6/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 50% of the time, average -0.25%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-12-03

Strongest call writers at 84000, strongest put writers at 83600; weakest call writers at 81700, weakest put writers at 84400. Covers 72% of near-money call OI and 63% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82500 | 19320 | 4116 | 1511.0 | 83759 | 1407.7 | 84011 | +338 | +103.3 | medium |
| Call | 82600 | 2040 | 512 | 1573.3 | 83939 | 1329.3 | 84173 | +500 | +244.0 | strong |
| Call | 82700 | 2420 | 699 | 1334.3 | 83724 | 1269.0 | 84034 | +361 | +65.3 | medium |
| Call | 82800 | 4780 | 2340 | 1272.8 | 83732 | 1205.1 | 84073 | +400 | +67.7 | strong |
| Call | 82900 | 5900 | 3540 | 1213.1 | 83741 | 1112.3 | 84113 | +440 | +100.8 | strong |
| Call | 83000 | 67500 | 26154 | 1222.0 | 83839 | 1071.7 | 84222 | +549 | +150.3 | strong |
| Call | 83100 | 15100 | 11500 | 1092.8 | 83768 | 1001.8 | 84193 | +520 | +91.0 | strong |
| Call | 83200 | 22620 | 12679 | 1026.0 | 83751 | 949.7 | 84226 | +553 | +76.3 | strong |
| Call | 83300 | 17500 | 14067 | 988.5 | 83788 | 883.9 | 84289 | +615 | +104.7 | strong |
| Call | 83400 | 48280 | 44140 | 952.3 | 83824 | 834.0 | 84352 | +679 | +118.3 | strong |
| Call | 83500 | 166000 | 117200 | 869.2 | 83775 | 780.0 | 84369 | +696 | +89.2 | strong |
| Call | 83600 | 168240 | 160180 | 764.4 | 83694 | 727.6 | 84364 | +691 | +36.8 | strong |
| Call | 83700 | 289140 | 272420 | 729.4 | 83742 | 680.0 | 84429 | +756 | +49.4 | strong |
| Call | 83800 | 243780 | 218760 | 722.5 | 83817 | 631.1 | 84523 | +849 | +91.4 | strong |
| Call | 83900 | 240100 | 200080 | 721.1 | 83895 | 585.9 | 84621 | +948 | +135.2 | strong |
| Call | 84000 | 960880 | 670060 | 703.5 | 83945 | 544.0 | 84704 | +1030 | +159.6 | strong |
| Call | 84100 | 398680 | 319505 | 727.6 | 84080 | 505.0 | 84828 | +1154 | +222.6 | strong |
| Call | 84200 | 385420 | 323404 | 693.1 | 84098 | 466.3 | 84893 | +1220 | +226.8 | strong |
| Call | 84300 | 315240 | 180203 | 640.3 | 84079 | 431.0 | 84940 | +1267 | +209.3 | strong |
| Call | 84400 | 245420 | 155782 | 513.4 | 83900 | 394.0 | 84913 | +1240 | +119.4 | strong |
| Call | 84500 | 496840 | 271840 | 523.9 | 84023 | 366.2 | 85024 | +1351 | +157.7 | strong |
| Call | 84600 | 148100 | 107889 | 484.8 | 84022 | 336.1 | 85085 | +1412 | +148.7 | strong |
| Call | 84700 | 122840 | 93960 | 442.0 | 84007 | 308.0 | 85142 | +1469 | +134.0 | strong |
| Call | 84800 | 139280 | 115600 | 391.6 | 83972 | 281.1 | 85192 | +1518 | +110.5 | strong |
| Call | 84900 | 124000 | 100731 | 352.8 | 83940 | 260.4 | 85253 | +1580 | +92.4 | strong |
| Put | 82500 | 196440 | 89582 | 218.7 | 84027 | 282.0 | 82281 | +1392 | -63.3 | strong |
| Put | 82600 | 76940 | 57918 | 254.7 | 83962 | 310.0 | 82345 | +1328 | -55.3 | strong |
| Put | 82700 | 84880 | 62416 | 284.4 | 83926 | 337.1 | 82416 | +1258 | -52.7 | strong |
| Put | 82800 | 84000 | 63237 | 286.3 | 84014 | 365.2 | 82514 | +1160 | -78.9 | strong |
| Put | 82900 | 79880 | 67233 | 326.8 | 83956 | 400.0 | 82573 | +1100 | -73.2 | strong |
| Put | 83000 | 309440 | 175665 | 312.3 | 84100 | 433.7 | 82688 | +986 | -121.4 | strong |
| Put | 83100 | 79040 | 59392 | 349.5 | 84066 | 472.1 | 82750 | +923 | -122.7 | strong |
| Put | 83200 | 92700 | 64845 | 418.9 | 83960 | 507.4 | 82781 | +892 | -88.5 | strong |
| Put | 83300 | 84440 | 75266 | 472.6 | 83912 | 547.5 | 82827 | +846 | -74.8 | strong |
| Put | 83400 | 100520 | 78256 | 472.8 | 83986 | 593.0 | 82927 | +746 | -120.2 | strong |
| Put | 83500 | 286080 | 160751 | 519.4 | 83975 | 637.0 | 82981 | +693 | -117.6 | strong |
| Put | 83600 | 244580 | 217891 | 626.4 | 83823 | 684.9 | 82974 | +700 | -58.5 | strong |
| Put | 83700 | 212860 | 181580 | 655.0 | 83870 | 736.3 | 83045 | +628 | -81.3 | strong |
| Put | 83800 | 171460 | 131501 | 644.9 | 83962 | 788.9 | 83155 | +518 | -143.9 | strong |
| Put | 83900 | 151300 | 105018 | 656.5 | 84009 | 845.0 | 83244 | +430 | -188.6 | strong |
| Put | 84000 | 557100 | 288402 | 667.5 | 84102 | 902.2 | 83332 | +341 | -234.7 | medium |
| Put | 84100 | 222380 | 156411 | 740.9 | 84056 | 964.0 | 83359 | +314 | -223.1 | medium |
| Put | 84200 | 123820 | 93142 | 767.9 | 84096 | 1035.5 | 83432 | +241 | -267.6 | medium |
| Put | 84300 | 98900 | 29149 | 818.5 | 84099 | 1090.0 | 83482 | +192 | -271.6 | medium |
| Put | 84400 | 57400 | 14776 | 863.4 | 84106 | 1163.5 | 83537 | +137 | -300.1 | weak |
| Put | 84500 | 106000 | 2375 | 1060.0 | 83935 | 1234.7 | 83440 | +233 | -174.6 | medium |
| Put | 84600 | 19120 | 8189 | 1015.1 | 84068 | 1339.0 | 83585 | +88 | -323.9 | weak |
| Put | 84700 | 10180 | 3489 | 1049.9 | 84093 | 1390.2 | 83650 | +23 | -340.3 | weak |
| Put | 84800 | 13900 | 7874 | 1123.9 | 84088 | 1450.0 | 83676 | -3 | -326.1 | weak |
| Put | 84900 | 7140 | 3092 | 1238.4 | 84014 | 1528.5 | 83662 | +12 | -290.1 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 84500, strongest put writers at 84500; weakest call writers at -, weakest put writers at 86000. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82500 | 960 | 932 | 2523.3 | 83629 | 2387.5 | 85023 | +1350 | +135.8 | strong |
| Call | 82600 | 120 | 120 | 1778.5 | 82439 | 1789.5 | 84378 | +705 | -10.9 | strong |
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +872 | -732.3 | strong |
| Call | 82800 | 1560 | 1487 | 2302.3 | 83528 | 2251.6 | 85102 | +1429 | +50.7 | strong |
| Call | 82900 | 220 | 186 | 1609.0 | 82444 | 2407.8 | 84509 | +836 | -798.9 | strong |
| Call | 83000 | 4520 | 4402 | 2219.5 | 83644 | 2048.0 | 85219 | +1546 | +171.5 | strong |
| Call | 83100 | 600 | 567 | 1626.2 | 82730 | 2289.2 | 84726 | +1053 | -663.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +1126 | -1016.5 | strong |
| Call | 83300 | 440 | 440 | 1780.0 | 83299 | 1924.8 | 85080 | +1407 | -144.8 | strong |
| Call | 83400 | 520 | 511 | 1612.7 | 83261 | 2300.0 | 85013 | +1340 | -687.3 | strong |
| Call | 83500 | 8600 | 8530 | 2089.3 | 83847 | 1775.7 | 85589 | +1916 | +313.6 | strong |
| Call | 83600 | 680 | 680 | 1807.9 | 83682 | 1760.0 | 85408 | +1735 | +47.9 | strong |
| Call | 83700 | 940 | 940 | 1622.6 | 83373 | 1592.7 | 85323 | +1649 | +29.9 | strong |
| Call | 83800 | 280 | 280 | 1697.3 | 83653 | 1713.3 | 85497 | +1824 | -16.1 | strong |
| Call | 83900 | 480 | 463 | 1509.7 | 83437 | 1550.8 | 85410 | +1737 | -41.1 | strong |
| Call | 84000 | 16540 | 16540 | 1782.1 | 83919 | 1488.9 | 85782 | +2109 | +293.2 | strong |
| Call | 84100 | 600 | 600 | 1637.5 | 83823 | 1490.8 | 85738 | +2064 | +146.7 | strong |
| Call | 84200 | 540 | 536 | 1488.9 | 83645 | 1475.0 | 85689 | +2016 | +13.9 | strong |
| Call | 84300 | 560 | 560 | 1607.7 | 83991 | 1399.8 | 85908 | +2235 | +207.9 | strong |
| Call | 84400 | 660 | 660 | 1465.0 | 83756 | 1440.0 | 85865 | +2192 | +25.0 | strong |
| Call | 84500 | 23600 | 23600 | 1465.2 | 83934 | 1237.5 | 85965 | +2292 | +227.7 | strong |
| Call | 84600 | 580 | 580 | 1371.6 | 83791 | 1420.0 | 85972 | +2298 | -48.4 | strong |
| Call | 84700 | 560 | 560 | 1269.8 | 83636 | 1249.2 | 85970 | +2297 | +20.6 | strong |
| Call | 84800 | 320 | 320 | 1243.1 | 83586 | 1330.0 | 86043 | +2370 | -87.0 | strong |
| Call | 84900 | 500 | 500 | 1161.1 | 83466 | 1472.5 | 86061 | +2388 | -311.3 | strong |
| Put | 82500 | 2460 | 2396 | 992.5 | 83571 | 863.9 | 81508 | +2166 | +128.6 | strong |
| Put | 82600 | 800 | 800 | 919.9 | 83832 | 884.0 | 81680 | +1993 | +35.9 | strong |
| Put | 82700 | 420 | 420 | 939.7 | 83833 | 866.5 | 81760 | +1913 | +73.2 | strong |
| Put | 82800 | 520 | 520 | 931.8 | 83810 | 949.7 | 81868 | +1805 | -17.9 | strong |
| Put | 82900 | 160 | 160 | 1015.8 | 83805 | 850.0 | 81884 | +1789 | +165.8 | strong |
| Put | 83000 | 11840 | 11423 | 1075.6 | 83777 | 1015.0 | 81924 | +1749 | +60.6 | strong |
| Put | 83100 | 120 | 120 | 1163.5 | 83622 | 1085.4 | 81936 | +1737 | +78.2 | strong |
| Put | 83200 | 460 | 460 | 1379.9 | 83227 | 984.0 | 81820 | +1853 | +395.9 | strong |
| Put | 83300 | 460 | 460 | 1447.4 | 83169 | 960.5 | 81853 | +1821 | +486.9 | strong |
| Put | 83400 | 720 | 720 | 1380.2 | 83427 | 1206.5 | 82020 | +1653 | +173.8 | strong |
| Put | 83500 | 8440 | 8177 | 1213.7 | 83861 | 1202.2 | 82286 | +1387 | +11.5 | strong |
| Put | 83600 | 1100 | 1100 | 1494.4 | 83372 | 1252.0 | 82106 | +1568 | +242.4 | strong |
| Put | 83700 | 640 | 640 | 1552.3 | 83332 | 1061.0 | 82148 | +1526 | +491.4 | strong |
| Put | 83800 | 840 | 840 | 1483.9 | 83560 | 1273.3 | 82316 | +1357 | +210.6 | strong |
| Put | 83900 | 440 | 429 | 1490.9 | 83623 | 1355.0 | 82409 | +1264 | +135.9 | strong |
| Put | 84000 | 16980 | 16980 | 1286.0 | 84125 | 1429.1 | 82714 | +959 | -143.1 | strong |
| Put | 84100 | 1620 | 1620 | 1465.8 | 83866 | 1503.5 | 82634 | +1039 | -37.6 | strong |
| Put | 84200 | 1240 | 1240 | 1420.0 | 83990 | 1500.0 | 82780 | +893 | -80.0 | strong |
| Put | 84300 | 1080 | 1080 | 1586.5 | 83821 | 1501.3 | 82714 | +960 | +85.1 | strong |
| Put | 84400 | 1740 | 1740 | 1693.5 | 83714 | 1580.5 | 82707 | +967 | +113.0 | strong |
| Put | 84500 | 21500 | 21500 | 1562.5 | 83973 | 1742.1 | 82937 | +736 | -179.6 | strong |
| Put | 84600 | 940 | 940 | 1691.8 | 83913 | 1458.4 | 82908 | +765 | +233.4 | strong |
| Put | 84700 | 780 | 780 | 1645.8 | 84081 | 1584.2 | 83054 | +619 | +61.6 | strong |
| Put | 84800 | 800 | 800 | 1641.3 | 84214 | 1639.6 | 83159 | +514 | +1.7 | strong |
| Put | 84900 | 780 | 780 | 2253.9 | 83187 | 1582.0 | 82646 | +1027 | +672.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 12 | 36% | -0.30% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 11 | 60% | -0.09% | -0.55 to +0.16% |  | no clear direction |
| monthly | PCR down · put and call writing · walls same · near put wall | 5 | 75% | +0.24% | -0.05 to +0.48% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 33% | -0.02% | -0.07 to +0.06% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · near call wall | 3 | 33% | -0.04% | -0.12 to +0.05% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.24% | -1.15 to +0.66% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 0% | -0.46% | -0.80 to -0.08% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 3 | 33% | -0.35% | -0.55 to +0.01% |  | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 100% | +0.65% | +0.11 to +0.97% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | -0.06% | -1.14 to +0.86% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 2 | 50% | +0.27% | -0.12 to +0.66% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near put wall | 1 | 0% | -0.30% | -0.30 to -0.30% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.32% | +0.32 to +0.32% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls up · near put wall | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 0% | -0.30% | -0.30 to -0.30% |  | too few (1/10) |
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
| monthly | PCR down · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.46% | +0.46 to +0.46% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.46% | +0.46 to +0.46% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 48 | 63% | +0.02% | no clear direction |
| intraday | weekly | writers even · few weak writers | 47 | 60% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 25% | -0.40% | too few (8/10) |
| intraday | weekly | writers even · weak calls | 8 | 62% | -0.19% | too few (8/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | writers even · weak on both sides | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers | 5 | 50% | -0.25% | too few (4/10) |
| day | weekly | writers even · few weak writers | 4 | 67% | +0.17% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak on both sides | 1 | 0% | -0.78% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 41 | 62% | +0.01% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 29 | 59% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 18 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 67% | +0.02% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 8 | 62% | -0.19% | too few (8/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 7 | 67% | +0.03% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 6 | 17% | -0.53% | too few (6/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 3 | 50% | +0.00% | too few (2/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 3 | 100% | +0.04% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m sideways | 1 | 0% | -0.50% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 50% | -0.25% | too few (4/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.65% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 0% | -0.78% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
