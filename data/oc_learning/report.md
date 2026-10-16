# Nifty option chain pattern log
Updated 2026-10-16 10:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 52 snapshots over 3 trading days
- 56 patterns logged; 44 different patterns so far

## Latest read (2026-10-16 10:45:32)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 3.2 | 23111 | 1.053 | 23000 | 22000 | 23200 | ±0.96% (22889-23333) | 13.25 |
| 2026-10-27 (monthly) | 11.2 | 23111 | 0.85 | 23100 | 22500 | 23500 | ±1.75% (22706-23517) | 12.59 |

- **Weekly, last 30 min**: `PCR up · put writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 12 times before; Nifty was up after it 75% of the time, average +0.20%. Too few outcomes (12/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 10 times before; Nifty was up after it 100% of the time, average +0.21%. Too few outcomes (9/20) to trade on.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.50%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23200, strongest put writers at 23000; weakest call writers at 23100, weakest put writers at -. Covers 71% of near-money call OI and 88% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 33966 | 17600 | 139.4 | 22804 | 308.9 | 22939 | -172 | -169.6 | weak |
| Call | 22850 | 15558 | 10337 | 140.8 | 22890 | 266.9 | 22991 | -120 | -126.1 | weak |
| Call | 22900 | 64846 | 45002 | 115.0 | 22881 | 226.8 | 23015 | -96 | -111.8 | weak |
| Call | 22950 | 47594 | 42160 | 111.1 | 22958 | 189.1 | 23061 | -50 | -77.9 | weak |
| Call | 23000 | 172793 | 131452 | 83.7 | 22929 | 155.8 | 23084 | -27 | -72.2 | weak |
| Call | 23050 | 94025 | 86153 | 75.4 | 22963 | 126.0 | 23125 | +14 | -50.5 | weak |
| Call | 23100 | 205785 | 155473 | 58.9 | 22971 | 99.8 | 23159 | +48 | -40.9 | weak |
| Call | 23150 | 160613 | 140398 | 60.0 | 23035 | 77.8 | 23210 | +99 | -17.8 | medium |
| Call | 23200 | 211474 | 138185 | 37.0 | 22970 | 59.7 | 23237 | +126 | -22.7 | strong |
| Call | 23250 | 98722 | 81096 | 28.1 | 22979 | 45.2 | 23278 | +167 | -17.1 | strong |
| Call | 23300 | 147966 | 97865 | 13.7 | 22891 | 33.7 | 23314 | +203 | -20.0 | strong |
| Call | 23350 | 72187 | 57388 | 14.9 | 22970 | 25.2 | 23365 | +254 | -10.4 | strong |
| Call | 23400 | 151590 | 109001 | 12.1 | 22986 | 18.7 | 23412 | +301 | -6.6 | strong |
| Call | 23450 | 49494 | 39868 | 9.4 | 22962 | 14.1 | 23459 | +348 | -4.7 | strong |
| Put | 22800 | 219591 | 205364 | 85.6 | 22928 | 33.0 | 22714 | +397 | +52.7 | strong |
| Put | 22850 | 109932 | 106964 | 93.2 | 22944 | 40.6 | 22757 | +354 | +52.6 | strong |
| Put | 22900 | 252821 | 248459 | 101.2 | 22971 | 50.5 | 22799 | +312 | +50.6 | strong |
| Put | 22950 | 168851 | 167293 | 119.2 | 22976 | 63.4 | 22831 | +280 | +55.8 | strong |
| Put | 23000 | 268743 | 262402 | 119.2 | 23029 | 79.0 | 22881 | +230 | +40.2 | strong |
| Put | 23050 | 106346 | 105916 | 127.9 | 23059 | 98.8 | 22922 | +189 | +29.1 | strong |
| Put | 23100 | 171939 | 170188 | 139.8 | 23083 | 122.3 | 22960 | +151 | +17.5 | strong |
| Put | 23150 | 85659 | 85517 | 159.3 | 23098 | 150.2 | 22991 | +120 | +9.1 | strong |
| Put | 23200 | 48509 | 47880 | 207.2 | 23077 | 182.2 | 22993 | +118 | +25.0 | strong |
| Put | 23250 | 9875 | 9554 | 247.2 | 23073 | 217.6 | 23003 | +108 | +29.6 | strong |
| Put | 23300 | 9361 | 8224 | 300.8 | 23058 | 256.4 | 22999 | +112 | +44.3 | strong |
| Put | 23350 | 1713 | 1621 | 350.0 | 23047 | 298.7 | 23000 | +111 | +51.3 | strong |
| Put | 23400 | 4408 | 2389 | 400.9 | 23036 | 340.9 | 22999 | +112 | +60.0 | strong |
| Put | 23450 | 2393 | 2331 | 502.9 | 22957 | 388.6 | 22947 | +164 | +114.3 | strong |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 23000, weakest put writers at -. Covers 31% of near-money call OI and 35% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 32998 | 9193 | 237.4 | 22802 | 402.2 | 23037 | -74 | -164.8 | weak |
| Call | 22850 | 5083 | 1243 | 273.3 | 22929 | 366.1 | 23123 | +12 | -92.8 | weak |
| Call | 22900 | 27739 | 11417 | 170.1 | 22758 | 328.0 | 23070 | -41 | -157.9 | weak |
| Call | 22950 | 6397 | 3368 | 205.6 | 22904 | 296.7 | 23156 | +44 | -91.1 | weak |
| Call | 23000 | 96609 | 22870 | 142.5 | 22793 | 265.4 | 23142 | +31 | -122.8 | weak |
| Call | 23050 | 6008 | 3212 | 152.0 | 22856 | 236.0 | 23202 | +91 | -84.0 | medium |
| Call | 23100 | 34839 | 10889 | 146.6 | 22926 | 208.5 | 23247 | +135 | -61.9 | strong |
| Call | 23150 | 7003 | 4604 | 161.6 | 23037 | 183.4 | 23312 | +200 | -21.8 | strong |
| Call | 23200 | 69969 | 21512 | 71.0 | 22730 | 158.9 | 23271 | +160 | -87.9 | strong |
| Call | 23250 | 6702 | 3187 | 87.5 | 22868 | 138.0 | 23338 | +226 | -50.5 | strong |
| Call | 23300 | 54166 | 7716 | 72.2 | 22879 | 117.7 | 23372 | +261 | -45.5 | strong |
| Call | 23350 | 5874 | 3960 | 61.4 | 22830 | 100.6 | 23411 | +300 | -39.2 | strong |
| Call | 23400 | 39729 | 9968 | 44.6 | 22799 | 85.1 | 23445 | +333 | -40.5 | strong |
| Call | 23450 | 6019 | 3783 | 44.1 | 22904 | 71.0 | 23494 | +383 | -26.9 | strong |
| Put | 22800 | 39380 | 12232 | 178.7 | 22894 | 91.8 | 22621 | +490 | +86.9 | strong |
| Put | 22850 | 8405 | 5852 | 201.6 | 22894 | 106.0 | 22648 | +463 | +95.5 | strong |
| Put | 22900 | 26108 | 16376 | 189.1 | 22953 | 120.0 | 22711 | +400 | +69.0 | strong |
| Put | 22950 | 10016 | 9055 | 198.1 | 22979 | 138.8 | 22752 | +359 | +59.3 | strong |
| Put | 23000 | 92861 | 44375 | 231.8 | 22968 | 155.6 | 22768 | +343 | +76.2 | strong |
| Put | 23050 | 4446 | 3869 | 205.0 | 23052 | 174.8 | 22845 | +266 | +30.2 | strong |
| Put | 23100 | 24383 | 9713 | 207.9 | 23091 | 197.1 | 22892 | +219 | +10.9 | strong |
| Put | 23150 | 3206 | 2839 | 235.8 | 23087 | 222.1 | 22914 | +197 | +13.7 | strong |
| Put | 23200 | 31649 | 5379 | 278.2 | 23062 | 246.9 | 22922 | +190 | +31.3 | strong |
| Put | 23250 | 1258 | 618 | 300.5 | 23074 | 276.2 | 22950 | +162 | +24.2 | strong |
| Put | 23300 | 29960 | 927 | 362.9 | 23028 | 305.2 | 22937 | +174 | +57.8 | strong |
| Put | 23350 | 648 | 284 | 407.3 | 23016 | 341.9 | 22943 | +169 | +65.4 | strong |
| Put | 23400 | 16171 | 873 | 503.4 | 22933 | 375.0 | 22897 | +215 | +128.4 | strong |
| Put | 23450 | 478 | 96 | 452.0 | 23051 | 421.6 | 22998 | +113 | +30.5 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put writing · walls same · near call wall | 4 | 100% | +0.25% | +0.03 to +0.37% |  | too few (4/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 4 | 50% | -0.03% | -0.44 to +0.28% |  | too few (4/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.65% | +0.28 to +1.02% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls | 13 | 75% | +0.20% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | monthly | writers even · weak calls | 11 | 100% | +0.21% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | put writers stronger · few weak writers | 3 | 100% | +0.05% | too few (2/10) |
| intraday | weekly | writers even · few weak writers | 3 | 33% | -0.08% | too few (3/10) |
| intraday | monthly | writers even · few weak writers | 2 | 100% | +0.82% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 100% | +0.50% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.50% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
