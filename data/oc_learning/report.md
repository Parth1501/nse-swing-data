# Nifty option chain pattern log
Updated 2026-10-22 11:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 133 snapshots over 6 trading days
- 143 patterns logged; 89 different patterns so far

## Latest read (2026-10-22 11:44:18)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 5.2 | 22661 | 1.077 | 22850 | 22000 | 23000 | ±1.41% (22341-22981) | 14.92 |
| 2026-11-23 (monthly) | 32.2 | 22661 | 1.361 | 23000 | 22000 | 23000 | ±3.64% (21835-23487) | 14.94 |

- **Weekly, last 30 min**: `PCR up · put writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. Seen 5 times before; Nifty was up after it 40% of the time, average -0.26%. Too few outcomes (5/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · unwinding · walls same · mid walls`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.14%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 19 times before; Nifty was up after it 44% of the time, average -0.09%. Too few outcomes (18/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.66%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22600; weakest call writers at -, weakest put writers at 22800. Covers 84% of near-money call OI and 81% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22350 | 2683 | 2086 | 412.2 | 22699 | 405.2 | 22762 | +101 | +7.0 | medium |
| Call | 22400 | 11536 | 4910 | 424.6 | 22752 | 366.6 | 22825 | +164 | +58.1 | strong |
| Call | 22450 | 3903 | 3198 | 322.0 | 22677 | 325.2 | 22772 | +111 | -3.2 | strong |
| Call | 22500 | 42918 | 26014 | 332.1 | 22728 | 290.0 | 22832 | +171 | +42.1 | strong |
| Call | 22550 | 14595 | 13764 | 270.1 | 22703 | 254.2 | 22820 | +159 | +16.0 | strong |
| Call | 22600 | 59962 | 52549 | 217.4 | 22671 | 221.8 | 22817 | +156 | -4.5 | strong |
| Call | 22650 | 28358 | 27566 | 186.4 | 22672 | 190.2 | 22836 | +175 | -3.8 | strong |
| Call | 22700 | 100217 | 86778 | 182.1 | 22701 | 162.6 | 22882 | +221 | +19.6 | strong |
| Call | 22750 | 61056 | 57716 | 163.2 | 22717 | 137.8 | 22913 | +252 | +25.3 | strong |
| Call | 22800 | 134952 | 120680 | 165.5 | 22758 | 115.9 | 22965 | +305 | +49.6 | strong |
| Call | 22850 | 44076 | 42306 | 153.7 | 22786 | 97.1 | 23004 | +343 | +56.6 | strong |
| Call | 22900 | 124616 | 114241 | 152.9 | 22830 | 80.0 | 23053 | +392 | +72.9 | strong |
| Call | 22950 | 57429 | 56049 | 142.8 | 22856 | 66.2 | 23093 | +432 | +76.6 | strong |
| Call | 23000 | 253948 | 201583 | 131.9 | 22868 | 54.1 | 23132 | +471 | +77.8 | strong |
| Put | 22350 | 41121 | 38244 | 41.5 | 22812 | 46.4 | 22309 | +352 | -5.0 | strong |
| Put | 22400 | 86954 | 69810 | 52.8 | 22829 | 55.2 | 22347 | +314 | -2.4 | strong |
| Put | 22450 | 36887 | 36104 | 61.6 | 22812 | 66.2 | 22388 | +273 | -4.5 | strong |
| Put | 22500 | 171110 | 121024 | 67.4 | 22864 | 78.7 | 22433 | +228 | -11.3 | strong |
| Put | 22550 | 56873 | 55111 | 92.4 | 22781 | 93.0 | 22458 | +203 | -0.6 | strong |
| Put | 22600 | 163809 | 141775 | 105.2 | 22807 | 109.3 | 22495 | +166 | -4.1 | strong |
| Put | 22650 | 55002 | 52791 | 124.0 | 22779 | 129.6 | 22526 | +135 | -5.6 | strong |
| Put | 22700 | 151804 | 127869 | 121.4 | 22846 | 152.6 | 22579 | +82 | -31.2 | medium |
| Put | 22750 | 59035 | 58156 | 140.0 | 22820 | 176.5 | 22610 | +51 | -36.5 | medium |
| Put | 22800 | 84885 | 68381 | 133.5 | 22907 | 203.9 | 22666 | -6 | -70.4 | weak |
| Put | 22850 | 16338 | 15711 | 147.3 | 22920 | 234.5 | 22703 | -42 | -87.2 | weak |
| Put | 22900 | 56451 | 52215 | 138.4 | 22995 | 268.0 | 22762 | -101 | -129.6 | weak |
| Put | 22950 | 12171 | 12065 | 147.1 | 23004 | 302.8 | 22803 | -142 | -155.7 | weak |
| Put | 23000 | 80803 | 65428 | 167.0 | 23032 | 344.0 | 22833 | -172 | -177.0 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at -, weakest put writers at 23200. Covers 43% of near-money call OI and 38% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22350 | 98 | 28 | 800.5 | 22862 | 738.2 | 23151 | +490 | +62.3 | strong |
| Call | 22400 | 1612 | 208 | 634.5 | 22697 | 638.9 | 23034 | +374 | -4.4 | strong |
| Call | 22450 | 212 | 134 | 613.4 | 22714 | 605.8 | 23063 | +403 | +7.6 | strong |
| Call | 22500 | 17339 | 6281 | 594.3 | 22716 | 570.0 | 23094 | +433 | +24.4 | strong |
| Call | 22550 | 452 | 226 | 545.9 | 22695 | 540.5 | 23096 | +435 | +5.4 | strong |
| Call | 22600 | 23224 | 14502 | 490.7 | 22665 | 507.0 | 23091 | +430 | -16.3 | strong |
| Call | 22650 | 2007 | 1685 | 461.7 | 22673 | 483.9 | 23112 | +451 | -22.2 | strong |
| Call | 22700 | 23812 | 19805 | 461.4 | 22710 | 446.0 | 23161 | +501 | +15.4 | strong |
| Call | 22750 | 1062 | 336 | 447.6 | 22711 | 425.1 | 23198 | +537 | +22.5 | strong |
| Call | 22800 | 16957 | 11310 | 407.8 | 22710 | 391.9 | 23208 | +547 | +15.9 | strong |
| Call | 22850 | 1280 | 750 | 379.3 | 22711 | 370.4 | 23229 | +568 | +8.9 | strong |
| Call | 22900 | 10803 | 7467 | 370.8 | 22733 | 339.9 | 23271 | +610 | +30.9 | strong |
| Call | 22950 | 1306 | 359 | 368.1 | 22771 | 319.9 | 23318 | +657 | +48.3 | strong |
| Call | 23000 | 73961 | 21968 | 355.1 | 22809 | 295.0 | 23355 | +694 | +60.1 | strong |
| Put | 22350 | 777 | 186 | 211.4 | 22805 | 234.7 | 22139 | +522 | -23.3 | strong |
| Put | 22400 | 15526 | 3184 | 236.7 | 22767 | 257.9 | 22163 | +498 | -21.2 | strong |
| Put | 22450 | 600 | 127 | 262.5 | 22732 | 271.0 | 22187 | +473 | -8.5 | strong |
| Put | 22500 | 40986 | 13597 | 243.4 | 22840 | 288.4 | 22257 | +404 | -45.0 | strong |
| Put | 22550 | 766 | 266 | 220.2 | 22944 | 305.2 | 22330 | +331 | -85.0 | strong |
| Put | 22600 | 23725 | 14392 | 338.1 | 22672 | 326.2 | 22262 | +399 | +11.9 | strong |
| Put | 22650 | 2415 | 1826 | 333.6 | 22731 | 342.0 | 22316 | +345 | -8.4 | strong |
| Put | 22700 | 26258 | 19090 | 347.9 | 22727 | 364.2 | 22352 | +309 | -16.4 | strong |
| Put | 22750 | 1173 | 628 | 309.6 | 22873 | 386.6 | 22440 | +221 | -77.0 | strong |
| Put | 22800 | 19790 | 9821 | 391.5 | 22729 | 406.5 | 22408 | +252 | -15.0 | strong |
| Put | 22850 | 2446 | 138 | 394.8 | 22776 | 430.0 | 22455 | +206 | -35.2 | strong |
| Put | 22900 | 7128 | 3131 | 403.4 | 22801 | 457.1 | 22497 | +164 | -53.7 | strong |
| Put | 22950 | 646 | 142 | 382.7 | 22867 | 478.8 | 22567 | +94 | -96.0 | medium |
| Put | 23000 | 63241 | 21539 | 427.6 | 22846 | 509.1 | 22572 | +88 | -81.5 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | +0.01% | -0.21 to +0.17% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 4 | 50% | +0.09% | -0.74 to +0.62% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 4 | 50% | +0.08% | -0.26 to +0.32% |  | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 3 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 50% | +0.03% | -0.04 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.29% | -0.52 to -0.07% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.52% | -0.52 to -0.52% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
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
| weekly | PCR up · put writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.66% | -0.66 to -0.66% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 20 | 44% | -0.09% | no clear direction |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | call writers stronger · weak puts | 18 | 69% | +0.18% | no clear direction |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 10 | 44% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · few weak writers | 10 | 10% | -0.56% | down |
| intraday | monthly | writers even · weak puts | 6 | 50% | +0.14% | too few (6/10) |
| intraday | weekly | writers even · weak puts | 6 | 40% | -0.26% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 100% | +0.39% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.66% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.50% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
