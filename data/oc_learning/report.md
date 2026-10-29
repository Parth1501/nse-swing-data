# Nifty option chain pattern log
Updated 2026-10-29 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 271 snapshots over 11 trading days
- 294 patterns logged; 118 different patterns so far

## Latest read (2026-10-29 14:42:48)

Nifty trend: weekly **bearish**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-03 (weekly) | 5.0 | 22939 | 1.036 | 22850 | 22700 | 23500 | ±1.22% (22659-23219) | 13.14 |
| 2026-11-23 (monthly) | 25.0 | 22939 | 0.999 | 23000 | 22000 | 23500 | ±3.0% (22251-23626) | 14.34 |

- **Weekly, last 30 min**: `PCR up · put writing · walls same · near put wall`. Seen 8 times before; Nifty was up after it 62% of the time, average +0.02%. Too few outcomes (8/20) to trade on.
  - Writers: `put writers stronger · weak calls`. Seen 19 times before; Nifty was up after it 78% of the time, average +0.13%. Too few outcomes (18/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 19 times before; Nifty was up after it 78% of the time, average +0.13%. Too few outcomes (18/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 1 times before; Nifty was up after it 0% of the time, average -1.11%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 1 times before; Nifty was up after it 0% of the time, average -1.11%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · unwinding · walls same · mid walls`. Seen 3 times before; Nifty was up after it 67% of the time, average +0.25%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 79 times before; Nifty was up after it 68% of the time, average +0.17%. History points to a bull call debit spread, ATM to about the call wall 23500.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 23 times before; Nifty was up after it 81% of the time, average +0.27%. History points to a bull call debit spread, ATM to about the call wall 23500.
- **Monthly, today vs previous day**: `PCR down · put writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.65%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 6 times before; Nifty was up after it 33% of the time, average +0.09%. Too few outcomes (6/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 2 times before; Nifty was up after it 50% of the time, average +0.42%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-03

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at 22800, weakest put writers at -. Covers 67% of near-money call OI and 84% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22600 | 19818 | 18278 | 211.2 | 22641 | 398.8 | 22811 | -127 | -187.5 | weak |
| Call | 22650 | 10846 | 10194 | 188.6 | 22661 | 355.4 | 22839 | -100 | -166.8 | weak |
| Call | 22700 | 50322 | 40686 | 166.2 | 22676 | 315.2 | 22866 | -72 | -149.1 | weak |
| Call | 22750 | 18936 | 16434 | 149.8 | 22706 | 276.1 | 22900 | -39 | -126.4 | weak |
| Call | 22800 | 74427 | 51185 | 132.7 | 22718 | 240.1 | 22933 | -6 | -107.4 | weak |
| Call | 22850 | 35863 | 32574 | 128.5 | 22769 | 205.8 | 22978 | +40 | -77.4 | weak |
| Call | 22900 | 76265 | 61630 | 101.2 | 22740 | 174.8 | 23001 | +63 | -73.6 | medium |
| Call | 22950 | 41172 | 38261 | 88.2 | 22745 | 146.0 | 23038 | +100 | -57.8 | medium |
| Call | 23000 | 132308 | 88073 | 59.8 | 22682 | 119.7 | 23060 | +121 | -59.9 | strong |
| Call | 23050 | 34265 | 24655 | 50.2 | 22719 | 96.9 | 23100 | +162 | -46.7 | strong |
| Call | 23100 | 65507 | 36886 | 40.3 | 22702 | 77.2 | 23140 | +202 | -36.9 | strong |
| Call | 23150 | 35597 | 26105 | 35.3 | 22718 | 60.2 | 23185 | +247 | -24.9 | strong |
| Call | 23200 | 92684 | 54082 | 27.9 | 22727 | 46.4 | 23228 | +289 | -18.4 | strong |
| Call | 23250 | 42581 | 32538 | 21.3 | 22693 | 35.1 | 23271 | +333 | -13.9 | strong |
| Put | 22600 | 120393 | 105320 | 131.5 | 22723 | 37.5 | 22468 | +470 | +94.0 | strong |
| Put | 22650 | 63250 | 59342 | 135.8 | 22741 | 45.0 | 22514 | +424 | +90.8 | strong |
| Put | 22700 | 169339 | 139113 | 130.8 | 22777 | 54.4 | 22569 | +369 | +76.5 | strong |
| Put | 22750 | 87180 | 82003 | 132.5 | 22806 | 65.3 | 22618 | +321 | +67.1 | strong |
| Put | 22800 | 155921 | 129157 | 139.0 | 22828 | 79.0 | 22661 | +278 | +60.0 | strong |
| Put | 22850 | 70690 | 68984 | 148.1 | 22846 | 94.8 | 22702 | +237 | +53.3 | strong |
| Put | 22900 | 96141 | 91003 | 155.0 | 22872 | 113.5 | 22745 | +194 | +41.5 | strong |
| Put | 22950 | 32624 | 31820 | 165.8 | 22894 | 134.0 | 22784 | +154 | +31.8 | strong |
| Put | 23000 | 64276 | 52219 | 248.4 | 22832 | 158.8 | 22752 | +187 | +89.5 | strong |
| Put | 23050 | 7782 | 7066 | 251.0 | 22862 | 185.8 | 22799 | +140 | +65.1 | strong |
| Put | 23100 | 15173 | 10017 | 300.9 | 22843 | 216.0 | 22799 | +140 | +84.9 | strong |
| Put | 23150 | 3920 | 3095 | 319.4 | 22868 | 248.9 | 22831 | +108 | +70.4 | strong |
| Put | 23200 | 11563 | 6629 | 396.0 | 22829 | 285.4 | 22804 | +135 | +110.6 | strong |
| Put | 23250 | 1767 | 813 | 379.4 | 22886 | 324.1 | 22871 | +68 | +55.3 | medium |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 22400, weakest put writers at -. Covers 71% of near-money call OI and 73% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22600 | 33166 | 28589 | 456.0 | 22623 | 621.6 | 23056 | +117 | -165.6 | strong |
| Call | 22650 | 3975 | 3800 | 456.9 | 22612 | 582.6 | 23107 | +168 | -125.7 | strong |
| Call | 22700 | 37576 | 35512 | 449.6 | 22691 | 550.5 | 23150 | +211 | -100.9 | strong |
| Call | 22750 | 4315 | 3868 | 394.6 | 22691 | 513.2 | 23145 | +206 | -118.6 | strong |
| Call | 22800 | 30650 | 27118 | 396.6 | 22699 | 481.7 | 23197 | +258 | -85.0 | strong |
| Call | 22850 | 1675 | 1371 | 367.1 | 22712 | 448.6 | 23217 | +278 | -81.5 | strong |
| Call | 22900 | 15000 | 12844 | 355.4 | 22714 | 418.1 | 23255 | +317 | -62.7 | strong |
| Call | 22950 | 3163 | 2503 | 335.7 | 22791 | 387.9 | 23286 | +347 | -52.2 | strong |
| Call | 23000 | 102248 | 64222 | 293.3 | 22668 | 359.4 | 23293 | +355 | -66.1 | strong |
| Call | 23050 | 1645 | 733 | 269.9 | 22700 | 332.9 | 23320 | +381 | -63.0 | strong |
| Call | 23100 | 16822 | 8712 | 277.8 | 22736 | 306.6 | 23378 | +439 | -28.7 | strong |
| Call | 23150 | 1395 | 728 | 234.8 | 22718 | 282.6 | 23385 | +446 | -47.7 | strong |
| Call | 23200 | 22485 | 11202 | 228.1 | 22709 | 257.6 | 23428 | +489 | -29.5 | strong |
| Call | 23250 | 2001 | 1047 | 204.9 | 22750 | 235.1 | 23455 | +516 | -30.2 | strong |
| Put | 22600 | 33505 | 28307 | 344.3 | 22639 | 183.7 | 22256 | +683 | +160.6 | strong |
| Put | 22650 | 5329 | 4909 | 350.1 | 22652 | 197.1 | 22300 | +639 | +153.1 | strong |
| Put | 22700 | 49744 | 44862 | 353.7 | 22707 | 212.1 | 22346 | +592 | +141.6 | strong |
| Put | 22750 | 4983 | 4684 | 336.5 | 22759 | 228.0 | 22414 | +525 | +108.5 | strong |
| Put | 22800 | 38188 | 30624 | 382.4 | 22723 | 243.9 | 22418 | +521 | +138.5 | strong |
| Put | 22850 | 2911 | 1663 | 356.6 | 22798 | 261.9 | 22493 | +445 | +94.7 | strong |
| Put | 22900 | 18742 | 15759 | 416.0 | 22740 | 280.8 | 22484 | +455 | +135.2 | strong |
| Put | 22950 | 1570 | 1314 | 369.8 | 22836 | 299.6 | 22580 | +358 | +70.2 | strong |
| Put | 23000 | 89122 | 54913 | 479.7 | 22733 | 321.4 | 22520 | +418 | +158.3 | strong |
| Put | 23050 | 904 | 600 | 444.6 | 22808 | 342.6 | 22605 | +333 | +102.1 | strong |
| Put | 23100 | 9916 | 5156 | 471.3 | 22833 | 367.3 | 22629 | +310 | +104.0 | strong |
| Put | 23150 | 1247 | 349 | 448.0 | 22896 | 390.5 | 22702 | +237 | +57.5 | strong |
| Put | 23200 | 16046 | 9450 | 560.3 | 22782 | 417.4 | 22640 | +299 | +142.9 | strong |
| Put | 23250 | 640 | 383 | 591.0 | 22757 | 447.0 | 22659 | +280 | +144.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 28 | 67% | +0.17% | -0.44 to +0.76% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · near call wall | 10 | 100% | +0.31% | +0.03 to +0.63% | 50% of 2 | up |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| weekly | PCR up · put writing · walls same · near put wall | 9 | 62% | +0.02% | -0.47 to +0.41% | 50% of 2 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.91% | 100% of 1 | too few (8/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 6 | 75% | +0.17% | -0.12 to +0.71% | 100% of 1 | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| weekly | PCR down · call writing · walls same · near put wall | 6 | 83% | +0.37% | -0.37 to +0.85% | 50% of 2 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 6 | 100% | +0.48% | +0.09 to +1.02% | 100% of 1 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 5 | 60% | +0.12% | -0.07 to +0.32% | 50% of 2 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 5 | 40% | +0.04% | -0.78 to +0.90% | 100% of 1 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls down · mid walls | 4 | 75% | +0.28% | -0.07 to +0.54% | 100% of 1 | too few (4/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 4 | 67% | +0.25% | -0.15 to +0.76% | 100% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% | 100% of 1 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 4 | 67% | +0.06% | -0.05 to +0.15% | 50% of 2 | too few (3/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 100% | +0.57% | +0.24 to +0.85% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 3 | 33% | -0.12% | -0.68 to +0.34% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · near call wall | 3 | 67% | +0.35% | -0.02 to +0.55% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 3 | 67% | +0.16% | -0.02 to +0.37% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 3 | 67% | +0.06% | -0.05 to +0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls up · near put wall | 3 | 67% | +0.24% | -0.01 to +0.36% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 2 | 100% | +0.19% | +0.13 to +0.26% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 50% | +0.10% | -0.16 to +0.36% | 100% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 2 | 100% | +0.78% | +0.70 to +0.86% |  | too few (2/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 1 | 100% | +0.43% | +0.43 to +0.43% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.06% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 80 | 68% | +0.17% | up |
| intraday | weekly | writers even · few weak writers | 35 | 39% | -0.09% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 20 | 78% | +0.13% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | weekly | put writers stronger · few weak writers | 17 | 94% | +0.16% | up |
| intraday | weekly | call writers stronger · few weak writers | 15 | 64% | +0.18% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | weekly | writers even · weak on both sides | 5 | 100% | +0.25% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak calls | 4 | 33% | -0.06% | too few (3/10) |
| day | monthly | writers even · few weak writers | 7 | 33% | +0.09% | too few (6/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | put writers stronger · weak calls | 2 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 2 | 50% | +0.34% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.02% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 24 | 81% | +0.27% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 20 | 78% | +0.13% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 17 | 94% | +0.16% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 12 | 73% | +0.32% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 11 | 40% | -0.01% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
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
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 3 | 50% | +0.42% | too few (2/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 0% | -1.11% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.06% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
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
