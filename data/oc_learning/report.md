# Nifty option chain pattern log
Updated 2026-10-23 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 161 snapshots over 7 trading days
- 175 patterns logged; 95 different patterns so far

## Latest read (2026-10-23 12:45:34)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 4.1 | 22398 | 0.971 | 22650 | 22000 | 23000 | ±1.35% (22096-22699) | 16.01 |
| 2026-11-23 (monthly) | 31.1 | 22397 | 1.446 | 23000 | 22000 | 23000 | ±3.81% (21544-23250) | 16.13 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · mid walls`. Seen 3 times before; Nifty was up after it 0% of the time, average -0.80%. Too few outcomes (3/20) to trade on.
  - Writers: `call writers stronger · weak puts`. Seen 27 times before; Nifty was up after it 64% of the time, average +0.11%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.44%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR up · quiet OI · walls same · mid walls`. Seen 4 times before; Nifty was up after it 50% of the time, average -0.06%. Too few outcomes (4/20) to trade on.
  - Writers: `call writers stronger · weak puts`. Seen 3 times before; Nifty was up after it 67% of the time, average +0.21%. Too few outcomes (3/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22000; weakest call writers at -, weakest put writers at 22500. Covers 94% of near-money call OI and 90% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22100 | 1907 | 1192 | 633.7 | 22678 | 393.6 | 22734 | +336 | +240.0 | strong |
| Call | 22150 | 753 | 541 | 506.1 | 22581 | 353.0 | 22656 | +258 | +153.1 | strong |
| Call | 22200 | 8601 | 2853 | 459.0 | 22574 | 314.7 | 22659 | +261 | +144.3 | strong |
| Call | 22250 | 3016 | 2306 | 375.2 | 22510 | 277.6 | 22625 | +228 | +97.6 | strong |
| Call | 22300 | 18461 | 11726 | 314.4 | 22493 | 241.9 | 22614 | +217 | +72.5 | strong |
| Call | 22350 | 11366 | 10839 | 276.1 | 22492 | 209.0 | 22626 | +228 | +67.1 | strong |
| Call | 22400 | 72891 | 66806 | 231.2 | 22473 | 178.8 | 22631 | +234 | +52.4 | strong |
| Call | 22450 | 72962 | 72478 | 196.5 | 22471 | 151.4 | 22646 | +249 | +45.1 | strong |
| Call | 22500 | 217351 | 203863 | 197.4 | 22516 | 127.2 | 22697 | +300 | +70.2 | strong |
| Call | 22550 | 75644 | 75199 | 174.1 | 22517 | 105.9 | 22724 | +326 | +68.2 | strong |
| Call | 22600 | 164232 | 160310 | 157.4 | 22536 | 87.8 | 22757 | +360 | +69.5 | strong |
| Call | 22650 | 85054 | 84730 | 136.1 | 22542 | 72.0 | 22786 | +389 | +64.2 | strong |
| Call | 22700 | 238814 | 229773 | 138.1 | 22598 | 59.1 | 22838 | +441 | +79.0 | strong |
| Put | 22100 | 74690 | 69251 | 21.6 | 22743 | 38.3 | 22078 | +319 | -16.7 | strong |
| Put | 22150 | 40062 | 38904 | 23.0 | 22759 | 47.4 | 22127 | +271 | -24.4 | strong |
| Put | 22200 | 130959 | 115648 | 27.1 | 22791 | 58.1 | 22173 | +225 | -31.0 | strong |
| Put | 22250 | 53474 | 51228 | 39.1 | 22679 | 70.1 | 22211 | +187 | -31.0 | strong |
| Put | 22300 | 132741 | 106304 | 43.4 | 22721 | 85.3 | 22257 | +141 | -41.9 | strong |
| Put | 22350 | 74611 | 72941 | 63.4 | 22618 | 102.1 | 22287 | +111 | -38.7 | strong |
| Put | 22400 | 189402 | 175661 | 74.7 | 22636 | 123.0 | 22325 | +72 | -48.2 | medium |
| Put | 22450 | 96958 | 96482 | 92.8 | 22603 | 144.4 | 22357 | +40 | -51.6 | weak |
| Put | 22500 | 215526 | 183543 | 83.0 | 22724 | 169.5 | 22417 | -19 | -86.5 | weak |
| Put | 22550 | 51303 | 50519 | 100.8 | 22696 | 199.8 | 22449 | -52 | -99.0 | weak |
| Put | 22600 | 107546 | 98057 | 107.0 | 22755 | 229.8 | 22493 | -95 | -122.8 | weak |
| Put | 22650 | 36930 | 36334 | 123.0 | 22722 | 265.0 | 22527 | -129 | -141.9 | weak |
| Put | 22700 | 93825 | 87862 | 131.6 | 22749 | 300.9 | 22568 | -171 | -169.4 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at -, weakest put writers at 23000. Covers 59% of near-money call OI and 48% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22100 | 299 | 113 | 797.3 | 22596 | 700.0 | 22897 | +501 | +97.3 | strong |
| Call | 22150 | 38 | 29 | 720.8 | 22500 | 665.0 | 22871 | +474 | +55.8 | strong |
| Call | 22200 | 2157 | 485 | 739.1 | 22599 | 617.0 | 22939 | +542 | +122.2 | strong |
| Call | 22250 | 136 | 48 | 696.1 | 22629 | 597.5 | 22946 | +549 | +98.6 | strong |
| Call | 22300 | 1420 | 622 | 684.0 | 22623 | 555.0 | 22984 | +587 | +129.0 | strong |
| Call | 22350 | 172 | 105 | 658.8 | 22649 | 529.0 | 23009 | +612 | +129.8 | strong |
| Call | 22400 | 2483 | 1116 | 547.5 | 22497 | 494.9 | 22947 | +551 | +52.5 | strong |
| Call | 22450 | 450 | 372 | 554.9 | 22573 | 468.0 | 23005 | +608 | +86.9 | strong |
| Call | 22500 | 25586 | 14945 | 545.5 | 22609 | 436.2 | 23046 | +649 | +109.3 | strong |
| Call | 22550 | 563 | 371 | 502.5 | 22592 | 408.3 | 23052 | +656 | +94.2 | strong |
| Call | 22600 | 27798 | 19195 | 478.7 | 22627 | 384.6 | 23079 | +682 | +94.0 | strong |
| Call | 22650 | 2076 | 1779 | 461.0 | 22666 | 361.0 | 23111 | +714 | +100.0 | strong |
| Call | 22700 | 30771 | 26779 | 452.3 | 22679 | 336.2 | 23152 | +755 | +116.1 | strong |
| Put | 22100 | 5827 | 2446 | 165.6 | 22755 | 250.0 | 21934 | +462 | -84.4 | strong |
| Put | 22150 | 759 | 286 | 179.4 | 22740 | 267.3 | 21971 | +426 | -87.9 | strong |
| Put | 22200 | 11121 | 2850 | 194.7 | 22730 | 282.2 | 22005 | +391 | -87.6 | strong |
| Put | 22250 | 1836 | 393 | 209.0 | 22745 | 298.4 | 22041 | +356 | -89.5 | strong |
| Put | 22300 | 17010 | 9983 | 230.2 | 22691 | 318.1 | 22070 | +327 | -88.0 | strong |
| Put | 22350 | 851 | 313 | 243.9 | 22696 | 337.0 | 22106 | +291 | -93.1 | strong |
| Put | 22400 | 16666 | 4508 | 260.7 | 22691 | 358.0 | 22139 | +258 | -97.3 | strong |
| Put | 22450 | 663 | 241 | 290.5 | 22643 | 376.0 | 22159 | +237 | -85.5 | strong |
| Put | 22500 | 49465 | 22430 | 279.5 | 22731 | 400.0 | 22221 | +176 | -120.5 | strong |
| Put | 22550 | 825 | 372 | 268.5 | 22806 | 421.1 | 22282 | +115 | -152.7 | strong |
| Put | 22600 | 26571 | 17479 | 348.5 | 22644 | 448.7 | 22252 | +145 | -100.2 | strong |
| Put | 22650 | 2390 | 1855 | 334.1 | 22725 | 467.0 | 22316 | +81 | -132.9 | medium |
| Put | 22700 | 30037 | 23135 | 353.4 | 22715 | 496.0 | 22347 | +50 | -142.6 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 5 | 60% | -0.06% | -0.44 to +0.17% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.20% | -1.34 to +0.62% |  | too few (5/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 5 | 50% | -0.06% | -0.39 to +0.34% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 4 | 0% | -0.80% | -1.32 to -0.30% |  | too few (3/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 4 | 25% | -0.17% | -0.38 to +0.25% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 50% | -0.08% | -0.35 to +0.15% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | -0.02% | -0.46 to +0.29% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 67% | +0.08% | -0.17 to +0.36% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls same · near put wall | 3 | 33% | -0.27% | -0.47 to +0.06% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 0% | -0.50% | -0.61 to -0.39% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 2 | 100% | +0.28% | +0.27 to +0.29% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · mid walls | 2 | 0% | -0.21% | -0.36 to -0.07% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.40% | -0.40 to -0.40% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
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
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
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
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -1.28% | -1.28 to -1.28% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.28% | -1.28 to -1.28% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 29 | 59% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 28 | 64% | +0.11% | no clear direction |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | weekly | writers even · few weak writers | 15 | 21% | -0.58% | down |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | writers even · weak puts | 11 | 36% | -0.01% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts | 6 | 50% | -0.18% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | call writers stronger · weak puts | 4 | 67% | +0.21% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| day | weekly | call writers stronger · weak puts | 3 | 0% | -0.44% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.91% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | call writers stronger · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -1.28% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
