# Nifty option chain pattern log
Updated 2026-10-16 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 60 snapshots over 3 trading days
- 64 patterns logged; 47 different patterns so far

## Latest read (2026-10-16 12:45:24)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 3.1 | 23130 | 1.038 | 23050 | 22000 | 23200 | ±0.87% (22929-23331) | 11.94 |
| 2026-10-27 (monthly) | 11.1 | 23126 | 0.857 | 23100 | 22500 | 23500 | ±1.7% (22734-23519) | 12.23 |

- **Weekly, last 30 min**: `PCR up · put writing · walls same · near call wall`. Seen 5 times before; Nifty was up after it 100% of the time, average +0.21%. Too few outcomes (5/20) to trade on.
  - Writers: `put writers stronger · weak calls`. Seen 15 times before; Nifty was up after it 80% of the time, average +0.19%. Too few outcomes (15/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put writing · walls same · mid walls`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.65%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 13 times before; Nifty was up after it 100% of the time, average +0.18%. Too few outcomes (12/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.58%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23200, strongest put writers at 23000; weakest call writers at 23100, weakest put writers at -. Covers 74% of near-money call OI and 89% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 28511 | 14773 | 139.4 | 22804 | 337.5 | 22939 | -191 | -198.1 | weak |
| Call | 22850 | 13315 | 8847 | 140.8 | 22890 | 293.2 | 22991 | -139 | -152.4 | weak |
| Call | 22900 | 59165 | 41059 | 115.0 | 22881 | 249.7 | 23015 | -115 | -134.7 | weak |
| Call | 22950 | 41914 | 37408 | 115.8 | 22967 | 209.7 | 23066 | -64 | -93.9 | weak |
| Call | 23000 | 158433 | 121762 | 86.6 | 22936 | 170.9 | 23087 | -43 | -84.4 | weak |
| Call | 23050 | 101749 | 94827 | 84.4 | 22988 | 137.1 | 23134 | +4 | -52.6 | weak |
| Call | 23100 | 269681 | 221450 | 71.4 | 23013 | 107.7 | 23171 | +41 | -36.3 | weak |
| Call | 23150 | 198788 | 179301 | 64.9 | 23053 | 82.7 | 23215 | +85 | -17.8 | medium |
| Call | 23200 | 245692 | 172403 | 41.5 | 22997 | 62.5 | 23241 | +111 | -21.0 | strong |
| Call | 23250 | 114877 | 97817 | 31.8 | 23008 | 46.0 | 23282 | +152 | -14.3 | strong |
| Call | 23300 | 161135 | 112906 | 16.9 | 22927 | 33.8 | 23317 | +187 | -16.9 | strong |
| Call | 23350 | 87948 | 73149 | 17.1 | 23003 | 24.4 | 23367 | +237 | -7.3 | strong |
| Call | 23400 | 157421 | 115418 | 12.5 | 22995 | 17.8 | 23413 | +283 | -5.2 | strong |
| Call | 23450 | 56716 | 47119 | 10.1 | 22984 | 13.3 | 23460 | +330 | -3.3 | strong |
| Put | 22800 | 230570 | 216343 | 82.6 | 22938 | 22.8 | 22717 | +413 | +59.8 | strong |
| Put | 22850 | 114782 | 111874 | 89.4 | 22955 | 28.1 | 22761 | +369 | +61.2 | strong |
| Put | 22900 | 257965 | 253726 | 98.2 | 22979 | 35.5 | 22802 | +328 | +62.7 | strong |
| Put | 22950 | 159749 | 158341 | 115.9 | 22982 | 44.8 | 22834 | +296 | +71.2 | strong |
| Put | 23000 | 286051 | 280004 | 113.3 | 23039 | 57.1 | 22887 | +243 | +56.2 | strong |
| Put | 23050 | 122895 | 122482 | 121.8 | 23067 | 73.0 | 22928 | +202 | +48.8 | strong |
| Put | 23100 | 245676 | 243959 | 128.3 | 23095 | 93.2 | 22972 | +158 | +35.1 | strong |
| Put | 23150 | 109440 | 109330 | 146.2 | 23108 | 118.0 | 23004 | +126 | +28.2 | strong |
| Put | 23200 | 58246 | 57705 | 192.8 | 23091 | 147.4 | 23007 | +123 | +45.3 | strong |
| Put | 23250 | 15210 | 14925 | 222.0 | 23095 | 181.1 | 23028 | +102 | +40.9 | medium |
| Put | 23300 | 12022 | 11075 | 272.0 | 23084 | 219.0 | 23028 | +102 | +53.0 | medium |
| Put | 23350 | 2126 | 2050 | 321.7 | 23074 | 259.8 | 23028 | +102 | +61.9 | medium |
| Put | 23400 | 4968 | 3177 | 371.0 | 23066 | 303.1 | 23029 | +101 | +67.9 | medium |
| Put | 23450 | 2435 | 2373 | 499.7 | 22961 | 349.7 | 22950 | +180 | +150.0 | strong |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 23000, weakest put writers at -. Covers 34% of near-money call OI and 38% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 34997 | 11393 | 270.1 | 22865 | 416.1 | 23070 | -56 | -146.0 | weak |
| Call | 22850 | 5047 | 1284 | 277.3 | 22938 | 376.8 | 23127 | +1 | -99.5 | weak |
| Call | 22900 | 28084 | 12076 | 181.5 | 22783 | 339.2 | 23082 | -45 | -157.7 | weak |
| Call | 22950 | 6408 | 3411 | 207.6 | 22909 | 304.3 | 23158 | +31 | -96.7 | weak |
| Call | 23000 | 101244 | 27628 | 162.4 | 22847 | 273.1 | 23162 | +36 | -110.7 | weak |
| Call | 23050 | 5819 | 3152 | 154.3 | 22864 | 240.8 | 23204 | +78 | -86.5 | medium |
| Call | 23100 | 39446 | 15982 | 163.9 | 22984 | 211.8 | 23264 | +138 | -47.9 | strong |
| Call | 23150 | 7342 | 4974 | 163.2 | 23044 | 186.8 | 23313 | +187 | -23.6 | strong |
| Call | 23200 | 73293 | 24854 | 82.6 | 22781 | 161.9 | 23283 | +156 | -79.3 | strong |
| Call | 23250 | 7489 | 3974 | 96.3 | 22915 | 139.2 | 23346 | +220 | -42.9 | strong |
| Call | 23300 | 55390 | 8955 | 77.8 | 22910 | 118.5 | 23378 | +252 | -40.7 | strong |
| Call | 23350 | 6369 | 4455 | 65.2 | 22860 | 99.8 | 23415 | +289 | -34.6 | strong |
| Call | 23400 | 41703 | 11942 | 50.5 | 22849 | 84.8 | 23451 | +324 | -34.2 | strong |
| Call | 23450 | 6178 | 3967 | 45.6 | 22916 | 70.5 | 23496 | +369 | -24.8 | strong |
| Put | 22800 | 43163 | 16015 | 157.6 | 22948 | 83.7 | 22642 | +484 | +73.9 | strong |
| Put | 22850 | 8852 | 6299 | 195.0 | 22909 | 96.5 | 22655 | +471 | +98.5 | strong |
| Put | 22900 | 26976 | 17308 | 184.6 | 22963 | 109.5 | 22715 | +411 | +75.1 | strong |
| Put | 22950 | 10971 | 10018 | 192.0 | 22993 | 125.6 | 22758 | +368 | +66.4 | strong |
| Put | 23000 | 97036 | 48560 | 225.4 | 22980 | 142.4 | 22775 | +352 | +83.0 | strong |
| Put | 23050 | 4953 | 4401 | 199.8 | 23062 | 161.6 | 22850 | +276 | +38.2 | strong |
| Put | 23100 | 30269 | 15599 | 203.3 | 23100 | 182.3 | 22897 | +230 | +21.1 | strong |
| Put | 23150 | 5201 | 4848 | 228.0 | 23102 | 205.9 | 22922 | +204 | +22.1 | strong |
| Put | 23200 | 34858 | 8588 | 265.8 | 23082 | 231.0 | 22934 | +192 | +34.8 | strong |
| Put | 23250 | 1242 | 702 | 292.4 | 23086 | 257.6 | 22958 | +169 | +34.8 | strong |
| Put | 23300 | 30491 | 1471 | 339.3 | 23062 | 287.6 | 22961 | +166 | +51.6 | strong |
| Put | 23350 | 632 | 317 | 390.3 | 23040 | 319.8 | 22960 | +167 | +70.5 | strong |
| Put | 23400 | 16096 | 950 | 491.1 | 22950 | 352.2 | 22909 | +217 | +138.9 | strong |
| Put | 23450 | 511 | 129 | 442.9 | 23068 | 387.7 | 23007 | +119 | +55.2 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.21% | +0.03 to +0.37% |  | too few (5/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 5 | 60% | -0.02% | -0.44 to +0.28% |  | too few (5/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 3 | 100% | +0.65% | +0.28 to +1.02% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 2 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.69% | +0.69 to +0.69% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.06% | +0.06 to +0.06% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.11% | +0.11 to +0.11% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.71% | +0.71 to +0.71% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.08% | +0.08 to +0.08% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.58% | +0.58 to +0.58% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.58% | +0.58 to +0.58% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls | 16 | 80% | +0.19% | up |
| intraday | monthly | writers even · weak calls | 14 | 100% | +0.18% | up |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | put writers stronger · few weak writers | 4 | 100% | +0.05% | too few (3/10) |
| intraday | weekly | writers even · few weak writers | 3 | 33% | -0.05% | too few (3/10) |
| intraday | monthly | writers even · few weak writers | 2 | 100% | +0.86% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers | 1 | 100% | +0.15% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 100% | +0.58% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.58% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
