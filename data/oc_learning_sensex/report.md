# Sensex option chain pattern log
Updated 2026-11-20 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 6 snapshots over 2 trading days
- 9 patterns logged; 9 different patterns so far

## Latest read (2026-11-20 10:46:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 6.2 | 83174 | 0.935 | 82800 | 82500 | 86000 | ±1.58% (81861-84488) | 15.2 |
| 2026-12-31 (monthly) | 41.2 | 83178 | 0.918 | 82000 | 82000 | 86000 | ±3.88% (79953-86404) | 14.4 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Sensex was up after it 100% of the time, average +0.19%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Sensex was up after it 100% of the time, average +0.19%. Too few outcomes (2/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Sensex was up after it 100% of the time, average +0.19%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Sensex was up after it 100% of the time, average +0.19%. Too few outcomes (2/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.19%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 100% of the time, average +0.19%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 83000, strongest put writers at 82500; weakest call writers at 82000, weakest put writers at 85000. Covers 64% of near-money call OI and 62% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82000 | 132720 | 27135 | 1250.4 | 83022 | 1389.0 | 83250 | +76 | -138.6 | weak |
| Call | 82100 | 18780 | 4686 | 1167.0 | 83023 | 1303.3 | 83267 | +93 | -136.3 | weak |
| Call | 82200 | 28920 | 2112 | 1110.0 | 83023 | 1220.6 | 83310 | +136 | -110.6 | weak |
| Call | 82300 | 40180 | 2863 | 1038.4 | 83023 | 1161.3 | 83338 | +164 | -122.9 | weak |
| Call | 82400 | 44000 | 9005 | 976.5 | 83023 | 1090.3 | 83376 | +202 | -113.9 | medium |
| Call | 82500 | 413780 | 157224 | 908.5 | 83022 | 1030.0 | 83408 | +234 | -121.6 | medium |
| Call | 82600 | 95040 | 71556 | 847.5 | 83023 | 962.9 | 83448 | +273 | -115.4 | medium |
| Call | 82700 | 132260 | 102957 | 791.0 | 83023 | 895.7 | 83491 | +317 | -104.7 | medium |
| Call | 82800 | 315100 | 228560 | 733.2 | 83023 | 834.0 | 83533 | +359 | -100.8 | medium |
| Call | 82900 | 236480 | 166822 | 688.0 | 83022 | 778.0 | 83588 | +414 | -89.9 | strong |
| Call | 83000 | 570480 | 336080 | 662.5 | 83020 | 724.0 | 83662 | +488 | -61.5 | strong |
| Call | 83100 | 292340 | 256180 | 630.2 | 83035 | 673.4 | 83730 | +556 | -43.1 | strong |
| Call | 83200 | 194000 | 163253 | 576.6 | 83051 | 621.5 | 83777 | +602 | -44.9 | strong |
| Call | 83300 | 131860 | 111466 | 518.0 | 83017 | 575.0 | 83818 | +644 | -57.0 | strong |
| Call | 83400 | 111320 | 84064 | 494.1 | 83024 | 529.9 | 83894 | +720 | -35.8 | strong |
| Call | 83500 | 234880 | 125060 | 446.6 | 83020 | 487.9 | 83947 | +772 | -41.3 | strong |
| Call | 83600 | 88080 | 70405 | 416.1 | 83048 | 449.1 | 84016 | +842 | -33.0 | strong |
| Call | 83700 | 99720 | 79328 | 369.4 | 83042 | 412.2 | 84069 | +895 | -42.8 | strong |
| Call | 83800 | 81500 | 56673 | 327.5 | 83021 | 377.9 | 84127 | +953 | -50.4 | strong |
| Call | 83900 | 105940 | 90200 | 311.5 | 83037 | 345.1 | 84211 | +1037 | -33.6 | strong |
| Call | 84000 | 338320 | 195530 | 282.9 | 83023 | 315.2 | 84283 | +1109 | -32.3 | strong |
| Call | 84100 | 57440 | 43740 | 254.5 | 83034 | 286.6 | 84354 | +1180 | -32.1 | strong |
| Call | 84200 | 58120 | 44000 | 229.2 | 83022 | 262.6 | 84429 | +1255 | -33.4 | strong |
| Call | 84300 | 63960 | 49007 | 209.9 | 83014 | 237.8 | 84510 | +1336 | -27.8 | strong |
| Call | 84400 | 69960 | 52074 | 193.9 | 83032 | 216.7 | 84594 | +1420 | -22.7 | strong |
| Put | 82000 | 468500 | 219960 | 314.5 | 83024 | 254.1 | 81686 | +1489 | +60.4 | strong |
| Put | 82100 | 93880 | 43140 | 340.4 | 83026 | 278.9 | 81760 | +1415 | +61.5 | strong |
| Put | 82200 | 143740 | 50480 | 363.4 | 83037 | 303.9 | 81837 | +1338 | +59.5 | strong |
| Put | 82300 | 126240 | 66720 | 401.4 | 83035 | 332.1 | 81899 | +1276 | +69.2 | strong |
| Put | 82400 | 181200 | 120991 | 442.1 | 83022 | 361.1 | 81958 | +1216 | +80.9 | strong |
| Put | 82500 | 682380 | 358320 | 479.1 | 83025 | 392.6 | 82021 | +1154 | +86.5 | strong |
| Put | 82600 | 189520 | 147505 | 516.1 | 83023 | 427.1 | 82084 | +1090 | +89.0 | strong |
| Put | 82700 | 258040 | 204214 | 560.0 | 83023 | 464.9 | 82140 | +1034 | +95.0 | strong |
| Put | 82800 | 408020 | 299992 | 596.5 | 83028 | 506.0 | 82204 | +971 | +90.5 | strong |
| Put | 82900 | 232120 | 184260 | 637.2 | 83030 | 549.1 | 82263 | +912 | +88.1 | strong |
| Put | 83000 | 493380 | 289276 | 653.0 | 83045 | 592.4 | 82347 | +827 | +60.6 | strong |
| Put | 83100 | 139160 | 125040 | 680.2 | 83055 | 640.4 | 82420 | +755 | +39.9 | strong |
| Put | 83200 | 76400 | 67140 | 735.9 | 83077 | 691.8 | 82464 | +710 | +44.1 | strong |
| Put | 83300 | 29240 | 22680 | 803.0 | 83073 | 744.2 | 82497 | +677 | +58.8 | strong |
| Put | 83400 | 28700 | 24100 | 906.6 | 83036 | 796.5 | 82493 | +681 | +110.1 | strong |
| Put | 83500 | 48880 | 32440 | 929.4 | 83073 | 856.2 | 82571 | +604 | +73.2 | strong |
| Put | 83600 | 11060 | 7680 | 1029.2 | 83020 | 919.8 | 82571 | +604 | +109.4 | strong |
| Put | 83700 | 11800 | 8060 | 1022.3 | 83103 | 977.8 | 82678 | +497 | +44.5 | strong |
| Put | 83800 | 7420 | 3860 | 1160.9 | 83042 | 1046.3 | 82639 | +535 | +114.6 | strong |
| Put | 83900 | 5520 | 2160 | 1200.1 | 83062 | 1112.7 | 82700 | +474 | +87.4 | strong |
| Put | 84000 | 22240 | 8660 | 1229.8 | 83051 | 1180.0 | 82770 | +404 | +49.8 | strong |
| Put | 84100 | 2320 | 1800 | 1453.0 | 83046 | 1254.8 | 82647 | +527 | +198.1 | strong |
| Put | 84200 | 1460 | 1340 | 1606.2 | 83029 | 1336.3 | 82594 | +581 | +269.9 | strong |
| Put | 84300 | 1800 | 178 | 1644.4 | 83057 | 1410.0 | 82656 | +519 | +234.4 | strong |
| Put | 84400 | 620 | 601 | 1781.0 | 83023 | 1590.0 | 82619 | +555 | +191.1 | strong |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 83000, strongest put writers at 82000; weakest call writers at -, weakest put writers at -. Covers 38% of near-money call OI and 36% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82000 | 3340 | 380 | 2400.4 | 83014 | 2480.0 | 84400 | +1222 | -79.6 | strong |
| Call | 82200 | 140 | 100 | 2124.2 | 83023 | 2124.2 | 84324 | +1146 | +0.0 | strong |
| Call | 82300 | 100 | 100 | 2134.5 | 83023 | 2134.5 | 84434 | +1256 | +0.0 | strong |
| Call | 82400 | 100 | 100 | 2074.4 | 83023 | 2074.4 | 84474 | +1296 | +0.0 | strong |
| Call | 82800 | 320 | 100 | 1766.7 | 83023 | 1766.7 | 84567 | +1388 | +0.0 | strong |
| Call | 83000 | 2140 | 1113 | 1806.5 | 83101 | 1900.0 | 84807 | +1628 | -93.5 | strong |
| Call | 83100 | 200 | 100 | 1607.8 | 83023 | 1607.8 | 84708 | +1529 | +0.0 | strong |
| Call | 83400 | 180 | 164 | 1484.0 | 83023 | 1620.0 | 84884 | +1706 | -136.1 | strong |
| Call | 83500 | 680 | 136 | 1462.5 | 83023 | 1562.5 | 84962 | +1784 | -100.0 | strong |
| Call | 83600 | 20 | 20 | 1525.5 | 83178 | 1525.5 | 85126 | +1947 | +0.0 | strong |
| Call | 83800 | 20 | 20 | 1414.8 | 83178 | 1414.8 | 85215 | +2036 | +0.0 | strong |
| Call | 83900 | 60 | 20 | 1376.3 | 83178 | 1376.3 | 85276 | +2098 | +0.0 | strong |
| Call | 84000 | 60 | 60 | 1274.2 | 83126 | 1301.8 | 85274 | +2096 | -27.6 | strong |
| Call | 84100 | 40 | 40 | 1280.8 | 83178 | 1280.8 | 85381 | +2202 | +0.0 | strong |
| Call | 84200 | 60 | 40 | 1184.1 | 83101 | 1235.5 | 85384 | +2206 | -51.4 | strong |
| Put | 82000 | 3780 | 680 | 1075.8 | 83029 | 1006.7 | 80924 | +2254 | +69.1 | strong |
| Put | 82700 | 60 | 60 | 1291.6 | 83017 | 1282.5 | 81408 | +1770 | +9.1 | strong |
| Put | 82800 | 60 | 60 | 1330.3 | 83126 | 1318.3 | 81470 | +1709 | +11.9 | strong |
| Put | 82900 | 80 | 80 | 1394.4 | 83062 | 1376.5 | 81506 | +1673 | +17.9 | strong |
| Put | 83000 | 1320 | 427 | 1409.5 | 83014 | 1394.5 | 81590 | +1588 | +15.1 | strong |
| Put | 83100 | 140 | 140 | 1449.2 | 83067 | 1403.8 | 81651 | +1528 | +45.4 | strong |
| Put | 83200 | 200 | 200 | 1531.5 | 83054 | 1494.0 | 81668 | +1510 | +37.6 | strong |
| Put | 83300 | 260 | 260 | 1554.0 | 83033 | 1489.7 | 81746 | +1432 | +64.3 | strong |
| Put | 83400 | 360 | 360 | 1576.2 | 83061 | 1566.0 | 81824 | +1355 | +10.2 | strong |
| Put | 83500 | 1120 | 640 | 1680.4 | 83060 | 1610.0 | 81820 | +1359 | +70.3 | strong |
| Put | 83600 | 160 | 160 | 1620.6 | 83178 | 1620.6 | 81979 | +1199 | +0.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.20% | +0.20 to +0.20% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.19% | +0.19 to +0.19% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.19% | +0.19 to +0.19% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 4 | 100% | +0.19% | too few (2/10) |
| intraday | weekly | writers even · few weak writers | 3 | 100% | +0.19% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts | 1 | 100% | +0.76% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 2 | 100% | +0.19% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +0.19% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 100% | +0.19% | too few (2/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 3 | 100% | +0.19% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 | 100% | +0.76% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.19% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +0.19% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
