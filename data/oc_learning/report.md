# Nifty option chain pattern log
Updated 2026-10-15 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 45 snapshots over 2 trading days
- 48 patterns logged; 36 different patterns so far

## Latest read (2026-10-15 15:40:00)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 4.0 | 22997 | 1.061 | 22900 | 22500 | 24000 | ±1.01% (22766-23229) | 11.89 |
| 2026-10-27 (monthly) | 12.0 | 22997 | 0.804 | 23000 | 22000 | 23500 | ±1.77% (22590-23404) | 12.0 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.05%. Too few outcomes (2/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · call writing · walls down · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.03%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 7 times before; Nifty was up after it 100% of the time, average +0.21%. Too few outcomes (7/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23300, strongest put writers at 22700; weakest call writers at 22900, weakest put writers at 23550. Covers 46% of near-money call OI and 75% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22700 | 42945 | 13642 | 110.2 | 22620 | 292.9 | 22810 | -187 | -182.7 | weak |
| Call | 22750 | 20340 | 8218 | 117.3 | 22721 | 252.0 | 22867 | -130 | -134.7 | weak |
| Call | 22800 | 45159 | 19006 | 108.3 | 22726 | 214.0 | 22908 | -89 | -105.7 | weak |
| Call | 22850 | 20205 | 8262 | 89.5 | 22747 | 179.9 | 22939 | -58 | -90.5 | weak |
| Call | 22900 | 72976 | 31706 | 70.8 | 22713 | 145.1 | 22971 | -27 | -74.3 | weak |
| Call | 22950 | 36802 | 18233 | 106.1 | 22894 | 116.2 | 23056 | +59 | -10.1 | medium |
| Call | 23000 | 131761 | 52474 | 65.2 | 22783 | 91.8 | 23065 | +68 | -26.6 | medium |
| Call | 23050 | 52859 | 39130 | 81.6 | 22911 | 70.7 | 23132 | +134 | +10.9 | strong |
| Call | 23100 | 101875 | 41389 | 60.8 | 22920 | 53.1 | 23161 | +163 | +7.7 | strong |
| Call | 23150 | 38841 | 17984 | 43.5 | 22893 | 39.0 | 23194 | +196 | +4.5 | strong |
| Call | 23200 | 104736 | 31657 | 31.2 | 22826 | 28.1 | 23231 | +234 | +3.1 | strong |
| Call | 23250 | 46171 | 28887 | 25.9 | 22909 | 20.4 | 23276 | +279 | +5.5 | strong |
| Call | 23300 | 112257 | 62367 | 11.6 | 22839 | 14.2 | 23312 | +314 | -2.6 | strong |
| Put | 22700 | 173052 | 128123 | 97.4 | 22811 | 41.7 | 22603 | +395 | +55.7 | strong |
| Put | 22750 | 76212 | 70236 | 105.1 | 22836 | 50.0 | 22645 | +352 | +55.0 | strong |
| Put | 22800 | 134975 | 120362 | 106.6 | 22884 | 62.4 | 22693 | +304 | +44.2 | strong |
| Put | 22850 | 79136 | 75208 | 106.7 | 22924 | 76.3 | 22743 | +254 | +30.4 | strong |
| Put | 22900 | 123539 | 118244 | 122.9 | 22930 | 94.8 | 22777 | +220 | +28.0 | strong |
| Put | 22950 | 53682 | 52097 | 135.2 | 22951 | 115.5 | 22815 | +183 | +19.7 | strong |
| Put | 23000 | 91867 | 85376 | 148.1 | 22973 | 140.0 | 22852 | +145 | +8.1 | strong |
| Put | 23050 | 18529 | 18068 | 157.4 | 22999 | 169.1 | 22893 | +105 | -11.7 | strong |
| Put | 23100 | 18406 | 16657 | 197.3 | 22982 | 201.3 | 22903 | +95 | -4.0 | medium |
| Put | 23150 | 3475 | 3323 | 227.9 | 22986 | 238.2 | 22922 | +75 | -10.3 | medium |
| Put | 23200 | 6174 | 5535 | 283.9 | 22961 | 274.0 | 22916 | +81 | +9.9 | medium |
| Put | 23250 | 1833 | 1529 | 315.8 | 22972 | 319.9 | 22934 | +63 | -4.1 | medium |
| Put | 23300 | 3062 | 1909 | 360.9 | 22968 | 360.1 | 22939 | +58 | +0.8 | medium |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 22800, weakest put writers at 23600. Covers 22% of near-money call OI and 25% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22700 | 52629 | 11601 | 223.6 | 22655 | 385.1 | 22924 | -74 | -161.5 | weak |
| Call | 22750 | 6572 | 1027 | 189.3 | 22635 | 347.9 | 22939 | -58 | -158.7 | weak |
| Call | 22800 | 58420 | 16276 | 237.4 | 22802 | 312.7 | 23037 | +40 | -75.3 | weak |
| Call | 22850 | 5235 | 819 | 214.4 | 22805 | 282.2 | 23064 | +67 | -67.8 | medium |
| Call | 22900 | 32905 | 12866 | 163.3 | 22739 | 249.4 | 23063 | +66 | -86.1 | medium |
| Call | 22950 | 5665 | 2561 | 200.9 | 22882 | 222.2 | 23151 | +154 | -21.2 | strong |
| Call | 23000 | 102389 | 15571 | 103.2 | 22659 | 195.0 | 23103 | +106 | -91.8 | strong |
| Call | 23050 | 5982 | 2764 | 136.9 | 22797 | 170.1 | 23187 | +190 | -33.2 | strong |
| Call | 23100 | 28981 | 4105 | 94.3 | 22730 | 147.9 | 23194 | +197 | -53.6 | strong |
| Call | 23150 | 3341 | 933 | 101.7 | 22804 | 130.4 | 23252 | +254 | -28.8 | strong |
| Call | 23200 | 68489 | 18893 | 61.3 | 22681 | 109.7 | 23261 | +264 | -48.3 | strong |
| Call | 23250 | 5935 | 2420 | 79.4 | 22815 | 93.5 | 23329 | +332 | -14.0 | strong |
| Call | 23300 | 51764 | 5226 | 57.8 | 22796 | 79.6 | 23358 | +360 | -21.9 | strong |
| Put | 22700 | 67925 | 25783 | 162.0 | 22856 | 99.0 | 22538 | +459 | +62.9 | strong |
| Put | 22750 | 9961 | 5186 | 185.6 | 22828 | 114.5 | 22564 | +433 | +71.1 | strong |
| Put | 22800 | 36468 | 9183 | 202.1 | 22841 | 129.0 | 22598 | +399 | +73.1 | strong |
| Put | 22850 | 7700 | 5147 | 211.1 | 22875 | 147.0 | 22639 | +358 | +64.1 | strong |
| Put | 22900 | 23350 | 13418 | 201.4 | 22927 | 165.9 | 22699 | +299 | +35.5 | strong |
| Put | 22950 | 8069 | 7108 | 209.7 | 22955 | 188.8 | 22740 | +257 | +20.9 | strong |
| Put | 23000 | 77291 | 26088 | 273.8 | 22895 | 212.0 | 22726 | +271 | +61.8 | strong |
| Put | 23050 | 1949 | 1372 | 230.5 | 23001 | 236.1 | 22820 | +178 | -5.6 | strong |
| Put | 23100 | 21663 | 1703 | 279.2 | 22956 | 262.4 | 22821 | +177 | +16.9 | strong |
| Put | 23150 | 682 | 313 | 315.1 | 22949 | 288.1 | 22835 | +162 | +27.0 | strong |
| Put | 23200 | 28228 | 1603 | 351.9 | 22944 | 323.1 | 22848 | +149 | +28.8 | strong |
| Put | 23250 | 748 | 107 | 386.2 | 22941 | 362.2 | 22864 | +134 | +24.0 | strong |
| Put | 23300 | 29753 | 423 | 431.6 | 22927 | 394.0 | 22868 | +129 | +37.6 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put writing · walls same · near call wall | 4 | 100% | +0.25% | +0.03 to +0.37% |  | too few (4/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 4 | 50% | -0.03% | -0.44 to +0.28% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.65% | +0.28 to +1.02% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | put writers stronger · weak calls | 10 | 70% | +0.22% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | monthly | writers even · weak calls | 8 | 100% | +0.21% | too few (7/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | put writers stronger · few weak writers | 3 | 100% | +0.05% | too few (2/10) |
| intraday | weekly | writers even · few weak writers | 2 | 0% | -0.43% | too few (2/10) |
| intraday | monthly | writers even · few weak writers | 1 | 100% | +1.02% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · weak calls | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
