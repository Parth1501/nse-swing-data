# Nifty option chain pattern log
Updated 2026-10-28 13:57 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 242 snapshots over 10 trading days
- 262 patterns logged; 113 different patterns so far

## Latest read (2026-10-28 13:26:31)

Nifty trend: weekly **bearish**, 125-min **sideways**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-03 (weekly) | 6.1 | 22730 | 1.003 | 22700 | 20050 | 23000 | ±1.64% (22358-23102) | 16.02 |
| 2026-11-23 (monthly) | 26.1 | 22727 | 1.18 | 23000 | 22000 | 23500 | ±3.34% (21969-23486) | 15.56 |

- **Weekly, last 30 min**: `PCR flat · quiet OI · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 27 times before; Nifty was up after it 38% of the time, average -0.19%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 15 times before; Nifty was up after it 47% of the time, average -0.09%. Too few outcomes (15/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.39%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls same · mid walls`. Seen 18 times before; Nifty was up after it 67% of the time, average +0.15%. Too few outcomes (18/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 63 times before; Nifty was up after it 69% of the time, average +0.13%. History points to a bull call debit spread, ATM to about the call wall 23500.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 33 times before; Nifty was up after it 72% of the time, average +0.18%. History points to a bull call debit spread, ATM to about the call wall 23500.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · mid walls`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.22%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 5 times before; Nifty was up after it 20% of the time, average -0.07%. Too few outcomes (5/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 1 times before; Nifty was up after it 0% of the time, average -0.02%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-11-03

Strongest call writers at 23000, strongest put writers at 22600; weakest call writers at 22500, weakest put writers at -. Covers 57% of near-money call OI and 60% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 13410 | 6989 | 296.3 | 22577 | 374.6 | 22696 | -34 | -78.4 | weak |
| Call | 22450 | 5565 | 4719 | 265.2 | 22575 | 338.4 | 22715 | -15 | -73.1 | weak |
| Call | 22500 | 36633 | 27938 | 238.1 | 22578 | 303.0 | 22738 | +8 | -64.9 | weak |
| Call | 22550 | 17912 | 17234 | 218.4 | 22593 | 270.8 | 22768 | +38 | -52.4 | weak |
| Call | 22600 | 52349 | 47224 | 201.1 | 22610 | 238.7 | 22801 | +71 | -37.6 | medium |
| Call | 22650 | 26164 | 23646 | 175.7 | 22614 | 210.1 | 22826 | +96 | -34.3 | medium |
| Call | 22700 | 92771 | 59328 | 147.0 | 22596 | 182.7 | 22847 | +117 | -35.7 | strong |
| Call | 22750 | 47988 | 32721 | 139.6 | 22632 | 157.1 | 22890 | +160 | -17.5 | strong |
| Call | 22800 | 91855 | 39744 | 111.6 | 22608 | 134.1 | 22912 | +182 | -22.4 | strong |
| Call | 22850 | 29405 | 19936 | 97.7 | 22620 | 113.5 | 22948 | +218 | -15.8 | strong |
| Call | 22900 | 56706 | 32088 | 80.8 | 22608 | 95.0 | 22981 | +251 | -14.3 | strong |
| Call | 22950 | 29474 | 24590 | 70.8 | 22620 | 78.7 | 23021 | +291 | -7.8 | strong |
| Call | 23000 | 130323 | 65675 | 55.5 | 22598 | 64.3 | 23056 | +326 | -8.8 | strong |
| Call | 23050 | 27519 | 13138 | 47.0 | 22625 | 52.0 | 23097 | +367 | -5.0 | strong |
| Put | 22400 | 78179 | 46794 | 106.2 | 22640 | 83.5 | 22294 | +436 | +22.7 | strong |
| Put | 22450 | 33412 | 25871 | 134.2 | 22620 | 96.7 | 22316 | +414 | +37.5 | strong |
| Put | 22500 | 128736 | 85695 | 153.0 | 22616 | 111.6 | 22347 | +383 | +41.4 | strong |
| Put | 22550 | 56181 | 48644 | 176.6 | 22615 | 128.5 | 22373 | +357 | +48.1 | strong |
| Put | 22600 | 118033 | 88979 | 198.1 | 22614 | 146.8 | 22402 | +328 | +51.3 | strong |
| Put | 22650 | 51083 | 43632 | 190.6 | 22659 | 167.6 | 22459 | +271 | +23.0 | strong |
| Put | 22700 | 104035 | 54136 | 189.3 | 22694 | 190.3 | 22511 | +219 | -1.0 | strong |
| Put | 22750 | 35225 | 24827 | 190.1 | 22725 | 214.6 | 22560 | +170 | -24.5 | strong |
| Put | 22800 | 52234 | 15205 | 210.6 | 22728 | 242.2 | 22589 | +141 | -31.6 | strong |
| Put | 22850 | 7123 | 3424 | 255.1 | 22706 | 271.4 | 22595 | +135 | -16.4 | strong |
| Put | 22900 | 12509 | 3381 | 306.4 | 22686 | 303.1 | 22594 | +136 | +3.3 | strong |
| Put | 22950 | 2799 | 1335 | 353.6 | 22671 | 335.9 | 22596 | +134 | +17.8 | strong |
| Put | 23000 | 30418 | 13373 | 470.0 | 22595 | 371.6 | 22530 | +200 | +98.4 | strong |
| Put | 23050 | 2275 | 1166 | 431.8 | 22673 | 408.7 | 22618 | +112 | +23.1 | strong |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23150. Covers 72% of near-money call OI and 69% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 3667 | 2769 | 553.0 | 22525 | 598.7 | 22953 | +226 | -45.7 | strong |
| Call | 22450 | 704 | 652 | 569.1 | 22596 | 561.5 | 23019 | +292 | +7.6 | strong |
| Call | 22500 | 33555 | 25933 | 524.7 | 22603 | 535.5 | 23025 | +298 | -10.9 | strong |
| Call | 22550 | 1503 | 1434 | 490.3 | 22615 | 505.4 | 23040 | +313 | -15.2 | strong |
| Call | 22600 | 34882 | 29770 | 454.5 | 22617 | 472.5 | 23055 | +327 | -18.0 | strong |
| Call | 22650 | 4286 | 4096 | 457.0 | 22611 | 438.9 | 23107 | +380 | +18.1 | strong |
| Call | 22700 | 43757 | 41267 | 450.4 | 22690 | 414.0 | 23150 | +423 | +36.4 | strong |
| Call | 22750 | 2609 | 2137 | 403.9 | 22662 | 384.8 | 23154 | +427 | +19.1 | strong |
| Call | 22800 | 29324 | 25379 | 403.0 | 22693 | 358.1 | 23203 | +476 | +44.9 | strong |
| Call | 22850 | 1668 | 1301 | 363.6 | 22685 | 335.2 | 23214 | +487 | +28.4 | strong |
| Call | 22900 | 14817 | 12347 | 358.8 | 22701 | 307.9 | 23259 | +532 | +50.9 | strong |
| Call | 22950 | 1736 | 1048 | 338.6 | 22712 | 285.0 | 23289 | +562 | +53.5 | strong |
| Call | 23000 | 102462 | 61631 | 294.2 | 22656 | 264.2 | 23294 | +567 | +29.9 | strong |
| Call | 23050 | 1603 | 625 | 271.6 | 22681 | 242.2 | 23322 | +595 | +29.4 | strong |
| Put | 22400 | 19895 | 9050 | 262.6 | 22665 | 240.0 | 22137 | +590 | +22.6 | strong |
| Put | 22450 | 1240 | 932 | 293.6 | 22621 | 253.5 | 22156 | +571 | +40.1 | strong |
| Put | 22500 | 69289 | 44120 | 293.8 | 22675 | 272.1 | 22206 | +521 | +21.7 | strong |
| Put | 22550 | 1870 | 1592 | 320.0 | 22644 | 288.0 | 22230 | +497 | +32.0 | strong |
| Put | 22600 | 36353 | 30369 | 348.0 | 22633 | 307.8 | 22252 | +475 | +40.2 | strong |
| Put | 22650 | 5434 | 4992 | 354.2 | 22645 | 330.0 | 22296 | +431 | +24.2 | strong |
| Put | 22700 | 52328 | 46859 | 356.1 | 22705 | 350.0 | 22344 | +383 | +6.1 | strong |
| Put | 22750 | 4320 | 4005 | 341.8 | 22754 | 373.7 | 22408 | +319 | -31.9 | strong |
| Put | 22800 | 30462 | 22667 | 398.0 | 22702 | 393.4 | 22402 | +325 | +4.7 | strong |
| Put | 22850 | 2241 | 923 | 395.7 | 22747 | 417.9 | 22454 | +273 | -22.1 | strong |
| Put | 22900 | 16524 | 13405 | 436.4 | 22711 | 444.0 | 22464 | +263 | -7.6 | strong |
| Put | 22950 | 714 | 439 | 434.0 | 22749 | 472.9 | 22516 | +211 | -38.8 | strong |
| Put | 23000 | 88266 | 52038 | 485.0 | 22728 | 495.5 | 22515 | +212 | -10.5 | strong |
| Put | 23050 | 746 | 432 | 476.6 | 22767 | 528.3 | 22573 | +154 | -51.7 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 19 | 67% | +0.15% | -0.44 to +0.76% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · near call wall | 9 | 100% | +0.30% | +0.03 to +0.58% | 50% of 2 | too few (9/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 8 | 100% | +0.38% | +0.05 to +0.70% |  | too few (6/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 7 | 86% | +0.32% | -0.39 to +0.91% | 100% of 1 | too few (7/10) |
| weekly | PCR up · put writing · walls same · near put wall | 7 | 57% | -0.03% | -0.47 to +0.41% | 50% of 2 | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 7 | 86% | +0.16% | -0.21 to +0.46% | 100% of 1 | too few (7/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.30% | -0.24 to +0.76% | 100% of 1 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 6 | 75% | +0.20% | -0.12 to +0.84% | 100% of 1 | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 5 | 100% | +0.44% | +0.09 to +1.02% | 100% of 1 | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 5 | 40% | +0.04% | -0.78 to +0.90% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near put wall | 5 | 80% | +0.35% | -0.37 to +0.85% | 50% of 2 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 4 | 100% | +0.19% | +0.06 to +0.32% | 50% of 2 | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 4 | 67% | +0.06% | -0.05 to +0.15% | 50% of 2 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 50% of 2 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 3 | 67% | +0.16% | -0.02 to +0.37% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 3 | 33% | -0.07% | -0.68 to +0.48% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · mid walls | 3 | 67% | +0.23% | -0.07 to +0.54% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 3 | 67% | +0.06% | -0.05 to +0.21% | 100% of 1 | too few (3/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 100% | +0.57% | +0.24 to +0.85% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 3 | 67% | +0.29% | -0.03 to +0.76% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 2 | 100% | +0.26% | +0.13 to +0.40% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 50% | +0.17% | -0.02 to +0.36% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% | 100% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 1 | 100% | +0.72% | +0.72 to +0.72% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.77% | +0.77 to +0.77% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 0% | -0.22% | -0.34 to -0.10% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.10% | -0.10 to -0.10% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 64 | 69% | +0.13% | up |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | weekly | writers even · few weak writers | 28 | 38% | -0.19% | no clear direction |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.46% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | weekly | call writers stronger · few weak writers | 15 | 64% | +0.22% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | weekly | writers even · weak on both sides | 5 | 100% | +0.25% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak calls | 4 | 33% | -0.06% | too few (3/10) |
| day | monthly | writers even · few weak writers | 6 | 20% | -0.07% | too few (5/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · few weak writers | 2 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.29% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.02% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 34 | 72% | +0.18% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 18 | 76% | +0.13% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 16 | 47% | -0.09% | no clear direction |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 12 | 73% | +0.37% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 11 | 60% | +0.05% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 7 | 14% | -0.40% | too few (7/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.20% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 1 | 0% | -0.10% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.10% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
