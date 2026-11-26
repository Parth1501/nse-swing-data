# Sensex option chain pattern log
Updated 2026-11-26 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 65 snapshots over 6 trading days
- 127 patterns logged; 59 different patterns so far

## Latest read (2026-11-26 12:49:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 0.1 | 84322 | 0.961 | 84300 | 84000 | 85000 | ±0.4% (83986-84658) | 27.94 |
| 2026-12-31 (monthly) | 35.1 | 84322 | 1.071 | 84000 | 84000 | 86000 | ±3.8% (81118-87526) | 15.15 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak on both sides`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak on both sides`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls same · near put wall`. Seen 6 times before; Sensex was up after it 67% of the time, average +0.00%. Too few outcomes (6/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 33 times before; Sensex was up after it 70% of the time, average +0.05%. History points to a bull call debit spread, ATM to about the call wall 86000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 29 times before; Sensex was up after it 69% of the time, average +0.06%. History points to a bull call debit spread, ATM to about the call wall 86000.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 67% of the time, average -0.08%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Sensex was up after it 67% of the time, average -0.08%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 84000; weakest call writers at 84300, weakest put writers at 84400. Covers 99% of near-money call OI and 100% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83100 | 38480 | 37311 | 622.4 | 83150 | 1255.5 | 83722 | -600 | -633.2 | weak |
| Call | 83200 | 51980 | 51362 | 616.6 | 83268 | 1157.8 | 83817 | -506 | -541.3 | weak |
| Call | 83300 | 34360 | 34037 | 577.9 | 83339 | 1066.0 | 83878 | -444 | -488.1 | weak |
| Call | 83400 | 68860 | 68069 | 576.9 | 83491 | 966.9 | 83977 | -345 | -389.9 | weak |
| Call | 83500 | 178920 | 175934 | 476.9 | 83488 | 869.3 | 83977 | -345 | -392.4 | weak |
| Call | 83600 | 137540 | 137234 | 420.3 | 83559 | 770.5 | 84020 | -302 | -350.2 | weak |
| Call | 83700 | 160860 | 160684 | 400.7 | 83713 | 672.0 | 84101 | -221 | -271.3 | weak |
| Call | 83800 | 353660 | 353316 | 333.4 | 83751 | 576.7 | 84133 | -189 | -243.3 | weak |
| Call | 83900 | 518620 | 518244 | 291.5 | 83757 | 487.9 | 84192 | -131 | -196.4 | weak |
| Call | 84000 | 1115680 | 1108261 | 257.6 | 83773 | 402.4 | 84258 | -65 | -144.7 | weak |
| Call | 84100 | 807360 | 807014 | 224.5 | 83920 | 325.4 | 84324 | +2 | -100.9 | weak |
| Call | 84200 | 1482320 | 1481765 | 205.4 | 84017 | 253.6 | 84405 | +83 | -48.1 | weak |
| Call | 84300 | 3032520 | 3030224 | 177.6 | 84059 | 192.8 | 84478 | +155 | -15.2 | weak |
| Call | 84400 | 4268280 | 4265510 | 178.1 | 84177 | 141.6 | 84578 | +256 | +36.5 | medium |
| Call | 84500 | 5719780 | 5677473 | 142.7 | 83978 | 105.2 | 84643 | +321 | +37.5 | medium |
| Call | 84600 | 3151440 | 3149005 | 133.2 | 84100 | 76.5 | 84733 | +411 | +56.8 | strong |
| Call | 84700 | 3325060 | 3320235 | 88.4 | 84066 | 55.5 | 84788 | +466 | +32.9 | strong |
| Call | 84800 | 3544100 | 3537874 | 77.6 | 84088 | 40.4 | 84878 | +555 | +37.3 | strong |
| Call | 84900 | 3895560 | 3887310 | 55.9 | 84125 | 30.2 | 84956 | +634 | +25.7 | strong |
| Call | 85000 | 8364380 | 8311787 | 53.5 | 83978 | 22.1 | 85054 | +731 | +31.4 | strong |
| Call | 85100 | 2730400 | 2728303 | 34.3 | 83972 | 15.3 | 85134 | +812 | +18.9 | strong |
| Call | 85200 | 2530020 | 2526724 | 41.7 | 84007 | 11.4 | 85242 | +920 | +30.2 | strong |
| Call | 85300 | 2894500 | 2893447 | 26.2 | 84007 | 8.4 | 85326 | +1004 | +17.8 | strong |
| Call | 85400 | 1954840 | 1951975 | 25.2 | 83925 | 6.5 | 85425 | +1103 | +18.7 | strong |
| Call | 85500 | 4073120 | 4048477 | 28.9 | 83753 | 5.3 | 85529 | +1207 | +23.5 | strong |
| Put | 83100 | 1341100 | 1340076 | 98.9 | 83899 | 5.7 | 83001 | +1321 | +93.2 | strong |
| Put | 83200 | 1850320 | 1849731 | 102.0 | 83927 | 6.8 | 83098 | +1224 | +95.3 | strong |
| Put | 83300 | 1966060 | 1965610 | 115.0 | 83928 | 7.9 | 83185 | +1137 | +107.1 | strong |
| Put | 83400 | 1897620 | 1897220 | 133.2 | 83966 | 9.8 | 83267 | +1055 | +123.3 | strong |
| Put | 83500 | 5454600 | 5451564 | 141.1 | 84015 | 12.5 | 83359 | +963 | +128.6 | strong |
| Put | 83600 | 2712200 | 2711930 | 142.7 | 84067 | 15.4 | 83457 | +865 | +127.2 | strong |
| Put | 83700 | 2958960 | 2958689 | 180.9 | 84037 | 20.9 | 83519 | +803 | +160.0 | strong |
| Put | 83800 | 3889940 | 3889607 | 226.9 | 84011 | 28.4 | 83573 | +749 | +198.4 | strong |
| Put | 83900 | 3303840 | 3303405 | 259.8 | 84016 | 39.4 | 83640 | +682 | +220.4 | strong |
| Put | 84000 | 8105360 | 8103609 | 199.1 | 84197 | 54.5 | 83801 | +521 | +144.5 | strong |
| Put | 84100 | 3480060 | 3480025 | 247.2 | 84151 | 76.2 | 83853 | +469 | +171.0 | strong |
| Put | 84200 | 3575880 | 3575869 | 219.0 | 84269 | 105.8 | 83981 | +341 | +113.2 | medium |
| Put | 84300 | 3890220 | 3890109 | 201.1 | 84338 | 143.1 | 84099 | +223 | +58.0 | medium |
| Put | 84400 | 3280240 | 3280239 | 221.9 | 84364 | 195.3 | 84178 | +144 | +26.6 | weak |
| Put | 84500 | 1925040 | 1925016 | 309.7 | 84346 | 256.9 | 84190 | +132 | +52.8 | weak |
| Put | 84600 | 726820 | 726820 | 361.8 | 84372 | 329.6 | 84238 | +84 | +32.2 | weak |
| Put | 84700 | 272300 | 272300 | 480.8 | 84317 | 406.6 | 84219 | +103 | +74.2 | weak |
| Put | 84800 | 122360 | 122360 | 510.0 | 84373 | 492.5 | 84290 | +32 | +17.5 | weak |
| Put | 84900 | 86820 | 86820 | 622.2 | 84348 | 580.4 | 84278 | +44 | +41.9 | weak |
| Put | 85000 | 354240 | 353685 | 732.1 | 84310 | 674.8 | 84268 | +54 | +57.3 | weak |
| Put | 85100 | 19700 | 19700 | 803.0 | 84342 | 758.9 | 84297 | +25 | +44.1 | weak |
| Put | 85200 | 12960 | 12960 | 949.0 | 84285 | 860.2 | 84251 | +71 | +88.7 | weak |
| Put | 85300 | 9440 | 3984 | 1126.2 | 84202 | 954.5 | 84174 | +148 | +171.8 | weak |
| Put | 85400 | 5420 | 5420 | 1213.1 | 84201 | 1053.2 | 84187 | +135 | +160.0 | weak |
| Put | 85500 | 97740 | 97740 | 1148.0 | 84331 | 1154.2 | 84352 | -30 | -6.1 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 86000, strongest put writers at 84000; weakest call writers at 82400, weakest put writers at -. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2100.0 | 84702 | +380 | -498.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +478 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +758 | -335.1 | strong |
| Call | 83400 | 540 | 531 | 1612.7 | 83261 | 2152.9 | 85013 | +691 | -540.2 | strong |
| Call | 83500 | 8360 | 8288 | 2097.0 | 83848 | 2338.2 | 85597 | +1275 | -241.2 | strong |
| Call | 83600 | 700 | 700 | 1823.9 | 83677 | 2151.3 | 85424 | +1102 | -327.4 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1805.5 | 85310 | +988 | -195.6 | strong |
| Call | 83800 | 300 | 300 | 1665.5 | 83527 | 2207.2 | 85465 | +1144 | -541.8 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +1035 | +287.6 | strong |
| Call | 84000 | 12680 | 12680 | 1781.9 | 83879 | 2015.2 | 85782 | +1460 | -233.4 | strong |
| Call | 84100 | 560 | 560 | 1638.5 | 83796 | 2032.0 | 85739 | +1417 | -393.5 | strong |
| Call | 84200 | 480 | 475 | 1485.4 | 83584 | 1909.4 | 85685 | +1363 | -424.0 | strong |
| Call | 84300 | 260 | 260 | 1632.4 | 83998 | 1856.2 | 85932 | +1611 | -223.8 | strong |
| Call | 84400 | 320 | 320 | 1322.6 | 83340 | 1720.0 | 85723 | +1401 | -397.3 | strong |
| Call | 84500 | 11280 | 11280 | 1566.2 | 83984 | 1741.1 | 86066 | +1744 | -174.9 | strong |
| Call | 84600 | 300 | 300 | 1256.5 | 83457 | 1616.6 | 85856 | +1535 | -360.1 | strong |
| Call | 84700 | 260 | 260 | 1113.5 | 83133 | 1576.0 | 85813 | +1492 | -462.5 | strong |
| Call | 84800 | 300 | 300 | 1202.4 | 83487 | 1582.8 | 86002 | +1680 | -380.3 | strong |
| Call | 84900 | 480 | 480 | 1148.2 | 83432 | 1444.8 | 86048 | +1726 | -296.7 | strong |
| Call | 85000 | 7200 | 7200 | 1224.2 | 83728 | 1455.0 | 86224 | +1902 | -230.8 | strong |
| Call | 85100 | 300 | 300 | 972.0 | 83276 | 1246.0 | 86072 | +1750 | -274.0 | strong |
| Call | 85200 | 340 | 340 | 848.1 | 82939 | 1347.2 | 86048 | +1726 | -499.1 | strong |
| Call | 85300 | 120 | 120 | 1035.2 | 83872 | 1035.5 | 86335 | +2013 | -0.4 | strong |
| Call | 85400 | 460 | 460 | 892.6 | 83194 | 1200.2 | 86293 | +1971 | -307.6 | strong |
| Call | 85500 | 2720 | 2720 | 1145.9 | 84100 | 1250.0 | 86646 | +2324 | -104.1 | strong |
| Put | 83100 | 100 | 100 | 1278.5 | 83394 | 868.2 | 81821 | +2500 | +410.3 | strong |
| Put | 83200 | 540 | 540 | 1379.9 | 83227 | 901.4 | 81820 | +2502 | +478.5 | strong |
| Put | 83300 | 460 | 460 | 1470.7 | 83125 | 930.5 | 81829 | +2493 | +540.2 | strong |
| Put | 83400 | 840 | 840 | 1387.1 | 83414 | 977.3 | 82013 | +2309 | +409.8 | strong |
| Put | 83500 | 8260 | 7994 | 1216.0 | 83859 | 1005.0 | 82284 | +2038 | +211.1 | strong |
| Put | 83600 | 1060 | 1060 | 1521.0 | 83328 | 1032.9 | 82079 | +2243 | +488.1 | strong |
| Put | 83700 | 640 | 640 | 1566.8 | 83306 | 1067.9 | 82133 | +2189 | +498.9 | strong |
| Put | 83800 | 800 | 800 | 1494.5 | 83550 | 1034.7 | 82306 | +2016 | +459.8 | strong |
| Put | 83900 | 540 | 526 | 1497.6 | 83620 | 1127.3 | 82402 | +1920 | +370.2 | strong |
| Put | 84000 | 13320 | 13320 | 1342.4 | 84048 | 1185.0 | 82658 | +1664 | +157.4 | strong |
| Put | 84100 | 1360 | 1360 | 1545.0 | 83738 | 1234.5 | 82555 | +1767 | +310.5 | strong |
| Put | 84200 | 840 | 840 | 1537.0 | 83811 | 1328.1 | 82663 | +1659 | +208.9 | strong |
| Put | 84300 | 980 | 980 | 1609.2 | 83804 | 1347.7 | 82691 | +1631 | +261.5 | strong |
| Put | 84400 | 1600 | 1600 | 1746.8 | 83653 | 1325.0 | 82653 | +1669 | +421.8 | strong |
| Put | 84500 | 11900 | 11900 | 1545.5 | 84111 | 1395.0 | 82954 | +1367 | +150.6 | strong |
| Put | 84600 | 920 | 920 | 1703.9 | 83894 | 1444.8 | 82896 | +1426 | +259.1 | strong |
| Put | 84700 | 720 | 720 | 1651.0 | 84077 | 1550.5 | 83049 | +1273 | +100.5 | strong |
| Put | 84800 | 760 | 760 | 1641.4 | 84218 | 1528.0 | 83159 | +1163 | +113.4 | strong |
| Put | 84900 | 780 | 780 | 2253.9 | 83187 | 1591.8 | 82646 | +1676 | +662.1 | strong |
| Put | 85000 | 5840 | 5840 | 1896.3 | 83941 | 1585.8 | 83104 | +1218 | +310.4 | strong |
| Put | 85100 | 420 | 420 | 1949.1 | 83844 | 1640.1 | 83151 | +1171 | +309.0 | strong |
| Put | 85200 | 620 | 620 | 2141.7 | 83689 | 2120.6 | 83058 | +1264 | +21.1 | strong |
| Put | 85300 | 1080 | 1080 | 2085.3 | 83780 | 2085.3 | 83215 | +1107 | +0.0 | strong |
| Put | 85400 | 140 | 140 | 2041.0 | 83938 | 2041.0 | 83359 | +963 | +0.0 | strong |
| Put | 85500 | 2600 | 2600 | 2388.7 | 83530 | 1961.2 | 83111 | +1211 | +427.5 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 11 | 30% | -0.34% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 7 | 67% | +0.00% | -0.22 to +0.16% |  | too few (6/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 4 | 67% | +0.21% | -0.05 to +0.48% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | -0.06% | -1.14 to +0.86% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 3 | 0% | -0.06% | -0.07 to -0.05% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.25% | -1.15 to +0.65% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 100% | +0.64% | +0.10 to +0.97% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 0% | -0.46% | -0.80 to -0.09% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.09% | -0.09 to -0.09% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.19% | +0.19 to +0.19% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.16% | -0.16 to -0.16% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.16% | -0.16 to -0.16% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.19% | +0.19 to +0.19% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
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
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.46% | +0.46 to +0.46% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.46% | +0.46 to +0.46% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 41 | 62% | +0.08% | no clear direction |
| intraday | monthly | writers even · few weak writers | 34 | 70% | +0.05% | up |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 5 | 20% | -0.61% | too few (5/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 4 | 67% | -0.08% | too few (3/10) |
| day | weekly | writers even · few weak writers | 4 | 67% | +0.17% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak on both sides | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 30 | 69% | +0.06% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 23 | 62% | +0.09% | no clear direction |
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
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 67% | -0.08% | too few (3/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.66% | too few (2/10) |
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
