# Nifty option chain pattern log
Updated 2026-11-06 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 401 snapshots over 17 trading days
- 441 patterns logged; 152 different patterns so far

## Latest read (2026-11-06 09:45:08)

Nifty trend: weekly **bearish**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-09 (weekly) | 3.2 | 24584 | 0.884 | 24450 | 24500 | 25000 | ±1.4% (24240-24927) | 19.48 |
| 2026-11-23 (monthly) | 17.2 | 24574 | 0.805 | 23800 | 23000 | 25000 | ±2.6% (23935-25213) | 15.1 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls up · near put wall`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.81%. Too few outcomes (2/20) to trade on.
  - Writers: `put writers stronger · few weak writers`. Seen 25 times before; Nifty was up after it 91% of the time, average +0.15%. History points to a bull call debit spread, ATM to about the call wall 25000.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 25 times before; Nifty was up after it 91% of the time, average +0.15%. History points to a bull call debit spread, ATM to about the call wall 25000.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. Seen 3 times before; Nifty was up after it 100% of the time, average +0.95%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 3 times before; Nifty was up after it 100% of the time, average +0.95%. Too few outcomes (3/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · unwinding · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 41 times before; Nifty was up after it 82% of the time, average +0.45%. History points to a bull call debit spread, ATM to about the call wall 25000.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 41 times before; Nifty was up after it 82% of the time, average +0.45%. History points to a bull call debit spread, ATM to about the call wall 25000.
- **Monthly, today vs previous day**: `PCR flat · unwinding · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.41%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 2 times before; Nifty was up after it 100% of the time, average +0.41%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-09

Strongest call writers at 25000, strongest put writers at 24500; weakest call writers at 24400, weakest put writers at 25300. Covers 83% of near-money call OI and 99% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24250 | 8828 | 7030 | 63.7 | 23900 | 349.9 | 24314 | -270 | -286.2 | weak |
| Call | 24300 | 47372 | 32340 | 130.3 | 24162 | 313.5 | 24430 | -153 | -183.2 | weak |
| Call | 24350 | 24312 | 23160 | 151.6 | 24320 | 278.5 | 24502 | -82 | -127.0 | weak |
| Call | 24400 | 67779 | 59313 | 170.6 | 24416 | 244.7 | 24571 | -13 | -74.0 | weak |
| Call | 24450 | 48485 | 46854 | 154.7 | 24435 | 214.2 | 24605 | +21 | -59.5 | weak |
| Call | 24500 | 189957 | 152192 | 144.7 | 24424 | 186.0 | 24645 | +61 | -41.3 | medium |
| Call | 24550 | 133824 | 130603 | 125.9 | 24456 | 160.2 | 24676 | +92 | -34.3 | medium |
| Call | 24600 | 175323 | 148727 | 109.8 | 24468 | 136.6 | 24710 | +126 | -26.8 | strong |
| Call | 24650 | 74825 | 70924 | 78.9 | 24408 | 116.5 | 24729 | +145 | -37.7 | strong |
| Call | 24700 | 148567 | 110734 | 72.5 | 24407 | 98.2 | 24772 | +189 | -25.7 | strong |
| Call | 24750 | 54642 | 51752 | 47.3 | 24323 | 82.2 | 24797 | +214 | -34.8 | strong |
| Call | 24800 | 139316 | 99589 | 40.9 | 24380 | 68.4 | 24841 | +257 | -27.5 | strong |
| Call | 24850 | 43418 | 41205 | 32.0 | 24267 | 56.6 | 24882 | +298 | -24.6 | strong |
| Call | 24900 | 72147 | 56241 | 27.5 | 24273 | 46.4 | 24927 | +344 | -18.9 | strong |
| Call | 24950 | 35579 | 33324 | 24.5 | 24361 | 37.9 | 24975 | +391 | -13.4 | strong |
| Put | 24250 | 76672 | 76659 | 82.5 | 24480 | 69.6 | 24167 | +416 | +12.9 | strong |
| Put | 24300 | 161863 | 161520 | 101.6 | 24467 | 81.9 | 24198 | +385 | +19.7 | strong |
| Put | 24350 | 104294 | 104294 | 126.7 | 24435 | 96.5 | 24223 | +360 | +30.1 | strong |
| Put | 24400 | 206253 | 206166 | 136.2 | 24485 | 114.0 | 24264 | +320 | +22.1 | strong |
| Put | 24450 | 113156 | 113156 | 139.1 | 24540 | 132.2 | 24311 | +273 | +6.8 | strong |
| Put | 24500 | 231391 | 228053 | 160.4 | 24539 | 153.7 | 24340 | +244 | +6.7 | strong |
| Put | 24550 | 91593 | 91593 | 169.9 | 24556 | 177.9 | 24380 | +203 | -8.0 | strong |
| Put | 24600 | 68494 | 68428 | 204.9 | 24551 | 206.8 | 24395 | +188 | -1.8 | strong |
| Put | 24650 | 11656 | 11656 | 236.5 | 24528 | 234.8 | 24413 | +170 | +1.8 | strong |
| Put | 24700 | 15186 | 15148 | 278.5 | 24522 | 266.4 | 24422 | +162 | +12.1 | strong |
| Put | 24750 | 5553 | 5549 | 302.2 | 24521 | 299.6 | 24448 | +136 | +2.6 | strong |
| Put | 24800 | 7153 | 7045 | 359.1 | 24513 | 337.0 | 24441 | +143 | +22.1 | strong |
| Put | 24850 | 1523 | 1492 | 411.0 | 24497 | 374.1 | 24439 | +145 | +36.8 | strong |
| Put | 24900 | 2424 | 2390 | 447.7 | 24510 | 414.1 | 24452 | +131 | +33.6 | strong |
| Put | 24950 | 763 | 746 | 470.8 | 24523 | 456.3 | 24479 | +104 | +14.5 | medium |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 25000, strongest put writers at 24000; weakest call writers at 24000, weakest put writers at -. Covers 88% of near-money call OI and 91% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24250 | 1035 | 985 | 68.2 | 23238 | 518.0 | 24318 | -256 | -449.8 | weak |
| Call | 24300 | 12830 | 11398 | 160.8 | 23640 | 482.7 | 24461 | -113 | -321.9 | weak |
| Call | 24350 | 1348 | 1310 | 171.5 | 23928 | 448.7 | 24522 | -53 | -277.2 | weak |
| Call | 24400 | 20196 | 19578 | 232.1 | 24070 | 418.4 | 24632 | +58 | -186.2 | medium |
| Call | 24450 | 2473 | 2430 | 200.2 | 24117 | 388.4 | 24650 | +76 | -188.1 | medium |
| Call | 24500 | 50486 | 42695 | 144.8 | 23773 | 360.3 | 24645 | +71 | -215.5 | medium |
| Call | 24550 | 3695 | 3634 | 233.2 | 24234 | 333.4 | 24783 | +209 | -100.2 | strong |
| Call | 24600 | 17986 | 17316 | 171.6 | 24116 | 305.7 | 24772 | +198 | -134.1 | strong |
| Call | 24650 | 1533 | 1494 | 148.6 | 24093 | 279.9 | 24799 | +225 | -131.3 | strong |
| Call | 24700 | 9239 | 8897 | 103.3 | 23892 | 257.2 | 24803 | +229 | -153.9 | strong |
| Call | 24750 | 1763 | 1716 | 147.4 | 24187 | 233.4 | 24897 | +323 | -86.0 | strong |
| Call | 24800 | 13084 | 12389 | 92.9 | 24002 | 212.6 | 24893 | +319 | -119.7 | strong |
| Call | 24850 | 2135 | 2134 | 44.9 | 23808 | 193.2 | 24895 | +321 | -148.3 | strong |
| Call | 24900 | 7264 | 7196 | 69.0 | 24058 | 174.8 | 24969 | +395 | -105.8 | strong |
| Put | 24250 | 1047 | 1038 | 287.3 | 24288 | 193.8 | 23963 | +611 | +93.4 | strong |
| Put | 24300 | 17496 | 17330 | 325.2 | 24263 | 208.8 | 23975 | +599 | +116.4 | strong |
| Put | 24350 | 1912 | 1902 | 270.5 | 24370 | 225.8 | 24079 | +495 | +44.7 | strong |
| Put | 24400 | 25869 | 25768 | 291.4 | 24378 | 243.4 | 24109 | +465 | +47.9 | strong |
| Put | 24450 | 2136 | 2129 | 295.9 | 24424 | 262.9 | 24154 | +420 | +33.0 | strong |
| Put | 24500 | 54259 | 46265 | 711.2 | 23937 | 281.4 | 23789 | +785 | +429.8 | strong |
| Put | 24550 | 1910 | 1864 | 304.8 | 24503 | 305.7 | 24245 | +329 | -0.9 | strong |
| Put | 24600 | 8168 | 8106 | 520.8 | 24250 | 327.0 | 24079 | +495 | +193.8 | strong |
| Put | 24650 | 599 | 592 | 381.2 | 24456 | 352.4 | 24269 | +305 | +28.8 | strong |
| Put | 24700 | 5117 | 4243 | 780.4 | 24014 | 378.7 | 23920 | +654 | +401.7 | strong |
| Put | 24750 | 268 | 262 | 437.9 | 24473 | 409.0 | 24312 | +262 | +28.9 | strong |
| Put | 24800 | 7278 | 7132 | 605.0 | 24272 | 436.1 | 24195 | +379 | +168.9 | strong |
| Put | 24850 | 141 | 135 | 611.4 | 24316 | 483.3 | 24239 | +335 | +128.1 | strong |
| Put | 24900 | 1391 | 1375 | 549.4 | 24443 | 497.9 | 24351 | +223 | +51.5 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 34 | 73% | +0.26% | -0.44 to +0.97% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 15 | 93% | +0.31% | -0.02 to +0.62% | 33% of 3 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 12 | 100% | +0.54% | +0.09 to +1.02% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near put wall | 11 | 64% | +0.05% | -0.47 to +0.42% | 33% of 3 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near call wall | 10 | 40% | -0.10% | -0.71 to +0.45% | 100% of 1 | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near call wall | 9 | 100% | +0.41% | +0.20 to +0.68% |  | too few (9/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| weekly | PCR down · call writing · walls same · near put wall | 8 | 88% | +0.36% | -0.37 to +0.85% | 33% of 3 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 8 | 57% | +0.11% | -0.07 to +0.32% | 33% of 3 | too few (7/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 7 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 7 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 7 | 80% | +0.21% | -0.12 to +0.71% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put writing · walls same · near call wall | 6 | 50% | +0.23% | -0.40 to +0.73% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put writing · walls same · mid walls | 6 | 100% | +0.65% | +0.24 to +0.85% | 100% of 1 | too few (6/10) |
| monthly | PCR down · call writing · walls same · near call wall | 6 | 80% | +0.09% | -0.78 to +0.58% | 100% of 1 | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 6 | 50% | +0.08% | -0.74 to +0.62% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 6 | 80% | +0.04% | -0.18 to +0.19% |  | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 6 | 50% | +0.17% | -0.78 to +0.90% | 100% of 1 | too few (6/10) |
| weekly | PCR up · put writing · walls up · near put wall | 6 | 50% | +0.12% | -0.13 to +0.35% | 0% of 2 | too few (6/10) |
| monthly | PCR down · call writing · walls same · mid walls | 5 | 60% | +0.05% | -0.47 to +0.49% | 100% of 1 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 5 | 75% | +0.21% | -0.05 to +0.63% | 50% of 2 | too few (4/10) |
| weekly | PCR down · call writing · walls down · mid walls | 5 | 80% | +0.31% | -0.07 to +0.54% | 50% of 2 | too few (5/10) |
| monthly | PCR flat · put writing · walls same · near call wall | 5 | 100% | +0.52% | +0.41 to +0.67% |  | too few (5/10) |
| weekly | PCR down · call writing · walls same · mid walls | 5 | 100% | +0.46% | +0.04 to +0.75% | 33% of 3 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near call wall | 5 | 80% | +0.53% | -0.02 to +0.91% | 50% of 2 | too few (5/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls down · near call wall | 4 | 75% | +0.32% | -0.06 to +0.58% | 100% of 1 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | +0.10% | -0.68 to +0.75% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 4 | 75% | +0.16% | -1.11 to +0.78% | 0% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR up · put writing · walls up · mid walls | 4 | 75% | +0.33% | -0.16 to +0.65% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 4 | 100% | +0.35% | +0.13 to +0.59% | 0% of 2 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 3 | 33% | +0.13% | -0.02 to +0.43% | 0% of 2 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 33% | -0.17% | -0.75 to +0.38% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 3 | 67% | +0.16% | -0.11 to +0.50% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 3 | 67% | +0.24% | -0.22 to +0.68% | 100% of 2 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 3 | 100% | +0.81% | +0.59 to +1.03% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · near call wall | 3 | 100% | +0.49% | +0.15 to +0.69% | 50% of 2 | too few (3/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 3 | 100% | +0.50% | +0.37 to +0.62% |  | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 0% | -0.44% | -0.69 to -0.20% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 2 | 100% | +0.50% | +0.47 to +0.53% | 50% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 2 | 50% | +0.16% | -0.57 to +0.89% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.89% | +0.89 to +0.89% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 | 100% | +0.53% | +0.53 to +0.53% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 100% | +0.58% | +0.58 to +0.58% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +1.01% | -0.39 to +2.40% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.19% | +0.19 to +0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.19% | +0.19 to +0.19% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 94 | 70% | +0.17% | up |
| intraday | weekly | put writers stronger · weak calls | 50 | 74% | +0.29% | up |
| intraday | weekly | writers even · few weak writers | 50 | 57% | +0.03% | no clear direction |
| intraday | monthly | put writers stronger · weak calls | 42 | 82% | +0.45% | up |
| intraday | monthly | writers even · weak calls | 41 | 92% | +0.26% | up |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | weekly | put writers stronger · few weak writers | 26 | 91% | +0.15% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | call writers stronger · few weak writers | 19 | 72% | +0.30% | no clear direction |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | weekly | writers even · weak calls | 18 | 88% | +0.47% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | weekly | writers even · weak on both sides | 6 | 100% | +0.36% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| day | monthly | writers even · few weak writers | 8 | 50% | +0.34% | too few (8/10) |
| day | monthly | writers even · weak calls | 4 | 75% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · few weak writers | 4 | 100% | +0.95% | too few (3/10) |
| day | monthly | put writers stronger · weak calls | 3 | 100% | +0.41% | too few (2/10) |
| day | weekly | put writers stronger · weak calls | 3 | 67% | +0.37% | too few (3/10) |
| day | weekly | writers even · few weak writers | 3 | 67% | +1.02% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak calls | 2 | 50% | +0.09% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 50 | 74% | +0.29% | up |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 42 | 82% | +0.45% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 41 | 92% | +0.26% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 26 | 91% | +0.15% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 26 | 75% | +0.18% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.59% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m up | 1 | 100% | +0.91% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 4 | 100% | +0.95% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 100% | +0.41% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m up | 1 | 100% | +0.19% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.22% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
