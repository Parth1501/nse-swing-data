# Nifty option chain pattern log
Updated 2026-10-16 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 63 snapshots over 3 trading days
- 68 patterns logged; 49 different patterns so far

## Latest read (2026-10-16 13:44:52)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 3.1 | 23121 | 1.038 | 23050 | 23000 | 23200 | ±0.82% (22931-23312) | 11.2 |
| 2026-10-27 (monthly) | 11.1 | 23121 | 0.869 | 23100 | 22500 | 23500 | ±1.68% (22733-23510) | 11.93 |

- **Weekly, last 30 min**: `PCR flat · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. Seen 5 times before; Nifty was up after it 100% of the time, average +0.04%. Too few outcomes (4/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.54%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls same · mid walls`. Seen 6 times before; Nifty was up after it 67% of the time, average -0.02%. Too few outcomes (6/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 15 times before; Nifty was up after it 86% of the time, average +0.15%. Too few outcomes (14/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.54%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23200, strongest put writers at 23000; weakest call writers at 23000, weakest put writers at -. Covers 76% of near-money call OI and 90% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 26991 | 13986 | 139.4 | 22804 | 334.8 | 22939 | -182 | -195.4 | weak |
| Call | 22850 | 12710 | 8563 | 146.4 | 22900 | 289.6 | 22996 | -125 | -143.3 | weak |
| Call | 22900 | 55174 | 38290 | 115.0 | 22881 | 246.3 | 23015 | -106 | -131.4 | weak |
| Call | 22950 | 40165 | 35889 | 116.7 | 22968 | 205.2 | 23067 | -55 | -88.5 | weak |
| Call | 23000 | 147811 | 113599 | 86.6 | 22936 | 167.1 | 23087 | -35 | -80.5 | weak |
| Call | 23050 | 96747 | 90326 | 85.5 | 22992 | 132.6 | 23135 | +14 | -47.1 | weak |
| Call | 23100 | 273416 | 228144 | 73.7 | 23022 | 102.7 | 23174 | +52 | -29.0 | medium |
| Call | 23150 | 221980 | 202493 | 66.2 | 23061 | 78.0 | 23216 | +95 | -11.8 | medium |
| Call | 23200 | 261027 | 187738 | 42.7 | 23007 | 58.0 | 23243 | +121 | -15.3 | strong |
| Call | 23250 | 117800 | 100862 | 32.2 | 23012 | 42.3 | 23282 | +161 | -10.1 | strong |
| Call | 23300 | 165633 | 118811 | 17.8 | 22942 | 30.7 | 23318 | +196 | -12.9 | strong |
| Call | 23350 | 97903 | 83104 | 17.6 | 23016 | 22.2 | 23368 | +246 | -4.6 | strong |
| Call | 23400 | 162204 | 120201 | 12.6 | 23000 | 16.1 | 23413 | +291 | -3.4 | strong |
| Call | 23450 | 60392 | 50795 | 10.2 | 22994 | 11.9 | 23460 | +339 | -1.7 | strong |
| Put | 22800 | 229114 | 214997 | 82.5 | 22938 | 20.3 | 22717 | +404 | +62.2 | strong |
| Put | 22850 | 111710 | 108896 | 89.0 | 22956 | 25.1 | 22761 | +360 | +63.9 | strong |
| Put | 22900 | 254497 | 250315 | 98.2 | 22979 | 31.8 | 22802 | +320 | +66.3 | strong |
| Put | 22950 | 160326 | 158926 | 115.3 | 22984 | 40.7 | 22835 | +287 | +74.6 | strong |
| Put | 23000 | 298793 | 292746 | 110.8 | 23043 | 52.7 | 22889 | +232 | +58.1 | strong |
| Put | 23050 | 133009 | 132596 | 118.1 | 23071 | 68.0 | 22932 | +190 | +50.2 | strong |
| Put | 23100 | 261951 | 260234 | 125.8 | 23097 | 87.8 | 22974 | +147 | +38.0 | strong |
| Put | 23150 | 129138 | 129029 | 140.8 | 23110 | 112.8 | 23009 | +112 | +28.1 | strong |
| Put | 23200 | 67077 | 66536 | 186.3 | 23095 | 143.2 | 23014 | +108 | +43.0 | strong |
| Put | 23250 | 15530 | 15272 | 216.8 | 23098 | 177.4 | 23033 | +88 | +39.4 | medium |
| Put | 23300 | 12409 | 11528 | 266.0 | 23088 | 216.2 | 23034 | +87 | +49.9 | medium |
| Put | 23350 | 2424 | 2348 | 314.5 | 23080 | 257.4 | 23036 | +86 | +57.1 | medium |
| Put | 23400 | 5518 | 3734 | 360.4 | 23074 | 301.4 | 23040 | +82 | +59.0 | medium |
| Put | 23450 | 2474 | 2413 | 496.0 | 22965 | 346.6 | 22954 | +167 | +149.3 | strong |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 23000, weakest put writers at -. Covers 34% of near-money call OI and 40% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 34663 | 11284 | 270.1 | 22865 | 410.7 | 23070 | -51 | -140.6 | weak |
| Call | 22850 | 5057 | 1294 | 278.0 | 22939 | 375.0 | 23128 | +7 | -97.0 | weak |
| Call | 22900 | 28432 | 12424 | 185.8 | 22793 | 334.6 | 23086 | -36 | -148.9 | weak |
| Call | 22950 | 6302 | 3355 | 207.6 | 22909 | 301.8 | 23158 | +36 | -94.2 | weak |
| Call | 23000 | 95602 | 26089 | 162.4 | 22847 | 268.6 | 23162 | +41 | -106.1 | weak |
| Call | 23050 | 5806 | 3152 | 154.7 | 22865 | 238.2 | 23205 | +83 | -83.4 | medium |
| Call | 23100 | 39791 | 16596 | 165.9 | 22990 | 209.0 | 23266 | +144 | -43.1 | strong |
| Call | 23150 | 7811 | 5465 | 165.1 | 23051 | 183.4 | 23315 | +194 | -18.3 | strong |
| Call | 23200 | 73639 | 25200 | 83.6 | 22786 | 158.3 | 23284 | +162 | -74.7 | strong |
| Call | 23250 | 7573 | 4058 | 97.1 | 22919 | 137.8 | 23347 | +226 | -40.7 | strong |
| Call | 23300 | 59432 | 12997 | 89.7 | 22976 | 116.3 | 23390 | +268 | -26.6 | strong |
| Call | 23350 | 6392 | 4493 | 65.7 | 22865 | 98.5 | 23416 | +294 | -32.8 | strong |
| Call | 23400 | 42088 | 12356 | 51.6 | 22858 | 83.2 | 23452 | +330 | -31.6 | strong |
| Call | 23450 | 6104 | 3919 | 45.6 | 22916 | 69.5 | 23496 | +374 | -23.9 | strong |
| Put | 22800 | 43445 | 16373 | 155.8 | 22952 | 82.6 | 22644 | +477 | +73.2 | strong |
| Put | 22850 | 9069 | 6516 | 191.7 | 22916 | 94.2 | 22658 | +463 | +97.5 | strong |
| Put | 22900 | 37118 | 27450 | 156.3 | 23022 | 107.5 | 22744 | +378 | +48.8 | strong |
| Put | 22950 | 11335 | 10382 | 189.7 | 22997 | 122.8 | 22760 | +361 | +66.9 | strong |
| Put | 23000 | 98368 | 49892 | 223.2 | 22984 | 140.6 | 22777 | +345 | +82.6 | strong |
| Put | 23050 | 5233 | 4681 | 197.4 | 23065 | 158.0 | 22853 | +269 | +39.4 | strong |
| Put | 23100 | 30690 | 16020 | 202.8 | 23100 | 179.7 | 22897 | +224 | +23.1 | strong |
| Put | 23150 | 5750 | 5405 | 224.9 | 23105 | 203.2 | 22925 | +196 | +21.8 | strong |
| Put | 23200 | 35805 | 9535 | 262.4 | 23086 | 228.2 | 22938 | +184 | +34.3 | strong |
| Put | 23250 | 1387 | 847 | 286.4 | 23092 | 257.0 | 22964 | +158 | +29.4 | strong |
| Put | 23300 | 31080 | 2147 | 322.7 | 23081 | 287.0 | 22977 | +144 | +35.7 | strong |
| Put | 23350 | 619 | 322 | 385.1 | 23046 | 317.9 | 22965 | +157 | +67.2 | strong |
| Put | 23400 | 16083 | 950 | 491.1 | 22950 | 350.7 | 22909 | +213 | +140.4 | strong |
| Put | 23450 | 508 | 130 | 441.9 | 23068 | 382.0 | 23008 | +113 | +59.9 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 7 | 67% | -0.02% | -0.44 to +0.28% |  | too few (6/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 83% | +0.16% | -0.04 to +0.37% |  | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 3 | 67% | +0.43% | -0.02 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 2 | 50% | +0.03% | -0.00 to +0.06% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.67% | +0.67 to +0.67% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.13% | +0.13 to +0.13% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.00% | +0.00 to +0.00% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.08% | +0.08 to +0.08% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.67% | +0.67 to +0.67% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 16 | 86% | +0.15% | up |
| intraday | weekly | put writers stronger · weak calls | 16 | 75% | +0.16% | up |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | weekly | put writers stronger · few weak writers | 6 | 100% | +0.04% | too few (4/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · few weak writers | 3 | 33% | -0.06% | too few (3/10) |
| intraday | monthly | writers even · few weak writers | 2 | 100% | +0.85% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers | 1 | 100% | +0.13% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 100% | +0.54% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 2 | 100% | +0.54% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
