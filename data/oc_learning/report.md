# Nifty option chain pattern log
Updated 2026-10-26 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 192 snapshots over 8 trading days
- 207 patterns logged; 103 different patterns so far

## Latest read (2026-10-26 13:45:52)

Nifty trend: weekly **bearish**, 125-min **sideways**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 1.1 | 22660 | 1.084 | 22700 | 22500 | 23000 | ±0.97% (22439-22880) | 22.62 |
| 2026-11-23 (monthly) | 28.1 | 22662 | 1.385 | 23000 | 22000 | 23000 | ±3.77% (21808-23516) | 17.2 |

- **Weekly, last 30 min**: `PCR up · put writing · walls same · near put wall`. Seen 4 times before; Nifty was up after it 50% of the time, average -0.15%. Too few outcomes (4/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 15 times before; Nifty was up after it 21% of the time, average -0.46%. Too few outcomes (14/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 3 times before; Nifty was up after it 0% of the time, average -0.92%. Too few outcomes (3/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.39%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls same · mid walls`. Seen 10 times before; Nifty was up after it 80% of the time, average +0.09%. Too few outcomes (10/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 37 times before; Nifty was up after it 65% of the time, average +0.02%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 11 times before; Nifty was up after it 82% of the time, average +0.12%. Too few outcomes (11/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 3 times before; Nifty was up after it 33% of the time, average -0.22%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at 22500, weakest put writers at 22800. Covers 95% of near-money call OI and 95% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22350 | 8009 | 7887 | 251.3 | 22473 | 388.4 | 22601 | -58 | -137.1 | weak |
| Call | 22400 | 33227 | 32268 | 212.5 | 22469 | 345.6 | 22612 | -47 | -133.1 | weak |
| Call | 22450 | 22301 | 22269 | 180.2 | 22479 | 301.9 | 22630 | -29 | -121.7 | weak |
| Call | 22500 | 122872 | 120082 | 165.7 | 22495 | 259.0 | 22666 | +6 | -93.3 | weak |
| Call | 22550 | 46151 | 46100 | 148.4 | 22530 | 219.8 | 22698 | +39 | -71.4 | weak |
| Call | 22600 | 158474 | 157508 | 128.4 | 22536 | 181.9 | 22728 | +69 | -53.5 | medium |
| Call | 22650 | 126665 | 126550 | 115.9 | 22559 | 147.2 | 22766 | +106 | -31.3 | strong |
| Call | 22700 | 259130 | 254317 | 109.7 | 22575 | 115.1 | 22810 | +150 | -5.4 | strong |
| Call | 22750 | 101090 | 100275 | 94.8 | 22595 | 90.0 | 22845 | +185 | +4.8 | strong |
| Call | 22800 | 242483 | 236890 | 88.0 | 22603 | 68.3 | 22888 | +229 | +19.7 | strong |
| Call | 22850 | 95471 | 94917 | 64.2 | 22583 | 50.8 | 22914 | +255 | +13.4 | strong |
| Call | 22900 | 162074 | 158143 | 78.5 | 22644 | 37.8 | 22979 | +319 | +40.7 | strong |
| Call | 22950 | 76206 | 75682 | 67.1 | 22656 | 27.6 | 23017 | +358 | +39.5 | strong |
| Put | 22350 | 119018 | 118365 | 58.0 | 22536 | 19.1 | 22292 | +367 | +38.9 | strong |
| Put | 22400 | 281368 | 273974 | 74.5 | 22545 | 23.6 | 22325 | +334 | +50.9 | strong |
| Put | 22450 | 173428 | 173194 | 82.7 | 22548 | 29.0 | 22367 | +292 | +53.7 | strong |
| Put | 22500 | 365268 | 344271 | 84.9 | 22618 | 36.5 | 22415 | +244 | +48.5 | strong |
| Put | 22550 | 137689 | 137377 | 87.0 | 22615 | 45.5 | 22463 | +196 | +41.4 | strong |
| Put | 22600 | 288213 | 282463 | 90.0 | 22655 | 57.5 | 22510 | +149 | +32.4 | strong |
| Put | 22650 | 140783 | 140538 | 93.7 | 22653 | 73.0 | 22556 | +103 | +20.8 | strong |
| Put | 22700 | 202438 | 198559 | 116.5 | 22677 | 93.9 | 22583 | +76 | +22.6 | medium |
| Put | 22750 | 44544 | 44490 | 139.1 | 22673 | 117.2 | 22611 | +49 | +21.9 | weak |
| Put | 22800 | 81924 | 77683 | 160.5 | 22728 | 144.4 | 22639 | +20 | +16.1 | weak |
| Put | 22850 | 16440 | 16311 | 182.4 | 22718 | 177.9 | 22668 | -8 | +4.5 | weak |
| Put | 22900 | 42370 | 40269 | 173.4 | 22885 | 212.7 | 22727 | -67 | -39.3 | weak |
| Put | 22950 | 9782 | 9729 | 195.9 | 22878 | 252.7 | 22754 | -95 | -56.8 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23200. Covers 59% of near-money call OI and 55% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22350 | 179 | 136 | 619.0 | 22563 | 683.0 | 22969 | +307 | -64.0 | strong |
| Call | 22400 | 3337 | 2245 | 545.7 | 22475 | 677.3 | 22946 | +284 | -131.6 | strong |
| Call | 22450 | 446 | 391 | 551.4 | 22552 | 625.0 | 23001 | +339 | -73.6 | strong |
| Call | 22500 | 26970 | 17720 | 543.0 | 22591 | 609.5 | 23043 | +381 | -66.5 | strong |
| Call | 22550 | 612 | 531 | 496.6 | 22539 | 573.4 | 23047 | +385 | -76.8 | strong |
| Call | 22600 | 21061 | 14981 | 476.9 | 22615 | 545.4 | 23077 | +415 | -68.5 | strong |
| Call | 22650 | 4555 | 4306 | 469.3 | 22610 | 502.9 | 23119 | +457 | -33.7 | strong |
| Call | 22700 | 24522 | 21459 | 450.1 | 22672 | 482.1 | 23150 | +488 | -32.1 | strong |
| Call | 22750 | 1368 | 797 | 412.9 | 22611 | 436.0 | 23163 | +501 | -23.1 | strong |
| Call | 22800 | 18165 | 14052 | 396.5 | 22665 | 426.4 | 23196 | +534 | -29.9 | strong |
| Call | 22850 | 1092 | 680 | 376.3 | 22695 | 389.1 | 23226 | +564 | -12.8 | strong |
| Call | 22900 | 10235 | 7646 | 361.2 | 22694 | 371.6 | 23261 | +599 | -10.4 | strong |
| Call | 22950 | 1158 | 424 | 336.5 | 22687 | 339.8 | 23286 | +624 | -3.2 | strong |
| Call | 23000 | 90926 | 45022 | 305.1 | 22655 | 321.3 | 23305 | +643 | -16.2 | strong |
| Put | 22350 | 866 | 386 | 256.8 | 22654 | 244.1 | 22093 | +569 | +12.7 | strong |
| Put | 22400 | 19451 | 7464 | 269.1 | 22653 | 261.1 | 22131 | +531 | +8.1 | strong |
| Put | 22450 | 914 | 562 | 310.5 | 22579 | 281.4 | 22139 | +523 | +29.1 | strong |
| Put | 22500 | 56364 | 29690 | 292.0 | 22690 | 288.8 | 22208 | +454 | +3.2 | strong |
| Put | 22550 | 1040 | 719 | 330.9 | 22628 | 307.6 | 22219 | +443 | +23.3 | strong |
| Put | 22600 | 20755 | 14160 | 349.4 | 22638 | 323.4 | 22251 | +412 | +26.0 | strong |
| Put | 22650 | 4273 | 3799 | 360.5 | 22630 | 350.9 | 22290 | +373 | +9.5 | strong |
| Put | 22700 | 29421 | 23121 | 357.0 | 22705 | 361.0 | 22343 | +319 | -4.0 | strong |
| Put | 22750 | 1165 | 818 | 361.7 | 22743 | 387.0 | 22388 | +274 | -25.3 | strong |
| Put | 22800 | 22345 | 14148 | 409.1 | 22685 | 403.5 | 22391 | +271 | +5.5 | strong |
| Put | 22850 | 1601 | 179 | 412.9 | 22717 | 432.9 | 22437 | +225 | -20.0 | strong |
| Put | 22900 | 10367 | 6985 | 458.6 | 22670 | 448.0 | 22441 | +221 | +10.6 | strong |
| Put | 22950 | 551 | 206 | 439.9 | 22748 | 480.7 | 22510 | +152 | -40.8 | strong |
| Put | 23000 | 74837 | 37468 | 491.0 | 22724 | 498.8 | 22509 | +153 | -7.8 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 11 | 80% | +0.09% | -0.44 to +0.36% |  | no clear direction |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 6 | 83% | +0.35% | -0.39 to +0.91% |  | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.48% | -0.37 to +0.89% |  | too few (6/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 5 | 100% | +0.26% | +0.18 to +0.29% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 5 | 100% | +0.44% | +0.09 to +1.02% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% |  | too few (5/10) |
| weekly | PCR up · put writing · walls same · near put wall | 5 | 50% | -0.15% | -0.47 to +0.19% | 0% of 1 | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 5 | 80% | +0.13% | -0.21 to +0.46% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 75% | +0.15% | -0.24 to +0.56% |  | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 50% | +0.25% | -0.40 to +0.90% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls same · near put wall | 4 | 75% | +0.13% | -0.37 to +0.44% | 0% of 1 | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 4 | 50% | +0.08% | -0.78 to +0.90% |  | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.03% | -1.22 to +0.82% |  | too few (4/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 100% | +0.30% | +0.21 to +0.45% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% |  | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · call writing · walls down · mid walls | 2 | 50% | +0.24% | -0.07 to +0.54% |  | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.11% | +0.01 to +0.21% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.25% | +0.15 to +0.36% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 0% | -0.06% | -0.06 to -0.06% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 38 | 65% | +0.02% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 31 | 86% | +0.36% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · weak puts | 17 | 82% | +0.38% | up |
| intraday | weekly | writers even · weak puts | 17 | 81% | +0.13% | up |
| intraday | weekly | writers even · few weak writers | 16 | 21% | -0.46% | down |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides | 1 | 0% | -0.05% | too few (1/10) |
| day | monthly | writers even · few weak writers | 4 | 33% | -0.22% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · few weak writers | 2 | 0% | -0.39% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +0.26% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 62% | +0.01% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.45% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 12 | 82% | +0.12% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.48% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 11 | 90% | +0.32% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.22% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 8 | 57% | +0.20% | too few (7/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 7 | 43% | -0.11% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 7 | 14% | -0.40% | too few (7/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 7 | 86% | +0.10% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 4 | 0% | -0.92% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 3 | 0% | -0.20% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 0% | -0.05% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.27% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.22% | too few (3/10) |
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
| day | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.26% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
