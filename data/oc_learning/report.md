# Nifty option chain pattern log
Updated 2026-10-15 11:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 31 snapshots over 2 trading days
- 32 patterns logged; 25 different patterns so far

## Latest read (2026-10-15 11:44:29)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 4.2 | 22968 | 1.137 | 22850 | 22700 | 23000 | ±1.16% (22701-23234) | 13.79 |
| 2026-10-27 (monthly) | 12.2 | 22964 | 0.801 | 23000 | 22000 | 23500 | ±1.96% (22513-23415) | 13.46 |

- **Weekly, last 30 min**: `PCR flat · put writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 4 times before; Nifty was up after it 100% of the time, average +0.37%. Too few outcomes (4/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put writing · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · unwinding · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 3 times before; Nifty was up after it 100% of the time, average +0.17%. Too few outcomes (3/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23300, strongest put writers at 22700; weakest call writers at 22900, weakest put writers at -. Covers 35% of near-money call OI and 70% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 20700 | 12942 | 125.8 | 22608 | 351.9 | 22776 | -192 | -226.1 | weak |
| Call | 22700 | 57294 | 18200 | 110.2 | 22620 | 310.8 | 22810 | -157 | -200.5 | weak |
| Call | 22750 | 34820 | 14068 | 117.3 | 22721 | 271.0 | 22867 | -100 | -153.7 | weak |
| Call | 22800 | 66175 | 25988 | 87.6 | 22689 | 232.9 | 22888 | -80 | -145.3 | weak |
| Call | 22850 | 32977 | 12488 | 74.2 | 22715 | 198.2 | 22924 | -43 | -124.0 | weak |
| Call | 22900 | 98481 | 41899 | 66.2 | 22702 | 165.4 | 22966 | -1 | -99.2 | weak |
| Call | 22950 | 59112 | 24089 | 98.5 | 22870 | 136.2 | 23048 | +81 | -37.7 | medium |
| Call | 23000 | 138373 | 38191 | 34.4 | 22646 | 110.0 | 23034 | +67 | -75.6 | medium |
| Call | 23050 | 42054 | 22421 | 40.5 | 22752 | 86.5 | 23090 | +123 | -46.0 | strong |
| Call | 23100 | 86753 | 17103 | 29.4 | 22775 | 67.3 | 23129 | +162 | -37.9 | strong |
| Call | 23150 | 39284 | 11637 | 29.1 | 22789 | 51.4 | 23179 | +212 | -22.2 | strong |
| Call | 23200 | 104675 | 19364 | 12.9 | 22648 | 38.8 | 23213 | +245 | -25.9 | strong |
| Call | 23250 | 44832 | 21665 | 18.2 | 22828 | 29.0 | 23268 | +301 | -10.8 | strong |
| Call | 23300 | 99964 | 43976 | 8.9 | 22763 | 21.9 | 23309 | +341 | -13.0 | strong |
| Put | 22650 | 79120 | 59929 | 88.8 | 22788 | 46.8 | 22561 | +406 | +42.0 | strong |
| Put | 22700 | 205173 | 150562 | 99.1 | 22804 | 55.8 | 22601 | +367 | +43.4 | strong |
| Put | 22750 | 113285 | 104401 | 105.1 | 22836 | 65.5 | 22645 | +323 | +39.6 | strong |
| Put | 22800 | 155570 | 135764 | 115.2 | 22859 | 78.0 | 22685 | +283 | +37.2 | strong |
| Put | 22850 | 73970 | 69266 | 115.0 | 22901 | 92.7 | 22735 | +232 | +22.2 | strong |
| Put | 22900 | 135566 | 128509 | 128.8 | 22916 | 110.3 | 22771 | +196 | +18.5 | strong |
| Put | 22950 | 53270 | 50889 | 145.4 | 22930 | 130.2 | 22805 | +163 | +15.1 | strong |
| Put | 23000 | 68004 | 56039 | 181.7 | 22915 | 154.4 | 22818 | +149 | +27.3 | strong |
| Put | 23050 | 9826 | 8681 | 209.0 | 22920 | 181.3 | 22841 | +127 | +27.6 | strong |
| Put | 23100 | 13998 | 10585 | 238.3 | 22923 | 211.9 | 22862 | +106 | +26.4 | strong |
| Put | 23150 | 2235 | 1901 | 280.6 | 22920 | 245.9 | 22869 | +98 | +34.7 | medium |
| Put | 23200 | 6976 | 5553 | 329.4 | 22905 | 283.3 | 22871 | +97 | +46.1 | medium |
| Put | 23250 | 865 | 480 | 405.8 | 22873 | 322.8 | 22844 | +123 | +83.0 | strong |
| Put | 23300 | 3461 | 1412 | 408.5 | 22916 | 365.4 | 22892 | +76 | +43.1 | medium |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23200, strongest put writers at 22700; weakest call writers at 22700, weakest put writers at -. Covers 17% of near-money call OI and 15% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 4399 | 1097 | 221.8 | 22596 | 449.1 | 22872 | -92 | -227.2 | weak |
| Call | 22700 | 56503 | 11562 | 208.3 | 22626 | 410.4 | 22908 | -56 | -202.1 | weak |
| Call | 22750 | 8209 | 1282 | 189.3 | 22635 | 371.1 | 22939 | -25 | -181.8 | weak |
| Call | 22800 | 56381 | 9563 | 175.6 | 22659 | 340.4 | 22976 | +12 | -164.8 | weak |
| Call | 22850 | 6025 | 545 | 163.9 | 22689 | 307.8 | 23014 | +50 | -143.8 | weak |
| Call | 22900 | 32950 | 10161 | 125.1 | 22640 | 273.0 | 23025 | +61 | -147.9 | medium |
| Call | 22950 | 5808 | 2119 | 191.5 | 22854 | 243.6 | 23142 | +178 | -52.1 | strong |
| Call | 23000 | 114043 | 17344 | 103.2 | 22659 | 216.7 | 23103 | +139 | -113.5 | strong |
| Call | 23050 | 5351 | 1894 | 95.7 | 22681 | 190.3 | 23146 | +182 | -94.6 | strong |
| Call | 23100 | 31909 | 3899 | 82.3 | 22684 | 166.3 | 23182 | +218 | -84.1 | strong |
| Call | 23150 | 4518 | 1115 | 93.2 | 22773 | 144.1 | 23243 | +279 | -50.9 | strong |
| Call | 23200 | 71056 | 18656 | 57.8 | 22659 | 125.7 | 23258 | +294 | -67.9 | strong |
| Call | 23250 | 5820 | 1787 | 56.8 | 22707 | 106.9 | 23307 | +343 | -50.1 | strong |
| Call | 23300 | 51675 | 3965 | 45.3 | 22722 | 91.0 | 23345 | +381 | -45.7 | strong |
| Put | 22650 | 6742 | 1916 | 182.1 | 22744 | 108.8 | 22468 | +496 | +73.2 | strong |
| Put | 22700 | 59714 | 15095 | 207.4 | 22733 | 121.7 | 22493 | +471 | +85.7 | strong |
| Put | 22750 | 9801 | 4838 | 193.5 | 22808 | 135.4 | 22557 | +407 | +58.0 | strong |
| Put | 22800 | 43375 | 9629 | 215.2 | 22812 | 150.0 | 22585 | +379 | +65.2 | strong |
| Put | 22850 | 6804 | 4113 | 231.6 | 22832 | 168.0 | 22618 | +345 | +63.6 | strong |
| Put | 22900 | 19122 | 8873 | 223.3 | 22886 | 186.1 | 22677 | +287 | +37.3 | strong |
| Put | 22950 | 6257 | 5260 | 217.9 | 22943 | 207.2 | 22732 | +232 | +10.7 | strong |
| Put | 23000 | 62164 | 10552 | 374.1 | 22730 | 227.7 | 22626 | +338 | +146.4 | strong |
| Put | 23050 | 1124 | 410 | 279.6 | 22915 | 251.2 | 22770 | +194 | +28.5 | strong |
| Put | 23100 | 21099 | 203 | 406.0 | 22776 | 276.5 | 22694 | +270 | +129.5 | strong |
| Put | 23150 | 640 | 193 | 340.5 | 22915 | 306.1 | 22810 | +154 | +34.4 | strong |
| Put | 23200 | 27676 | 752 | 401.7 | 22878 | 335.8 | 22798 | +166 | +65.9 | strong |
| Put | 23250 | 809 | 54 | 442.3 | 22868 | 368.5 | 22808 | +156 | +73.8 | strong |
| Put | 23300 | 35492 | 290 | 452.0 | 22900 | 399.6 | 22848 | +116 | +52.4 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put writing · walls same · near call wall | 3 | 100% | +0.19% | +0.15 to +0.24% |  | too few (3/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.51% | +0.14 to +0.88% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | -0.16% | -0.44 to +0.13% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | -0.01% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.11% | too few (8/10) |
| intraday | weekly | put writers stronger · weak calls | 5 | 100% | +0.37% | too few (4/10) |
| intraday | monthly | writers even · weak calls | 4 | 100% | +0.17% | too few (3/10) |
| intraday | weekly | writers even · few weak writers | 2 | 0% | -0.43% | too few (2/10) |
| intraday | monthly | writers even · few weak writers | 1 | 100% | +0.88% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.52% | too few (1/10) |
| day | monthly | writers even · weak calls | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.52% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
