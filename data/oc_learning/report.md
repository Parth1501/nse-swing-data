# Nifty option chain pattern log
Updated 2026-10-16 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 70 snapshots over 3 trading days
- 76 patterns logged; 51 different patterns so far

## Latest read (2026-10-16 15:40:00)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 3.0 | 23146 | 0.975 | 23050 | 22000 | 24000 | ±0.79% (22963-23330) | 10.94 |
| 2026-10-27 (monthly) | 11.0 | 23146 | 0.876 | 23150 | 22500 | 23500 | ±1.68% (22757-23535) | 11.98 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 16 times before; Nifty was up after it 81% of the time, average +0.20%. Too few outcomes (16/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put writing · walls same · mid walls`. Seen 3 times before; Nifty was up after it 100% of the time, average +0.46%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 17 times before; Nifty was up after it 100% of the time, average +0.19%. Too few outcomes (16/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.65%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 23100, weakest put writers at -. Covers 74% of near-money call OI and 89% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 21612 | 11428 | 146.6 | 22816 | 310.0 | 22947 | -200 | -163.4 | weak |
| Call | 22850 | 10368 | 7112 | 153.0 | 22910 | 265.7 | 23003 | -143 | -112.7 | weak |
| Call | 22900 | 43139 | 30454 | 121.0 | 22893 | 221.8 | 23021 | -125 | -100.8 | weak |
| Call | 22950 | 17899 | 15994 | 116.7 | 22968 | 182.0 | 23067 | -79 | -65.3 | weak |
| Call | 23000 | 104123 | 80023 | 86.6 | 22936 | 144.0 | 23087 | -60 | -57.4 | weak |
| Call | 23050 | 54156 | 50821 | 87.7 | 23000 | 112.2 | 23138 | -8 | -24.5 | weak |
| Call | 23100 | 147060 | 124850 | 75.0 | 23030 | 85.0 | 23175 | +29 | -9.9 | weak |
| Call | 23150 | 100394 | 91581 | 66.2 | 23061 | 62.8 | 23216 | +70 | +3.4 | medium |
| Call | 23200 | 149761 | 107712 | 42.7 | 23007 | 45.0 | 23243 | +97 | -2.3 | medium |
| Call | 23250 | 74868 | 64103 | 32.2 | 23012 | 32.4 | 23282 | +136 | -0.2 | strong |
| Call | 23300 | 122260 | 87699 | 17.8 | 22942 | 23.1 | 23318 | +172 | -5.3 | strong |
| Call | 23350 | 68002 | 58045 | 17.6 | 23019 | 16.4 | 23368 | +221 | +1.2 | strong |
| Call | 23400 | 113299 | 83960 | 12.6 | 23000 | 11.7 | 23413 | +266 | +1.0 | strong |
| Call | 23450 | 65089 | 55496 | 10.1 | 23004 | 9.0 | 23460 | +314 | +1.1 | strong |
| Put | 22800 | 164207 | 154353 | 80.8 | 22943 | 18.1 | 22719 | +427 | +62.7 | strong |
| Put | 22850 | 88436 | 86288 | 86.7 | 22962 | 23.9 | 22763 | +383 | +62.9 | strong |
| Put | 22900 | 174081 | 171266 | 97.1 | 22981 | 30.0 | 22803 | +343 | +67.1 | strong |
| Put | 22950 | 94220 | 93407 | 114.5 | 22985 | 40.2 | 22836 | +311 | +74.2 | strong |
| Put | 23000 | 177528 | 174023 | 109.4 | 23044 | 54.0 | 22891 | +256 | +55.5 | strong |
| Put | 23050 | 64110 | 63928 | 114.0 | 23073 | 71.0 | 22936 | +210 | +42.9 | strong |
| Put | 23100 | 139796 | 138902 | 125.0 | 23097 | 93.8 | 22975 | +171 | +31.1 | strong |
| Put | 23150 | 64296 | 64242 | 140.8 | 23110 | 120.7 | 23009 | +137 | +20.1 | strong |
| Put | 23200 | 34887 | 34606 | 186.3 | 23095 | 152.7 | 23014 | +132 | +33.6 | strong |
| Put | 23250 | 7549 | 7424 | 216.8 | 23098 | 189.7 | 23033 | +113 | +27.1 | strong |
| Put | 23300 | 7722 | 7192 | 264.8 | 23089 | 230.3 | 23035 | +111 | +34.5 | strong |
| Put | 23350 | 1980 | 1920 | 312.7 | 23081 | 274.7 | 23037 | +109 | +38.0 | strong |
| Put | 23400 | 3435 | 2324 | 360.4 | 23074 | 318.1 | 23040 | +107 | +42.3 | strong |
| Put | 23450 | 2408 | 2348 | 495.3 | 22965 | 368.1 | 22955 | +191 | +127.2 | strong |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 23000, weakest put writers at -. Covers 36% of near-money call OI and 41% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 33893 | 11074 | 270.8 | 22866 | 385.8 | 23071 | -75 | -115.0 | weak |
| Call | 22850 | 4882 | 1282 | 280.7 | 22944 | 347.8 | 23131 | -15 | -67.1 | weak |
| Call | 22900 | 27619 | 12068 | 185.8 | 22793 | 314.9 | 23086 | -60 | -129.1 | weak |
| Call | 22950 | 5407 | 2878 | 207.6 | 22909 | 271.2 | 23158 | +11 | -63.6 | weak |
| Call | 23000 | 91036 | 24843 | 162.4 | 22847 | 251.9 | 23162 | +16 | -89.5 | weak |
| Call | 23050 | 5418 | 2963 | 155.9 | 22869 | 218.9 | 23206 | +60 | -63.1 | medium |
| Call | 23100 | 39834 | 17216 | 167.8 | 22998 | 194.3 | 23268 | +122 | -26.6 | strong |
| Call | 23150 | 10732 | 8415 | 167.9 | 23077 | 171.5 | 23318 | +172 | -3.6 | strong |
| Call | 23200 | 77493 | 30147 | 94.9 | 22846 | 147.1 | 23295 | +149 | -52.2 | strong |
| Call | 23250 | 8356 | 4885 | 102.3 | 22951 | 126.5 | 23352 | +206 | -24.2 | strong |
| Call | 23300 | 57842 | 13724 | 91.7 | 22989 | 109.0 | 23392 | +246 | -17.3 | strong |
| Call | 23350 | 7010 | 5134 | 69.1 | 22901 | 90.6 | 23419 | +273 | -21.5 | strong |
| Call | 23400 | 39290 | 11844 | 52.5 | 22867 | 77.1 | 23452 | +306 | -24.6 | strong |
| Call | 23450 | 6356 | 4216 | 47.2 | 22935 | 64.6 | 23497 | +351 | -17.4 | strong |
| Put | 22800 | 45279 | 18214 | 148.6 | 22970 | 84.4 | 22651 | +495 | +64.2 | strong |
| Put | 22850 | 8910 | 6444 | 189.5 | 22920 | 97.4 | 22660 | +486 | +92.1 | strong |
| Put | 22900 | 38309 | 28879 | 153.0 | 23028 | 112.7 | 22747 | +399 | +40.3 | strong |
| Put | 22950 | 10018 | 9176 | 189.7 | 22997 | 131.6 | 22760 | +386 | +58.2 | strong |
| Put | 23000 | 96312 | 49162 | 222.2 | 22985 | 148.0 | 22778 | +368 | +74.2 | strong |
| Put | 23050 | 4987 | 4486 | 195.6 | 23068 | 168.6 | 22854 | +292 | +27.1 | strong |
| Put | 23100 | 30325 | 16252 | 202.2 | 23103 | 191.2 | 22898 | +248 | +10.9 | strong |
| Put | 23150 | 5512 | 5187 | 224.8 | 23105 | 217.7 | 22925 | +221 | +7.1 | strong |
| Put | 23200 | 35822 | 9981 | 260.8 | 23087 | 242.0 | 22939 | +207 | +18.8 | strong |
| Put | 23250 | 1315 | 811 | 285.8 | 23093 | 275.9 | 22964 | +182 | +9.9 | strong |
| Put | 23300 | 32084 | 3667 | 314.1 | 23109 | 302.6 | 22986 | +160 | +11.6 | strong |
| Put | 23350 | 605 | 323 | 382.1 | 23051 | 331.1 | 22968 | +178 | +51.0 | strong |
| Put | 23400 | 16254 | 1168 | 466.8 | 22978 | 369.9 | 22933 | +213 | +97.0 | strong |
| Put | 23450 | 497 | 131 | 440.6 | 23071 | 406.2 | 23009 | +137 | +34.3 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% |  | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 3 | 33% | -0.11% | -0.47 to +0.14% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 2 | 100% | +0.14% | +0.07 to +0.21% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 2 | 100% | +0.14% | +0.11 to +0.17% |  | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 18 | 100% | +0.19% | up |
| intraday | weekly | put writers stronger · weak calls | 17 | 81% | +0.20% | up |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | weekly | put writers stronger · few weak writers | 9 | 100% | +0.12% | too few (8/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | writers even · few weak writers | 3 | 100% | +0.65% | too few (3/10) |
| intraday | weekly | writers even · few weak writers | 3 | 33% | -0.03% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.23% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 100% | +0.65% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
