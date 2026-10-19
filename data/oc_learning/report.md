# Nifty option chain pattern log
Updated 2026-10-19 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 84 snapshots over 4 trading days
- 92 patterns logged; 62 different patterns so far

## Latest read (2026-10-19 12:45:22)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 0.1 | 22932 | 0.838 | 22950 | 22900 | 23000 | ±0.47% (22823-23040) | 10.98 |
| 2026-10-27 (monthly) | 8.1 | 22938 | 0.934 | 23100 | 22000 | 23500 | ±1.57% (22578-23297) | 13.18 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls down · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · mid walls`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.14%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.03%. Too few outcomes (1/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23000, strongest put writers at 22800; weakest call writers at 22800, weakest put writers at 22950. Covers 91% of near-money call OI and 92% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22600 | 14268 | 9473 | 143.3 | 22598 | 315.9 | 22743 | -188 | -172.6 | weak |
| Call | 22650 | 7836 | 4940 | 133.6 | 22620 | 267.6 | 22784 | -148 | -134.0 | weak |
| Call | 22700 | 24059 | 9655 | 144.2 | 22716 | 220.0 | 22844 | -88 | -75.8 | weak |
| Call | 22750 | 9300 | 4476 | 134.2 | 22780 | 173.4 | 22884 | -48 | -39.3 | weak |
| Call | 22800 | 44424 | 35748 | 157.9 | 22924 | 130.8 | 22958 | +26 | +27.1 | weak |
| Call | 22850 | 35554 | 32562 | 126.2 | 22952 | 91.3 | 22976 | +44 | +34.9 | weak |
| Call | 22900 | 168546 | 157813 | 82.8 | 22942 | 59.8 | 22983 | +51 | +23.1 | medium |
| Call | 22950 | 307152 | 305401 | 55.7 | 22957 | 36.6 | 23006 | +74 | +19.1 | medium |
| Call | 23000 | 516121 | 492621 | 54.2 | 22978 | 21.8 | 23054 | +122 | +32.4 | strong |
| Call | 23050 | 325246 | 322138 | 57.1 | 23028 | 12.6 | 23107 | +175 | +44.5 | strong |
| Call | 23100 | 501068 | 479948 | 53.7 | 23049 | 7.5 | 23154 | +222 | +46.1 | strong |
| Call | 23150 | 315381 | 307601 | 54.4 | 23096 | 4.9 | 23204 | +273 | +49.5 | strong |
| Call | 23200 | 401276 | 366557 | 36.5 | 23085 | 3.4 | 23236 | +305 | +33.1 | strong |
| Call | 23250 | 177198 | 168648 | 28.1 | 23092 | 2.4 | 23278 | +346 | +25.8 | strong |
| Put | 22600 | 222425 | 178299 | 28.4 | 23002 | 1.8 | 22572 | +360 | +26.6 | strong |
| Put | 22650 | 159908 | 148483 | 28.0 | 23002 | 2.7 | 22622 | +310 | +25.3 | strong |
| Put | 22700 | 280052 | 247825 | 44.3 | 22977 | 4.8 | 22656 | +276 | +39.5 | strong |
| Put | 22750 | 189328 | 185640 | 35.0 | 22998 | 8.4 | 22715 | +217 | +26.6 | strong |
| Put | 22800 | 354212 | 344604 | 40.3 | 23012 | 15.2 | 22760 | +172 | +25.1 | strong |
| Put | 22850 | 253448 | 251496 | 37.6 | 23012 | 26.8 | 22812 | +119 | +10.8 | strong |
| Put | 22900 | 402986 | 400258 | 53.8 | 23026 | 45.4 | 22846 | +86 | +8.4 | medium |
| Put | 22950 | 253823 | 253044 | 58.9 | 23048 | 71.7 | 22891 | +41 | -12.8 | weak |
| Put | 23000 | 224083 | 222241 | 62.4 | 23088 | 106.8 | 22938 | -6 | -44.4 | weak |
| Put | 23050 | 80048 | 79999 | 62.0 | 23095 | 147.7 | 22988 | -56 | -85.6 | weak |
| Put | 23100 | 110957 | 110628 | 91.2 | 23111 | 192.8 | 23009 | -77 | -101.7 | weak |
| Put | 23150 | 64929 | 64907 | 103.5 | 23132 | 239.3 | 23047 | -115 | -135.9 | weak |
| Put | 23200 | 32539 | 32425 | 144.9 | 23118 | 288.4 | 23055 | -123 | -143.5 | weak |
| Put | 23250 | 8858 | 8803 | 173.9 | 23123 | 337.9 | 23076 | -144 | -164.0 | weak |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at 22500, weakest put writers at 23100. Covers 50% of near-money call OI and 49% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22600 | 19430 | 5466 | 261.9 | 22634 | 398.6 | 22862 | -76 | -136.6 | weak |
| Call | 22650 | 2983 | 798 | 244.9 | 22639 | 360.0 | 22895 | -43 | -115.1 | weak |
| Call | 22700 | 25827 | 6454 | 241.3 | 22701 | 324.9 | 22941 | +4 | -83.5 | weak |
| Call | 22750 | 5825 | 1289 | 250.3 | 22772 | 289.0 | 23000 | +63 | -38.7 | medium |
| Call | 22800 | 28068 | 10136 | 273.8 | 22883 | 258.2 | 23074 | +136 | +15.6 | strong |
| Call | 22850 | 5872 | 2316 | 267.6 | 22957 | 226.8 | 23118 | +180 | +40.8 | strong |
| Call | 22900 | 32700 | 18094 | 196.1 | 22856 | 197.4 | 23096 | +159 | -1.3 | strong |
| Call | 22950 | 13997 | 11565 | 188.2 | 22943 | 171.8 | 23138 | +201 | +16.4 | strong |
| Call | 23000 | 125993 | 62355 | 175.2 | 22943 | 147.7 | 23175 | +238 | +27.5 | strong |
| Call | 23050 | 15609 | 13221 | 169.4 | 22999 | 126.5 | 23219 | +282 | +42.9 | strong |
| Call | 23100 | 68480 | 45915 | 158.8 | 23027 | 107.0 | 23259 | +321 | +51.8 | strong |
| Call | 23150 | 25651 | 22732 | 132.6 | 23023 | 89.8 | 23283 | +345 | +42.8 | strong |
| Call | 23200 | 98935 | 52064 | 102.5 | 22931 | 75.8 | 23303 | +365 | +26.7 | strong |
| Call | 23250 | 29885 | 26419 | 79.4 | 22971 | 62.3 | 23329 | +392 | +17.1 | strong |
| Put | 22600 | 63181 | 35242 | 93.1 | 22970 | 66.5 | 22507 | +431 | +26.5 | strong |
| Put | 22650 | 10089 | 6240 | 89.5 | 23009 | 78.0 | 22560 | +377 | +11.5 | strong |
| Put | 22700 | 79962 | 41693 | 119.0 | 22967 | 90.8 | 22581 | +356 | +28.1 | strong |
| Put | 22750 | 14974 | 12975 | 89.6 | 23074 | 105.8 | 22660 | +277 | -16.2 | strong |
| Put | 22800 | 50680 | 23866 | 135.1 | 22984 | 123.1 | 22665 | +273 | +12.0 | strong |
| Put | 22850 | 10974 | 8806 | 154.6 | 22979 | 143.1 | 22695 | +242 | +11.5 | strong |
| Put | 22900 | 42382 | 33406 | 146.1 | 23037 | 163.6 | 22754 | +184 | -17.5 | strong |
| Put | 22950 | 16565 | 15764 | 177.2 | 22999 | 187.4 | 22773 | +165 | -10.3 | strong |
| Put | 23000 | 114158 | 69024 | 204.0 | 23004 | 214.2 | 22796 | +142 | -10.1 | strong |
| Put | 23050 | 8070 | 7679 | 179.3 | 23077 | 242.0 | 22871 | +67 | -62.7 | medium |
| Put | 23100 | 39790 | 26804 | 189.1 | 23116 | 273.0 | 22911 | +27 | -83.9 | weak |
| Put | 23150 | 6335 | 5766 | 214.2 | 23117 | 306.2 | 22936 | +2 | -92.0 | weak |
| Put | 23200 | 38345 | 14277 | 247.1 | 23103 | 339.4 | 22953 | -15 | -92.3 | weak |
| Put | 23250 | 1633 | 1198 | 279.1 | 23095 | 378.0 | 22971 | -33 | -98.8 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% | 0% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 3 | 33% | -0.11% | -0.47 to +0.14% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.05% | -0.33 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 3 | 100% | +0.14% | +0.11 to +0.17% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 2 | 50% | +0.06% | -0.03 to +0.15% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.08% | -0.93 to +0.78% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 2 | 100% | +0.14% | +0.07 to +0.21% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 1 | 0% | -0.29% | -0.29 to -0.29% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.92% | -0.92 to -0.92% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.50% | -0.50 to -0.50% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.53% | -0.53 to -0.53% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.51% | -0.51 to -0.51% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.59% | -0.59 to -0.59% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
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
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.90% | -0.90 to -0.90% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -0.90% | -0.90 to -0.90% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.07% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.14% | up |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | +0.00% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | monthly | writers even · few weak writers | 7 | 43% | +0.01% | too few (7/10) |
| intraday | weekly | writers even · few weak writers | 7 | 14% | -0.30% | too few (7/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts | 2 | 0% | -0.03% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts | 1 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak puts | 1 | 0% | -0.08% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.13% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -0.90% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
