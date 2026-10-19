# Nifty option chain pattern log
Updated 2026-10-19 14:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 92 snapshots over 4 trading days
- 100 patterns logged; 65 different patterns so far

## Latest read (2026-10-19 14:45:48)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 0.0 | 22885 | 0.842 | 22900 | 22800 | 22900 | ±0.3% (22817-22953) | 7.52 |
| 2026-10-27 (monthly) | 8.0 | 22877 | 0.959 | 23050 | 22000 | 23500 | ±1.52% (22529-23226) | 12.99 |

- **Weekly, last 30 min**: `PCR up · unwinding · walls down · near call wall`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.14%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.28%. Too few outcomes (1/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 9 times before; Nifty was up after it 56% of the time, average -0.10%. Too few outcomes (9/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23000, strongest put writers at 22800; weakest call writers at 22850, weakest put writers at 22900. Covers 94% of near-money call OI and 92% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22550 | 4662 | 3760 | 244.1 | 22720 | 340.9 | 22794 | -91 | -96.9 | weak |
| Call | 22600 | 11142 | 7461 | 146.3 | 22604 | 290.6 | 22746 | -139 | -144.3 | weak |
| Call | 22650 | 7417 | 4694 | 134.7 | 22622 | 241.3 | 22785 | -100 | -106.7 | weak |
| Call | 22700 | 36185 | 21781 | 160.9 | 22805 | 189.1 | 22861 | -24 | -28.2 | weak |
| Call | 22750 | 26270 | 21446 | 128.5 | 22854 | 140.9 | 22879 | -7 | -12.4 | weak |
| Call | 22800 | 120333 | 111657 | 109.8 | 22891 | 94.9 | 22910 | +25 | +14.8 | weak |
| Call | 22850 | 278119 | 275127 | 60.0 | 22884 | 57.3 | 22910 | +25 | +2.7 | weak |
| Call | 22900 | 590456 | 579723 | 44.0 | 22896 | 28.6 | 22944 | +59 | +15.5 | medium |
| Call | 22950 | 421564 | 419866 | 45.1 | 22938 | 12.6 | 22995 | +110 | +32.5 | strong |
| Call | 23000 | 502469 | 481686 | 50.3 | 22971 | 5.8 | 23050 | +165 | +44.5 | strong |
| Call | 23050 | 279918 | 277382 | 54.5 | 23022 | 2.8 | 23105 | +219 | +51.7 | strong |
| Call | 23100 | 332925 | 318892 | 53.7 | 23049 | 1.6 | 23154 | +269 | +52.0 | strong |
| Call | 23150 | 220479 | 215040 | 54.4 | 23096 | 1.2 | 23204 | +319 | +53.2 | strong |
| Call | 23200 | 272997 | 249377 | 36.5 | 23085 | 0.9 | 23236 | +351 | +35.6 | strong |
| Put | 22550 | 93246 | 78606 | 18.7 | 23034 | 0.3 | 22531 | +354 | +18.4 | strong |
| Put | 22600 | 206818 | 166773 | 27.6 | 22998 | 0.3 | 22572 | +313 | +27.2 | strong |
| Put | 22650 | 144385 | 134779 | 26.1 | 22991 | 0.5 | 22624 | +261 | +25.6 | strong |
| Put | 22700 | 285547 | 255355 | 40.5 | 22970 | 0.8 | 22659 | +226 | +39.7 | strong |
| Put | 22750 | 309314 | 305626 | 24.2 | 22950 | 1.8 | 22726 | +159 | +22.5 | strong |
| Put | 22800 | 495764 | 486156 | 32.5 | 22975 | 6.1 | 22767 | +118 | +26.4 | strong |
| Put | 22850 | 393183 | 391231 | 35.5 | 22964 | 17.1 | 22814 | +71 | +18.5 | medium |
| Put | 22900 | 286064 | 284432 | 53.0 | 23007 | 39.8 | 22847 | +38 | +13.3 | weak |
| Put | 22950 | 102880 | 102564 | 58.9 | 23048 | 74.2 | 22891 | -6 | -15.3 | weak |
| Put | 23000 | 109032 | 108136 | 62.4 | 23088 | 114.8 | 22938 | -53 | -52.4 | weak |
| Put | 23050 | 40811 | 40786 | 62.0 | 23095 | 164.2 | 22988 | -103 | -102.2 | weak |
| Put | 23100 | 84861 | 84609 | 91.2 | 23111 | 212.8 | 23009 | -124 | -121.7 | weak |
| Put | 23150 | 56734 | 56715 | 103.5 | 23132 | 262.2 | 23047 | -161 | -158.7 | weak |
| Put | 23200 | 31119 | 31013 | 149.4 | 23113 | 310.8 | 23051 | -165 | -161.3 | weak |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at 22600, weakest put writers at 23100. Covers 54% of near-money call OI and 52% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22550 | 5671 | 3833 | 419.3 | 22880 | 399.6 | 22969 | +92 | +19.7 | medium |
| Call | 22600 | 20293 | 6380 | 279.3 | 22671 | 360.1 | 22879 | +2 | -80.8 | weak |
| Call | 22650 | 3090 | 905 | 255.8 | 22668 | 325.0 | 22906 | +28 | -69.2 | weak |
| Call | 22700 | 27517 | 8144 | 253.4 | 22738 | 287.0 | 22953 | +76 | -33.6 | medium |
| Call | 22750 | 6422 | 1886 | 253.3 | 22805 | 255.8 | 23003 | +126 | -2.5 | strong |
| Call | 22800 | 33295 | 15363 | 258.5 | 22879 | 226.3 | 23058 | +181 | +32.1 | strong |
| Call | 22850 | 11743 | 8187 | 217.9 | 22895 | 197.3 | 23068 | +190 | +20.6 | strong |
| Call | 22900 | 55687 | 41081 | 185.4 | 22870 | 170.2 | 23085 | +208 | +15.2 | strong |
| Call | 22950 | 18888 | 16456 | 178.5 | 22925 | 145.9 | 23128 | +251 | +32.6 | strong |
| Call | 23000 | 148709 | 85071 | 163.4 | 22927 | 124.8 | 23163 | +286 | +38.6 | strong |
| Call | 23050 | 17066 | 14678 | 163.3 | 22986 | 103.8 | 23213 | +336 | +59.6 | strong |
| Call | 23100 | 79201 | 56636 | 146.4 | 23000 | 88.6 | 23246 | +369 | +57.8 | strong |
| Call | 23150 | 32780 | 29911 | 119.4 | 22989 | 72.7 | 23269 | +392 | +46.7 | strong |
| Call | 23200 | 109930 | 63059 | 96.0 | 22922 | 61.2 | 23296 | +419 | +34.8 | strong |
| Put | 22550 | 11004 | 7602 | 67.5 | 23006 | 60.9 | 22482 | +395 | +6.6 | strong |
| Put | 22600 | 62964 | 35280 | 92.9 | 22969 | 71.8 | 22507 | +370 | +21.1 | strong |
| Put | 22650 | 10403 | 6703 | 89.3 | 22994 | 84.4 | 22561 | +317 | +4.9 | strong |
| Put | 22700 | 81105 | 42902 | 118.3 | 22964 | 99.2 | 22582 | +296 | +19.1 | strong |
| Put | 22750 | 14819 | 12872 | 90.1 | 23070 | 115.7 | 22660 | +218 | -25.5 | strong |
| Put | 22800 | 54661 | 27847 | 135.0 | 22969 | 134.7 | 22665 | +212 | +0.3 | strong |
| Put | 22850 | 15223 | 13055 | 155.9 | 22944 | 156.1 | 22694 | +183 | -0.2 | strong |
| Put | 22900 | 47284 | 38308 | 150.5 | 23016 | 178.6 | 22749 | +128 | -28.0 | strong |
| Put | 22950 | 14313 | 13635 | 177.3 | 22997 | 205.1 | 22773 | +105 | -27.8 | strong |
| Put | 23000 | 116272 | 71739 | 204.9 | 22999 | 234.0 | 22795 | +82 | -29.1 | medium |
| Put | 23050 | 6925 | 6589 | 179.3 | 23077 | 266.0 | 22871 | +7 | -86.7 | weak |
| Put | 23100 | 42090 | 29167 | 198.9 | 23094 | 298.0 | 22901 | -24 | -99.1 | weak |
| Put | 23150 | 5411 | 4925 | 214.2 | 23117 | 334.0 | 22936 | -58 | -119.8 | weak |
| Put | 23200 | 38270 | 14307 | 247.9 | 23101 | 370.6 | 22952 | -75 | -122.6 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% | 0% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.08% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | -0.02% | -0.29 to +0.15% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 3 | 67% | +0.00% | -0.26 to +0.17% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.19% | -0.53 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.14% | +0.07 to +0.21% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.02% | -0.11 to +0.07% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.18% | -1.13 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.46% | -0.77 to -0.16% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.76% | -0.76 to -0.76% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.18% | -1.18 to -1.18% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.83% | -0.83 to -0.83% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.79% | -0.79 to -0.79% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 1 | 0% | -0.56% | -0.56 to -0.56% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.71% | -0.71 to -0.71% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.80% | -0.80 to -0.80% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.11% | +0.11 to +0.11% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.16% | -1.16 to -1.16% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.16% | -1.16 to -1.16% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.04% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.12% | up |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | monthly | writers even · few weak writers | 10 | 56% | -0.10% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | weekly | writers even · few weak writers | 7 | 14% | -0.41% | too few (7/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts | 4 | 50% | -0.05% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 3 | 0% | -0.25% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.23% | too few (2/10) |
| intraday | weekly | writers even · weak puts | 2 | 0% | -0.28% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.26% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.16% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
