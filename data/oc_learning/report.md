# Nifty option chain pattern log
Updated 2026-10-16 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 67 snapshots over 3 trading days
- 72 patterns logged; 50 different patterns so far

## Latest read (2026-10-16 14:45:39)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 3.0 | 23097 | 1.101 | 23050 | 23000 | 23100 | ±0.77% (22920-23275) | 10.81 |
| 2026-10-27 (monthly) | 11.0 | 23096 | 0.909 | 23150 | 22500 | 23500 | ±1.65% (22715-23477) | 11.88 |

- **Weekly, last 30 min**: `PCR up · unwinding · walls down · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.07%. Too few outcomes (1/20) to trade on.
  - Writers: `put writers stronger · few weak writers`. Seen 7 times before; Nifty was up after it 33% of the time, average -0.04%. Too few outcomes (6/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.43%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR up · unwinding · walls same · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.07%. Too few outcomes (1/20) to trade on.
  - Writers: `put writers stronger · few weak writers`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.02%. Too few outcomes (1/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23150, strongest put writers at 23000; weakest call writers at 23000, weakest put writers at 23500. Covers 76% of near-money call OI and 90% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22800 | 26901 | 14224 | 146.6 | 22816 | 313.6 | 22947 | -151 | -167.0 | weak |
| Call | 22850 | 13164 | 9030 | 153.0 | 22910 | 268.1 | 23003 | -94 | -115.1 | weak |
| Call | 22900 | 54817 | 38698 | 121.0 | 22893 | 225.0 | 23021 | -76 | -104.0 | weak |
| Call | 22950 | 39877 | 35632 | 116.7 | 22968 | 183.8 | 23067 | -31 | -67.1 | weak |
| Call | 23000 | 139131 | 106928 | 86.6 | 22936 | 146.7 | 23087 | -11 | -60.1 | weak |
| Call | 23050 | 104263 | 97842 | 87.7 | 23000 | 113.5 | 23138 | +40 | -25.9 | weak |
| Call | 23100 | 299766 | 254494 | 75.0 | 23030 | 85.2 | 23175 | +78 | -10.2 | medium |
| Call | 23150 | 218129 | 198980 | 66.2 | 23061 | 62.5 | 23216 | +119 | +3.7 | strong |
| Call | 23200 | 245890 | 176851 | 42.7 | 23007 | 45.0 | 23243 | +145 | -2.3 | strong |
| Call | 23250 | 110695 | 94779 | 32.2 | 23012 | 32.0 | 23282 | +185 | +0.1 | strong |
| Call | 23300 | 162313 | 116429 | 17.8 | 22942 | 22.9 | 23318 | +220 | -5.1 | strong |
| Call | 23350 | 93958 | 80200 | 17.6 | 23019 | 16.4 | 23368 | +270 | +1.2 | strong |
| Call | 23400 | 143190 | 106111 | 12.6 | 23000 | 11.8 | 23413 | +315 | +0.8 | strong |
| Put | 22800 | 231155 | 217283 | 80.8 | 22943 | 20.8 | 22719 | +378 | +60.0 | strong |
| Put | 22850 | 114630 | 111845 | 86.7 | 22962 | 25.6 | 22763 | +334 | +61.1 | strong |
| Put | 22900 | 251085 | 247024 | 97.1 | 22981 | 32.3 | 22803 | +294 | +64.8 | strong |
| Put | 22950 | 151462 | 150155 | 114.5 | 22985 | 41.5 | 22836 | +262 | +73.0 | strong |
| Put | 23000 | 291671 | 285913 | 109.4 | 23044 | 54.0 | 22891 | +207 | +55.4 | strong |
| Put | 23050 | 145823 | 145410 | 114.0 | 23073 | 70.6 | 22936 | +161 | +43.4 | strong |
| Put | 23100 | 244984 | 243418 | 125.0 | 23097 | 92.5 | 22975 | +122 | +32.5 | strong |
| Put | 23150 | 109897 | 109804 | 140.8 | 23110 | 119.2 | 23009 | +88 | +21.6 | medium |
| Put | 23200 | 54136 | 53700 | 186.3 | 23095 | 152.0 | 23014 | +84 | +34.3 | medium |
| Put | 23250 | 12794 | 12582 | 216.8 | 23098 | 188.4 | 23033 | +64 | +28.4 | medium |
| Put | 23300 | 12285 | 11441 | 264.8 | 23089 | 229.6 | 23035 | +62 | +35.1 | medium |
| Put | 23350 | 2523 | 2447 | 312.7 | 23081 | 274.1 | 23037 | +60 | +38.6 | medium |
| Put | 23400 | 4260 | 2883 | 360.4 | 23074 | 318.7 | 23040 | +58 | +41.7 | medium |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 22900, weakest put writers at 23700. Covers 34% of near-money call OI and 40% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22750 | 5519 | 895 | 199.9 | 22655 | 431.1 | 22950 | -146 | -231.2 | weak |
| Call | 22800 | 34371 | 11230 | 270.8 | 22866 | 392.8 | 23071 | -25 | -122.0 | weak |
| Call | 22850 | 5093 | 1338 | 280.7 | 22944 | 356.5 | 23131 | +35 | -75.8 | weak |
| Call | 22900 | 28234 | 12337 | 185.8 | 22793 | 318.5 | 23086 | -10 | -132.7 | weak |
| Call | 22950 | 6191 | 3296 | 207.6 | 22909 | 286.1 | 23158 | +62 | -78.5 | medium |
| Call | 23000 | 93382 | 25483 | 162.4 | 22847 | 254.0 | 23162 | +66 | -91.6 | medium |
| Call | 23050 | 5857 | 3203 | 155.9 | 22869 | 223.6 | 23206 | +110 | -67.7 | strong |
| Call | 23100 | 39617 | 16931 | 167.2 | 22995 | 195.8 | 23267 | +171 | -28.5 | strong |
| Call | 23150 | 9284 | 6967 | 167.2 | 23064 | 171.1 | 23317 | +221 | -3.9 | strong |
| Call | 23200 | 74174 | 25735 | 84.9 | 22793 | 147.0 | 23285 | +189 | -62.1 | strong |
| Call | 23250 | 8260 | 4753 | 101.4 | 22945 | 126.2 | 23351 | +255 | -24.7 | strong |
| Call | 23300 | 59911 | 14215 | 91.7 | 22989 | 107.2 | 23392 | +296 | -15.5 | strong |
| Call | 23350 | 6499 | 4623 | 66.7 | 22874 | 90.0 | 23417 | +321 | -23.3 | strong |
| Call | 23400 | 42290 | 12748 | 52.5 | 22867 | 75.3 | 23452 | +356 | -22.9 | strong |
| Put | 22750 | 13191 | 10178 | 115.2 | 23017 | 73.8 | 22635 | +461 | +41.4 | strong |
| Put | 22800 | 43967 | 16902 | 153.5 | 22957 | 83.5 | 22646 | +450 | +70.0 | strong |
| Put | 22850 | 8926 | 6420 | 191.3 | 22916 | 96.3 | 22659 | +437 | +95.0 | strong |
| Put | 22900 | 37941 | 28491 | 153.7 | 23027 | 109.9 | 22746 | +350 | +43.8 | strong |
| Put | 22950 | 10754 | 9850 | 189.7 | 22997 | 125.2 | 22760 | +336 | +64.5 | strong |
| Put | 23000 | 97809 | 49926 | 222.2 | 22985 | 144.0 | 22778 | +318 | +78.2 | strong |
| Put | 23050 | 4819 | 4311 | 197.4 | 23065 | 163.0 | 22853 | +243 | +34.4 | strong |
| Put | 23100 | 29854 | 15583 | 202.8 | 23100 | 185.0 | 22897 | +199 | +17.8 | strong |
| Put | 23150 | 5409 | 5084 | 224.9 | 23105 | 208.9 | 22925 | +171 | +16.0 | strong |
| Put | 23200 | 36416 | 10146 | 260.8 | 23087 | 235.0 | 22939 | +157 | +25.8 | strong |
| Put | 23250 | 1360 | 839 | 285.8 | 23093 | 263.9 | 22964 | +132 | +21.9 | strong |
| Put | 23300 | 30603 | 2114 | 322.7 | 23081 | 295.1 | 22977 | +119 | +27.7 | strong |
| Put | 23350 | 599 | 312 | 384.9 | 23046 | 326.8 | 22965 | +131 | +58.1 | strong |
| Put | 23400 | 16296 | 1163 | 467.6 | 22977 | 363.0 | 22932 | +164 | +104.6 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 25% | -0.06% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 67% | +0.13% | -0.14 to +0.37% |  | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 3 | 67% | +0.39% | -0.13 to +1.02% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 2 | 0% | -0.08% | -0.11 to -0.05% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 0% | -0.10% | -0.10 to -0.10% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +0.56% | +0.56 to +0.56% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 0% | -0.10% | -0.10 to -0.10% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 0% | -0.06% | -0.06 to -0.06% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 0% | -0.06% | -0.06 to -0.06% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.43% | +0.43 to +0.43% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.43% | +0.43 to +0.43% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 16 | 53% | +0.08% | no clear direction |
| intraday | weekly | put writers stronger · weak calls | 16 | 56% | +0.12% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | weekly | put writers stronger · few weak writers | 8 | 33% | -0.04% | too few (6/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | writers even · few weak writers | 3 | 67% | +0.51% | too few (3/10) |
| intraday | weekly | writers even · few weak writers | 3 | 33% | -0.10% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.02% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 2 | 100% | +0.43% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | put writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | monthly | writers even · weak calls | 1 | 100% | +0.43% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
