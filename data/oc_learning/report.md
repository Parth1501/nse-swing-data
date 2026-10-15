# Nifty option chain pattern log
Updated 2026-10-15 13:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 39 snapshots over 2 trading days
- 40 patterns logged; 31 different patterns so far

## Latest read (2026-10-15 13:45:39)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 4.1 | 23048 | 1.171 | 22900 | 22700 | 23500 | ±1.08% (22799-23297) | 12.72 |
| 2026-10-27 (monthly) | 12.1 | 23050 | 0.807 | 23000 | 22500 | 23500 | ±1.89% (22613-23486) | 12.98 |

- **Weekly, last 30 min**: `PCR flat · quiet OI · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 7 times before; Nifty was up after it 100% of the time, average +0.54%. Too few outcomes (7/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.16%. Too few outcomes (1/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23300, strongest put writers at 22800; weakest call writers at 23000, weakest put writers at -. Covers 41% of near-money call OI and 77% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22750 | 28652 | 11576 | 117.3 | 22721 | 337.0 | 22867 | -181 | -219.7 | weak |
| Call | 22800 | 51136 | 20082 | 87.6 | 22689 | 296.0 | 22888 | -161 | -208.4 | weak |
| Call | 22850 | 25728 | 9743 | 74.2 | 22715 | 256.1 | 22924 | -124 | -181.9 | weak |
| Call | 22900 | 87458 | 37890 | 70.2 | 22712 | 217.8 | 22970 | -78 | -147.6 | weak |
| Call | 22950 | 42263 | 19489 | 105.4 | 22887 | 182.9 | 23055 | +7 | -77.6 | weak |
| Call | 23000 | 136201 | 47863 | 56.4 | 22740 | 150.8 | 23056 | +8 | -94.4 | weak |
| Call | 23050 | 62083 | 43580 | 75.7 | 22888 | 122.2 | 23126 | +78 | -46.6 | medium |
| Call | 23100 | 104331 | 34926 | 56.8 | 22894 | 97.0 | 23157 | +109 | -40.2 | strong |
| Call | 23150 | 46133 | 18486 | 40.2 | 22863 | 75.8 | 23190 | +142 | -35.6 | strong |
| Call | 23200 | 111197 | 27013 | 24.3 | 22757 | 58.4 | 23224 | +176 | -34.1 | strong |
| Call | 23250 | 58847 | 35680 | 26.3 | 22902 | 44.8 | 23276 | +228 | -18.4 | strong |
| Call | 23300 | 89077 | 39187 | 8.9 | 22763 | 34.0 | 23309 | +261 | -25.1 | strong |
| Call | 23350 | 32650 | 16909 | 12.3 | 22851 | 25.9 | 23362 | +314 | -13.6 | strong |
| Put | 22750 | 92652 | 85386 | 105.1 | 22836 | 43.4 | 22645 | +403 | +61.7 | strong |
| Put | 22800 | 182941 | 163135 | 106.6 | 22884 | 51.1 | 22693 | +355 | +55.4 | strong |
| Put | 22850 | 94758 | 90054 | 106.7 | 22924 | 60.8 | 22743 | +305 | +45.9 | strong |
| Put | 22900 | 157686 | 150867 | 123.3 | 22929 | 73.0 | 22777 | +271 | +50.3 | strong |
| Put | 22950 | 80229 | 77848 | 135.3 | 22951 | 87.7 | 22815 | +233 | +47.6 | strong |
| Put | 23000 | 162592 | 150627 | 149.5 | 22971 | 106.0 | 22851 | +198 | +43.5 | strong |
| Put | 23050 | 38216 | 37071 | 161.1 | 22994 | 127.0 | 22889 | +159 | +34.2 | strong |
| Put | 23100 | 33568 | 30155 | 199.7 | 22979 | 152.0 | 22900 | +148 | +47.7 | strong |
| Put | 23150 | 6647 | 6313 | 232.5 | 22981 | 181.3 | 22918 | +131 | +51.1 | strong |
| Put | 23200 | 13174 | 11751 | 286.4 | 22958 | 214.0 | 22914 | +135 | +72.4 | strong |
| Put | 23250 | 2160 | 1775 | 320.0 | 22967 | 250.6 | 22930 | +118 | +69.4 | strong |
| Put | 23300 | 5444 | 3395 | 360.9 | 22968 | 290.0 | 22939 | +109 | +70.9 | strong |
| Put | 23350 | 493 | 392 | 425.9 | 22947 | 334.4 | 22924 | +124 | +91.5 | strong |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23200, strongest put writers at 22700; weakest call writers at 22700, weakest put writers at 23700. Covers 19% of near-money call OI and 23% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22750 | 7131 | 1114 | 189.3 | 22635 | 436.2 | 22939 | -110 | -246.9 | weak |
| Call | 22800 | 51925 | 8807 | 175.6 | 22659 | 398.4 | 22976 | -74 | -222.9 | weak |
| Call | 22850 | 5616 | 508 | 163.9 | 22689 | 361.8 | 23014 | -36 | -197.8 | weak |
| Call | 22900 | 29607 | 9293 | 130.2 | 22651 | 327.5 | 23030 | -19 | -197.2 | weak |
| Call | 22950 | 5478 | 2143 | 197.1 | 22866 | 294.6 | 23147 | +98 | -97.5 | medium |
| Call | 23000 | 107916 | 16412 | 103.2 | 22659 | 264.1 | 23103 | +54 | -160.9 | medium |
| Call | 23050 | 6130 | 2680 | 130.2 | 22775 | 233.8 | 23180 | +131 | -103.7 | strong |
| Call | 23100 | 29485 | 3950 | 90.7 | 22712 | 207.0 | 23191 | +141 | -116.3 | strong |
| Call | 23150 | 3610 | 990 | 100.0 | 22798 | 180.5 | 23250 | +200 | -80.5 | strong |
| Call | 23200 | 67918 | 18012 | 58.7 | 22664 | 157.6 | 23259 | +209 | -98.9 | strong |
| Call | 23250 | 6150 | 2403 | 78.6 | 22803 | 135.6 | 23329 | +279 | -57.0 | strong |
| Call | 23300 | 51256 | 4508 | 54.2 | 22762 | 117.2 | 23354 | +305 | -63.1 | strong |
| Call | 23350 | 7845 | 5257 | 60.8 | 22826 | 100.1 | 23411 | +361 | -39.3 | strong |
| Put | 22750 | 9972 | 5027 | 190.4 | 22816 | 104.8 | 22560 | +490 | +85.7 | strong |
| Put | 22800 | 39878 | 9185 | 211.3 | 22822 | 117.0 | 22589 | +461 | +94.2 | strong |
| Put | 22850 | 7692 | 5001 | 216.6 | 22864 | 130.9 | 22633 | +416 | +85.7 | strong |
| Put | 22900 | 21277 | 11202 | 209.7 | 22914 | 145.8 | 22690 | +359 | +63.8 | strong |
| Put | 22950 | 6933 | 5972 | 213.4 | 22952 | 163.0 | 22737 | +313 | +50.4 | strong |
| Put | 23000 | 75703 | 24091 | 280.4 | 22884 | 182.6 | 22720 | +330 | +97.8 | strong |
| Put | 23050 | 1999 | 1300 | 233.3 | 22996 | 202.9 | 22817 | +233 | +30.4 | strong |
| Put | 23100 | 21194 | 1005 | 288.3 | 22951 | 224.6 | 22812 | +238 | +63.7 | strong |
| Put | 23150 | 711 | 308 | 319.0 | 22945 | 252.5 | 22831 | +219 | +66.5 | strong |
| Put | 23200 | 28310 | 1505 | 356.1 | 22938 | 275.0 | 22844 | +206 | +81.1 | strong |
| Put | 23250 | 848 | 122 | 386.2 | 22941 | 305.6 | 22864 | +186 | +80.6 | strong |
| Put | 23300 | 35508 | 505 | 431.6 | 22927 | 335.1 | 22868 | +181 | +96.5 | strong |
| Put | 23350 | 576 | 147 | 439.0 | 22964 | 370.1 | 22911 | +139 | +68.9 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put writing · walls same · near call wall | 4 | 100% | +0.47% | +0.25 to +0.60% |  | too few (4/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 3 | 67% | +0.15% | -0.44 to +0.50% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.88% | +0.51 to +1.25% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.60% | +0.60 to +0.60% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.39% | +0.39 to +0.39% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.26% | +1.26 to +1.26% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.03% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.15% | too few (8/10) |
| intraday | weekly | put writers stronger · weak calls | 8 | 100% | +0.54% | too few (7/10) |
| intraday | monthly | writers even · weak calls | 6 | 100% | +0.43% | too few (6/10) |
| intraday | monthly | put writers stronger · weak calls | 2 | 100% | +0.16% | too few (1/10) |
| intraday | weekly | writers even · few weak writers | 2 | 0% | -0.43% | too few (2/10) |
| intraday | monthly | writers even · few weak writers | 1 | 100% | +1.25% | too few (1/10) |
| intraday | weekly | put writers stronger · few weak writers | 1 | 100% | +0.25% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.89% | too few (1/10) |
| day | monthly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.89% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
