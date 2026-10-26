# Nifty option chain pattern log
Updated 2026-10-26 10:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 180 snapshots over 8 trading days
- 195 patterns logged; 102 different patterns so far

## Latest read (2026-10-26 10:45:29)

Nifty trend: weekly **bearish**, 125-min **down**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 1.2 | 22622 | 1.195 | 22700 | 22500 | 23000 | ±1.19% (22352-22891) | 28.4 |
| 2026-11-23 (monthly) | 28.2 | 22615 | 1.417 | 23000 | 22000 | 23000 | ±3.85% (21743-23486) | 17.34 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · near put wall`. Seen 2 times before; Nifty was up after it 50% of the time, average -0.28%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 11 times before; Nifty was up after it 70% of the time, average +0.03%. Too few outcomes (10/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m down`: Seen 7 times before; Nifty was up after it 83% of the time, average +0.18%. Too few outcomes (6/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.07%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m down`: Seen 1 times before; Nifty was up after it 100% of the time, average +0.07%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR up · put writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.24%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 31 times before; Nifty was up after it 57% of the time, average -0.05%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m down`: Seen 17 times before; Nifty was up after it 57% of the time, average -0.04%. Too few outcomes (14/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Nifty was up after it 33% of the time, average -0.29%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m down`: Seen 3 times before; Nifty was up after it 33% of the time, average -0.29%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at 22500, weakest put writers at 22700. Covers 94% of near-money call OI and 94% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 14208 | 11490 | 291.1 | 22473 | 417.4 | 22591 | -30 | -126.3 | weak |
| Call | 22350 | 8399 | 8267 | 249.2 | 22470 | 373.2 | 22599 | -22 | -124.0 | weak |
| Call | 22400 | 43583 | 42319 | 212.2 | 22469 | 329.9 | 22612 | -9 | -117.7 | weak |
| Call | 22450 | 26357 | 26317 | 177.2 | 22472 | 290.1 | 22627 | +6 | -112.9 | weak |
| Call | 22500 | 148143 | 144612 | 164.8 | 22491 | 250.8 | 22665 | +43 | -85.9 | weak |
| Call | 22550 | 37529 | 37449 | 140.5 | 22493 | 213.8 | 22690 | +69 | -73.3 | medium |
| Call | 22600 | 117201 | 115989 | 125.0 | 22504 | 180.0 | 22725 | +103 | -55.0 | strong |
| Call | 22650 | 82760 | 82633 | 117.9 | 22534 | 148.7 | 22768 | +146 | -30.7 | strong |
| Call | 22700 | 201638 | 196564 | 117.6 | 22570 | 120.6 | 22818 | +196 | -3.0 | strong |
| Call | 22750 | 89085 | 88218 | 101.0 | 22596 | 96.0 | 22851 | +229 | +5.0 | strong |
| Call | 22800 | 206370 | 200502 | 97.3 | 22609 | 75.0 | 22897 | +276 | +22.3 | strong |
| Call | 22850 | 79343 | 78775 | 69.6 | 22578 | 58.0 | 22920 | +298 | +11.6 | strong |
| Call | 22900 | 173664 | 169333 | 79.8 | 22644 | 43.9 | 22980 | +358 | +36.0 | strong |
| Call | 22950 | 67338 | 66795 | 74.7 | 22664 | 33.0 | 23025 | +403 | +41.7 | strong |
| Put | 22300 | 186107 | 168302 | 45.4 | 22598 | 27.2 | 22255 | +367 | +18.2 | strong |
| Put | 22350 | 111521 | 110800 | 63.6 | 22521 | 33.4 | 22286 | +335 | +30.3 | strong |
| Put | 22400 | 289627 | 281883 | 75.3 | 22543 | 40.7 | 22325 | +297 | +34.6 | strong |
| Put | 22450 | 164251 | 163993 | 89.2 | 22537 | 49.5 | 22361 | +261 | +39.7 | strong |
| Put | 22500 | 340843 | 319366 | 86.6 | 22621 | 60.6 | 22413 | +208 | +26.0 | strong |
| Put | 22550 | 101224 | 100900 | 87.0 | 22630 | 73.5 | 22463 | +159 | +13.5 | strong |
| Put | 22600 | 245713 | 238723 | 92.5 | 22673 | 89.5 | 22507 | +114 | +3.0 | strong |
| Put | 22650 | 102054 | 101723 | 95.6 | 22672 | 108.2 | 22554 | +67 | -12.6 | medium |
| Put | 22700 | 168961 | 164518 | 117.2 | 22694 | 129.3 | 22583 | +39 | -12.1 | weak |
| Put | 22750 | 56773 | 56689 | 138.5 | 22683 | 155.2 | 22611 | +10 | -16.7 | weak |
| Put | 22800 | 101026 | 95488 | 161.4 | 22732 | 184.0 | 22639 | -17 | -22.6 | weak |
| Put | 22850 | 16890 | 16716 | 181.2 | 22738 | 218.3 | 22669 | -47 | -37.2 | weak |
| Put | 22900 | 44120 | 41870 | 171.8 | 22892 | 253.2 | 22728 | -107 | -81.4 | weak |
| Put | 22950 | 10360 | 10304 | 195.6 | 22879 | 292.2 | 22754 | -133 | -96.7 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23200. Covers 58% of near-money call OI and 53% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 1467 | 768 | 662.8 | 22577 | 733.4 | 22963 | +348 | -70.6 | strong |
| Call | 22350 | 166 | 123 | 614.1 | 22557 | 745.0 | 22964 | +349 | -130.9 | strong |
| Call | 22400 | 3240 | 2111 | 538.4 | 22466 | 661.0 | 22938 | +324 | -122.6 | strong |
| Call | 22450 | 411 | 355 | 545.9 | 22546 | 638.1 | 22996 | +381 | -92.2 | strong |
| Call | 22500 | 25396 | 16001 | 540.5 | 22591 | 598.5 | 23040 | +426 | -58.0 | strong |
| Call | 22550 | 769 | 629 | 477.8 | 22519 | 566.4 | 23028 | +413 | -88.6 | strong |
| Call | 22600 | 29237 | 20654 | 476.6 | 22616 | 532.8 | 23077 | +462 | -56.1 | strong |
| Call | 22650 | 5064 | 4769 | 469.4 | 22613 | 507.9 | 23119 | +505 | -38.5 | strong |
| Call | 22700 | 26192 | 22860 | 450.1 | 22674 | 477.3 | 23150 | +535 | -27.1 | strong |
| Call | 22750 | 1129 | 556 | 407.4 | 22607 | 438.8 | 23157 | +543 | -31.4 | strong |
| Call | 22800 | 17261 | 13148 | 396.8 | 22670 | 418.2 | 23197 | +582 | -21.5 | strong |
| Call | 22850 | 1133 | 698 | 376.0 | 22696 | 390.8 | 23226 | +611 | -14.8 | strong |
| Call | 22900 | 9008 | 6412 | 364.4 | 22714 | 366.4 | 23264 | +650 | -2.0 | strong |
| Call | 22950 | 1214 | 435 | 337.2 | 22691 | 339.1 | 23287 | +672 | -1.9 | strong |
| Put | 22300 | 17819 | 10891 | 235.3 | 22673 | 244.0 | 22065 | +550 | -8.7 | strong |
| Put | 22350 | 812 | 330 | 253.6 | 22667 | 256.8 | 22096 | +518 | -3.2 | strong |
| Put | 22400 | 18595 | 6580 | 268.7 | 22656 | 275.0 | 22131 | +484 | -6.3 | strong |
| Put | 22450 | 741 | 373 | 312.8 | 22578 | 286.0 | 22137 | +478 | +26.8 | strong |
| Put | 22500 | 53793 | 27119 | 289.8 | 22698 | 303.0 | 22210 | +405 | -13.2 | strong |
| Put | 22550 | 1191 | 787 | 328.6 | 22635 | 320.8 | 22221 | +393 | +7.8 | strong |
| Put | 22600 | 27826 | 18836 | 349.2 | 22639 | 338.8 | 22251 | +364 | +10.5 | strong |
| Put | 22650 | 4761 | 4228 | 360.3 | 22630 | 358.1 | 22290 | +325 | +2.2 | strong |
| Put | 22700 | 29968 | 23382 | 355.3 | 22709 | 377.1 | 22345 | +270 | -21.8 | strong |
| Put | 22750 | 1041 | 684 | 346.4 | 22778 | 400.9 | 22404 | +211 | -54.6 | strong |
| Put | 22800 | 20415 | 12211 | 402.5 | 22701 | 420.5 | 22398 | +217 | -18.0 | strong |
| Put | 22850 | 1572 | 132 | 401.9 | 22744 | 441.0 | 22448 | +167 | -39.1 | strong |
| Put | 22900 | 7988 | 4554 | 433.6 | 22721 | 467.6 | 22466 | +148 | -33.9 | strong |
| Put | 22950 | 610 | 227 | 439.0 | 22750 | 513.9 | 22511 | +104 | -74.9 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 9 | 78% | +0.07% | -0.44 to +0.28% |  | too few (9/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.44% | -0.37 to +0.89% |  | too few (6/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 6 | 83% | +0.35% | -0.39 to +0.91% |  | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 5 | 100% | +0.44% | +0.09 to +1.02% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 5 | 80% | +0.13% | -0.21 to +0.46% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 4 | 50% | +0.08% | -0.78 to +0.90% |  | too few (4/10) |
| weekly | PCR up · put writing · walls same · near put wall | 4 | 50% | -0.15% | -0.47 to +0.19% | 0% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 50% | +0.25% | -0.40 to +0.90% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 75% | +0.15% | -0.24 to +0.56% |  | too few (4/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 3 | 100% | +0.28% | +0.27 to +0.29% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 3 | 50% | -0.28% | -1.22 to +0.66% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · mid walls | 2 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · call writing · walls down · mid walls | 2 | 50% | +0.24% | -0.07 to +0.54% |  | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.11% | +0.01 to +0.21% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 0% | -0.26% | -0.26 to -0.26% |  | too few (1/10) |
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
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
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
| weekly | PCR up · put writing · walls up · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 32 | 57% | -0.05% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 31 | 86% | +0.36% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · weak puts | 17 | 82% | +0.35% | up |
| intraday | weekly | writers even · few weak writers | 15 | 21% | -0.46% | down |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak puts | 12 | 70% | +0.03% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides | 1 | 0% | -0.22% | too few (1/10) |
| day | monthly | writers even · few weak writers | 4 | 33% | -0.29% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 100% | +0.07% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.39% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 18 | 57% | -0.04% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.44% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.45% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 11 | 90% | +0.32% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 8 | 57% | +0.20% | too few (7/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 8 | 83% | +0.18% | too few (6/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 7 | 71% | +0.00% | too few (7/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 7 | 43% | -0.11% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 7 | 14% | -0.40% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 3 | 0% | -0.20% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.92% | too few (3/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 3 | 67% | -0.18% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 0% | -0.22% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.27% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 4 | 33% | -0.29% | too few (3/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 2 | 100% | +0.07% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
