# Sensex option chain pattern log
Updated 2026-11-23 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 18 snapshots over 3 trading days
- 33 patterns logged; 24 different patterns so far

## Latest read (2026-11-23 09:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 3.2 | 83520 | 0.872 | 83500 | 80000 | 88000 | ±1.66% (82137-84903) | 22.02 |
| 2026-12-31 (monthly) | 38.2 | 83517 | 1.289 | 83000 | 83000 | 87900 | ±4.16% (80047-86988) | 15.91 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 7 times before; Sensex was up after it 100% of the time, average +0.84%. Too few outcomes (6/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 7 times before; Sensex was up after it 100% of the time, average +0.84%. Too few outcomes (6/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Sensex was up after it 0% of the time, average -0.48%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 0% of the time, average -0.48%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR up · put writing · walls same · near put wall`. Seen 3 times before; Sensex was up after it 100% of the time, average +0.20%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 13 times before; Sensex was up after it 82% of the time, average +0.27%. Too few outcomes (11/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 13 times before; Sensex was up after it 82% of the time, average +0.27%. Too few outcomes (11/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Sensex was up after it 50% of the time, average +0.30%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 50% of the time, average +0.30%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 84500, strongest put writers at 81500; weakest call writers at 83000, weakest put writers at 84800. Covers 85% of near-money call OI and 82% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82300 | 26840 | 1913 | 1038.4 | 83023 | 1497.0 | 83338 | -182 | -458.6 | weak |
| Call | 82400 | 21420 | 4384 | 976.5 | 83023 | 1442.3 | 83376 | -144 | -465.9 | weak |
| Call | 82500 | 130560 | 49609 | 908.5 | 83022 | 1333.0 | 83408 | -112 | -424.5 | weak |
| Call | 82600 | 31960 | 24100 | 848.4 | 83024 | 1297.3 | 83448 | -72 | -448.9 | weak |
| Call | 82700 | 66580 | 52329 | 807.7 | 83044 | 1178.0 | 83508 | -12 | -370.3 | weak |
| Call | 82800 | 96860 | 70353 | 738.7 | 83030 | 1108.5 | 83539 | +18 | -369.8 | weak |
| Call | 82900 | 72700 | 51486 | 704.0 | 83043 | 1054.5 | 83604 | +84 | -350.6 | weak |
| Call | 83000 | 204180 | 120286 | 662.5 | 83020 | 975.0 | 83662 | +142 | -312.6 | weak |
| Call | 83100 | 71600 | 63259 | 633.5 | 83044 | 918.0 | 83734 | +213 | -284.5 | medium |
| Call | 83200 | 93060 | 87775 | 701.9 | 83263 | 858.3 | 83902 | +382 | -156.4 | strong |
| Call | 83300 | 79700 | 74940 | 643.5 | 83245 | 800.0 | 83944 | +423 | -156.5 | strong |
| Call | 83400 | 121660 | 112309 | 662.7 | 83367 | 746.5 | 84063 | +542 | -83.8 | strong |
| Call | 83500 | 295140 | 253344 | 638.4 | 83413 | 694.9 | 84138 | +618 | -56.5 | strong |
| Call | 83600 | 167100 | 161622 | 611.2 | 83447 | 648.6 | 84211 | +691 | -37.4 | strong |
| Call | 83700 | 179500 | 172080 | 601.2 | 83512 | 603.9 | 84301 | +781 | -2.6 | strong |
| Call | 83800 | 199940 | 185032 | 563.1 | 83524 | 561.0 | 84363 | +843 | +2.1 | strong |
| Call | 83900 | 177660 | 168742 | 539.5 | 83556 | 520.0 | 84439 | +919 | +19.5 | strong |
| Call | 84000 | 564700 | 452719 | 424.6 | 83383 | 480.0 | 84425 | +904 | -55.4 | strong |
| Call | 84100 | 143380 | 134090 | 413.4 | 83444 | 444.9 | 84513 | +993 | -31.5 | strong |
| Call | 84200 | 199140 | 192830 | 402.1 | 83501 | 410.3 | 84602 | +1082 | -8.2 | strong |
| Call | 84300 | 222820 | 213416 | 350.1 | 83455 | 381.4 | 84650 | +1130 | -31.3 | strong |
| Call | 84400 | 230040 | 221494 | 338.9 | 83484 | 352.4 | 84739 | +1219 | -13.4 | strong |
| Call | 84500 | 674440 | 589561 | 355.1 | 83706 | 325.6 | 84855 | +1335 | +29.6 | strong |
| Call | 84600 | 259520 | 254029 | 290.5 | 83496 | 299.4 | 84890 | +1370 | -9.0 | strong |
| Call | 84700 | 163860 | 155092 | 262.5 | 83492 | 275.4 | 84963 | +1442 | -12.9 | strong |
| Put | 82300 | 122280 | 88249 | 293.7 | 83409 | 263.9 | 82006 | +1514 | +29.8 | strong |
| Put | 82400 | 136920 | 95367 | 415.0 | 83107 | 289.0 | 81985 | +1535 | +126.0 | strong |
| Put | 82500 | 389600 | 205985 | 475.4 | 83036 | 311.9 | 82025 | +1496 | +163.4 | strong |
| Put | 82600 | 145720 | 117155 | 487.1 | 83104 | 341.1 | 82113 | +1407 | +146.0 | strong |
| Put | 82700 | 196900 | 170824 | 465.6 | 83253 | 370.0 | 82234 | +1286 | +95.6 | strong |
| Put | 82800 | 258340 | 191051 | 593.2 | 83034 | 401.1 | 82207 | +1313 | +192.1 | strong |
| Put | 82900 | 128980 | 104944 | 612.5 | 83088 | 434.6 | 82288 | +1233 | +177.9 | strong |
| Put | 83000 | 430220 | 278665 | 625.1 | 83104 | 469.4 | 82375 | +1145 | +155.7 | strong |
| Put | 83100 | 143460 | 135942 | 609.1 | 83236 | 509.9 | 82491 | +1029 | +99.2 | strong |
| Put | 83200 | 211420 | 205453 | 624.5 | 83320 | 549.4 | 82575 | +945 | +75.1 | strong |
| Put | 83300 | 146240 | 141437 | 637.3 | 83395 | 595.1 | 82663 | +858 | +42.2 | strong |
| Put | 83400 | 146220 | 142755 | 661.5 | 83452 | 638.8 | 82739 | +782 | +22.6 | strong |
| Put | 83500 | 368360 | 354803 | 652.7 | 83549 | 688.0 | 82847 | +673 | -35.3 | strong |
| Put | 83600 | 180380 | 177903 | 681.6 | 83597 | 739.4 | 82918 | +602 | -57.8 | strong |
| Put | 83700 | 154940 | 152055 | 653.8 | 83699 | 793.2 | 83046 | +474 | -139.4 | strong |
| Put | 83800 | 187400 | 184573 | 650.0 | 83771 | 850.2 | 83150 | +370 | -200.2 | medium |
| Put | 83900 | 154480 | 151891 | 682.1 | 83798 | 911.5 | 83218 | +302 | -229.3 | medium |
| Put | 84000 | 242280 | 228718 | 798.6 | 83727 | 971.8 | 83201 | +319 | -173.2 | medium |
| Put | 84100 | 55260 | 54822 | 945.9 | 83614 | 1030.0 | 83154 | +366 | -84.1 | medium |
| Put | 84200 | 46700 | 46594 | 1005.7 | 83630 | 1100.0 | 83194 | +326 | -94.3 | medium |
| Put | 84300 | 52260 | 51192 | 1083.0 | 83615 | 1169.7 | 83217 | +303 | -86.7 | medium |
| Put | 84400 | 81680 | 81662 | 1199.7 | 83553 | 1230.4 | 83200 | +320 | -30.7 | medium |
| Put | 84500 | 184260 | 183844 | 1279.5 | 83547 | 1301.8 | 83220 | +300 | -22.2 | medium |
| Put | 84600 | 65360 | 65360 | 1360.0 | 83540 | 1380.9 | 83240 | +280 | -20.9 | medium |
| Put | 84700 | 32760 | 32760 | 1409.2 | 83544 | 1431.7 | 83291 | +229 | -22.5 | medium |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 83000, strongest put writers at 83000; weakest call writers at -, weakest put writers at -. Covers 82% of near-money call OI and 84% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82300 | 100 | 100 | 2134.5 | 83023 | 2134.5 | 84434 | +917 | +0.0 | strong |
| Call | 82400 | 100 | 100 | 2074.4 | 83023 | 2074.4 | 84474 | +957 | +0.0 | strong |
| Call | 82800 | 320 | 100 | 1766.7 | 83023 | 1766.7 | 84567 | +1049 | +0.0 | strong |
| Call | 83000 | 3260 | 2906 | 2176.3 | 83599 | 2192.8 | 85176 | +1659 | -16.5 | strong |
| Call | 83100 | 80 | 40 | 1607.8 | 83023 | 1786.2 | 84708 | +1190 | -178.4 | strong |
| Call | 83200 | 120 | 15 | 2180.4 | 83732 | 2129.1 | 85380 | +1863 | +51.4 | strong |
| Call | 83300 | 40 | 40 | 1653.3 | 83117 | 1653.3 | 84953 | +1436 | +0.0 | strong |
| Call | 83400 | 120 | 109 | 1484.0 | 83023 | 2050.1 | 84884 | +1367 | -566.1 | strong |
| Call | 83500 | 740 | 403 | 1683.2 | 83274 | 2087.1 | 85183 | +1666 | -403.9 | strong |
| Call | 83600 | 260 | 260 | 1610.9 | 83438 | 1627.2 | 85211 | +1694 | -16.3 | strong |
| Call | 83700 | 360 | 360 | 1620.8 | 83414 | 1957.8 | 85321 | +1803 | -337.0 | strong |
| Call | 83800 | 200 | 200 | 1589.6 | 83443 | 1589.3 | 85390 | +1872 | +0.3 | strong |
| Call | 83900 | 640 | 604 | 1444.1 | 83262 | 1522.5 | 85344 | +1827 | -78.4 | strong |
| Call | 84000 | 1840 | 1840 | 1524.9 | 83460 | 1621.2 | 85525 | +2008 | -96.3 | strong |
| Call | 84100 | 140 | 140 | 1489.5 | 83469 | 1547.0 | 85590 | +2072 | -57.5 | strong |
| Call | 84200 | 720 | 703 | 1320.8 | 83321 | 1580.3 | 85521 | +2003 | -259.6 | strong |
| Call | 84300 | 40 | 40 | 1278.3 | 83117 | 1528.3 | 85578 | +2061 | -250.0 | strong |
| Call | 84400 | 400 | 400 | 1461.7 | 83517 | 1461.7 | 85862 | +2344 | +0.0 | strong |
| Call | 84500 | 820 | 820 | 1487.2 | 83829 | 1401.7 | 85987 | +2470 | +85.5 | strong |
| Call | 84600 | 160 | 160 | 1196.3 | 83470 | 1216.8 | 85796 | +2279 | -20.5 | strong |
| Call | 84700 | 360 | 360 | 1227.4 | 83402 | 1322.5 | 85927 | +2410 | -95.1 | strong |
| Put | 82300 | 800 | 800 | 926.9 | 83582 | 936.3 | 81373 | +2144 | -9.4 | strong |
| Put | 82400 | 1140 | 1140 | 918.4 | 83738 | 967.5 | 81482 | +2036 | -49.0 | strong |
| Put | 82500 | 520 | 352 | 898.8 | 83860 | 1011.4 | 81601 | +1916 | -112.6 | strong |
| Put | 82600 | 180 | 180 | 900.6 | 83867 | 1049.8 | 81699 | +1818 | -149.1 | strong |
| Put | 82700 | 160 | 160 | 1145.6 | 83395 | 1084.7 | 81554 | +1963 | +61.0 | strong |
| Put | 82800 | 520 | 520 | 1180.6 | 83375 | 1110.4 | 81619 | +1898 | +70.2 | strong |
| Put | 82900 | 180 | 180 | 1342.9 | 83166 | 1263.3 | 81557 | +1960 | +79.5 | strong |
| Put | 83000 | 9600 | 8725 | 1264.0 | 83348 | 1189.8 | 81736 | +1781 | +74.1 | strong |
| Put | 83100 | 480 | 480 | 1314.1 | 83314 | 1205.1 | 81786 | +1731 | +109.0 | strong |
| Put | 83200 | 560 | 560 | 1402.2 | 83208 | 1242.8 | 81798 | +1720 | +159.4 | strong |
| Put | 83300 | 440 | 440 | 1514.9 | 83101 | 1379.7 | 81785 | +1732 | +135.3 | strong |
| Put | 83400 | 780 | 780 | 1469.4 | 83277 | 1340.0 | 81931 | +1587 | +129.4 | strong |
| Put | 83500 | 1820 | 1402 | 1498.2 | 83329 | 1383.3 | 82002 | +1516 | +114.9 | strong |
| Put | 83600 | 1020 | 1020 | 1523.9 | 83329 | 1424.8 | 82076 | +1441 | +99.2 | strong |
| Put | 83700 | 500 | 500 | 1559.8 | 83353 | 1551.0 | 82140 | +1377 | +8.8 | strong |
| Put | 83800 | 520 | 520 | 1469.3 | 83587 | 1493.0 | 82331 | +1187 | -23.7 | strong |
| Put | 83900 | 280 | 265 | 1435.8 | 83751 | 1325.2 | 82464 | +1053 | +110.5 | strong |
| Put | 84000 | 880 | 880 | 1520.7 | 83670 | 1614.4 | 82479 | +1038 | -93.7 | strong |
| Put | 84100 | 760 | 760 | 1553.1 | 83731 | 1661.0 | 82547 | +970 | -107.9 | strong |
| Put | 84200 | 440 | 440 | 1541.5 | 83800 | 1625.6 | 82659 | +859 | -84.1 | strong |
| Put | 84300 | 540 | 540 | 1618.0 | 83777 | 1673.5 | 82682 | +835 | -55.6 | strong |
| Put | 84400 | 960 | 960 | 1657.6 | 83810 | 1747.5 | 82742 | +775 | -89.9 | strong |
| Put | 84500 | 460 | 460 | 1683.1 | 83808 | 2004.2 | 82817 | +700 | -321.1 | strong |
| Put | 84600 | 400 | 400 | 1820.1 | 83706 | 1648.8 | 82780 | +737 | +171.3 | strong |
| Put | 84700 | 220 | 220 | 1959.9 | 83572 | 1820.5 | 82740 | +777 | +139.4 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls same · near put wall | 4 | 100% | +0.20% | +0.17 to +0.22% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 3 | 67% | +0.04% | -0.07 to +0.16% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.86% | +0.86 to +0.86% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.48% | -0.48 to -0.48% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 14 | 82% | +0.27% | up |
| intraday | weekly | writers even · few weak writers | 8 | 100% | +0.84% | too few (6/10) |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.03% | too few (7/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.91% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts | 1 | 100% | +1.66% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 3 | 50% | +0.30% | too few (2/10) |
| day | weekly | writers even · few weak writers | 2 | 0% | -0.48% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 14 | 82% | +0.27% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 8 | 100% | +0.84% | too few (6/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.03% | too few (7/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.91% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | +0.30% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 0% | -0.48% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
