# Nifty option chain pattern log
Updated 2026-10-15 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 42 snapshots over 2 trading days
- 44 patterns logged; 34 different patterns so far

## Latest read (2026-10-15 14:45:09)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 4.0 | 22981 | 1.242 | 22900 | 22700 | 23000 | ±1.03% (22744-23218) | 12.32 |
| 2026-10-27 (monthly) | 12.0 | 22981 | 0.899 | 23000 | 22500 | 23500 | ±1.83% (22560-23402) | 12.61 |

- **Weekly, last 30 min**: `PCR up · unwinding · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.04%. Too few outcomes (1/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put writing · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · unwinding · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 3 times before; Nifty was up after it 0% of the time, average -0.21%. Too few outcomes (3/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23300, strongest put writers at 22800; weakest call writers at 22900, weakest put writers at 23300. Covers 44% of near-money call OI and 75% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 17176 | 10738 | 125.8 | 22608 | 361.1 | 22776 | -205 | -235.3 | weak |
| Call | 22700 | 46704 | 14836 | 110.2 | 22620 | 317.9 | 22810 | -171 | -207.7 | weak |
| Call | 22750 | 26405 | 10669 | 117.3 | 22721 | 276.6 | 22867 | -114 | -159.4 | weak |
| Call | 22800 | 52143 | 21946 | 108.3 | 22726 | 236.9 | 22908 | -73 | -128.6 | weak |
| Call | 22850 | 23274 | 9158 | 84.0 | 22734 | 199.9 | 22934 | -47 | -115.9 | weak |
| Call | 22900 | 83065 | 36090 | 70.8 | 22713 | 165.8 | 22971 | -10 | -95.0 | weak |
| Call | 22950 | 39437 | 18186 | 105.4 | 22887 | 134.5 | 23055 | +74 | -29.1 | medium |
| Call | 23000 | 145121 | 57148 | 64.8 | 22780 | 107.0 | 23065 | +84 | -42.2 | medium |
| Call | 23050 | 64488 | 47739 | 81.6 | 22911 | 83.2 | 23132 | +151 | -1.7 | strong |
| Call | 23100 | 103855 | 39538 | 62.2 | 22918 | 63.0 | 23162 | +181 | -0.9 | strong |
| Call | 23150 | 51486 | 23839 | 43.5 | 22893 | 47.2 | 23194 | +213 | -3.7 | strong |
| Call | 23200 | 117762 | 35392 | 31.2 | 22824 | 35.1 | 23231 | +250 | -3.9 | strong |
| Call | 23250 | 44567 | 27022 | 26.3 | 22902 | 25.6 | 23276 | +295 | +0.8 | strong |
| Call | 23300 | 98983 | 49093 | 11.1 | 22808 | 18.7 | 23311 | +330 | -7.6 | strong |
| Put | 22650 | 72268 | 54936 | 88.1 | 22791 | 34.8 | 22562 | +419 | +53.3 | strong |
| Put | 22700 | 197027 | 145874 | 97.4 | 22811 | 41.6 | 22603 | +378 | +55.8 | strong |
| Put | 22750 | 87897 | 81004 | 105.1 | 22836 | 50.0 | 22645 | +336 | +55.0 | strong |
| Put | 22800 | 174800 | 155876 | 106.6 | 22884 | 60.4 | 22693 | +288 | +46.2 | strong |
| Put | 22850 | 93650 | 89001 | 106.7 | 22924 | 73.0 | 22743 | +238 | +33.6 | strong |
| Put | 22900 | 155384 | 148724 | 122.9 | 22930 | 89.0 | 22777 | +204 | +33.9 | strong |
| Put | 22950 | 80394 | 78020 | 135.2 | 22951 | 107.7 | 22815 | +166 | +27.5 | strong |
| Put | 23000 | 150038 | 139437 | 148.1 | 22973 | 130.3 | 22852 | +129 | +17.8 | strong |
| Put | 23050 | 37548 | 36613 | 157.4 | 22999 | 156.8 | 22893 | +88 | +0.7 | medium |
| Put | 23100 | 31407 | 28423 | 197.3 | 22982 | 187.2 | 22903 | +78 | +10.2 | medium |
| Put | 23150 | 6626 | 6336 | 227.9 | 22986 | 220.7 | 22922 | +59 | +7.2 | medium |
| Put | 23200 | 10437 | 9357 | 283.9 | 22961 | 258.0 | 22916 | +65 | +25.9 | medium |
| Put | 23250 | 2185 | 1822 | 315.8 | 22972 | 299.2 | 22934 | +47 | +16.6 | weak |
| Put | 23300 | 4540 | 2831 | 360.9 | 22968 | 342.4 | 22939 | +42 | +18.4 | weak |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23200, strongest put writers at 22700; weakest call writers at 22700, weakest put writers at 23600. Covers 18% of near-money call OI and 23% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 3926 | 979 | 221.8 | 22596 | 449.0 | 22872 | -109 | -227.2 | weak |
| Call | 22700 | 51609 | 10581 | 208.9 | 22627 | 412.0 | 22909 | -72 | -203.1 | weak |
| Call | 22750 | 6963 | 1088 | 189.3 | 22635 | 375.1 | 22939 | -42 | -185.8 | weak |
| Call | 22800 | 50753 | 8609 | 175.6 | 22659 | 336.2 | 22976 | -5 | -160.7 | weak |
| Call | 22850 | 4923 | 445 | 163.9 | 22689 | 302.9 | 23014 | +33 | -139.0 | weak |
| Call | 22900 | 29448 | 9409 | 133.9 | 22659 | 271.4 | 23034 | +53 | -137.5 | medium |
| Call | 22950 | 5251 | 2054 | 197.1 | 22866 | 243.2 | 23147 | +166 | -46.1 | strong |
| Call | 23000 | 104660 | 15917 | 103.2 | 22659 | 214.8 | 23103 | +122 | -111.6 | strong |
| Call | 23050 | 6101 | 2777 | 136.1 | 22793 | 187.6 | 23186 | +205 | -51.4 | strong |
| Call | 23100 | 28968 | 3880 | 90.7 | 22712 | 163.3 | 23191 | +210 | -72.7 | strong |
| Call | 23150 | 3455 | 965 | 101.7 | 22804 | 143.3 | 23252 | +271 | -41.6 | strong |
| Call | 23200 | 67497 | 17901 | 58.7 | 22664 | 122.6 | 23259 | +278 | -63.9 | strong |
| Call | 23250 | 5769 | 2254 | 78.6 | 22803 | 106.3 | 23329 | +348 | -27.7 | strong |
| Call | 23300 | 51089 | 4494 | 54.2 | 22762 | 88.8 | 23354 | +373 | -34.6 | strong |
| Put | 22650 | 6807 | 2095 | 172.9 | 22772 | 90.6 | 22477 | +504 | +82.3 | strong |
| Put | 22700 | 70454 | 26377 | 163.4 | 22853 | 101.8 | 22537 | +444 | +61.6 | strong |
| Put | 22750 | 9879 | 4996 | 189.9 | 22818 | 115.7 | 22560 | +421 | +74.2 | strong |
| Put | 22800 | 36857 | 8489 | 211.3 | 22822 | 128.3 | 22589 | +392 | +83.0 | strong |
| Put | 22850 | 7537 | 4911 | 216.1 | 22865 | 147.2 | 22634 | +347 | +68.9 | strong |
| Put | 22900 | 22396 | 12372 | 204.3 | 22925 | 164.6 | 22696 | +285 | +39.8 | strong |
| Put | 22950 | 7029 | 6068 | 212.9 | 22953 | 184.3 | 22737 | +244 | +28.5 | strong |
| Put | 23000 | 76996 | 25436 | 275.8 | 22892 | 206.6 | 22724 | +257 | +69.2 | strong |
| Put | 23050 | 1978 | 1373 | 230.2 | 23001 | 227.2 | 22820 | +161 | +3.0 | strong |
| Put | 23100 | 20954 | 994 | 288.3 | 22951 | 256.0 | 22812 | +169 | +32.3 | strong |
| Put | 23150 | 746 | 343 | 315.1 | 22949 | 283.4 | 22835 | +146 | +31.7 | strong |
| Put | 23200 | 28322 | 1608 | 351.9 | 22944 | 314.2 | 22848 | +133 | +37.7 | strong |
| Put | 23250 | 813 | 117 | 386.2 | 22941 | 342.1 | 22864 | +117 | +44.2 | strong |
| Put | 23300 | 30237 | 430 | 431.6 | 22927 | 377.4 | 22868 | +113 | +54.2 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 4 | 50% | -0.09% | -0.44 to +0.20% |  | too few (4/10) |
| weekly | PCR up · put writing · walls same · near call wall | 4 | 75% | +0.18% | -0.04 to +0.30% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.58% | +0.21 to +0.95% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.06% | -0.06 to -0.06% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.30% | -0.30 to -0.30% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.18% | -0.18 to -0.18% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.06% | +0.06 to +0.06% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.29% | -0.29 to -0.29% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.96% | +0.96 to +0.96% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.10% | +0.10 to +0.10% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | -0.00% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.12% | too few (8/10) |
| intraday | weekly | put writers stronger · weak calls | 9 | 67% | +0.14% | too few (9/10) |
| intraday | monthly | writers even · weak calls | 6 | 83% | +0.14% | too few (6/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 0% | -0.21% | too few (3/10) |
| intraday | weekly | put writers stronger · few weak writers | 2 | 0% | -0.04% | too few (1/10) |
| intraday | weekly | writers even · few weak writers | 2 | 0% | -0.43% | too few (2/10) |
| intraday | monthly | writers even · few weak writers | 1 | 100% | +0.95% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.58% | too few (1/10) |
| day | monthly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.58% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
