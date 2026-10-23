# Nifty option chain pattern log
Updated 2026-10-23 11:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 158 snapshots over 7 trading days
- 171 patterns logged; 95 different patterns so far

## Latest read (2026-10-23 11:45:24)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 4.2 | 22464 | 0.97 | 22700 | 22000 | 23000 | ±1.39% (22153-22776) | 16.53 |
| 2026-11-23 (monthly) | 31.2 | 22463 | 1.423 | 23000 | 22000 | 23000 | ±3.85% (21598-23328) | 16.23 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · mid walls`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.90%. Too few outcomes (2/20) to trade on.
  - Writers: `call writers stronger · weak puts`. Seen 25 times before; Nifty was up after it 70% of the time, average +0.18%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.44%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR up · quiet OI · walls same · mid walls`. Seen 3 times before; Nifty was up after it 67% of the time, average +0.01%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 10 times before; Nifty was up after it 40% of the time, average +0.10%. Too few outcomes (10/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22000; weakest call writers at -, weakest put writers at 22500. Covers 94% of near-money call OI and 90% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22150 | 601 | 389 | 555.4 | 22642 | 411.9 | 22705 | +241 | +143.6 | strong |
| Call | 22200 | 7508 | 1760 | 533.3 | 22668 | 370.0 | 22733 | +269 | +163.3 | strong |
| Call | 22250 | 2297 | 1587 | 412.2 | 22553 | 328.8 | 22662 | +198 | +83.4 | strong |
| Call | 22300 | 13481 | 6746 | 355.9 | 22549 | 292.7 | 22656 | +192 | +63.2 | strong |
| Call | 22350 | 6107 | 5580 | 327.1 | 22565 | 257.2 | 22677 | +213 | +69.9 | strong |
| Call | 22400 | 37310 | 31225 | 269.9 | 22529 | 223.2 | 22670 | +206 | +46.7 | strong |
| Call | 22450 | 47575 | 47091 | 212.2 | 22497 | 191.8 | 22662 | +198 | +20.4 | strong |
| Call | 22500 | 196678 | 183190 | 203.8 | 22526 | 164.0 | 22704 | +240 | +39.8 | strong |
| Call | 22550 | 70695 | 70250 | 178.2 | 22524 | 138.7 | 22728 | +264 | +39.5 | strong |
| Call | 22600 | 149478 | 145556 | 163.2 | 22548 | 116.3 | 22763 | +299 | +46.9 | strong |
| Call | 22650 | 79437 | 79113 | 140.4 | 22552 | 97.0 | 22790 | +326 | +43.4 | strong |
| Call | 22700 | 232206 | 223165 | 140.2 | 22603 | 80.4 | 22840 | +376 | +59.8 | strong |
| Call | 22750 | 104793 | 102421 | 146.0 | 22681 | 66.0 | 22896 | +432 | +80.0 | strong |
| Call | 22800 | 248293 | 237076 | 128.7 | 22675 | 54.2 | 22929 | +465 | +74.4 | strong |
| Put | 22150 | 38242 | 37060 | 21.7 | 22782 | 39.0 | 22128 | +336 | -17.4 | strong |
| Put | 22200 | 122759 | 107448 | 25.1 | 22820 | 47.5 | 22175 | +289 | -22.5 | strong |
| Put | 22250 | 44522 | 42276 | 34.1 | 22733 | 57.6 | 22216 | +248 | -23.6 | strong |
| Put | 22300 | 133885 | 105544 | 40.1 | 22747 | 69.8 | 22260 | +204 | -29.7 | strong |
| Put | 22350 | 69268 | 67598 | 60.9 | 22634 | 84.0 | 22289 | +175 | -23.0 | strong |
| Put | 22400 | 159912 | 146171 | 66.3 | 22681 | 100.5 | 22334 | +130 | -34.2 | strong |
| Put | 22450 | 106436 | 105909 | 92.3 | 22605 | 119.7 | 22358 | +106 | -27.4 | strong |
| Put | 22500 | 238897 | 203446 | 83.0 | 22724 | 141.0 | 22417 | +47 | -58.0 | weak |
| Put | 22550 | 57758 | 56875 | 100.8 | 22696 | 166.2 | 22449 | +15 | -65.5 | weak |
| Put | 22600 | 115831 | 105611 | 107.0 | 22755 | 193.8 | 22493 | -29 | -86.8 | weak |
| Put | 22650 | 39494 | 38857 | 123.0 | 22722 | 223.8 | 22527 | -63 | -100.8 | weak |
| Put | 22700 | 98916 | 92630 | 131.6 | 22749 | 256.6 | 22568 | -104 | -125.0 | weak |
| Put | 22750 | 30998 | 30870 | 155.6 | 22728 | 292.7 | 22594 | -130 | -137.1 | weak |
| Put | 22800 | 88692 | 81345 | 164.9 | 22774 | 330.0 | 22635 | -171 | -165.1 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at -, weakest put writers at 23000. Covers 56% of near-money call OI and 47% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22150 | 37 | 28 | 722.8 | 22502 | 688.0 | 22873 | +410 | +34.8 | strong |
| Call | 22200 | 2080 | 408 | 758.4 | 22631 | 656.5 | 22958 | +496 | +101.9 | strong |
| Call | 22250 | 135 | 47 | 698.2 | 22634 | 622.0 | 22948 | +485 | +76.2 | strong |
| Call | 22300 | 1379 | 581 | 691.4 | 22637 | 598.8 | 22991 | +529 | +92.7 | strong |
| Call | 22350 | 174 | 105 | 659.9 | 22651 | 555.2 | 23010 | +547 | +104.7 | strong |
| Call | 22400 | 1973 | 606 | 581.7 | 22568 | 534.0 | 22982 | +519 | +47.8 | strong |
| Call | 22450 | 373 | 295 | 571.9 | 22611 | 504.9 | 23022 | +559 | +66.9 | strong |
| Call | 22500 | 24155 | 13514 | 555.3 | 22628 | 474.9 | 23055 | +593 | +80.4 | strong |
| Call | 22550 | 511 | 319 | 517.0 | 22622 | 442.9 | 23067 | +604 | +74.1 | strong |
| Call | 22600 | 27230 | 18627 | 481.3 | 22633 | 420.5 | 23081 | +619 | +60.8 | strong |
| Call | 22650 | 2074 | 1777 | 461.1 | 22666 | 390.2 | 23111 | +648 | +70.8 | strong |
| Call | 22700 | 30545 | 26553 | 453.1 | 22682 | 369.0 | 23153 | +690 | +84.1 | strong |
| Call | 22750 | 1185 | 508 | 420.0 | 22644 | 345.6 | 23170 | +707 | +74.4 | strong |
| Put | 22150 | 764 | 288 | 179.4 | 22740 | 256.3 | 21971 | +492 | -76.9 | strong |
| Put | 22200 | 11268 | 2887 | 194.7 | 22730 | 267.0 | 22005 | +457 | -72.3 | strong |
| Put | 22250 | 1836 | 388 | 207.6 | 22751 | 286.9 | 22042 | +420 | -79.2 | strong |
| Put | 22300 | 17418 | 10223 | 230.2 | 22691 | 300.6 | 22070 | +393 | -70.5 | strong |
| Put | 22350 | 841 | 303 | 241.2 | 22705 | 322.0 | 22109 | +354 | -80.8 | strong |
| Put | 22400 | 16318 | 4160 | 253.3 | 22715 | 337.2 | 22147 | +316 | -83.9 | strong |
| Put | 22450 | 677 | 243 | 289.4 | 22646 | 359.9 | 22161 | +302 | -70.6 | strong |
| Put | 22500 | 48979 | 21944 | 277.0 | 22738 | 376.6 | 22223 | +240 | -99.5 | strong |
| Put | 22550 | 823 | 361 | 261.2 | 22826 | 401.1 | 22289 | +174 | -139.9 | strong |
| Put | 22600 | 26453 | 17312 | 347.3 | 22647 | 421.2 | 22253 | +210 | -74.0 | strong |
| Put | 22650 | 2404 | 1866 | 334.0 | 22726 | 448.6 | 22316 | +147 | -114.7 | strong |
| Put | 22700 | 30331 | 23361 | 353.4 | 22715 | 470.1 | 22347 | +116 | -116.8 | strong |
| Put | 22750 | 1248 | 775 | 338.1 | 22804 | 500.8 | 22412 | +51 | -162.7 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 5 | 60% | +0.00% | -0.21 to +0.17% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.14% | -1.05 to +0.62% |  | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 4 | 67% | +0.01% | -0.39 to +0.34% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 50% | -0.00% | -0.24 to +0.15% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 3 | 33% | -0.07% | -0.37 to +0.25% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | +0.08% | -0.17 to +0.29% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 0% | -0.90% | -1.02 to -0.78% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls same · near put wall | 3 | 33% | -0.27% | -0.47 to +0.06% | 0% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 0% | -0.36% | -0.61 to -0.10% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 2 | 100% | +0.28% | +0.27 to +0.29% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · mid walls | 2 | 100% | +0.20% | +0.04 to +0.36% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls down · mid walls | 2 | 0% | -0.07% | -0.07 to -0.06% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.40% | -0.40 to -0.40% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
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
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.99% | -0.99 to -0.99% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.99% | -0.99 to -0.99% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 29 | 59% | -0.09% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 26 | 70% | +0.18% | no clear direction |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | weekly | writers even · few weak writers | 15 | 21% | -0.54% | down |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | writers even · weak puts | 11 | 40% | +0.10% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts | 6 | 50% | -0.18% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 100% | +0.39% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 3 | 0% | -0.44% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.77% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.99% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
