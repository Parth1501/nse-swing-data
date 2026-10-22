# Nifty option chain pattern log
Updated 2026-10-22 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 145 snapshots over 6 trading days
- 155 patterns logged; 93 different patterns so far

## Latest read (2026-10-22 14:45:23)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 5.0 | 22686 | 0.883 | 22800 | 22000 | 23000 | ±1.33% (22384-22989) | 14.04 |
| 2026-11-23 (monthly) | 32.0 | 22692 | 1.176 | 23000 | 22000 | 23000 | ±3.58% (21878-23505) | 14.91 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 10 times before; Nifty was up after it 44% of the time, average +0.05%. Too few outcomes (9/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 1 times before; Nifty was up after it 100% of the time, average +1.66%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · near call wall`. Seen 4 times before; Nifty was up after it 75% of the time, average +0.15%. Too few outcomes (4/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 24 times before; Nifty was up after it 65% of the time, average +0.00%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.52%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22600; weakest call writers at 22300, weakest put writers at 23000. Covers 86% of near-money call OI and 84% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22350 | 2697 | 2144 | 406.3 | 22690 | 443.7 | 22756 | +70 | -37.4 | medium |
| Call | 22400 | 11641 | 5393 | 410.9 | 22733 | 401.1 | 22811 | +125 | +9.8 | strong |
| Call | 22450 | 4412 | 3846 | 308.2 | 22655 | 362.3 | 22758 | +72 | -54.0 | medium |
| Call | 22500 | 51418 | 36313 | 300.7 | 22687 | 320.4 | 22801 | +114 | -19.6 | strong |
| Call | 22550 | 18341 | 17653 | 249.5 | 22671 | 281.9 | 22800 | +113 | -32.3 | strong |
| Call | 22600 | 76730 | 71598 | 200.2 | 22643 | 245.4 | 22800 | +114 | -45.2 | strong |
| Call | 22650 | 43475 | 43032 | 166.8 | 22636 | 212.1 | 22817 | +130 | -45.3 | strong |
| Call | 22700 | 121637 | 109899 | 166.0 | 22674 | 181.2 | 22866 | +180 | -15.2 | strong |
| Call | 22750 | 62247 | 59223 | 158.8 | 22708 | 155.2 | 22909 | +222 | +3.6 | strong |
| Call | 22800 | 132711 | 119896 | 158.4 | 22744 | 130.6 | 22958 | +272 | +27.8 | strong |
| Call | 22850 | 41086 | 39565 | 147.4 | 22772 | 107.8 | 22997 | +311 | +39.6 | strong |
| Call | 22900 | 99985 | 91765 | 151.7 | 22827 | 88.7 | 23052 | +365 | +63.0 | strong |
| Call | 22950 | 59123 | 57956 | 126.0 | 22812 | 71.7 | 23076 | +390 | +54.3 | strong |
| Call | 23000 | 262358 | 214899 | 118.5 | 22830 | 58.9 | 23119 | +432 | +59.7 | strong |
| Put | 22350 | 33864 | 32170 | 44.4 | 22759 | 33.7 | 22306 | +381 | +10.7 | strong |
| Put | 22400 | 93334 | 78260 | 53.6 | 22789 | 40.4 | 22346 | +340 | +13.2 | strong |
| Put | 22450 | 36575 | 35952 | 62.9 | 22781 | 49.2 | 22387 | +299 | +13.7 | strong |
| Put | 22500 | 162308 | 118861 | 69.6 | 22838 | 59.4 | 22430 | +256 | +10.2 | strong |
| Put | 22550 | 62346 | 60685 | 93.0 | 22762 | 71.6 | 22457 | +229 | +21.4 | strong |
| Put | 22600 | 161018 | 141116 | 107.8 | 22789 | 85.7 | 22492 | +194 | +22.1 | strong |
| Put | 22650 | 66604 | 64525 | 128.3 | 22746 | 102.3 | 22522 | +165 | +26.0 | strong |
| Put | 22700 | 131764 | 115017 | 126.4 | 22808 | 121.5 | 22574 | +113 | +4.8 | strong |
| Put | 22750 | 40071 | 39630 | 148.4 | 22782 | 143.2 | 22602 | +85 | +5.3 | medium |
| Put | 22800 | 70359 | 57358 | 137.9 | 22892 | 167.1 | 22662 | +24 | -29.1 | weak |
| Put | 22850 | 13932 | 13450 | 153.8 | 22896 | 195.6 | 22696 | -10 | -41.8 | weak |
| Put | 22900 | 49704 | 46078 | 142.5 | 22985 | 226.6 | 22758 | -71 | -84.1 | weak |
| Put | 22950 | 11495 | 11399 | 154.5 | 22989 | 260.6 | 22795 | -109 | -106.1 | weak |
| Put | 23000 | 75413 | 61196 | 169.0 | 23028 | 298.0 | 22831 | -145 | -129.0 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23200. Covers 46% of near-money call OI and 43% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 1639 | 254 | 628.6 | 22684 | 666.3 | 23029 | +337 | -37.6 | strong |
| Call | 22450 | 235 | 157 | 608.1 | 22702 | 571.0 | 23058 | +366 | +37.1 | strong |
| Call | 22500 | 18620 | 7692 | 587.5 | 22702 | 598.1 | 23088 | +396 | -10.6 | strong |
| Call | 22550 | 450 | 239 | 541.2 | 22685 | 572.0 | 23091 | +399 | -30.8 | strong |
| Call | 22600 | 23714 | 15098 | 489.9 | 22663 | 533.5 | 23090 | +398 | -43.6 | strong |
| Call | 22650 | 2068 | 1754 | 462.2 | 22671 | 504.8 | 23112 | +420 | -42.6 | strong |
| Call | 22700 | 24709 | 20702 | 460.6 | 22708 | 472.0 | 23161 | +469 | -11.4 | strong |
| Call | 22750 | 1103 | 388 | 442.8 | 22702 | 443.3 | 23193 | +501 | -0.5 | strong |
| Call | 22800 | 17447 | 11837 | 406.3 | 22706 | 415.4 | 23206 | +515 | -9.2 | strong |
| Call | 22850 | 1295 | 772 | 378.8 | 22710 | 387.9 | 23229 | +537 | -9.2 | strong |
| Call | 22900 | 10866 | 7586 | 369.1 | 22729 | 361.6 | 23269 | +577 | +7.5 | strong |
| Call | 22950 | 1358 | 414 | 358.0 | 22751 | 323.1 | 23308 | +616 | +34.9 | strong |
| Call | 23000 | 77839 | 25846 | 343.9 | 22782 | 315.0 | 23344 | +652 | +28.9 | strong |
| Put | 22400 | 15467 | 3232 | 237.8 | 22763 | 239.6 | 22162 | +529 | -1.8 | strong |
| Put | 22450 | 578 | 123 | 262.5 | 22732 | 252.1 | 22187 | +504 | +10.5 | strong |
| Put | 22500 | 42919 | 15530 | 250.2 | 22816 | 268.0 | 22250 | +442 | -17.8 | strong |
| Put | 22550 | 767 | 274 | 224.2 | 22932 | 285.6 | 22326 | +366 | -61.4 | strong |
| Put | 22600 | 24175 | 15008 | 338.6 | 22670 | 303.8 | 22261 | +430 | +34.9 | strong |
| Put | 22650 | 2409 | 1835 | 333.6 | 22729 | 321.4 | 22316 | +375 | +12.2 | strong |
| Put | 22700 | 26420 | 19398 | 348.3 | 22726 | 341.4 | 22352 | +340 | +6.9 | strong |
| Put | 22750 | 1100 | 603 | 312.3 | 22864 | 360.2 | 22438 | +254 | -47.9 | strong |
| Put | 22800 | 19844 | 10009 | 392.0 | 22727 | 381.8 | 22408 | +284 | +10.2 | strong |
| Put | 22850 | 2254 | 135 | 396.0 | 22770 | 403.2 | 22454 | +238 | -7.2 | strong |
| Put | 22900 | 7425 | 3437 | 409.5 | 22787 | 429.1 | 22490 | +201 | -19.6 | strong |
| Put | 22950 | 615 | 136 | 383.6 | 22865 | 454.8 | 22566 | +125 | -71.2 | strong |
| Put | 23000 | 66674 | 24972 | 440.8 | 22820 | 480.1 | 22559 | +133 | -39.3 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 75% | +0.15% | -0.12 to +0.32% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 4 | 75% | +0.05% | -0.21 to +0.17% |  | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.19% | +0.07 to +0.32% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 4 | 50% | +0.09% | -0.74 to +0.62% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls same · near put wall | 3 | 33% | -0.27% | -0.47 to +0.06% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.37% | -0.78 to +0.04% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 2 | 100% | +0.29% | +0.28 to +0.30% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · mid walls | 2 | 100% | +0.20% | +0.04 to +0.35% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.07 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 2 | 50% | -0.02% | -0.39 to +0.36% |  | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.39 to -0.07% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.41% | -0.41 to -0.41% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 2 | 100% | +0.20% | +0.12 to +0.28% |  | too few (2/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.09% | -0.09 to -0.09% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.52% | -0.52 to -0.52% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 25 | 65% | +0.00% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 22 | 80% | +0.22% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 44% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · few weak writers | 11 | 18% | -0.50% | down |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | writers even · weak puts | 7 | 57% | +0.19% | too few (7/10) |
| intraday | weekly | writers even · weak puts | 6 | 50% | -0.18% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 100% | +0.39% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.52% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 2 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.43% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
