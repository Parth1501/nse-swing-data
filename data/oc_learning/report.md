# Nifty option chain pattern log
Updated 2026-10-16 11:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 56 snapshots over 3 trading days
- 60 patterns logged; 47 different patterns so far

## Latest read (2026-10-16 11:45:31)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 3.2 | 23121 | 0.99 | 23050 | 22000 | 23200 | ±0.92% (22909-23333) | 12.67 |
| 2026-10-27 (monthly) | 11.2 | 23122 | 0.848 | 23100 | 22500 | 23500 | ±1.74% (22719-23524) | 12.43 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 14 times before; Nifty was up after it 79% of the time, average +0.19%. Too few outcomes (14/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.06%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 11 times before; Nifty was up after it 100% of the time, average +0.20%. Too few outcomes (10/20) to trade on.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.54%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23200, strongest put writers at 23000; weakest call writers at 23100, weakest put writers at -. Covers 74% of near-money call OI and 89% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 30495 | 15801 | 139.4 | 22804 | 326.7 | 22939 | -181 | -187.3 | weak |
| Call | 22850 | 14224 | 9451 | 140.8 | 22890 | 285.0 | 22991 | -130 | -144.2 | weak |
| Call | 22900 | 62978 | 43706 | 115.0 | 22881 | 241.9 | 23015 | -106 | -127.0 | weak |
| Call | 22950 | 45758 | 40838 | 115.8 | 22967 | 204.0 | 23066 | -55 | -88.2 | weak |
| Call | 23000 | 178613 | 137272 | 86.6 | 22936 | 167.2 | 23087 | -34 | -80.6 | weak |
| Call | 23050 | 114049 | 106290 | 84.4 | 22988 | 136.3 | 23134 | +14 | -51.9 | weak |
| Call | 23100 | 264707 | 214395 | 69.0 | 23004 | 106.2 | 23169 | +48 | -37.2 | weak |
| Call | 23150 | 206212 | 185997 | 64.9 | 23053 | 84.0 | 23215 | +94 | -19.1 | medium |
| Call | 23200 | 240562 | 167273 | 40.9 | 22993 | 64.2 | 23241 | +120 | -23.4 | strong |
| Call | 23250 | 104469 | 87163 | 29.8 | 22991 | 47.5 | 23280 | +159 | -17.6 | strong |
| Call | 23300 | 149847 | 101618 | 15.0 | 22905 | 35.6 | 23315 | +194 | -20.6 | strong |
| Call | 23350 | 80757 | 65958 | 16.3 | 22989 | 26.3 | 23366 | +245 | -10.0 | strong |
| Call | 23400 | 154577 | 112427 | 12.3 | 22992 | 19.3 | 23412 | +292 | -7.0 | strong |
| Call | 23450 | 55677 | 46051 | 10.0 | 22980 | 14.6 | 23460 | +339 | -4.6 | strong |
| Put | 22800 | 226541 | 212314 | 83.7 | 22935 | 27.0 | 22716 | +405 | +56.7 | strong |
| Put | 22850 | 110989 | 108081 | 91.4 | 22950 | 33.8 | 22759 | +362 | +57.6 | strong |
| Put | 22900 | 250687 | 246448 | 100.0 | 22974 | 42.1 | 22800 | +321 | +57.9 | strong |
| Put | 22950 | 153643 | 152235 | 118.8 | 22977 | 52.6 | 22831 | +290 | +66.1 | strong |
| Put | 23000 | 275099 | 269052 | 115.5 | 23036 | 66.5 | 22884 | +236 | +49.0 | strong |
| Put | 23050 | 127933 | 127503 | 121.8 | 23067 | 84.7 | 22928 | +193 | +37.1 | strong |
| Put | 23100 | 201039 | 199322 | 134.3 | 23089 | 105.7 | 22966 | +155 | +28.6 | strong |
| Put | 23150 | 82102 | 81992 | 153.8 | 23102 | 130.1 | 22996 | +125 | +23.8 | strong |
| Put | 23200 | 49613 | 49072 | 199.8 | 23084 | 160.9 | 23000 | +121 | +38.9 | strong |
| Put | 23250 | 11384 | 11099 | 235.2 | 23084 | 196.3 | 23015 | +106 | +38.9 | strong |
| Put | 23300 | 9739 | 8778 | 286.8 | 23071 | 233.9 | 23013 | +108 | +52.9 | strong |
| Put | 23350 | 1752 | 1676 | 335.0 | 23062 | 275.0 | 23015 | +106 | +60.0 | strong |
| Put | 23400 | 4542 | 2715 | 384.1 | 23054 | 318.6 | 23016 | +105 | +65.6 | strong |
| Put | 23450 | 2385 | 2323 | 502.9 | 22957 | 363.6 | 22947 | +174 | +139.4 | strong |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 23000, weakest put writers at -. Covers 33% of near-money call OI and 37% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 35295 | 11490 | 270.1 | 22865 | 403.6 | 23070 | -52 | -133.4 | weak |
| Call | 22850 | 5081 | 1286 | 276.7 | 22936 | 373.2 | 23127 | +5 | -96.6 | weak |
| Call | 22900 | 27577 | 11569 | 174.7 | 22768 | 330.4 | 23075 | -47 | -155.7 | weak |
| Call | 22950 | 6476 | 3447 | 207.6 | 22909 | 295.5 | 23158 | +36 | -87.9 | weak |
| Call | 23000 | 100188 | 26449 | 157.7 | 22835 | 266.4 | 23158 | +36 | -108.7 | weak |
| Call | 23050 | 5731 | 3064 | 152.0 | 22856 | 237.7 | 23202 | +80 | -85.7 | medium |
| Call | 23100 | 38890 | 14940 | 160.1 | 22972 | 208.0 | 23260 | +138 | -47.9 | strong |
| Call | 23150 | 7439 | 5040 | 163.2 | 23044 | 182.4 | 23313 | +192 | -19.2 | strong |
| Call | 23200 | 72304 | 23847 | 79.2 | 22767 | 158.8 | 23279 | +158 | -79.6 | strong |
| Call | 23250 | 7168 | 3653 | 92.7 | 22897 | 137.4 | 23343 | +221 | -44.7 | strong |
| Call | 23300 | 54831 | 8396 | 75.2 | 22896 | 118.0 | 23375 | +254 | -42.7 | strong |
| Call | 23350 | 6208 | 4294 | 64.0 | 22851 | 100.2 | 23414 | +292 | -36.2 | strong |
| Call | 23400 | 41367 | 11606 | 49.6 | 22841 | 85.4 | 23450 | +328 | -35.8 | strong |
| Call | 23450 | 5970 | 3759 | 44.3 | 22905 | 71.2 | 23494 | +373 | -27.0 | strong |
| Put | 22800 | 41862 | 14714 | 163.9 | 22932 | 90.3 | 22636 | +486 | +73.6 | strong |
| Put | 22850 | 8830 | 6277 | 195.3 | 22908 | 104.2 | 22655 | +467 | +91.2 | strong |
| Put | 22900 | 26408 | 16740 | 187.1 | 22958 | 118.2 | 22713 | +409 | +68.9 | strong |
| Put | 22950 | 11060 | 10099 | 192.0 | 22993 | 136.0 | 22758 | +364 | +56.0 | strong |
| Put | 23000 | 95257 | 46781 | 228.4 | 22975 | 152.9 | 22772 | +350 | +75.5 | strong |
| Put | 23050 | 4943 | 4366 | 201.8 | 23058 | 172.1 | 22848 | +273 | +29.8 | strong |
| Put | 23100 | 28402 | 13732 | 205.7 | 23096 | 194.6 | 22894 | +227 | +11.1 | strong |
| Put | 23150 | 4129 | 3776 | 231.6 | 23097 | 220.7 | 22918 | +203 | +10.9 | strong |
| Put | 23200 | 33677 | 7407 | 270.9 | 23075 | 246.0 | 22929 | +193 | +24.9 | strong |
| Put | 23250 | 1225 | 676 | 294.4 | 23084 | 272.1 | 22956 | +166 | +22.2 | strong |
| Put | 23300 | 29961 | 941 | 362.0 | 23029 | 302.1 | 22938 | +184 | +59.9 | strong |
| Put | 23350 | 598 | 283 | 397.9 | 23030 | 335.6 | 22952 | +170 | +62.3 | strong |
| Put | 23400 | 16236 | 938 | 494.4 | 22946 | 368.1 | 22906 | +216 | +126.2 | strong |
| Put | 23450 | 488 | 106 | 448.2 | 23056 | 398.9 | 23002 | +120 | +49.3 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 4 | 50% | -0.03% | -0.44 to +0.28% |  | too few (4/10) |
| weekly | PCR up · put writing · walls same · near call wall | 4 | 100% | +0.25% | +0.03 to +0.37% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 2 | 100% | +0.06% | +0.06 to +0.06% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.65% | +0.28 to +1.02% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.67% | +0.67 to +0.67% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.13% | +0.13 to +0.13% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.67% | +0.67 to +0.67% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.54% | +0.54 to +0.54% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls | 15 | 79% | +0.19% | up |
| intraday | monthly | writers even · weak calls | 12 | 100% | +0.20% | up |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | put writers stronger · few weak writers | 3 | 100% | +0.05% | too few (2/10) |
| intraday | weekly | writers even · few weak writers | 3 | 33% | -0.06% | too few (3/10) |
| intraday | monthly | writers even · few weak writers | 2 | 100% | +0.85% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers | 1 | 100% | +0.13% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 100% | +0.54% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.54% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
