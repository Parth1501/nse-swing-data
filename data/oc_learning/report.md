# Nifty option chain pattern log
Updated 2026-10-19 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 73 snapshots over 4 trading days
- 80 patterns logged; 54 different patterns so far

## Latest read (2026-10-19 09:45:08)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 0.2 | 23147 | 0.966 | 23100 | 23000 | 23200 | ±0.63% (23002-23292) | 14.89 |
| 2026-10-27 (monthly) | 8.2 | 23151 | 0.86 | 23150 | 22000 | 23500 | ±1.56% (22789-23513) | 13.25 |

- **Weekly, last 30 min**: `PCR flat · put and call writing · walls same · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.78%. Too few outcomes (1/20) to trade on.
  - Writers: `put writers stronger · few weak writers`. Seen 9 times before; Nifty was up after it 100% of the time, average +0.12%. Too few outcomes (8/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.65%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 19 times before; Nifty was up after it 100% of the time, average +0.18%. Too few outcomes (17/20) to trade on.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.33%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23300, strongest put writers at 23000; weakest call writers at 23100, weakest put writers at -. Covers 85% of near-money call OI and 93% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 18410 | 9734 | 146.6 | 22816 | 345.4 | 22947 | -200 | -198.8 | weak |
| Call | 22850 | 9525 | 6533 | 153.0 | 22910 | 296.0 | 23003 | -144 | -143.0 | weak |
| Call | 22900 | 39020 | 27546 | 121.0 | 22893 | 251.1 | 23021 | -126 | -130.0 | weak |
| Call | 22950 | 22759 | 20974 | 141.8 | 23019 | 204.6 | 23092 | -55 | -62.8 | weak |
| Call | 23000 | 120540 | 97040 | 101.9 | 22977 | 164.8 | 23102 | -45 | -62.9 | weak |
| Call | 23050 | 67456 | 64301 | 97.6 | 23037 | 126.9 | 23148 | +1 | -29.3 | weak |
| Call | 23100 | 221065 | 199945 | 82.6 | 23077 | 93.6 | 23183 | +36 | -11.0 | weak |
| Call | 23150 | 242611 | 234086 | 66.8 | 23114 | 67.1 | 23217 | +70 | -0.3 | medium |
| Call | 23200 | 314189 | 275899 | 45.0 | 23097 | 46.2 | 23245 | +98 | -1.2 | medium |
| Call | 23250 | 179838 | 169538 | 31.2 | 23098 | 30.7 | 23281 | +134 | +0.5 | strong |
| Call | 23300 | 244327 | 210378 | 18.9 | 23063 | 19.6 | 23319 | +172 | -0.8 | strong |
| Call | 23350 | 118681 | 108780 | 15.1 | 23079 | 12.2 | 23365 | +218 | +2.8 | strong |
| Call | 23400 | 190738 | 161658 | 10.2 | 23071 | 7.6 | 23410 | +263 | +2.6 | strong |
| Call | 23450 | 112473 | 102895 | 7.6 | 23070 | 4.6 | 23458 | +311 | +3.0 | strong |
| Put | 22800 | 251527 | 241919 | 52.7 | 23020 | 6.3 | 22747 | +399 | +46.4 | strong |
| Put | 22850 | 133408 | 131333 | 58.3 | 23030 | 8.8 | 22792 | +355 | +49.4 | strong |
| Put | 22900 | 263653 | 260925 | 66.3 | 23041 | 12.4 | 22834 | +313 | +53.9 | strong |
| Put | 22950 | 172198 | 171419 | 68.5 | 23062 | 18.2 | 22882 | +265 | +50.2 | strong |
| Put | 23000 | 329649 | 326246 | 69.5 | 23094 | 26.6 | 22930 | +216 | +42.9 | strong |
| Put | 23050 | 152480 | 152311 | 68.2 | 23118 | 38.8 | 22982 | +165 | +29.5 | strong |
| Put | 23100 | 250859 | 249967 | 94.1 | 23119 | 55.7 | 23006 | +141 | +38.4 | strong |
| Put | 23150 | 151175 | 151123 | 103.5 | 23132 | 78.0 | 23047 | +100 | +25.5 | medium |
| Put | 23200 | 73109 | 72832 | 144.6 | 23122 | 108.0 | 23055 | +91 | +36.5 | medium |
| Put | 23250 | 18172 | 18050 | 172.4 | 23127 | 142.7 | 23078 | +69 | +29.8 | medium |
| Put | 23300 | 15302 | 14782 | 221.6 | 23119 | 182.2 | 23078 | +68 | +39.4 | medium |
| Put | 23350 | 2846 | 2787 | 285.1 | 23102 | 225.7 | 23065 | +82 | +59.4 | medium |
| Put | 23400 | 4881 | 3794 | 324.2 | 23103 | 270.0 | 23076 | +71 | +54.2 | medium |
| Put | 23450 | 2744 | 2673 | 473.5 | 22987 | 315.9 | 22976 | +170 | +157.6 | strong |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 23000, weakest put writers at -. Covers 41% of near-money call OI and 45% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22850 | 4899 | 1324 | 284.0 | 22952 | 368.7 | 23134 | -17 | -84.7 | weak |
| Call | 22900 | 26598 | 11622 | 185.8 | 22793 | 329.9 | 23086 | -65 | -144.2 | weak |
| Call | 22950 | 5382 | 2937 | 212.2 | 22922 | 295.4 | 23162 | +11 | -83.2 | weak |
| Call | 23000 | 93962 | 30324 | 183.3 | 22912 | 260.6 | 23183 | +32 | -77.3 | weak |
| Call | 23050 | 7002 | 4614 | 183.6 | 22975 | 229.7 | 23234 | +82 | -46.1 | medium |
| Call | 23100 | 47564 | 24999 | 177.8 | 23046 | 199.7 | 23278 | +127 | -21.9 | strong |
| Call | 23150 | 13185 | 10266 | 169.1 | 23090 | 174.8 | 23319 | +168 | -5.7 | strong |
| Call | 23200 | 83406 | 36535 | 104.9 | 22902 | 149.2 | 23305 | +154 | -44.4 | strong |
| Call | 23250 | 9723 | 6257 | 108.0 | 22995 | 128.2 | 23358 | +207 | -20.2 | strong |
| Call | 23300 | 62730 | 18704 | 96.2 | 23033 | 108.6 | 23396 | +245 | -12.4 | strong |
| Call | 23350 | 13819 | 11868 | 81.3 | 23043 | 90.6 | 23431 | +280 | -9.3 | strong |
| Call | 23400 | 45609 | 18308 | 60.8 | 22968 | 75.9 | 23461 | +310 | -15.1 | strong |
| Call | 23450 | 7576 | 5514 | 51.2 | 22992 | 62.5 | 23501 | +350 | -11.2 | strong |
| Put | 22850 | 9811 | 7364 | 175.1 | 22951 | 80.3 | 22675 | +476 | +94.8 | strong |
| Put | 22900 | 40448 | 31303 | 146.6 | 23041 | 92.2 | 22753 | +398 | +54.3 | strong |
| Put | 22950 | 11372 | 10550 | 177.5 | 23020 | 108.5 | 22773 | +379 | +69.0 | strong |
| Put | 23000 | 99920 | 54786 | 208.4 | 23009 | 124.8 | 22792 | +360 | +83.6 | strong |
| Put | 23050 | 6442 | 5945 | 182.4 | 23089 | 142.9 | 22868 | +284 | +39.5 | strong |
| Put | 23100 | 40867 | 26800 | 187.3 | 23122 | 164.4 | 22913 | +238 | +22.9 | strong |
| Put | 23150 | 7943 | 7215 | 214.2 | 23118 | 187.0 | 22936 | +215 | +27.1 | strong |
| Put | 23200 | 38803 | 13782 | 246.6 | 23106 | 213.3 | 22953 | +198 | +33.3 | strong |
| Put | 23250 | 1605 | 1112 | 272.4 | 23109 | 239.1 | 22978 | +174 | +33.4 | strong |
| Put | 23300 | 33591 | 5180 | 302.0 | 23121 | 272.7 | 22998 | +153 | +29.3 | strong |
| Put | 23350 | 731 | 450 | 359.4 | 23080 | 301.8 | 22991 | +161 | +57.6 | strong |
| Put | 23400 | 16201 | 1164 | 466.8 | 22978 | 338.1 | 22933 | +218 | +128.7 | strong |
| Put | 23450 | 505 | 151 | 429.8 | 23085 | 375.6 | 23020 | +131 | +54.2 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% | 0% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 3 | 33% | -0.11% | -0.47 to +0.14% |  | too few (3/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 2 | 100% | +0.14% | +0.11 to +0.17% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 100% | +0.78% | +0.78 to +0.78% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 2 | 100% | +0.14% | +0.07 to +0.21% | 0% of 1 | too few (2/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% | 100% of 1 | too few (1/10) |
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
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 100% | +0.18% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.19% | up |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 100% | +0.12% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | writers even · few weak writers | 3 | 100% | +0.65% | too few (3/10) |
| intraday | weekly | writers even · few weak writers | 3 | 33% | -0.03% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.23% | too few (2/10) |
| day | monthly | writers even · weak calls | 3 | 100% | +0.33% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers | 2 | 100% | +0.65% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 100% | +0.02% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
