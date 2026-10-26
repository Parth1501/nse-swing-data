# Nifty option chain pattern log
Updated 2026-10-26 11:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 184 snapshots over 8 trading days
- 199 patterns logged; 102 different patterns so far

## Latest read (2026-10-26 11:45:18)

Nifty trend: weekly **bearish**, 125-min **sideways**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 1.2 | 22561 | 1.168 | 22700 | 22500 | 23000 | ±1.08% (22316-22805) | 26.02 |
| 2026-11-23 (monthly) | 28.2 | 22561 | 1.443 | 23000 | 22000 | 23000 | ±3.87% (21688-23433) | 17.45 |

- **Weekly, last 30 min**: `PCR down · call writing · walls same · near put wall`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.37%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 13 times before; Nifty was up after it 58% of the time, average -0.03%. Too few outcomes (12/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 3 times before; Nifty was up after it 67% of the time, average -0.18%. Too few outcomes (3/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.17%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put writing · walls same · mid walls`. Seen 2 times before; Nifty was up after it 50% of the time, average +0.00%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 33 times before; Nifty was up after it 53% of the time, average -0.06%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 7 times before; Nifty was up after it 71% of the time, average +0.00%. Too few outcomes (7/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Nifty was up after it 0% of the time, average -0.37%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at 22300, weakest put writers at 22700. Covers 95% of near-money call OI and 95% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22250 | 3042 | 2764 | 336.6 | 22481 | 383.3 | 22587 | +26 | -46.6 | weak |
| Call | 22300 | 14721 | 12003 | 293.4 | 22477 | 338.7 | 22593 | +33 | -45.3 | weak |
| Call | 22350 | 8467 | 8335 | 249.7 | 22471 | 298.0 | 22600 | +39 | -48.3 | weak |
| Call | 22400 | 43331 | 42081 | 212.5 | 22469 | 257.1 | 22612 | +52 | -44.7 | medium |
| Call | 22450 | 27364 | 27325 | 179.7 | 22478 | 217.9 | 22630 | +69 | -38.3 | medium |
| Call | 22500 | 153857 | 150364 | 165.7 | 22495 | 183.3 | 22666 | +105 | -17.6 | strong |
| Call | 22550 | 69165 | 69085 | 147.1 | 22527 | 150.3 | 22697 | +136 | -3.2 | strong |
| Call | 22600 | 178097 | 176885 | 126.5 | 22527 | 121.0 | 22726 | +166 | +5.5 | strong |
| Call | 22650 | 105975 | 105848 | 116.7 | 22545 | 96.6 | 22767 | +206 | +20.1 | strong |
| Call | 22700 | 244424 | 239350 | 112.0 | 22571 | 76.5 | 22812 | +251 | +35.6 | strong |
| Call | 22750 | 100155 | 99288 | 96.6 | 22593 | 58.4 | 22847 | +286 | +38.2 | strong |
| Call | 22800 | 241859 | 235991 | 89.9 | 22603 | 44.7 | 22890 | +329 | +45.2 | strong |
| Call | 22850 | 84724 | 84159 | 67.8 | 22578 | 34.0 | 22918 | +357 | +33.8 | strong |
| Put | 22250 | 80029 | 78823 | 38.1 | 22573 | 26.2 | 22212 | +349 | +11.9 | strong |
| Put | 22300 | 185511 | 168441 | 44.9 | 22597 | 32.5 | 22255 | +306 | +12.3 | strong |
| Put | 22350 | 107739 | 107055 | 63.2 | 22522 | 40.0 | 22287 | +274 | +23.1 | strong |
| Put | 22400 | 281230 | 273711 | 75.3 | 22543 | 50.2 | 22325 | +236 | +25.1 | strong |
| Put | 22450 | 156710 | 156469 | 88.6 | 22538 | 61.6 | 22361 | +199 | +27.0 | strong |
| Put | 22500 | 365692 | 344215 | 85.8 | 22618 | 75.7 | 22414 | +147 | +10.1 | strong |
| Put | 22550 | 136016 | 135692 | 88.2 | 22615 | 94.0 | 22462 | +99 | -5.8 | medium |
| Put | 22600 | 215681 | 209931 | 93.6 | 22667 | 115.5 | 22506 | +54 | -21.9 | medium |
| Put | 22650 | 75365 | 75120 | 95.6 | 22672 | 139.8 | 22554 | +6 | -44.1 | weak |
| Put | 22700 | 155494 | 151615 | 119.3 | 22689 | 167.6 | 22581 | -20 | -48.3 | weak |
| Put | 22750 | 40118 | 40059 | 138.5 | 22683 | 201.6 | 22611 | -51 | -63.1 | weak |
| Put | 22800 | 82912 | 78367 | 161.4 | 22732 | 237.6 | 22639 | -78 | -76.2 | weak |
| Put | 22850 | 12559 | 12430 | 181.2 | 22738 | 276.8 | 22669 | -108 | -95.6 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22000; weakest call writers at -, weakest put writers at 23200. Covers 59% of near-money call OI and 54% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22250 | 136 | 52 | 694.3 | 22618 | 716.2 | 22944 | +384 | -21.9 | strong |
| Call | 22300 | 1517 | 818 | 664.3 | 22576 | 680.8 | 22964 | +403 | -16.5 | strong |
| Call | 22350 | 171 | 128 | 615.0 | 22557 | 637.1 | 22965 | +404 | -22.1 | strong |
| Call | 22400 | 3412 | 2283 | 544.4 | 22474 | 611.5 | 22944 | +384 | -67.1 | strong |
| Call | 22450 | 422 | 366 | 547.1 | 22546 | 571.8 | 22997 | +436 | -24.6 | strong |
| Call | 22500 | 26182 | 16787 | 541.2 | 22590 | 545.7 | 23041 | +480 | -4.5 | strong |
| Call | 22550 | 891 | 751 | 487.2 | 22527 | 517.3 | 23037 | +476 | -30.1 | strong |
| Call | 22600 | 29689 | 21106 | 476.8 | 22615 | 487.6 | 23077 | +516 | -10.7 | strong |
| Call | 22650 | 5384 | 5089 | 469.2 | 22610 | 467.0 | 23119 | +558 | +2.2 | strong |
| Call | 22700 | 26488 | 23156 | 450.0 | 22673 | 430.0 | 23150 | +589 | +20.0 | strong |
| Call | 22750 | 1219 | 646 | 408.0 | 22603 | 403.4 | 23158 | +597 | +4.5 | strong |
| Call | 22800 | 17785 | 13672 | 396.2 | 22666 | 377.9 | 23196 | +635 | +18.2 | strong |
| Call | 22850 | 1077 | 663 | 376.0 | 22696 | 355.3 | 23226 | +665 | +20.7 | strong |
| Put | 22250 | 1904 | 480 | 220.4 | 22699 | 250.0 | 22030 | +531 | -29.6 | strong |
| Put | 22300 | 17891 | 10970 | 235.6 | 22672 | 269.4 | 22064 | +496 | -33.8 | strong |
| Put | 22350 | 861 | 379 | 256.6 | 22655 | 279.4 | 22093 | +467 | -22.8 | strong |
| Put | 22400 | 18639 | 6645 | 269.0 | 22655 | 302.1 | 22131 | +430 | -33.0 | strong |
| Put | 22450 | 937 | 569 | 310.9 | 22578 | 316.6 | 22139 | +422 | -5.7 | strong |
| Put | 22500 | 54141 | 27467 | 290.3 | 22696 | 335.4 | 22210 | +351 | -45.1 | strong |
| Put | 22550 | 1270 | 866 | 330.4 | 22629 | 355.0 | 22220 | +341 | -24.6 | strong |
| Put | 22600 | 27888 | 18898 | 349.3 | 22639 | 374.9 | 22251 | +310 | -25.7 | strong |
| Put | 22650 | 4775 | 4242 | 360.4 | 22630 | 394.0 | 22290 | +271 | -33.6 | strong |
| Put | 22700 | 30512 | 23926 | 356.7 | 22706 | 419.4 | 22343 | +217 | -62.7 | strong |
| Put | 22750 | 1022 | 671 | 346.4 | 22778 | 438.6 | 22404 | +157 | -92.2 | strong |
| Put | 22800 | 21812 | 13608 | 408.0 | 22688 | 464.9 | 22392 | +169 | -56.8 | strong |
| Put | 22850 | 1556 | 132 | 403.2 | 22741 | 489.3 | 22447 | +114 | -86.1 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 10 | 70% | +0.05% | -0.44 to +0.28% |  | no clear direction |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.40% | -0.37 to +0.89% |  | too few (6/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 6 | 83% | +0.35% | -0.39 to +0.91% |  | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 5 | 100% | +0.44% | +0.09 to +1.02% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 5 | 80% | +0.13% | -0.21 to +0.46% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 25% | -0.30% | -1.22 to +0.39% |  | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 4 | 50% | +0.08% | -0.78 to +0.90% |  | too few (4/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 50% | +0.25% | -0.40 to +0.90% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 75% | +0.15% | -0.24 to +0.56% |  | too few (4/10) |
| weekly | PCR up · put writing · walls same · near put wall | 4 | 50% | -0.15% | -0.47 to +0.19% | 0% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 50% | +0.00% | -0.24 to +0.24% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 3 | 100% | +0.28% | +0.27 to +0.29% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · call writing · walls same · near put wall | 2 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 2 | 50% | +0.24% | -0.07 to +0.54% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.11% | +0.01 to +0.21% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 0% | -0.50% | -0.50 to -0.50% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 0% | -0.49% | -0.49 to -0.49% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.17% | -0.17 to -0.17% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.17% | -0.17 to -0.17% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 34 | 53% | -0.06% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 31 | 86% | +0.35% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · weak puts | 17 | 82% | +0.32% | up |
| intraday | weekly | writers even · few weak writers | 15 | 21% | -0.46% | down |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak puts | 14 | 58% | -0.03% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides | 1 | 0% | -0.49% | too few (1/10) |
| day | monthly | writers even · few weak writers | 4 | 0% | -0.37% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 0% | -0.17% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.39% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 50% | -0.07% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.42% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.41% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 11 | 90% | +0.32% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 62% | +0.05% | too few (8/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 8 | 71% | +0.00% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 8 | 57% | +0.20% | too few (7/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 7 | 43% | -0.11% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 7 | 14% | -0.40% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 4 | 67% | -0.18% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 3 | 0% | -0.20% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.92% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 0% | -0.49% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.27% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 0% | -0.37% | too few (3/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 0% | -0.17% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m sideways | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
