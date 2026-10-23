# Nifty option chain pattern log
Updated 2026-10-23 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 165 snapshots over 7 trading days
- 179 patterns logged; 96 different patterns so far

## Latest read (2026-10-23 13:45:44)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 4.1 | 22568 | 0.932 | 22700 | 22500 | 23000 | ±1.37% (22259-22877) | 15.43 |
| 2026-11-23 (monthly) | 31.1 | 22553 | 1.331 | 23000 | 22000 | 23000 | ±3.8% (21696-23410) | 15.95 |

- **Weekly, last 30 min**: `PCR flat · unwinding · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. Seen 6 times before; Nifty was up after it 50% of the time, average -0.18%. Too few outcomes (6/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · put writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.01%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 11 times before; Nifty was up after it 73% of the time, average +0.24%. Too few outcomes (11/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at 22300, weakest put writers at 22700. Covers 93% of near-money call OI and 90% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22250 | 3010 | 2419 | 356.6 | 22487 | 430.1 | 22607 | +39 | -73.5 | weak |
| Call | 22300 | 18346 | 12691 | 299.9 | 22472 | 389.4 | 22600 | +32 | -89.6 | weak |
| Call | 22350 | 11396 | 11020 | 258.2 | 22464 | 349.8 | 22608 | +40 | -91.6 | weak |
| Call | 22400 | 53308 | 49550 | 223.3 | 22460 | 308.9 | 22623 | +55 | -85.6 | medium |
| Call | 22450 | 42965 | 42698 | 193.9 | 22466 | 271.4 | 22644 | +76 | -77.5 | medium |
| Call | 22500 | 148136 | 138943 | 197.4 | 22516 | 233.8 | 22697 | +130 | -36.4 | strong |
| Call | 22550 | 53965 | 53647 | 174.1 | 22517 | 203.1 | 22724 | +156 | -29.0 | strong |
| Call | 22600 | 131342 | 128459 | 151.8 | 22525 | 172.6 | 22752 | +184 | -20.8 | strong |
| Call | 22650 | 62588 | 62366 | 131.8 | 22532 | 145.8 | 22782 | +214 | -14.0 | strong |
| Call | 22700 | 202944 | 195324 | 137.5 | 22597 | 121.5 | 22837 | +270 | +16.0 | strong |
| Call | 22750 | 84248 | 82463 | 139.8 | 22663 | 99.7 | 22890 | +322 | +40.1 | strong |
| Call | 22800 | 201800 | 193278 | 123.0 | 22657 | 80.9 | 22923 | +355 | +42.0 | strong |
| Call | 22850 | 79230 | 78241 | 95.3 | 22627 | 64.8 | 22945 | +377 | +30.5 | strong |
| Call | 22900 | 157322 | 151468 | 102.2 | 22696 | 53.0 | 23002 | +434 | +49.1 | strong |
| Put | 22250 | 42845 | 41046 | 39.1 | 22679 | 35.4 | 22211 | +357 | +3.8 | strong |
| Put | 22300 | 127980 | 103619 | 45.2 | 22704 | 43.0 | 22255 | +313 | +2.2 | strong |
| Put | 22350 | 73756 | 72370 | 68.1 | 22582 | 51.7 | 22282 | +286 | +16.4 | strong |
| Put | 22400 | 173005 | 160650 | 75.3 | 22632 | 62.7 | 22325 | +243 | +12.6 | strong |
| Put | 22450 | 82529 | 82126 | 92.7 | 22603 | 74.5 | 22357 | +211 | +18.2 | strong |
| Put | 22500 | 233537 | 204701 | 84.3 | 22694 | 89.8 | 22416 | +152 | -5.4 | strong |
| Put | 22550 | 59799 | 59135 | 102.3 | 22661 | 106.2 | 22448 | +120 | -4.0 | strong |
| Put | 22600 | 118107 | 108717 | 109.1 | 22735 | 126.1 | 22491 | +77 | -17.0 | medium |
| Put | 22650 | 40651 | 40082 | 126.5 | 22701 | 148.3 | 22524 | +44 | -21.9 | weak |
| Put | 22700 | 100180 | 94438 | 135.9 | 22730 | 173.5 | 22564 | +4 | -37.6 | weak |
| Put | 22750 | 29591 | 29470 | 156.0 | 22727 | 203.2 | 22594 | -26 | -47.2 | weak |
| Put | 22800 | 85668 | 78572 | 164.9 | 22774 | 233.3 | 22635 | -67 | -68.4 | weak |
| Put | 22850 | 12065 | 11843 | 182.1 | 22800 | 269.7 | 22668 | -100 | -87.6 | weak |
| Put | 22900 | 47901 | 45298 | 169.9 | 22907 | 304.1 | 22730 | -162 | -134.2 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at -, weakest put writers at 23000. Covers 56% of near-money call OI and 49% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22250 | 137 | 49 | 696.3 | 22627 | 708.7 | 22946 | +393 | -12.4 | strong |
| Call | 22300 | 1426 | 648 | 676.0 | 22608 | 682.8 | 22976 | +423 | -6.8 | strong |
| Call | 22350 | 166 | 113 | 624.5 | 22582 | 644.5 | 22974 | +421 | -20.0 | strong |
| Call | 22400 | 2975 | 1677 | 529.5 | 22462 | 611.5 | 22929 | +376 | -82.1 | strong |
| Call | 22450 | 416 | 347 | 551.0 | 22565 | 579.6 | 23001 | +448 | -28.6 | strong |
| Call | 22500 | 25334 | 14961 | 542.7 | 22603 | 547.4 | 23043 | +490 | -4.7 | strong |
| Call | 22550 | 600 | 414 | 490.9 | 22566 | 519.4 | 23041 | +488 | -28.5 | strong |
| Call | 22600 | 27817 | 19218 | 478.7 | 22626 | 487.8 | 23079 | +526 | -9.1 | strong |
| Call | 22650 | 3579 | 3282 | 459.8 | 22614 | 458.9 | 23110 | +557 | +1.0 | strong |
| Call | 22700 | 29515 | 25737 | 450.6 | 22675 | 430.8 | 23151 | +597 | +19.8 | strong |
| Call | 22750 | 1304 | 630 | 408.9 | 22612 | 405.2 | 23159 | +606 | +3.8 | strong |
| Call | 22800 | 21265 | 16015 | 399.4 | 22679 | 379.2 | 23199 | +646 | +20.2 | strong |
| Call | 22850 | 1206 | 742 | 376.1 | 22696 | 352.8 | 23226 | +673 | +23.2 | strong |
| Put | 22250 | 1867 | 424 | 214.6 | 22722 | 239.8 | 22035 | +518 | -25.3 | strong |
| Put | 22300 | 17277 | 10250 | 232.2 | 22683 | 253.1 | 22068 | +485 | -20.9 | strong |
| Put | 22350 | 801 | 298 | 245.8 | 22689 | 267.4 | 22104 | +449 | -21.5 | strong |
| Put | 22400 | 17209 | 5051 | 266.9 | 22668 | 286.9 | 22133 | +420 | -20.0 | strong |
| Put | 22450 | 664 | 251 | 291.0 | 22638 | 299.0 | 22159 | +394 | -8.0 | strong |
| Put | 22500 | 49963 | 22928 | 281.1 | 22726 | 319.1 | 22219 | +334 | -38.1 | strong |
| Put | 22550 | 845 | 392 | 272.8 | 22792 | 337.8 | 22277 | +276 | -65.0 | strong |
| Put | 22600 | 26892 | 17809 | 348.7 | 22642 | 358.2 | 22251 | +302 | -9.5 | strong |
| Put | 22650 | 3931 | 3399 | 353.3 | 22647 | 376.1 | 22297 | +256 | -22.8 | strong |
| Put | 22700 | 29222 | 22509 | 353.4 | 22715 | 397.2 | 22347 | +207 | -43.8 | strong |
| Put | 22750 | 1174 | 737 | 343.4 | 22792 | 420.3 | 22407 | +146 | -76.9 | strong |
| Put | 22800 | 20544 | 11714 | 397.3 | 22715 | 442.9 | 22403 | +150 | -45.6 | strong |
| Put | 22850 | 1868 | 125 | 399.6 | 22763 | 468.4 | 22450 | +103 | -68.9 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 5 | 80% | +0.08% | -0.21 to +0.26% |  | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 5 | 80% | +0.28% | -0.37 to +0.68% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.06% | -0.74 to +0.62% |  | too few (5/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 5 | 80% | +0.23% | -0.39 to +0.70% |  | too few (5/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 4 | 50% | -0.03% | -0.78 to +0.76% |  | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 75% | +0.10% | -0.24 to +0.35% |  | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 3 | 50% | +0.17% | -0.40 to +0.75% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR up · put writing · walls same · near put wall | 3 | 33% | -0.27% | -0.47 to +0.06% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.33% | +0.04 to +0.59% | 0% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.24% | +0.13 to +0.29% |  | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.12% | -0.61 to +0.37% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 2 | 100% | +0.28% | +0.27 to +0.29% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 2 | 50% | +0.17% | -0.07 to +0.40% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
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
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.59% | -0.59 to -0.59% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.59% | -0.59 to -0.59% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 29 | 59% | -0.06% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 29 | 85% | +0.30% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | weekly | writers even · few weak writers | 15 | 21% | -0.48% | down |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | writers even · weak puts | 12 | 73% | +0.24% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts | 7 | 50% | -0.18% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.54% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.57% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | monthly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.59% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
