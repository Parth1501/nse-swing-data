# Sensex option chain pattern log
Updated 2026-11-24 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 40 snapshots over 4 trading days
- 77 patterns logged; 38 different patterns so far

## Latest read (2026-11-24 13:46:00)

Sensex trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 2.1 | 82436 | 1.013 | 82800 | 79000 | 88000 | ±1.36% (81318-83554) | 18.73 |
| 2026-12-31 (monthly) | 37.1 | 82436 | 2.003 | 83000 | 82000 | 87900 | ±3.95% (79181-85691) | 15.11 |

- **Weekly, last 30 min**: `PCR flat · quiet OI · walls same · mid walls`. Seen 8 times before. Too few outcomes (0/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 20 times before; Sensex was up after it 67% of the time, average +0.18%. Too few outcomes (9/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 10 times before. Too few outcomes (0/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · mid walls`. Seen 1 times before. Too few outcomes (0/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Sensex was up after it 0% of the time, average -1.77%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 1 times before. Too few outcomes (0/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls same · near put wall`. Seen 8 times before. Too few outcomes (0/20) to trade on.
  - Writers: `put writers stronger · weak puts`. Seen 13 times before; Sensex was up after it 0% of the time, average -0.21%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 13 times before; Sensex was up after it 0% of the time, average -0.21%. Too few outcomes (3/20) to trade on.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak puts`. Seen 1 times before. Too few outcomes (0/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 1 times before. Too few outcomes (0/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 84000, strongest put writers at 80000; weakest call writers at 81200, weakest put writers at 83000. Covers 92% of near-money call OI and 88% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 81200 | 4620 | 1528 | 1398.9 | 82458 | 1416.0 | 82599 | +163 | -17.1 | weak |
| Call | 81300 | 4780 | 1163 | 1388.2 | 82525 | 1326.7 | 82688 | +252 | +61.5 | medium |
| Call | 81400 | 4180 | 1525 | 1372.5 | 82615 | 1272.7 | 82772 | +336 | +99.8 | medium |
| Call | 81500 | 53520 | 29849 | 1631.5 | 82991 | 1218.9 | 83131 | +695 | +412.6 | strong |
| Call | 81600 | 5140 | 1726 | 1282.2 | 82668 | 1135.0 | 82882 | +446 | +147.2 | strong |
| Call | 81700 | 9020 | 4669 | 1192.2 | 82656 | 1054.3 | 82892 | +456 | +137.9 | strong |
| Call | 81800 | 11500 | 6283 | 1050.4 | 82567 | 986.1 | 82850 | +414 | +64.3 | strong |
| Call | 81900 | 15180 | 9203 | 1014.4 | 82644 | 925.1 | 82914 | +478 | +89.3 | strong |
| Call | 82000 | 124220 | 53019 | 1083.5 | 82786 | 867.1 | 83084 | +648 | +216.4 | strong |
| Call | 82100 | 18960 | 12107 | 940.2 | 82711 | 814.4 | 83040 | +604 | +125.8 | strong |
| Call | 82200 | 25380 | 8985 | 903.8 | 82757 | 743.0 | 83104 | +668 | +160.8 | strong |
| Call | 82300 | 72380 | 48102 | 718.2 | 82560 | 682.0 | 83018 | +582 | +36.2 | strong |
| Call | 82400 | 163820 | 147692 | 637.7 | 82503 | 630.0 | 83038 | +602 | +7.7 | strong |
| Call | 82500 | 431540 | 360861 | 628.2 | 82576 | 575.0 | 83128 | +692 | +53.2 | strong |
| Call | 82600 | 167460 | 159932 | 653.7 | 82715 | 529.2 | 83254 | +818 | +124.5 | strong |
| Call | 82700 | 235340 | 223507 | 643.7 | 82788 | 486.1 | 83344 | +908 | +157.6 | strong |
| Call | 82800 | 277800 | 255768 | 617.7 | 82842 | 448.0 | 83418 | +982 | +169.7 | strong |
| Call | 82900 | 214140 | 197626 | 622.3 | 82936 | 414.1 | 83522 | +1086 | +208.2 | strong |
| Call | 83000 | 703940 | 622904 | 577.6 | 82924 | 380.8 | 83578 | +1142 | +196.8 | strong |
| Call | 83100 | 213020 | 205770 | 615.8 | 83104 | 342.6 | 83716 | +1280 | +273.3 | strong |
| Call | 83200 | 290640 | 286303 | 618.8 | 83207 | 309.0 | 83819 | +1383 | +309.8 | strong |
| Call | 83300 | 257920 | 254128 | 573.9 | 83218 | 290.4 | 83874 | +1438 | +283.4 | strong |
| Call | 83400 | 282120 | 274838 | 581.3 | 83300 | 266.1 | 83981 | +1545 | +315.2 | strong |
| Call | 83500 | 891560 | 850116 | 508.4 | 83213 | 239.5 | 84008 | +1572 | +268.9 | strong |
| Call | 83600 | 317800 | 313399 | 498.0 | 83264 | 220.2 | 84098 | +1662 | +277.7 | strong |
| Put | 81200 | 136120 | 130851 | 107.2 | 83168 | 114.1 | 81093 | +1343 | -6.9 | strong |
| Put | 81300 | 126900 | 116669 | 124.9 | 83029 | 127.8 | 81175 | +1261 | -2.9 | strong |
| Put | 81400 | 138380 | 128714 | 144.7 | 82950 | 146.1 | 81255 | +1181 | -1.4 | strong |
| Put | 81500 | 678260 | 617693 | 144.7 | 83052 | 162.8 | 81355 | +1081 | -18.1 | strong |
| Put | 81600 | 108700 | 101004 | 170.3 | 83124 | 187.8 | 81430 | +1006 | -17.5 | strong |
| Put | 81700 | 135880 | 115171 | 210.3 | 82954 | 225.0 | 81490 | +946 | -14.7 | strong |
| Put | 81800 | 163440 | 149596 | 229.6 | 82806 | 250.0 | 81570 | +866 | -20.4 | strong |
| Put | 81900 | 95180 | 72624 | 221.9 | 83235 | 282.7 | 81678 | +758 | -60.8 | strong |
| Put | 82000 | 476620 | 334370 | 267.8 | 83030 | 310.0 | 81732 | +704 | -42.2 | strong |
| Put | 82100 | 97340 | 68843 | 298.1 | 83065 | 353.9 | 81802 | +634 | -55.9 | strong |
| Put | 82200 | 151180 | 104941 | 337.3 | 82906 | 391.1 | 81863 | +573 | -53.8 | strong |
| Put | 82300 | 140120 | 109773 | 306.9 | 83301 | 438.0 | 81993 | +443 | -131.1 | strong |
| Put | 82400 | 231240 | 198727 | 446.5 | 82879 | 488.0 | 81953 | +483 | -41.5 | strong |
| Put | 82500 | 427900 | 280299 | 482.6 | 82906 | 528.6 | 82017 | +419 | -46.0 | strong |
| Put | 82600 | 172500 | 153166 | 525.8 | 82912 | 577.6 | 82074 | +362 | -51.8 | medium |
| Put | 82700 | 196360 | 182490 | 531.3 | 83002 | 635.4 | 82169 | +267 | -104.1 | medium |
| Put | 82800 | 146360 | 118516 | 581.3 | 83016 | 693.9 | 82219 | +217 | -112.6 | medium |
| Put | 82900 | 112720 | 101622 | 590.0 | 83071 | 763.8 | 82310 | +126 | -173.8 | weak |
| Put | 83000 | 379220 | 263260 | 638.5 | 83064 | 833.6 | 82361 | +75 | -195.1 | weak |
| Put | 83100 | 79700 | 76743 | 597.0 | 83256 | 891.9 | 82503 | -67 | -294.9 | weak |
| Put | 83200 | 95280 | 93257 | 632.3 | 83294 | 961.2 | 82568 | -132 | -328.9 | weak |
| Put | 83300 | 78720 | 77447 | 670.8 | 83317 | 1041.8 | 82629 | -193 | -371.0 | weak |
| Put | 83400 | 81100 | 79845 | 679.1 | 83407 | 1109.1 | 82721 | -285 | -430.0 | weak |
| Put | 83500 | 249520 | 242515 | 673.8 | 83507 | 1179.3 | 82826 | -390 | -505.5 | weak |
| Put | 83600 | 67220 | 66315 | 686.8 | 83587 | 1264.4 | 82913 | -477 | -577.6 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 83000, strongest put writers at 83000; weakest call writers at -, weakest put writers at 84000. Covers 86% of near-money call OI and 91% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 81500 | 980 | 131 | 2661.4 | 82866 | 2477.2 | 84161 | +1725 | +184.2 | strong |
| Call | 82000 | 1320 | 292 | 2450.0 | 83052 | 2133.9 | 84450 | +2014 | +316.0 | strong |
| Call | 82200 | 160 | 120 | 2106.2 | 82925 | 2016.4 | 84306 | +1870 | +89.8 | strong |
| Call | 82300 | 120 | 120 | 2104.6 | 82925 | 1955.2 | 84405 | +1969 | +149.4 | strong |
| Call | 82400 | 180 | 180 | 1994.6 | 82762 | 1894.8 | 84395 | +1959 | +99.8 | strong |
| Call | 82500 | 400 | 371 | 2243.9 | 83363 | 1875.0 | 84744 | +2308 | +368.9 | strong |
| Call | 82600 | 120 | 120 | 1778.5 | 82439 | 1789.5 | 84378 | +1943 | -10.9 | strong |
| Call | 82700 | 440 | 160 | 1800.6 | 82515 | 1760.5 | 84501 | +2065 | +40.2 | strong |
| Call | 82800 | 1620 | 1400 | 1729.5 | 82627 | 1687.2 | 84530 | +2094 | +42.4 | strong |
| Call | 82900 | 260 | 220 | 1609.0 | 82444 | 1609.0 | 84509 | +2073 | +0.0 | strong |
| Call | 83000 | 2920 | 2746 | 1922.9 | 83128 | 1604.9 | 84923 | +2487 | +318.0 | strong |
| Call | 83100 | 680 | 640 | 1583.5 | 82644 | 1506.4 | 84683 | +2247 | +77.1 | strong |
| Call | 83200 | 560 | 455 | 1599.7 | 82751 | 1444.6 | 84800 | +2364 | +155.1 | strong |
| Call | 83300 | 360 | 360 | 1633.4 | 83053 | 1552.0 | 84933 | +2497 | +81.3 | strong |
| Call | 83400 | 600 | 589 | 1578.4 | 83222 | 1556.7 | 84978 | +2542 | +21.8 | strong |
| Call | 83500 | 1540 | 1264 | 1547.2 | 82945 | 1360.8 | 85047 | +2611 | +186.3 | strong |
| Call | 83600 | 540 | 540 | 1550.3 | 83212 | 1273.7 | 85150 | +2714 | +276.6 | strong |
| Put | 81200 | 40 | 40 | 874.0 | 82436 | 874.0 | 80326 | +2110 | +0.0 | strong |
| Put | 81300 | 20 | 20 | 910.5 | 82436 | 910.5 | 80390 | +2046 | +0.0 | strong |
| Put | 81400 | 40 | 40 | 909.0 | 82700 | 953.3 | 80491 | +1945 | -44.3 | strong |
| Put | 81500 | 1060 | 156 | 890.3 | 82947 | 1027.9 | 80610 | +1826 | -137.6 | strong |
| Put | 81600 | 120 | 120 | 940.6 | 82851 | 1018.2 | 80659 | +1777 | -77.6 | strong |
| Put | 81700 | 640 | 640 | 877.3 | 83342 | 1056.0 | 80823 | +1613 | -178.7 | strong |
| Put | 81800 | 40 | 40 | 1067.5 | 82444 | 1067.5 | 80732 | +1704 | +0.0 | strong |
| Put | 81900 | 800 | 800 | 966.7 | 83123 | 1111.6 | 80933 | +1503 | -144.9 | strong |
| Put | 82000 | 5260 | 3344 | 983.5 | 83140 | 1141.0 | 81017 | +1419 | -157.5 | strong |
| Put | 82100 | 200 | 200 | 984.2 | 83181 | 1183.0 | 81116 | +1320 | -198.7 | strong |
| Put | 82200 | 40 | 40 | 1252.7 | 82444 | 1215.4 | 80947 | +1489 | +37.3 | strong |
| Put | 82300 | 2000 | 2000 | 979.1 | 83457 | 1296.0 | 81321 | +1115 | -316.9 | strong |
| Put | 82400 | 2000 | 2000 | 988.3 | 83554 | 1360.0 | 81412 | +1024 | -371.7 | strong |
| Put | 82500 | 1520 | 1433 | 1169.8 | 83067 | 1367.5 | 81330 | +1106 | -197.8 | strong |
| Put | 82600 | 540 | 540 | 1057.4 | 83368 | 1292.2 | 81543 | +893 | -234.9 | strong |
| Put | 82700 | 500 | 500 | 1198.0 | 83200 | 1398.7 | 81502 | +934 | -200.7 | strong |
| Put | 82800 | 680 | 680 | 1205.1 | 83249 | 1479.7 | 81595 | +841 | -274.5 | strong |
| Put | 82900 | 520 | 520 | 1295.1 | 83129 | 1486.2 | 81605 | +831 | -191.1 | strong |
| Put | 83000 | 9180 | 8384 | 1269.9 | 83339 | 1579.3 | 81730 | +706 | -309.5 | strong |
| Put | 83100 | 580 | 580 | 1313.5 | 83301 | 1631.5 | 81787 | +649 | -318.1 | strong |
| Put | 83200 | 880 | 880 | 1394.6 | 83202 | 1729.5 | 81805 | +631 | -335.0 | strong |
| Put | 83300 | 840 | 840 | 1504.6 | 83049 | 1631.3 | 81795 | +641 | -126.7 | strong |
| Put | 83400 | 1040 | 1040 | 1469.3 | 83258 | 1633.6 | 81931 | +505 | -164.3 | strong |
| Put | 83500 | 1680 | 1349 | 1505.7 | 83309 | 1892.5 | 81994 | +442 | -386.8 | strong |
| Put | 83600 | 1240 | 1240 | 1521.0 | 83328 | 1942.0 | 82079 | +357 | -421.0 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls same · near put wall | 9 | 25% | -0.43% | -1.29 to +0.22% |  | too few (8/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 9 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 9 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 4 | 50% | -0.03% | -0.22 to +0.16% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · near put wall | 3 | 33% | -0.24% | -0.70 to +0.25% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 2 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.14% | -1.14 to +0.86% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 2 | 0% | -0.86% | -1.30 to -0.43% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 2 | 0% | -0.43% | -0.64 to -0.22% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · near put wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.70% | -0.70 to -0.70% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 0% | -1.14% | -1.14 to -1.14% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 0% | -0.28% | -0.28 to -0.28% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 0% | -0.80% | -0.80 to -0.80% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -1.77% | -1.77 to -1.77% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | writers even · few weak writers | 21 | 67% | +0.18% | too few (9/10) |
| intraday | monthly | put writers stronger · weak puts | 14 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | writers even · few weak writers | 14 | 75% | +0.03% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 6 | 17% | +0.06% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 4 | 0% | -0.82% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers | 3 | 0% | -1.77% | too few (1/10) |
| day | monthly | put writers stronger · weak puts | 2 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 2 | 50% | -0.34% | too few (2/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 14 | 0% | -0.21% | too few (3/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 14 | 75% | +0.03% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 11 |  |  | too few (0/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 10 | 67% | +0.18% | too few (9/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 22% | -0.44% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.22% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 4 | 0% | -0.82% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 4 | 0% | -0.21% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 50% | +0.62% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | put writers stronger · weak puts · weekly sideways · 125m sideways | 2 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.34% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 |  |  | too few (0/10) |
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
