# Nifty option chain pattern log
Updated 2026-10-23 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 155 snapshots over 7 trading days
- 167 patterns logged; 95 different patterns so far

## Latest read (2026-10-23 10:45:29)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 4.2 | 22502 | 0.96 | 22700 | 22500 | 23000 | ±1.42% (22182-22821) | 16.81 |
| 2026-11-23 (monthly) | 31.2 | 22496 | 1.415 | 23000 | 22000 | 23000 | ±3.82% (21637-23355) | 16.24 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls up · near put wall`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.21%. Too few outcomes (2/20) to trade on.
  - Writers: `call writers stronger · weak puts`. Seen 23 times before; Nifty was up after it 81% of the time, average +0.22%. History points to a bull call debit spread, ATM to about the call wall 23000.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.44%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · mid walls`. Seen 4 times before; Nifty was up after it 75% of the time, average +0.04%. Too few outcomes (4/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 8 times before; Nifty was up after it 62% of the time, average +0.17%. Too few outcomes (8/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22000; weakest call writers at -, weakest put writers at 22600. Covers 93% of near-money call OI and 89% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22200 | 7117 | 1369 | 578.2 | 22722 | 391.2 | 22778 | +276 | +187.0 | strong |
| Call | 22250 | 2121 | 1411 | 421.3 | 22562 | 351.0 | 22671 | +170 | +70.3 | strong |
| Call | 22300 | 12009 | 5166 | 374.1 | 22572 | 311.8 | 22674 | +172 | +62.3 | strong |
| Call | 22350 | 4556 | 4029 | 350.9 | 22599 | 276.6 | 22701 | +199 | +74.2 | strong |
| Call | 22400 | 25276 | 19191 | 295.4 | 22563 | 241.3 | 22695 | +194 | +54.0 | strong |
| Call | 22450 | 20508 | 20024 | 231.7 | 22526 | 210.0 | 22682 | +180 | +21.7 | strong |
| Call | 22500 | 156691 | 143203 | 213.4 | 22541 | 180.7 | 22713 | +212 | +32.7 | strong |
| Call | 22550 | 72715 | 72250 | 178.7 | 22525 | 153.8 | 22729 | +227 | +24.9 | strong |
| Call | 22600 | 131504 | 127582 | 169.3 | 22558 | 130.6 | 22769 | +268 | +38.8 | strong |
| Call | 22650 | 75840 | 75516 | 142.2 | 22555 | 109.3 | 22792 | +290 | +32.9 | strong |
| Call | 22700 | 216127 | 207086 | 144.6 | 22613 | 91.0 | 22845 | +343 | +53.6 | strong |
| Call | 22750 | 100059 | 97687 | 149.8 | 22691 | 75.4 | 22900 | +398 | +74.4 | strong |
| Call | 22800 | 245964 | 234747 | 129.4 | 22677 | 62.0 | 22929 | +428 | +67.4 | strong |
| Put | 22200 | 115563 | 100252 | 23.4 | 22845 | 48.4 | 22177 | +325 | -25.0 | strong |
| Put | 22250 | 43052 | 40797 | 33.1 | 22744 | 58.5 | 22217 | +285 | -25.4 | strong |
| Put | 22300 | 139122 | 108273 | 38.3 | 22765 | 70.1 | 22262 | +240 | -31.8 | strong |
| Put | 22350 | 51196 | 49526 | 52.3 | 22694 | 83.9 | 22298 | +204 | -31.6 | strong |
| Put | 22400 | 146460 | 132719 | 62.8 | 22703 | 99.8 | 22337 | +165 | -37.1 | strong |
| Put | 22450 | 83658 | 83131 | 84.7 | 22643 | 118.0 | 22365 | +136 | -33.3 | strong |
| Put | 22500 | 245211 | 207097 | 79.8 | 22738 | 138.9 | 22420 | +82 | -59.1 | medium |
| Put | 22550 | 70286 | 69161 | 97.7 | 22707 | 162.2 | 22452 | +49 | -64.6 | weak |
| Put | 22600 | 120496 | 109650 | 105.1 | 22761 | 187.9 | 22495 | +7 | -82.8 | weak |
| Put | 22650 | 51692 | 50858 | 123.0 | 22722 | 217.2 | 22527 | -25 | -94.2 | weak |
| Put | 22700 | 109927 | 102941 | 131.6 | 22749 | 248.4 | 22568 | -67 | -116.9 | weak |
| Put | 22750 | 37064 | 36911 | 155.6 | 22728 | 283.4 | 22594 | -93 | -127.8 | weak |
| Put | 22800 | 94393 | 86574 | 164.9 | 22774 | 317.9 | 22635 | -133 | -152.9 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at -, weakest put writers at 23000. Covers 55% of near-money call OI and 46% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22200 | 2028 | 356 | 772.8 | 22655 | 688.0 | 22973 | +477 | +84.8 | strong |
| Call | 22250 | 133 | 45 | 701.0 | 22641 | 635.0 | 22951 | +455 | +66.0 | strong |
| Call | 22300 | 1302 | 504 | 705.3 | 22662 | 623.0 | 23005 | +510 | +82.3 | strong |
| Call | 22350 | 159 | 90 | 676.9 | 22681 | 560.8 | 23027 | +531 | +116.1 | strong |
| Call | 22400 | 1799 | 432 | 598.5 | 22604 | 557.9 | 22999 | +503 | +40.6 | strong |
| Call | 22450 | 306 | 228 | 588.9 | 22649 | 528.5 | 23039 | +543 | +60.4 | strong |
| Call | 22500 | 22997 | 12356 | 562.5 | 22643 | 496.9 | 23062 | +567 | +65.5 | strong |
| Call | 22550 | 505 | 312 | 518.7 | 22626 | 468.1 | 23069 | +573 | +50.6 | strong |
| Call | 22600 | 26118 | 17515 | 485.0 | 22644 | 440.8 | 23085 | +589 | +44.2 | strong |
| Call | 22650 | 2049 | 1752 | 462.0 | 22669 | 415.3 | 23112 | +616 | +46.7 | strong |
| Call | 22700 | 29893 | 25901 | 455.1 | 22687 | 386.5 | 23155 | +659 | +68.6 | strong |
| Call | 22750 | 1155 | 474 | 425.0 | 22657 | 364.1 | 23175 | +679 | +60.9 | strong |
| Call | 22800 | 21908 | 16379 | 401.8 | 22686 | 340.1 | 23202 | +706 | +61.8 | strong |
| Put | 22200 | 11081 | 2700 | 189.7 | 22748 | 257.2 | 22010 | +485 | -67.5 | strong |
| Put | 22250 | 1832 | 378 | 205.1 | 22760 | 272.4 | 22045 | +451 | -67.3 | strong |
| Put | 22300 | 17135 | 9940 | 228.2 | 22697 | 289.9 | 22072 | +424 | -61.8 | strong |
| Put | 22350 | 858 | 281 | 229.8 | 22739 | 315.6 | 22120 | +376 | -85.8 | strong |
| Put | 22400 | 16223 | 4065 | 251.3 | 22720 | 325.2 | 22149 | +347 | -73.9 | strong |
| Put | 22450 | 636 | 202 | 276.2 | 22681 | 344.2 | 22174 | +322 | -68.0 | strong |
| Put | 22500 | 47436 | 20401 | 269.5 | 22758 | 362.1 | 22231 | +265 | -92.6 | strong |
| Put | 22550 | 871 | 382 | 261.2 | 22826 | 388.4 | 22289 | +207 | -127.2 | strong |
| Put | 22600 | 25864 | 16723 | 344.7 | 22653 | 405.6 | 22255 | +240 | -60.9 | strong |
| Put | 22650 | 2454 | 1905 | 334.0 | 22726 | 426.2 | 22316 | +180 | -92.2 | strong |
| Put | 22700 | 30144 | 23167 | 352.3 | 22717 | 452.8 | 22348 | +148 | -100.5 | strong |
| Put | 22750 | 1228 | 754 | 333.1 | 22814 | 476.1 | 22417 | +79 | -143.0 | medium |
| Put | 22800 | 22170 | 12618 | 396.8 | 22716 | 501.8 | 22403 | +93 | -105.0 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 5 | 75% | +0.04% | -0.21 to +0.17% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.11% | -0.90 to +0.62% |  | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 75% | +0.03% | -0.24 to +0.15% |  | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.21% | +0.13 to +0.29% |  | too few (2/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 3 | 67% | +0.01% | -0.39 to +0.34% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls same · near put wall | 3 | 33% | -0.27% | -0.47 to +0.06% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 0% | -0.82% | -0.86 to -0.78% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.27% | -0.61 to +0.07% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 2 | 100% | +0.28% | +0.27 to +0.29% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls same · mid walls | 2 | 100% | +0.20% | +0.04 to +0.36% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.40% | -0.40 to -0.40% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.82% | -0.82 to -0.82% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.82% | -0.82 to -0.82% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 29 | 59% | -0.08% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 24 | 81% | +0.22% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | weekly | writers even · few weak writers | 15 | 21% | -0.52% | down |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | writers even · weak puts | 9 | 62% | +0.17% | too few (8/10) |
| intraday | weekly | writers even · weak puts | 6 | 50% | -0.18% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 100% | +0.39% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 3 | 0% | -0.44% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.68% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.82% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
