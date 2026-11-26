# Sensex option chain pattern log
Updated 2026-11-26 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 60 snapshots over 6 trading days
- 117 patterns logged; 53 different patterns so far

## Latest read (2026-11-26 09:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 0.2 | 83776 | 0.968 | 84000 | 83000 | 85000 | ±0.7% (83190-84363) | 33.62 |
| 2026-12-31 (monthly) | 35.2 | 83776 | 1.195 | 84000 | 83000 | 84500 | ±3.82% (80577-86976) | 15.32 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · mid walls`. Seen 2 times before; Sensex was up after it 0% of the time, average -1.15%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 36 times before; Sensex was up after it 58% of the time, average +0.03%. Too few outcomes (19/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 18 times before; Sensex was up after it 56% of the time, average +0.04%. Too few outcomes (16/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Sensex was up after it 33% of the time, average -0.05%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 0% of the time, average -0.98%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 28 times before; Sensex was up after it 68% of the time, average +0.01%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 24 times before; Sensex was up after it 67% of the time, average +0.01%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 33% of the time, average -0.29%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Sensex was up after it 33% of the time, average -0.29%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 83000; weakest call writers at 83000, weakest put writers at 84100. Covers 99% of near-money call OI and 99% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82600 | 49040 | 46879 | 667.7 | 82737 | 1155.0 | 83268 | -509 | -487.2 | weak |
| Call | 82700 | 68960 | 65679 | 660.9 | 82828 | 1073.5 | 83361 | -416 | -412.7 | weak |
| Call | 82800 | 78460 | 72404 | 630.8 | 82868 | 1002.4 | 83431 | -346 | -371.6 | weak |
| Call | 82900 | 59580 | 55036 | 624.6 | 82943 | 912.8 | 83525 | -252 | -288.2 | weak |
| Call | 83000 | 195260 | 176119 | 610.3 | 83032 | 818.0 | 83610 | -166 | -207.7 | weak |
| Call | 83100 | 50920 | 49373 | 622.4 | 83150 | 739.9 | 83722 | -54 | -117.5 | weak |
| Call | 83200 | 70780 | 69938 | 616.6 | 83268 | 660.9 | 83817 | +40 | -44.3 | weak |
| Call | 83300 | 53000 | 52502 | 577.9 | 83339 | 584.1 | 83878 | +101 | -6.2 | weak |
| Call | 83400 | 103260 | 102074 | 576.9 | 83491 | 506.2 | 83977 | +200 | +70.7 | medium |
| Call | 83500 | 360020 | 353770 | 464.7 | 83458 | 442.1 | 83965 | +188 | +22.6 | medium |
| Call | 83600 | 238840 | 238297 | 414.3 | 83543 | 377.3 | 84014 | +238 | +37.0 | medium |
| Call | 83700 | 502080 | 501481 | 383.7 | 83667 | 321.4 | 84084 | +307 | +62.2 | medium |
| Call | 83800 | 1089180 | 1088061 | 324.1 | 83724 | 270.3 | 84124 | +348 | +53.8 | medium |
| Call | 83900 | 1277000 | 1276066 | 290.3 | 83753 | 226.3 | 84190 | +414 | +64.0 | strong |
| Call | 84000 | 2977080 | 2954221 | 243.0 | 83700 | 189.4 | 84243 | +467 | +53.6 | strong |
| Call | 84100 | 2039880 | 2038498 | 191.0 | 83764 | 156.6 | 84291 | +515 | +34.4 | strong |
| Call | 84200 | 2009860 | 2008234 | 182.2 | 83779 | 128.2 | 84382 | +606 | +54.0 | strong |
| Call | 84300 | 2261600 | 2257459 | 174.1 | 83800 | 103.7 | 84474 | +698 | +70.4 | strong |
| Call | 84400 | 1687720 | 1684134 | 181.1 | 83821 | 84.5 | 84581 | +805 | +96.6 | strong |
| Call | 84500 | 3622180 | 3579873 | 141.5 | 83765 | 68.2 | 84642 | +865 | +73.3 | strong |
| Call | 84600 | 1445480 | 1443045 | 135.0 | 83797 | 54.6 | 84735 | +959 | +80.4 | strong |
| Call | 84700 | 1431120 | 1426295 | 106.8 | 83758 | 44.1 | 84807 | +1030 | +62.8 | strong |
| Call | 84800 | 1460760 | 1454534 | 88.5 | 83727 | 35.5 | 84888 | +1112 | +53.0 | strong |
| Call | 84900 | 1286360 | 1278110 | 76.5 | 83752 | 28.4 | 84976 | +1200 | +48.1 | strong |
| Call | 85000 | 5005160 | 4952567 | 60.1 | 83725 | 22.6 | 85060 | +1284 | +37.4 | strong |
| Put | 82600 | 1133420 | 1125240 | 70.4 | 83751 | 24.7 | 82530 | +1247 | +45.7 | strong |
| Put | 82700 | 1506320 | 1498891 | 83.5 | 83787 | 31.1 | 82616 | +1160 | +52.4 | strong |
| Put | 82800 | 1267860 | 1253807 | 86.2 | 83794 | 39.5 | 82714 | +1063 | +46.6 | strong |
| Put | 82900 | 1078420 | 1072144 | 99.6 | 83789 | 50.0 | 82800 | +976 | +49.6 | strong |
| Put | 83000 | 4862180 | 4798281 | 104.4 | 83802 | 63.2 | 82896 | +881 | +41.2 | strong |
| Put | 83100 | 1189060 | 1187768 | 130.6 | 83783 | 79.4 | 82969 | +807 | +51.2 | strong |
| Put | 83200 | 1672960 | 1672191 | 138.6 | 83783 | 99.7 | 83061 | +715 | +39.0 | strong |
| Put | 83300 | 1341320 | 1340847 | 159.8 | 83777 | 122.5 | 83140 | +636 | +37.3 | strong |
| Put | 83400 | 1437160 | 1436680 | 189.1 | 83797 | 149.5 | 83211 | +566 | +39.6 | strong |
| Put | 83500 | 3276100 | 3272522 | 231.1 | 83806 | 182.0 | 83269 | +508 | +49.1 | strong |
| Put | 83600 | 1362520 | 1362217 | 264.4 | 83786 | 220.2 | 83336 | +441 | +44.1 | strong |
| Put | 83700 | 1529720 | 1529444 | 295.0 | 83786 | 264.0 | 83405 | +371 | +31.0 | medium |
| Put | 83800 | 2162500 | 2162167 | 343.7 | 83798 | 316.1 | 83456 | +320 | +27.5 | medium |
| Put | 83900 | 1858940 | 1858505 | 385.0 | 83820 | 374.9 | 83515 | +261 | +10.0 | medium |
| Put | 84000 | 2559640 | 2557889 | 423.1 | 83863 | 432.6 | 83577 | +200 | -9.5 | medium |
| Put | 84100 | 979100 | 979063 | 474.2 | 83866 | 500.2 | 83626 | +151 | -26.0 | weak |
| Put | 84200 | 582340 | 582329 | 513.8 | 83922 | 570.4 | 83686 | +90 | -56.6 | weak |
| Put | 84300 | 306260 | 306149 | 540.4 | 84007 | 645.4 | 83760 | +17 | -105.0 | weak |
| Put | 84400 | 196600 | 196599 | 537.9 | 84141 | 728.1 | 83862 | -86 | -190.3 | weak |
| Put | 84500 | 381300 | 381259 | 669.4 | 84033 | 809.5 | 83831 | -54 | -140.2 | weak |
| Put | 84600 | 97500 | 97500 | 621.3 | 84258 | 896.0 | 83979 | -202 | -274.8 | weak |
| Put | 84700 | 52320 | 52320 | 896.6 | 83981 | 991.1 | 83803 | -27 | -94.5 | weak |
| Put | 84800 | 21240 | 21240 | 791.9 | 84151 | 1076.0 | 84008 | -232 | -284.2 | weak |
| Put | 84900 | 23320 | 23320 | 879.4 | 84155 | 1181.8 | 84021 | -244 | -302.4 | weak |
| Put | 85000 | 122380 | 121685 | 999.3 | 84093 | 1263.5 | 84001 | -224 | -264.2 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 84500, strongest put writers at 84500; weakest call writers at -, weakest put writers at 86000. Covers 96% of near-money call OI and 97% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82600 | 120 | 120 | 1778.5 | 82439 | 1789.5 | 84378 | +602 | -10.9 | strong |
| Call | 82700 | 380 | 149 | 1845.6 | 82665 | 2577.9 | 84546 | +769 | -732.3 | strong |
| Call | 82800 | 1540 | 1464 | 2305.2 | 83514 | 2606.6 | 85105 | +1329 | -301.4 | strong |
| Call | 82900 | 260 | 220 | 1609.0 | 82444 | 1609.0 | 84509 | +733 | +0.0 | strong |
| Call | 83000 | 3020 | 2894 | 2053.9 | 83339 | 2187.0 | 85054 | +1278 | -133.1 | strong |
| Call | 83100 | 700 | 660 | 1602.0 | 82679 | 2100.0 | 84702 | +926 | -498.0 | strong |
| Call | 83200 | 460 | 374 | 1599.7 | 82751 | 2616.2 | 84800 | +1023 | -1016.5 | strong |
| Call | 83300 | 460 | 460 | 1780.0 | 83299 | 2115.2 | 85080 | +1304 | -335.1 | strong |
| Call | 83400 | 540 | 531 | 1612.7 | 83261 | 2152.9 | 85013 | +1236 | -540.2 | strong |
| Call | 83500 | 8080 | 8008 | 2088.4 | 83831 | 2072.6 | 85588 | +1812 | +15.8 | strong |
| Call | 83600 | 500 | 500 | 1550.3 | 83212 | 2020.4 | 85150 | +1374 | -470.1 | strong |
| Call | 83700 | 880 | 880 | 1609.9 | 83329 | 1805.5 | 85310 | +1534 | -195.6 | strong |
| Call | 83800 | 260 | 260 | 1570.1 | 83332 | 1919.4 | 85370 | +1594 | -349.3 | strong |
| Call | 83900 | 460 | 438 | 1457.4 | 83284 | 1169.8 | 85357 | +1581 | +287.6 | strong |
| Call | 84000 | 10180 | 10180 | 1723.9 | 83757 | 1684.8 | 85724 | +1948 | +39.1 | strong |
| Call | 84100 | 480 | 480 | 1604.9 | 83720 | 1579.0 | 85705 | +1928 | +25.9 | strong |
| Call | 84200 | 520 | 514 | 1376.2 | 83377 | 1527.0 | 85576 | +1800 | -150.8 | strong |
| Call | 84300 | 180 | 180 | 1469.0 | 83665 | 1485.2 | 85769 | +1993 | -16.2 | strong |
| Call | 84400 | 300 | 300 | 1270.9 | 83215 | 1427.1 | 85671 | +1894 | -156.2 | strong |
| Call | 84500 | 10720 | 10720 | 1466.3 | 83779 | 1435.5 | 85966 | +2190 | +30.7 | strong |
| Call | 84600 | 300 | 300 | 1256.5 | 83457 | 1342.4 | 85856 | +2080 | -86.0 | strong |
| Call | 84700 | 220 | 220 | 1029.4 | 82892 | 1295.4 | 85729 | +1953 | -266.0 | strong |
| Call | 84800 | 180 | 180 | 997.6 | 82976 | 1237.8 | 85798 | +2021 | -240.2 | strong |
| Call | 84900 | 360 | 360 | 1049.3 | 83164 | 1209.1 | 85949 | +2173 | -159.8 | strong |
| Call | 85000 | 5660 | 5660 | 1139.3 | 83536 | 1195.0 | 86139 | +2363 | -55.7 | strong |
| Put | 82600 | 740 | 740 | 924.9 | 83826 | 880.8 | 81675 | +2101 | +44.1 | strong |
| Put | 82700 | 360 | 360 | 951.9 | 83853 | 947.0 | 81748 | +2028 | +4.9 | strong |
| Put | 82800 | 280 | 280 | 948.1 | 83794 | 903.2 | 81852 | +1925 | +44.9 | strong |
| Put | 82900 | 120 | 120 | 1084.5 | 83634 | 989.2 | 81815 | +1961 | +95.3 | strong |
| Put | 83000 | 11060 | 10586 | 1127.3 | 83655 | 1085.0 | 81873 | +1904 | +42.3 | strong |
| Put | 83100 | 200 | 200 | 1278.5 | 83394 | 1111.0 | 81821 | +1955 | +167.6 | strong |
| Put | 83200 | 560 | 560 | 1379.9 | 83227 | 1036.0 | 81820 | +1956 | +343.8 | strong |
| Put | 83300 | 600 | 600 | 1470.7 | 83125 | 1069.2 | 81829 | +1947 | +401.6 | strong |
| Put | 83400 | 820 | 820 | 1397.1 | 83392 | 1142.8 | 82003 | +1773 | +254.3 | strong |
| Put | 83500 | 8060 | 7790 | 1224.3 | 83841 | 1272.7 | 82276 | +1501 | -48.4 | strong |
| Put | 83600 | 1080 | 1080 | 1521.0 | 83328 | 1195.1 | 82079 | +1697 | +325.9 | strong |
| Put | 83700 | 680 | 680 | 1566.8 | 83306 | 1219.6 | 82133 | +1643 | +347.2 | strong |
| Put | 83800 | 820 | 820 | 1494.5 | 83550 | 1280.2 | 82306 | +1471 | +214.2 | strong |
| Put | 83900 | 520 | 506 | 1512.2 | 83593 | 1318.9 | 82388 | +1389 | +193.3 | strong |
| Put | 84000 | 8880 | 8880 | 1412.8 | 83886 | 1489.7 | 82587 | +1189 | -76.9 | strong |
| Put | 84100 | 1440 | 1440 | 1545.0 | 83738 | 1530.0 | 82555 | +1221 | +15.0 | strong |
| Put | 84200 | 860 | 860 | 1537.0 | 83811 | 1404.4 | 82663 | +1113 | +132.6 | strong |
| Put | 84300 | 1020 | 1020 | 1614.7 | 83792 | 1554.3 | 82685 | +1091 | +60.4 | strong |
| Put | 84400 | 1460 | 1460 | 1796.7 | 83562 | 1658.0 | 82603 | +1173 | +138.6 | strong |
| Put | 84500 | 12520 | 12520 | 1570.5 | 84068 | 1729.9 | 82929 | +847 | -159.4 | strong |
| Put | 84600 | 920 | 920 | 1703.9 | 83894 | 1630.7 | 82896 | +880 | +73.2 | strong |
| Put | 84700 | 560 | 560 | 1672.2 | 84036 | 1515.0 | 83028 | +749 | +157.1 | strong |
| Put | 84800 | 540 | 540 | 1673.6 | 84175 | 1586.3 | 83126 | +650 | +87.3 | strong |
| Put | 84900 | 680 | 680 | 2351.3 | 83032 | 1633.4 | 82549 | +1228 | +717.9 | strong |
| Put | 85000 | 4300 | 4300 | 2012.5 | 83743 | 2001.7 | 82988 | +789 | +10.8 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 13 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near put wall | 11 | 30% | -0.34% | -1.29 to +0.23% |  | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 6 | 67% | +0.00% | -0.22 to +0.16% |  | too few (6/10) |
| monthly | PCR down · call writing · walls same · near put wall | 5 | 60% | -0.10% | -0.70 to +0.25% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 4 | 67% | +0.21% | -0.05 to +0.48% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 0% | -1.15% | -1.15 to -1.15% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 3 | 0% | -0.06% | -0.07 to -0.05% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 3 | 0% | -0.36% | -0.64 to -0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 50% | +0.10% | -0.01 to +0.20% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 3 | 0% | -0.47% | -0.50 to -0.44% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.14% | -1.14 to +0.86% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 50% | -0.45% | -1.14 to +0.23% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 0% | -0.65% | -0.80 to -0.50% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.63% | -0.63 to -0.63% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.19% | +0.19 to +0.19% | 100% of 1 | too few (1/10) |
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
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 | 100% | +1.82% | +1.82 to +1.82% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 37 | 58% | +0.03% | no clear direction |
| intraday | monthly | writers even · few weak writers | 29 | 68% | +0.01% | no clear direction |
| intraday | monthly | put writers stronger · weak puts | 18 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 10 | 20% | -0.45% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 5 | 20% | -0.61% | too few (5/10) |
| intraday | weekly | writers even · weak puts | 2 | 100% | +0.54% | too few (1/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | call writers stronger · weak calls | 1 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | put writers stronger · weak calls | 1 | 0% | -0.50% | too few (1/10) |
| day | weekly | writers even · few weak writers | 5 | 33% | -0.05% | too few (3/10) |
| day | monthly | writers even · few weak writers | 4 | 33% | -0.29% | too few (3/10) |
| day | monthly | put writers stronger · weak puts | 2 | 100% | +1.82% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 25 | 67% | +0.01% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 19 | 56% | +0.04% | no clear direction |
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
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 33% | -0.29% | too few (3/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 3 | 0% | -0.98% | too few (2/10) |
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
