# Sensex option chain pattern log
Updated 2026-11-26 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 67 snapshots over 6 trading days
- 131 patterns logged; 61 different patterns so far

## Latest read (2026-11-26 13:50:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 0.1 | 84062 | 0.901 | 84100 | 84000 | 84500 | ±0.33% (83781-84343) | 30.12 |
| 2026-12-31 (monthly) | 35.1 | 84062 | 1.066 | 84000 | 84000 | 86000 | ±3.7% (80950-87173) | 14.84 |

- **Weekly, last 30 min**: `PCR down · call writing · walls down · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 42 times before; Sensex was up after it 52% of the time, average +0.00%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 24 times before; Sensex was up after it 50% of the time, average -0.00%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 67% of the time, average +0.07%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 50% of the time, average -0.81%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · near put wall`. Seen 4 times before; Sensex was up after it 67% of the time, average +0.21%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 35 times before; Sensex was up after it 59% of the time, average -0.02%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 31 times before; Sensex was up after it 57% of the time, average -0.03%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 67% of the time, average -0.18%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Sensex was up after it 67% of the time, average -0.18%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 84500, strongest put writers at 83500; weakest call writers at 84000, weakest put writers at 84200. Covers 100% of near-money call OI and 100% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82900 | 47540 | 43915 | 624.6 | 82943 | 1117.8 | 83525 | -537 | -493.2 | weak |
| Call | 83000 | 158680 | 143519 | 628.7 | 83065 | 1007.1 | 83629 | -433 | -378.4 | weak |
| Call | 83100 | 43640 | 42471 | 661.0 | 83262 | 927.0 | 83761 | -301 | -266.0 | weak |
| Call | 83200 | 48660 | 48081 | 616.6 | 83268 | 819.1 | 83817 | -245 | -202.6 | weak |
| Call | 83300 | 39920 | 39605 | 600.5 | 83456 | 718.0 | 83901 | -161 | -117.5 | weak |
| Call | 83400 | 70740 | 70016 | 582.7 | 83553 | 629.4 | 83983 | -79 | -46.7 | weak |
| Call | 83500 | 194340 | 191371 | 482.1 | 83538 | 537.5 | 83982 | -80 | -55.5 | weak |
| Call | 83600 | 153760 | 153454 | 434.7 | 83622 | 435.7 | 84035 | -27 | -1.0 | weak |
| Call | 83700 | 219100 | 218924 | 398.8 | 83816 | 346.0 | 84099 | +37 | +52.8 | weak |
| Call | 83800 | 466260 | 465935 | 314.9 | 83839 | 268.1 | 84115 | +53 | +46.8 | weak |
| Call | 83900 | 873280 | 872904 | 281.7 | 83908 | 201.7 | 84182 | +120 | +80.1 | weak |
| Call | 84000 | 2705100 | 2697681 | 219.7 | 83978 | 139.7 | 84220 | +158 | +80.0 | weak |
| Call | 84100 | 3164160 | 3163814 | 159.5 | 84068 | 97.2 | 84260 | +198 | +62.3 | medium |
| Call | 84200 | 4538100 | 4537545 | 137.7 | 84100 | 63.4 | 84338 | +276 | +74.3 | medium |
| Call | 84300 | 4902500 | 4900204 | 133.8 | 84083 | 38.9 | 84434 | +372 | +95.0 | medium |
| Call | 84400 | 5892120 | 5889350 | 139.5 | 84159 | 24.4 | 84540 | +478 | +115.2 | strong |
| Call | 84500 | 7513320 | 7471013 | 115.4 | 84013 | 16.6 | 84615 | +554 | +98.8 | strong |
| Call | 84600 | 3831440 | 3829005 | 112.5 | 84100 | 11.6 | 84712 | +651 | +100.9 | strong |
| Call | 84700 | 3244240 | 3239582 | 87.5 | 84066 | 8.1 | 84788 | +726 | +79.5 | strong |
| Call | 84800 | 3012780 | 3007596 | 76.2 | 84088 | 6.3 | 84876 | +814 | +69.8 | strong |
| Call | 84900 | 3209620 | 3202823 | 55.9 | 84125 | 5.2 | 84956 | +894 | +50.7 | strong |
| Call | 85000 | 6308800 | 6269132 | 53.5 | 83978 | 4.2 | 85054 | +992 | +49.4 | strong |
| Call | 85100 | 1833840 | 1832432 | 34.3 | 83972 | 3.2 | 85134 | +1072 | +31.0 | strong |
| Call | 85200 | 1977720 | 1975144 | 41.7 | 84007 | 2.8 | 85242 | +1180 | +38.9 | strong |
| Call | 85300 | 1638900 | 1638304 | 26.2 | 84007 | 2.4 | 85326 | +1264 | +23.8 | strong |
| Put | 82900 | 1249100 | 1245589 | 55.4 | 84000 | 2.8 | 82845 | +1217 | +52.6 | strong |
| Put | 83000 | 4682700 | 4636752 | 82.4 | 83898 | 3.7 | 82918 | +1144 | +78.7 | strong |
| Put | 83100 | 1384980 | 1384034 | 89.0 | 83929 | 4.5 | 83011 | +1051 | +84.5 | strong |
| Put | 83200 | 1949100 | 1948534 | 93.6 | 83939 | 5.7 | 83106 | +955 | +87.9 | strong |
| Put | 83300 | 1981740 | 1981290 | 114.0 | 83929 | 8.1 | 83186 | +876 | +105.9 | strong |
| Put | 83400 | 2160560 | 2160160 | 118.2 | 83987 | 11.6 | 83282 | +780 | +106.7 | strong |
| Put | 83500 | 6314500 | 6311464 | 123.9 | 84029 | 17.0 | 83376 | +686 | +106.9 | strong |
| Put | 83600 | 3358820 | 3358550 | 118.8 | 84083 | 23.4 | 83481 | +581 | +95.4 | strong |
| Put | 83700 | 4515580 | 4515309 | 129.3 | 84065 | 37.8 | 83571 | +491 | +91.6 | strong |
| Put | 83800 | 4807080 | 4806747 | 192.6 | 84030 | 55.5 | 83607 | +454 | +137.1 | strong |
| Put | 83900 | 4156840 | 4156405 | 219.0 | 84043 | 85.0 | 83681 | +381 | +134.0 | strong |
| Put | 84000 | 7006960 | 7005446 | 199.1 | 84197 | 130.8 | 83801 | +261 | +68.3 | medium |
| Put | 84100 | 3488600 | 3488567 | 240.0 | 84153 | 183.9 | 83860 | +202 | +56.1 | medium |
| Put | 84200 | 1817460 | 1817454 | 219.0 | 84269 | 250.7 | 83981 | +81 | -31.7 | weak |
| Put | 84300 | 1176540 | 1176507 | 201.1 | 84338 | 320.3 | 84099 | -37 | -119.2 | weak |
| Put | 84400 | 691980 | 691980 | 221.9 | 84364 | 415.5 | 84178 | -116 | -193.6 | weak |
| Put | 84500 | 1054320 | 1054307 | 309.7 | 84346 | 495.1 | 84190 | -129 | -185.4 | weak |
| Put | 84600 | 465420 | 465420 | 361.8 | 84372 | 593.1 | 84238 | -176 | -231.4 | weak |
| Put | 84700 | 130560 | 130560 | 480.8 | 84317 | 694.6 | 84219 | -157 | -213.8 | weak |
| Put | 84800 | 47380 | 47380 | 510.0 | 84373 | 793.2 | 84290 | -228 | -283.2 | weak |
| Put | 84900 | 55580 | 55580 | 622.2 | 84348 | 899.0 | 84278 | -216 | -276.8 | weak |
| Put | 85000 | 115820 | 115639 | 732.1 | 84310 | 995.0 | 84268 | -206 | -262.9 | weak |
| Put | 85100 | 16420 | 16420 | 826.2 | 84319 | 1096.8 | 84274 | -212 | -270.5 | weak |
| Put | 85200 | 13400 | 13400 | 951.5 | 84281 | 1155.4 | 84248 | -187 | -203.9 | weak |
| Put | 85300 | 10700 | 5244 | 1121.4 | 84195 | 1289.2 | 84179 | -117 | -167.8 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 86000, strongest put writers at 84500; weakest call writers at -, weakest put writers at 86500. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82900 | 260 | 220 | 1609.0 | 82444 | 1609.0 | 84509 | +447 | +0.0 | strong |
| Call | 83000 | 3980 | 3857 | 2221.1 | 83613 | 2468.0 | 85221 | +1159 | -246.9 | strong |
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2100.0 | 84702 | +640 | -498.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +738 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +1018 | -335.1 | strong |
| Call | 83400 | 540 | 531 | 1612.7 | 83261 | 2152.9 | 85013 | +951 | -540.2 | strong |
| Call | 83500 | 8420 | 8348 | 2097.4 | 83850 | 2154.0 | 85597 | +1536 | -56.6 | strong |
| Call | 83600 | 700 | 700 | 1823.9 | 83677 | 2151.3 | 85424 | +1362 | -327.4 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1805.5 | 85310 | +1248 | -195.6 | strong |
| Call | 83800 | 300 | 300 | 1665.5 | 83527 | 2059.2 | 85465 | +1404 | -393.8 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +1296 | +287.6 | strong |
| Call | 84000 | 13260 | 13260 | 1785.5 | 83890 | 1880.0 | 85785 | +1724 | -94.5 | strong |
| Call | 84100 | 600 | 600 | 1647.6 | 83817 | 1796.4 | 85748 | +1686 | -148.8 | strong |
| Call | 84200 | 480 | 475 | 1485.4 | 83584 | 1909.4 | 85685 | +1624 | -424.0 | strong |
| Call | 84300 | 360 | 360 | 1640.1 | 84016 | 1660.0 | 85940 | +1878 | -19.9 | strong |
| Call | 84400 | 500 | 500 | 1429.4 | 83600 | 1619.2 | 85829 | +1768 | -189.8 | strong |
| Call | 84500 | 11380 | 11380 | 1566.8 | 83986 | 1511.2 | 86067 | +2005 | +55.6 | strong |
| Call | 84600 | 480 | 480 | 1347.7 | 83694 | 1503.6 | 85948 | +1886 | -155.9 | strong |
| Call | 84700 | 320 | 320 | 1188.2 | 83315 | 1463.0 | 85888 | +1826 | -274.8 | strong |
| Call | 84800 | 300 | 300 | 1202.4 | 83487 | 1370.3 | 86002 | +1941 | -167.9 | strong |
| Call | 84900 | 480 | 480 | 1148.2 | 83432 | 1444.8 | 86048 | +1986 | -296.7 | strong |
| Call | 85000 | 11300 | 11300 | 1256.0 | 83852 | 1309.2 | 86256 | +2194 | -53.2 | strong |
| Call | 85100 | 300 | 300 | 972.0 | 83276 | 1251.6 | 86072 | +2010 | -279.6 | strong |
| Call | 85200 | 560 | 560 | 978.6 | 83380 | 1180.2 | 86179 | +2117 | -201.6 | strong |
| Call | 85300 | 120 | 120 | 1035.2 | 83872 | 1035.5 | 86335 | +2273 | -0.4 | strong |
| Put | 82900 | 120 | 120 | 1084.5 | 83634 | 828.3 | 81815 | +2246 | +256.2 | strong |
| Put | 83000 | 12760 | 12299 | 1081.5 | 83768 | 902.2 | 81918 | +2143 | +179.3 | strong |
| Put | 83100 | 140 | 140 | 1184.0 | 83585 | 947.9 | 81916 | +2146 | +236.2 | strong |
| Put | 83200 | 540 | 540 | 1379.9 | 83227 | 981.6 | 81820 | +2242 | +398.2 | strong |
| Put | 83300 | 460 | 460 | 1470.7 | 83125 | 930.5 | 81829 | +2232 | +540.2 | strong |
| Put | 83400 | 800 | 800 | 1387.1 | 83414 | 1097.0 | 82013 | +2049 | +290.0 | strong |
| Put | 83500 | 8240 | 7974 | 1216.0 | 83859 | 1085.8 | 82284 | +1778 | +130.2 | strong |
| Put | 83600 | 1060 | 1060 | 1521.0 | 83328 | 1032.9 | 82079 | +1983 | +488.1 | strong |
| Put | 83700 | 660 | 660 | 1552.3 | 83332 | 1089.1 | 82148 | +1914 | +463.2 | strong |
| Put | 83800 | 800 | 800 | 1494.5 | 83550 | 1034.7 | 82306 | +1756 | +459.8 | strong |
| Put | 83900 | 520 | 506 | 1497.6 | 83620 | 1265.3 | 82402 | +1659 | +232.2 | strong |
| Put | 84000 | 13360 | 13360 | 1342.1 | 84048 | 1298.5 | 82658 | +1404 | +43.6 | strong |
| Put | 84100 | 1380 | 1380 | 1541.6 | 83743 | 1315.0 | 82558 | +1503 | +226.6 | strong |
| Put | 84200 | 820 | 820 | 1537.0 | 83811 | 1410.0 | 82663 | +1399 | +127.0 | strong |
| Put | 84300 | 1040 | 1040 | 1595.2 | 83826 | 1399.0 | 82705 | +1357 | +196.2 | strong |
| Put | 84400 | 1580 | 1580 | 1746.8 | 83653 | 1430.6 | 82653 | +1409 | +316.2 | strong |
| Put | 84500 | 14060 | 14060 | 1531.0 | 84121 | 1462.8 | 82969 | +1093 | +68.2 | strong |
| Put | 84600 | 920 | 920 | 1703.9 | 83894 | 1444.8 | 82896 | +1166 | +259.1 | strong |
| Put | 84700 | 720 | 720 | 1651.0 | 84077 | 1550.5 | 83049 | +1013 | +100.5 | strong |
| Put | 84800 | 760 | 760 | 1641.4 | 84218 | 1550.0 | 83159 | +903 | +91.4 | strong |
| Put | 84900 | 780 | 780 | 2253.9 | 83187 | 1591.8 | 82646 | +1416 | +662.1 | strong |
| Put | 85000 | 8800 | 8800 | 1830.2 | 83984 | 1699.8 | 83170 | +892 | +130.4 | strong |
| Put | 85100 | 420 | 420 | 1949.1 | 83844 | 1640.1 | 83151 | +911 | +309.0 | strong |
| Put | 85200 | 620 | 620 | 2141.7 | 83689 | 2120.6 | 83058 | +1003 | +21.1 | strong |
| Put | 85300 | 1080 | 1080 | 2085.3 | 83780 | 2085.3 | 83215 | +847 | +0.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 12 | 27% | -0.33% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 7 | 57% | -0.04% | -0.31 to +0.16% |  | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 5 | 67% | +0.21% | -0.05 to +0.48% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 0% | -0.57% | -0.80 to -0.40% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 33% | -0.16% | -1.14 to +0.86% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 3 | 0% | -0.06% | -0.07 to -0.05% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.40% | -1.15 to +0.34% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 67% | +0.54% | -0.21 to +0.97% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 1 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 0% | -0.12% | -0.12 to -0.12% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.47% | -0.47 to -0.47% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.47% | -0.47 to -0.47% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.31% | -0.31 to -0.31% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.12% | -0.12 to -0.12% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
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
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +1.82% | +1.82 to +1.82% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 43 | 52% | +0.00% | no clear direction |
| intraday | monthly | writers even · few weak writers | 36 | 59% | -0.02% | no clear direction |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 5 | 20% | -0.61% | too few (5/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides | 1 | 0% | -0.31% | too few (1/10) |
| day | weekly | writers even · few weak writers | 5 | 67% | +0.07% | too few (3/10) |
| day | monthly | writers even · few weak writers | 4 | 67% | -0.18% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 32 | 57% | -0.03% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 25 | 50% | -0.00% | no clear direction |
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
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 0% | -0.31% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 67% | -0.18% | too few (3/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | -0.81% | too few (2/10) |
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
