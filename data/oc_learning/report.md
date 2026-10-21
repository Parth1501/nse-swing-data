# Nifty option chain pattern log
Updated 2026-10-21 11:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 107 snapshots over 5 trading days
- 115 patterns logged; 76 different patterns so far

## Latest read (2026-10-21 11:45:58)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 6.2 | 22828 | 0.846 | 23000 | 22000 | 23500 | ±1.55% (22473-23183) | 15.04 |
| 2026-11-23 (monthly) | 33.2 | 22828 | 1.043 | 23000 | 22000 | 23000 | ±3.56% (22016-23639) | 14.36 |

- **Weekly, last 30 min**: `PCR down · call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 5 times before; Nifty was up after it 50% of the time, average -0.03%. Too few outcomes (4/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.27%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR up · put and call writing · walls same · near call wall`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.74%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 12 times before; Nifty was up after it 58% of the time, average -0.08%. Too few outcomes (12/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at -, weakest put writers at 23000. Covers 74% of near-money call OI and 72% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22500 | 30454 | 9537 | 455.0 | 22852 | 396.3 | 22955 | +127 | +58.7 | strong |
| Call | 22550 | 4918 | 3486 | 418.6 | 22882 | 357.9 | 22969 | +141 | +60.7 | strong |
| Call | 22600 | 19923 | 6785 | 293.3 | 22701 | 319.2 | 22893 | +66 | -26.0 | medium |
| Call | 22650 | 4448 | 2317 | 300.6 | 22801 | 285.2 | 22951 | +123 | +15.4 | strong |
| Call | 22700 | 30072 | 12036 | 260.4 | 22782 | 252.3 | 22960 | +133 | +8.1 | strong |
| Call | 22750 | 9570 | 5099 | 243.9 | 22836 | 222.2 | 22994 | +166 | +21.7 | strong |
| Call | 22800 | 62952 | 46770 | 218.3 | 22852 | 193.7 | 23018 | +191 | +24.6 | strong |
| Call | 22850 | 32952 | 30600 | 185.4 | 22855 | 167.9 | 23035 | +208 | +17.4 | strong |
| Call | 22900 | 110215 | 97765 | 173.5 | 22873 | 144.2 | 23073 | +246 | +29.2 | strong |
| Call | 22950 | 55430 | 53516 | 172.7 | 22931 | 123.5 | 23123 | +295 | +49.1 | strong |
| Call | 23000 | 221448 | 161819 | 157.0 | 22934 | 105.0 | 23157 | +329 | +52.1 | strong |
| Call | 23050 | 74699 | 72341 | 165.2 | 23015 | 88.5 | 23215 | +388 | +76.8 | strong |
| Call | 23100 | 165687 | 144299 | 147.3 | 23022 | 74.0 | 23247 | +420 | +73.3 | strong |
| Call | 23150 | 69222 | 66662 | 128.5 | 23032 | 62.0 | 23279 | +451 | +66.5 | strong |
| Put | 22500 | 141207 | 82851 | 48.8 | 22993 | 65.2 | 22451 | +376 | -16.4 | strong |
| Put | 22550 | 30323 | 27730 | 43.4 | 23008 | 76.5 | 22507 | +321 | -33.1 | strong |
| Put | 22600 | 95480 | 68718 | 65.6 | 23010 | 89.6 | 22534 | +293 | -24.0 | strong |
| Put | 22650 | 27846 | 24297 | 61.8 | 23019 | 104.7 | 22588 | +239 | -42.9 | strong |
| Put | 22700 | 96960 | 67260 | 81.5 | 23028 | 121.7 | 22618 | +209 | -40.1 | strong |
| Put | 22750 | 35862 | 34089 | 79.4 | 23034 | 141.0 | 22671 | +157 | -61.6 | strong |
| Put | 22800 | 102613 | 75799 | 107.7 | 22989 | 162.6 | 22692 | +135 | -54.9 | strong |
| Put | 22850 | 45095 | 42927 | 125.4 | 22979 | 187.0 | 22725 | +103 | -61.6 | strong |
| Put | 22900 | 87802 | 80855 | 131.1 | 23013 | 212.9 | 22769 | +59 | -81.8 | medium |
| Put | 22950 | 36303 | 35977 | 143.4 | 23012 | 242.1 | 22807 | +21 | -98.6 | weak |
| Put | 23000 | 128650 | 102856 | 156.2 | 23054 | 272.6 | 22844 | -16 | -116.3 | weak |
| Put | 23050 | 28676 | 28556 | 145.0 | 23091 | 308.2 | 22905 | -77 | -163.2 | weak |
| Put | 23100 | 50574 | 45359 | 173.1 | 23094 | 342.1 | 22927 | -99 | -169.0 | weak |
| Put | 23150 | 10426 | 10209 | 205.0 | 23083 | 380.1 | 22945 | -117 | -175.1 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23500. Covers 10% of near-money call OI and 14% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22500 | 11820 | 416 | 745.3 | 22940 | 667.5 | 23245 | +418 | +77.9 | strong |
| Call | 22550 | 261 | 12 | 676.0 | 22851 | 661.2 | 23226 | +398 | +14.8 | strong |
| Call | 22600 | 9070 | 12 | 629.9 | 22875 | 595.6 | 23230 | +402 | +34.2 | strong |
| Call | 22650 | 331 | 1 | 638.4 | 22942 | 580.0 | 23288 | +461 | +58.4 | strong |
| Call | 22700 | 4118 | 56 | 590.4 | 22913 | 537.9 | 23290 | +463 | +52.5 | strong |
| Call | 22800 | 6225 | 317 | 499.6 | 22878 | 471.0 | 23300 | +472 | +28.6 | strong |
| Call | 22850 | 587 | 52 | 465.2 | 22866 | 446.6 | 23315 | +488 | +18.6 | strong |
| Call | 22900 | 4119 | 781 | 440.7 | 22877 | 414.6 | 23341 | +513 | +26.2 | strong |
| Call | 22950 | 1061 | 87 | 451.9 | 22940 | 385.0 | 23402 | +574 | +66.9 | strong |
| Call | 23000 | 62058 | 9778 | 405.7 | 22919 | 362.8 | 23406 | +578 | +42.9 | strong |
| Call | 23050 | 1619 | 31 | 389.9 | 22951 | 334.8 | 23440 | +612 | +55.1 | strong |
| Call | 23100 | 13174 | 2730 | 356.1 | 22930 | 313.4 | 23456 | +628 | +42.6 | strong |
| Call | 23150 | 1179 | 20 | 350.8 | 22961 | 291.5 | 23501 | +673 | +59.3 | strong |
| Put | 22500 | 34642 | 5789 | 186.2 | 23006 | 240.7 | 22314 | +514 | -54.5 | strong |
| Put | 22550 | 680 | 172 | 174.3 | 23077 | 253.2 | 22376 | +452 | -78.8 | strong |
| Put | 22600 | 9819 | 183 | 210.7 | 22988 | 271.1 | 22389 | +438 | -60.4 | strong |
| Put | 22650 | 883 | 263 | 193.2 | 23093 | 287.0 | 22457 | +371 | -93.8 | strong |
| Put | 22700 | 7752 | 561 | 217.7 | 23052 | 303.3 | 22482 | +345 | -85.6 | strong |
| Put | 22750 | 867 | 270 | 222.1 | 23084 | 325.1 | 22528 | +300 | -103.0 | strong |
| Put | 22800 | 10741 | 666 | 266.5 | 23010 | 341.7 | 22533 | +294 | -75.2 | strong |
| Put | 22850 | 3061 | 18 | 243.0 | 23094 | 365.1 | 22607 | +221 | -122.2 | strong |
| Put | 22900 | 4946 | 866 | 291.7 | 23023 | 386.8 | 22608 | +219 | -95.1 | strong |
| Put | 22950 | 838 | 115 | 326.5 | 22972 | 403.0 | 22624 | +204 | -76.5 | strong |
| Put | 23000 | 52095 | 10242 | 332.0 | 23019 | 429.2 | 22668 | +160 | -97.2 | strong |
| Put | 23050 | 714 | 146 | 330.0 | 23069 | 454.0 | 22720 | +108 | -124.0 | strong |
| Put | 23100 | 8881 | 2686 | 392.7 | 22979 | 482.9 | 22707 | +120 | -90.2 | strong |
| Put | 23150 | 1515 | 154 | 355.0 | 23094 | 504.2 | 22795 | +33 | -149.2 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% | 0% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 3 | 67% | +0.02% | -0.21 to +0.17% |  | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.60% | -0.71 to -0.50% |  | too few (3/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 2 | 0% | -0.74% | -0.74 to -0.74% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 1 | 0% | -0.51% | -0.51 to -0.51% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.15% | -1.15 to -1.15% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.50% | -0.50 to -0.50% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.27% | -0.27 to -0.27% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.27% | -0.27 to -0.27% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · few weak writers | 13 | 58% | -0.08% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 12 | 50% | +0.00% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 10 | 44% | +0.06% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · few weak writers | 10 | 10% | -0.54% | down |
| intraday | weekly | call writers stronger · weak puts | 6 | 50% | -0.03% | too few (4/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.37% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak puts | 4 | 50% | -0.18% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 3 | 0% | -0.20% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.69% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.27% | too few (1/10) |
| day | monthly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
