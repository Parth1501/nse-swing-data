# Nifty option chain pattern log
Updated 2026-10-21 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 99 snapshots over 5 trading days
- 107 patterns logged; 71 different patterns so far

## Latest read (2026-10-21 09:45:28)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 6.2 | 23094 | 0.861 | 23100 | 23000 | 23500 | ±1.45% (22758-23429) | 14.12 |
| 2026-11-23 (monthly) | 33.2 | 23094 | 0.814 | 23000 | 23000 | 24000 | ±3.32% (22326-23862) | 13.7 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 8 times before; Nifty was up after it 25% of the time, average -0.31%. Too few outcomes (8/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.23%. Too few outcomes (2/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `put writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23100, strongest put writers at 23000; weakest call writers at 22900, weakest put writers at 23700. Covers 70% of near-money call OI and 72% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22750 | 6723 | 2238 | 254.1 | 22820 | 409.3 | 23004 | -89 | -155.2 | weak |
| Call | 22800 | 33649 | 17292 | 252.5 | 22881 | 370.5 | 23053 | -41 | -118.0 | weak |
| Call | 22850 | 9277 | 6925 | 211.6 | 22890 | 332.5 | 23062 | -32 | -120.9 | weak |
| Call | 22900 | 65069 | 52521 | 179.9 | 22875 | 294.4 | 23080 | -14 | -114.5 | weak |
| Call | 22950 | 16935 | 15021 | 173.6 | 22919 | 261.2 | 23124 | +30 | -87.6 | weak |
| Call | 23000 | 157798 | 96921 | 165.6 | 22937 | 228.9 | 23166 | +72 | -63.3 | medium |
| Call | 23050 | 50680 | 48295 | 186.2 | 23056 | 199.3 | 23236 | +143 | -13.2 | strong |
| Call | 23100 | 139208 | 117498 | 159.9 | 23050 | 171.6 | 23260 | +166 | -11.7 | strong |
| Call | 23150 | 62949 | 60313 | 134.0 | 23046 | 146.3 | 23284 | +190 | -12.4 | strong |
| Call | 23200 | 144368 | 97610 | 102.1 | 22971 | 123.6 | 23302 | +209 | -21.5 | strong |
| Call | 23250 | 46918 | 43521 | 84.3 | 23001 | 103.2 | 23334 | +241 | -19.0 | strong |
| Call | 23300 | 113174 | 69391 | 77.5 | 23024 | 85.3 | 23377 | +284 | -7.8 | strong |
| Call | 23350 | 30588 | 29361 | 56.3 | 22988 | 69.8 | 23406 | +313 | -13.4 | strong |
| Call | 23400 | 84211 | 57451 | 53.0 | 23017 | 56.5 | 23453 | +359 | -3.6 | strong |
| Put | 22750 | 30569 | 28622 | 77.0 | 23057 | 53.2 | 22673 | +421 | +23.7 | strong |
| Put | 22800 | 89543 | 62729 | 107.0 | 23000 | 63.5 | 22693 | +401 | +43.5 | strong |
| Put | 22850 | 31494 | 29326 | 115.7 | 23014 | 75.1 | 22734 | +359 | +40.6 | strong |
| Put | 22900 | 92474 | 83498 | 129.5 | 23027 | 88.1 | 22770 | +323 | +41.4 | strong |
| Put | 22950 | 37475 | 36851 | 128.8 | 23060 | 103.6 | 22821 | +272 | +25.2 | strong |
| Put | 23000 | 199059 | 158805 | 155.9 | 23055 | 122.0 | 22844 | +249 | +33.8 | strong |
| Put | 23050 | 67723 | 67439 | 144.7 | 23092 | 141.4 | 22905 | +188 | +3.3 | strong |
| Put | 23100 | 122189 | 109589 | 173.1 | 23094 | 164.1 | 22927 | +167 | +9.0 | strong |
| Put | 23150 | 23305 | 22819 | 205.0 | 23083 | 189.4 | 22945 | +149 | +15.6 | strong |
| Put | 23200 | 55819 | 32182 | 231.5 | 23095 | 216.1 | 22969 | +125 | +15.4 | strong |
| Put | 23250 | 4805 | 4398 | 264.9 | 23079 | 245.7 | 22985 | +108 | +19.2 | strong |
| Put | 23300 | 36407 | 9243 | 305.5 | 23089 | 277.5 | 22994 | +99 | +28.0 | medium |
| Put | 23350 | 1376 | 1165 | 338.2 | 23075 | 311.9 | 23012 | +82 | +26.3 | medium |
| Put | 23400 | 17995 | 3228 | 413.2 | 23025 | 347.2 | 22987 | +107 | +66.0 | strong |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23200, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23700. Covers 2% of near-money call OI and 9% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 23200 | 14026 | 497 | 377.1 | 23094 | 377.1 | 23577 | +483 | +0.0 | strong |
| Call | 23250 | 1402 | 8 | 355.0 | 23094 | 355.0 | 23605 | +511 | +0.0 | strong |
| Call | 23350 | 1033 | 4 | 305.0 | 23094 | 305.0 | 23655 | +561 | +0.0 | strong |
| Call | 23400 | 6309 | 87 | 277.8 | 23094 | 277.8 | 23678 | +584 | +0.0 | strong |
| Put | 22750 | 853 | 255 | 218.4 | 23094 | 218.4 | 22532 | +562 | +0.0 | strong |
| Put | 22800 | 10461 | 386 | 234.3 | 23094 | 234.3 | 22566 | +528 | +0.0 | strong |
| Put | 22850 | 3130 | 18 | 243.0 | 23094 | 243.0 | 22607 | +487 | +0.0 | strong |
| Put | 22900 | 4562 | 478 | 262.5 | 23094 | 262.5 | 22638 | +456 | +0.0 | strong |
| Put | 22950 | 796 | 12 | 278.2 | 23094 | 278.2 | 22672 | +422 | +0.0 | strong |
| Put | 23000 | 47276 | 5423 | 298.8 | 23094 | 298.8 | 22701 | +393 | +0.0 | strong |
| Put | 23050 | 714 | 126 | 318.2 | 23094 | 318.2 | 22732 | +362 | +0.0 | strong |
| Put | 23100 | 7054 | 859 | 333.9 | 23094 | 333.9 | 22766 | +328 | +0.0 | strong |
| Put | 23150 | 1579 | 161 | 355.0 | 23094 | 355.0 | 22795 | +299 | +0.0 | strong |
| Put | 23200 | 8927 | 877 | 378.6 | 23094 | 378.6 | 22821 | +272 | +0.0 | strong |
| Put | 23250 | 468 | 42 | 397.0 | 23094 | 397.0 | 22853 | +241 | +0.0 | strong |
| Put | 23300 | 2420 | 140 | 425.4 | 23094 | 425.4 | 22875 | +219 | +0.0 | strong |
| Put | 23350 | 102 | 3 | 445.9 | 23094 | 445.9 | 22904 | +190 | +0.0 | strong |
| Put | 23400 | 1958 | 90 | 471.4 | 23094 | 471.4 | 22929 | +165 | +0.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% | 0% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 3 | 67% | +0.02% | -0.21 to +0.17% |  | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.74% | -0.74 to -0.74% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 1 | 0% | -0.51% | -0.51 to -0.51% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.71% | -0.71 to -0.71% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 12 | 50% | +0.00% | no clear direction |
| intraday | monthly | writers even · few weak writers | 11 | 64% | -0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | weekly | writers even · few weak writers | 9 | 25% | -0.31% | too few (8/10) |
| intraday | weekly | call writers stronger · weak puts | 5 | 50% | -0.03% | too few (4/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | put writers stronger · few weak writers | 3 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts | 3 | 0% | -0.20% | too few (3/10) |
| intraday | weekly | writers even · weak puts | 3 | 67% | -0.06% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 100% | +1.28% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | put writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts | 1 | 100% | +0.90% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
