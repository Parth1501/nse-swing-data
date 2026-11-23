# Sensex option chain pattern log
Updated 2026-11-23 11:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 22 snapshots over 3 trading days
- 41 patterns logged; 29 different patterns so far

## Latest read (2026-11-23 11:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 3.2 | 83104 | 0.838 | 83300 | 79000 | 88000 | ±1.5% (81857-84351) | 20.21 |
| 2026-12-31 (monthly) | 38.2 | 83104 | 2.21 | 83300 | 83000 | 87900 | ±3.67% (80053-86155) | 14.09 |

- **Weekly, last 30 min**: `PCR up · put writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 1 times before; Sensex was up after it 0% of the time, average -0.34%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 0% of the time, average -0.34%. Too few outcomes (1/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put writing · walls same · near put wall`. Seen 5 times before; Sensex was up after it 50% of the time, average -0.06%. Too few outcomes (4/20) to trade on.
  - Writers: `put writers stronger · few weak writers`. Seen 5 times before; Sensex was up after it 40% of the time, average +0.20%. Too few outcomes (5/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 5 times before; Sensex was up after it 40% of the time, average +0.20%. Too few outcomes (5/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85000, strongest put writers at 81000; weakest call writers at 82000, weakest put writers at 84000. Covers 88% of near-money call OI and 83% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 81900 | 8960 | 711 | 1438.9 | 83168 | 1527.0 | 83339 | +235 | -88.1 | medium |
| Call | 82000 | 95660 | 23627 | 1283.2 | 83060 | 1286.0 | 83283 | +179 | -2.9 | weak |
| Call | 82100 | 9800 | 2862 | 1198.5 | 83088 | 1211.9 | 83298 | +195 | -13.4 | medium |
| Call | 82200 | 19820 | 1503 | 1111.2 | 83026 | 1140.5 | 83311 | +207 | -29.3 | medium |
| Call | 82300 | 27860 | 3582 | 1124.7 | 83179 | 1064.5 | 83425 | +321 | +60.2 | medium |
| Call | 82400 | 22380 | 6252 | 1032.6 | 83127 | 998.9 | 83433 | +329 | +33.7 | medium |
| Call | 82500 | 131520 | 54004 | 915.3 | 83038 | 933.4 | 83415 | +311 | -18.1 | medium |
| Call | 82600 | 42180 | 34357 | 901.5 | 83127 | 868.1 | 83501 | +397 | +33.3 | strong |
| Call | 82700 | 74920 | 61517 | 836.1 | 83107 | 809.2 | 83536 | +432 | +26.9 | strong |
| Call | 82800 | 104340 | 78070 | 753.3 | 83063 | 750.7 | 83553 | +449 | +2.6 | strong |
| Call | 82900 | 85060 | 64671 | 730.1 | 83111 | 699.7 | 83630 | +526 | +30.4 | strong |
| Call | 83000 | 293200 | 212164 | 714.0 | 83173 | 645.0 | 83714 | +610 | +69.0 | strong |
| Call | 83100 | 156260 | 147919 | 666.2 | 83194 | 599.0 | 83766 | +662 | +67.2 | strong |
| Call | 83200 | 250620 | 245335 | 675.8 | 83320 | 552.0 | 83876 | +772 | +123.8 | strong |
| Call | 83300 | 271640 | 266911 | 604.4 | 83286 | 506.8 | 83904 | +800 | +97.7 | strong |
| Call | 83400 | 308800 | 299986 | 599.0 | 83337 | 469.5 | 83999 | +895 | +129.5 | strong |
| Call | 83500 | 693300 | 651504 | 572.5 | 83379 | 431.1 | 84073 | +969 | +141.4 | strong |
| Call | 83600 | 282940 | 277719 | 560.2 | 83406 | 395.2 | 84160 | +1056 | +164.9 | strong |
| Call | 83700 | 274800 | 267391 | 552.3 | 83466 | 363.5 | 84252 | +1148 | +188.8 | strong |
| Call | 83800 | 239400 | 224715 | 529.0 | 83473 | 333.2 | 84329 | +1225 | +195.8 | strong |
| Call | 83900 | 206580 | 198161 | 506.0 | 83508 | 305.3 | 84406 | +1302 | +200.7 | strong |
| Call | 84000 | 791300 | 679319 | 393.6 | 83354 | 280.1 | 84394 | +1290 | +113.6 | strong |
| Call | 84100 | 171420 | 162284 | 397.4 | 83428 | 257.9 | 84497 | +1393 | +139.4 | strong |
| Call | 84200 | 210760 | 204639 | 389.5 | 83476 | 233.4 | 84590 | +1486 | +156.1 | strong |
| Call | 84300 | 236700 | 227296 | 344.3 | 83444 | 216.5 | 84644 | +1540 | +127.8 | strong |
| Put | 81900 | 102580 | 74973 | 214.9 | 83315 | 208.3 | 81685 | +1419 | +6.6 | strong |
| Put | 82000 | 473440 | 298662 | 254.4 | 83229 | 231.1 | 81746 | +1358 | +23.3 | strong |
| Put | 82100 | 91860 | 58167 | 290.6 | 83154 | 257.2 | 81809 | +1295 | +33.5 | strong |
| Put | 82200 | 141640 | 78474 | 305.1 | 83189 | 284.8 | 81895 | +1209 | +20.3 | strong |
| Put | 82300 | 140000 | 106504 | 292.5 | 83379 | 315.1 | 82008 | +1096 | -22.6 | strong |
| Put | 82400 | 139420 | 103608 | 387.2 | 83165 | 347.6 | 82013 | +1091 | +39.6 | strong |
| Put | 82500 | 339780 | 187389 | 461.5 | 83065 | 383.6 | 82038 | +1066 | +77.9 | strong |
| Put | 82600 | 127480 | 102491 | 487.1 | 83104 | 419.8 | 82113 | +991 | +67.3 | strong |
| Put | 82700 | 206780 | 181353 | 459.6 | 83260 | 461.3 | 82240 | +864 | -1.7 | strong |
| Put | 82800 | 260800 | 200889 | 570.5 | 83074 | 504.9 | 82230 | +874 | +65.5 | strong |
| Put | 82900 | 155380 | 131631 | 585.2 | 83136 | 550.0 | 82315 | +789 | +35.2 | strong |
| Put | 83000 | 426980 | 280813 | 622.0 | 83111 | 597.0 | 82378 | +726 | +25.0 | strong |
| Put | 83100 | 202640 | 195122 | 597.0 | 83256 | 647.8 | 82503 | +601 | -50.7 | strong |
| Put | 83200 | 280980 | 275013 | 632.3 | 83294 | 704.6 | 82568 | +536 | -72.4 | strong |
| Put | 83300 | 221140 | 217565 | 670.8 | 83317 | 762.6 | 82629 | +475 | -91.9 | strong |
| Put | 83400 | 160980 | 158490 | 679.1 | 83407 | 820.0 | 82721 | +383 | -140.9 | strong |
| Put | 83500 | 423540 | 411583 | 672.2 | 83510 | 877.4 | 82828 | +276 | -205.1 | medium |
| Put | 83600 | 116040 | 114477 | 686.8 | 83587 | 949.1 | 82913 | +191 | -262.4 | medium |
| Put | 83700 | 109720 | 107677 | 653.8 | 83699 | 1016.1 | 83046 | +58 | -362.4 | weak |
| Put | 83800 | 141560 | 139465 | 658.2 | 83759 | 1080.0 | 83142 | -38 | -421.8 | weak |
| Put | 83900 | 133200 | 130968 | 682.1 | 83798 | 1155.2 | 83218 | -114 | -473.1 | weak |
| Put | 84000 | 181520 | 171359 | 798.6 | 83727 | 1224.0 | 83201 | -97 | -425.4 | weak |
| Put | 84100 | 50140 | 49797 | 996.3 | 83544 | 1312.8 | 83104 | +0 | -316.6 | weak |
| Put | 84200 | 37800 | 37717 | 1016.4 | 83615 | 1370.8 | 83184 | -80 | -354.4 | weak |
| Put | 84300 | 47260 | 46295 | 1083.3 | 83614 | 1461.0 | 83217 | -113 | -377.7 | weak |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 84000, strongest put writers at 83000; weakest call writers at -, weakest put writers at 85500. Covers 78% of near-money call OI and 88% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82000 | 3060 | 489 | 2571.6 | 83246 | 2468.2 | 84572 | +1468 | +103.3 | strong |
| Call | 82200 | 140 | 100 | 2124.2 | 83023 | 2124.2 | 84324 | +1220 | +0.0 | strong |
| Call | 82300 | 100 | 100 | 2134.5 | 83023 | 2134.5 | 84434 | +1331 | +0.0 | strong |
| Call | 82400 | 100 | 100 | 2074.4 | 83023 | 2074.4 | 84474 | +1370 | +0.0 | strong |
| Call | 82500 | 580 | 536 | 2250.0 | 83384 | 2250.1 | 84750 | +1646 | -0.1 | strong |
| Call | 82800 | 320 | 100 | 1766.7 | 83023 | 1766.7 | 84567 | +1463 | +0.0 | strong |
| Call | 83000 | 1740 | 1553 | 2173.2 | 83592 | 1942.2 | 85173 | +2069 | +231.0 | strong |
| Call | 83100 | 80 | 40 | 1607.8 | 83023 | 1786.2 | 84708 | +1604 | -178.4 | strong |
| Call | 83200 | 120 | 15 | 2180.4 | 83732 | 2129.1 | 85380 | +2276 | +51.4 | strong |
| Call | 83300 | 120 | 120 | 1645.2 | 83295 | 1641.2 | 84945 | +1841 | +4.0 | strong |
| Call | 83400 | 460 | 449 | 1582.3 | 83297 | 1595.2 | 84982 | +1878 | -12.8 | strong |
| Call | 83500 | 1100 | 763 | 1701.6 | 83311 | 1686.1 | 85202 | +2098 | +15.5 | strong |
| Call | 83600 | 420 | 420 | 1605.3 | 83390 | 1552.7 | 85205 | +2101 | +52.6 | strong |
| Call | 83700 | 1060 | 1060 | 1614.9 | 83340 | 1532.2 | 85315 | +2211 | +82.6 | strong |
| Call | 83800 | 260 | 260 | 1583.3 | 83374 | 1556.5 | 85383 | +2279 | +26.9 | strong |
| Call | 83900 | 760 | 724 | 1457.4 | 83284 | 1410.2 | 85357 | +2253 | +47.2 | strong |
| Call | 84000 | 2520 | 2520 | 1515.3 | 83429 | 1443.2 | 85515 | +2411 | +72.2 | strong |
| Call | 84100 | 160 | 160 | 1477.4 | 83460 | 1392.3 | 85577 | +2473 | +85.0 | strong |
| Call | 84200 | 600 | 586 | 1320.8 | 83321 | 1387.7 | 85521 | +2417 | -66.9 | strong |
| Call | 84300 | 140 | 140 | 1278.0 | 83161 | 1256.5 | 85578 | +2474 | +21.6 | strong |
| Put | 81900 | 600 | 600 | 920.2 | 83350 | 954.4 | 80980 | +2124 | -34.2 | strong |
| Put | 82000 | 6440 | 3573 | 948.9 | 83311 | 975.5 | 81051 | +2053 | -26.6 | strong |
| Put | 82100 | 200 | 200 | 962.1 | 83263 | 949.2 | 81138 | +1966 | +12.9 | strong |
| Put | 82300 | 2080 | 2080 | 979.1 | 83457 | 1077.9 | 81321 | +1783 | -98.8 | strong |
| Put | 82400 | 1980 | 1980 | 976.8 | 83589 | 1116.6 | 81423 | +1681 | -139.8 | strong |
| Put | 82500 | 1560 | 1392 | 1040.7 | 83470 | 1140.0 | 81459 | +1645 | -99.3 | strong |
| Put | 82600 | 480 | 480 | 1029.1 | 83460 | 1111.6 | 81571 | +1533 | -82.5 | strong |
| Put | 82700 | 420 | 420 | 1159.7 | 83349 | 1192.3 | 81540 | +1564 | -32.6 | strong |
| Put | 82800 | 620 | 620 | 1182.8 | 83320 | 1135.8 | 81617 | +1487 | +47.0 | strong |
| Put | 82900 | 460 | 460 | 1277.4 | 83200 | 1272.0 | 81623 | +1481 | +5.4 | strong |
| Put | 83000 | 9600 | 8757 | 1266.6 | 83348 | 1360.5 | 81733 | +1371 | -93.9 | strong |
| Put | 83100 | 580 | 580 | 1313.5 | 83301 | 1265.2 | 81787 | +1317 | +48.3 | strong |
| Put | 83200 | 880 | 880 | 1380.6 | 83241 | 1349.7 | 81819 | +1285 | +31.0 | strong |
| Put | 83300 | 720 | 720 | 1476.0 | 83133 | 1439.1 | 81824 | +1280 | +36.9 | strong |
| Put | 83400 | 980 | 980 | 1459.8 | 83287 | 1411.0 | 81940 | +1164 | +48.8 | strong |
| Put | 83500 | 2100 | 1686 | 1505.7 | 83309 | 1583.3 | 81994 | +1110 | -77.6 | strong |
| Put | 83600 | 1260 | 1260 | 1521.0 | 83328 | 1462.5 | 82079 | +1025 | +58.5 | strong |
| Put | 83700 | 740 | 740 | 1565.1 | 83321 | 1661.2 | 82135 | +969 | -96.1 | strong |
| Put | 83800 | 760 | 760 | 1526.0 | 83478 | 1655.7 | 82274 | +830 | -129.6 | strong |
| Put | 83900 | 440 | 425 | 1519.5 | 83554 | 1658.2 | 82381 | +723 | -138.7 | strong |
| Put | 84000 | 1540 | 1540 | 1636.6 | 83546 | 1820.0 | 82363 | +741 | -183.4 | strong |
| Put | 84100 | 1140 | 1140 | 1593.2 | 83618 | 1673.3 | 82507 | +597 | -80.1 | strong |
| Put | 84200 | 440 | 440 | 1541.5 | 83800 | 1625.6 | 82659 | +445 | -84.1 | strong |
| Put | 84300 | 600 | 600 | 1651.7 | 83738 | 1954.8 | 82648 | +456 | -303.1 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls same · near put wall | 6 | 50% | -0.06% | -0.49 to +0.22% |  | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 3 | 67% | +0.04% | -0.07 to +0.16% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.93% | +0.89 to +0.97% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | +0.26% | -0.34 to +0.86% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.91% | +0.86 to +0.97% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.13% | +0.03 to +0.22% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| monthly | PCR up · put writing · walls down · near put wall | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.08% | +1.08 to +1.08% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.48% | +0.48 to +0.48% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.50% | -0.50 to -0.50% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.97% | -0.97 to -0.97% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 14 | 75% | +0.17% | no clear direction |
| intraday | weekly | writers even · few weak writers | 10 | 67% | +0.45% | too few (9/10) |
| intraday | weekly | writers even · weak calls | 7 | 71% | -0.10% | too few (7/10) |
| intraday | monthly | put writers stronger · few weak writers | 6 | 40% | +0.20% | too few (5/10) |
| intraday | weekly | call writers stronger · few weak writers | 2 | 0% | -0.34% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts | 1 | 100% | +1.66% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 2 | 50% | +0.05% | too few (2/10) |
| day | monthly | put writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.97% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +1.08% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 14 | 75% | +0.17% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 10 | 67% | +0.45% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 7 | 71% | -0.10% | too few (7/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 6 | 40% | +0.20% | too few (5/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 2 | 0% | -0.34% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | +0.05% | too few (2/10) |
| day | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 | 0% | -0.97% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +1.08% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
