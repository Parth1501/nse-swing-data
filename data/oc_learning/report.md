# Nifty option chain pattern log
Updated 2026-10-19 10:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 76 snapshots over 4 trading days
- 84 patterns logged; 58 different patterns so far

## Latest read (2026-10-19 10:45:08)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 0.2 | 23048 | 0.932 | 23050 | 23000 | 23200 | ±0.56% (22919-23177) | 13.21 |
| 2026-10-27 (monthly) | 8.2 | 23053 | 0.926 | 23150 | 22000 | 23500 | ±1.56% (22693-23412) | 12.96 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Nifty was up after it 25% of the time, average -0.04%. Too few outcomes (4/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Nifty was up after it 75% of the time, average +0.48%. Too few outcomes (4/20) to trade on.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23200, strongest put writers at 23000; weakest call writers at 22950, weakest put writers at 23100. Covers 88% of near-money call OI and 92% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22750 | 8483 | 3427 | 117.3 | 22721 | 295.1 | 22867 | -181 | -177.9 | weak |
| Call | 22800 | 19783 | 11107 | 161.0 | 22846 | 249.2 | 22961 | -87 | -88.2 | weak |
| Call | 22850 | 10963 | 7971 | 162.6 | 22936 | 203.8 | 23013 | -36 | -41.1 | weak |
| Call | 22900 | 43548 | 32074 | 126.6 | 22915 | 160.1 | 23027 | -22 | -33.5 | weak |
| Call | 22950 | 34185 | 32400 | 135.8 | 23031 | 121.3 | 23086 | +38 | +14.4 | weak |
| Call | 23000 | 158568 | 135068 | 99.5 | 22999 | 87.3 | 23100 | +51 | +12.2 | medium |
| Call | 23050 | 168470 | 165315 | 78.6 | 23049 | 59.5 | 23129 | +80 | +19.1 | medium |
| Call | 23100 | 356294 | 335174 | 67.7 | 23069 | 39.0 | 23168 | +119 | +28.6 | strong |
| Call | 23150 | 305163 | 296638 | 59.0 | 23102 | 24.6 | 23209 | +161 | +34.4 | strong |
| Call | 23200 | 411889 | 373599 | 38.3 | 23087 | 15.2 | 23238 | +190 | +23.0 | strong |
| Call | 23250 | 201688 | 191652 | 28.7 | 23093 | 9.3 | 23279 | +231 | +19.4 | strong |
| Call | 23300 | 280422 | 246473 | 17.1 | 23062 | 5.8 | 23317 | +269 | +11.3 | strong |
| Call | 23350 | 158494 | 148593 | 12.2 | 23072 | 3.6 | 23362 | +314 | +8.6 | strong |
| Put | 22750 | 138182 | 134494 | 45.7 | 23008 | 5.2 | 22704 | +344 | +40.5 | strong |
| Put | 22800 | 274524 | 264916 | 48.8 | 23024 | 8.1 | 22751 | +297 | +40.7 | strong |
| Put | 22850 | 149891 | 147816 | 53.1 | 23033 | 12.5 | 22797 | +251 | +40.6 | strong |
| Put | 22900 | 294673 | 291945 | 61.2 | 23043 | 19.6 | 22839 | +209 | +41.6 | strong |
| Put | 22950 | 184153 | 183374 | 65.9 | 23062 | 30.6 | 22884 | +164 | +35.4 | strong |
| Put | 23000 | 349292 | 345889 | 68.0 | 23092 | 46.8 | 22932 | +116 | +21.3 | strong |
| Put | 23050 | 186404 | 186245 | 66.8 | 23105 | 69.3 | 22983 | +65 | -2.5 | medium |
| Put | 23100 | 197647 | 196944 | 94.1 | 23119 | 98.5 | 23006 | +42 | -4.4 | weak |
| Put | 23150 | 107566 | 107529 | 103.5 | 23132 | 134.4 | 23047 | +2 | -31.0 | weak |
| Put | 23200 | 51138 | 50945 | 144.6 | 23122 | 174.7 | 23055 | -7 | -30.1 | weak |
| Put | 23250 | 13688 | 13596 | 172.4 | 23127 | 218.2 | 23078 | -29 | -45.8 | weak |
| Put | 23300 | 9420 | 9100 | 221.6 | 23119 | 265.4 | 23078 | -30 | -43.8 | weak |
| Put | 23350 | 2612 | 2559 | 285.2 | 23101 | 314.1 | 23065 | -17 | -28.9 | weak |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 22900, weakest put writers at 23600. Covers 44% of near-money call OI and 47% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22750 | 5710 | 1136 | 241.9 | 22745 | 370.0 | 22992 | -61 | -128.1 | weak |
| Call | 22800 | 27161 | 8880 | 270.9 | 22866 | 333.8 | 23071 | +18 | -62.9 | weak |
| Call | 22850 | 5065 | 1490 | 286.9 | 22964 | 303.6 | 23137 | +84 | -16.6 | medium |
| Call | 22900 | 26639 | 12033 | 190.3 | 22808 | 264.8 | 23090 | +38 | -74.5 | weak |
| Call | 22950 | 5653 | 3221 | 214.3 | 22934 | 234.6 | 23164 | +112 | -20.2 | strong |
| Call | 23000 | 97138 | 33500 | 186.3 | 22926 | 205.7 | 23186 | +134 | -19.4 | strong |
| Call | 23050 | 9930 | 7542 | 183.1 | 23006 | 177.5 | 23233 | +181 | +5.6 | strong |
| Call | 23100 | 53524 | 30959 | 173.8 | 23047 | 153.2 | 23274 | +221 | +20.5 | strong |
| Call | 23150 | 15114 | 12195 | 164.5 | 23085 | 131.6 | 23314 | +262 | +32.9 | strong |
| Call | 23200 | 88550 | 41679 | 106.4 | 22921 | 112.0 | 23306 | +254 | -5.6 | strong |
| Call | 23250 | 13268 | 9802 | 104.5 | 23018 | 94.0 | 23354 | +302 | +10.4 | strong |
| Call | 23300 | 68349 | 24323 | 93.0 | 23038 | 78.7 | 23393 | +340 | +14.4 | strong |
| Call | 23350 | 15003 | 13052 | 80.0 | 23044 | 65.0 | 23430 | +377 | +15.1 | strong |
| Put | 22750 | 20830 | 18003 | 89.4 | 23076 | 75.4 | 22661 | +392 | +14.0 | strong |
| Put | 22800 | 46444 | 19630 | 143.2 | 22979 | 88.1 | 22657 | +396 | +55.1 | strong |
| Put | 22850 | 11961 | 9514 | 157.4 | 22975 | 103.5 | 22693 | +360 | +53.8 | strong |
| Put | 22900 | 41144 | 31999 | 145.9 | 23041 | 119.1 | 22754 | +298 | +26.8 | strong |
| Put | 22950 | 12055 | 11233 | 174.6 | 23023 | 138.6 | 22775 | +277 | +36.0 | strong |
| Put | 23000 | 103682 | 58548 | 205.1 | 23012 | 159.4 | 22795 | +258 | +45.7 | strong |
| Put | 23050 | 9322 | 8825 | 180.7 | 23078 | 182.1 | 22869 | +183 | -1.4 | strong |
| Put | 23100 | 41574 | 27719 | 188.3 | 23118 | 207.6 | 22912 | +141 | -19.3 | strong |
| Put | 23150 | 7314 | 6644 | 214.2 | 23118 | 235.8 | 22936 | +117 | -21.6 | strong |
| Put | 23200 | 39038 | 14017 | 246.8 | 23105 | 264.1 | 22953 | +99 | -17.4 | medium |
| Put | 23250 | 1567 | 1125 | 275.3 | 23103 | 298.2 | 22975 | +78 | -22.9 | medium |
| Put | 23300 | 33338 | 5141 | 302.0 | 23121 | 333.4 | 22998 | +55 | -31.4 | medium |
| Put | 23350 | 700 | 441 | 360.0 | 23078 | 369.4 | 22990 | +63 | -9.3 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% | 0% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 3 | 33% | -0.11% | -0.47 to +0.14% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 2 | 100% | +0.14% | +0.11 to +0.17% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 2 | 100% | +0.14% | +0.07 to +0.21% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.18% | -0.43 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.43% | -0.43 to -0.43% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% | 0% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 1 | 0% | -0.06% | -0.06 to -0.06% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -0.40% | -0.40 to -0.40% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.13% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.17% | up |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | +0.06% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | monthly | writers even · few weak writers | 5 | 75% | +0.48% | too few (4/10) |
| intraday | weekly | writers even · few weak writers | 5 | 25% | -0.04% | too few (4/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.23% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | +0.12% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -0.40% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
