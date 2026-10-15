# Nifty option chain pattern log
Updated 2026-10-15 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 27 snapshots over 2 trading days
- 28 patterns logged; 23 different patterns so far

## Latest read (2026-10-15 10:45:43)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 4.2 | 22928 | 1.092 | 22800 | 22700 | 23000 | ±1.14% (22667-23189) | 13.68 |
| 2026-10-27 (monthly) | 12.2 | 22932 | 0.79 | 23000 | 22000 | 23500 | ±1.93% (22489-23375) | 13.37 |

- **Weekly, last 30 min**: `PCR up · put writing · walls same · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.07%. Too few outcomes (1/20) to trade on.
  - Writers: `put writers stronger · weak calls`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.40%. Too few outcomes (2/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put writing · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.74%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.09%. Too few outcomes (1/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at 22900, weakest put writers at -. Covers 32% of near-money call OI and 67% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22600 | 44248 | 29329 | 141.5 | 22595 | 363.3 | 22741 | -186 | -221.8 | weak |
| Call | 22650 | 24148 | 15097 | 125.8 | 22608 | 321.8 | 22776 | -152 | -195.9 | weak |
| Call | 22700 | 66033 | 20977 | 110.2 | 22620 | 282.2 | 22810 | -118 | -172.0 | weak |
| Call | 22750 | 38141 | 15410 | 117.3 | 22721 | 243.3 | 22867 | -60 | -126.1 | weak |
| Call | 22800 | 81663 | 32071 | 87.6 | 22689 | 207.2 | 22888 | -40 | -119.5 | weak |
| Call | 22850 | 44548 | 16869 | 74.2 | 22715 | 174.6 | 22924 | -4 | -100.4 | weak |
| Call | 22900 | 109481 | 46579 | 66.2 | 22702 | 144.4 | 22966 | +38 | -78.2 | weak |
| Call | 22950 | 55489 | 16210 | 85.4 | 22828 | 116.7 | 23035 | +108 | -31.3 | strong |
| Call | 23000 | 143840 | 39700 | 34.4 | 22646 | 93.2 | 23034 | +107 | -58.9 | strong |
| Call | 23050 | 37906 | 18273 | 31.7 | 22707 | 73.1 | 23082 | +154 | -41.4 | strong |
| Call | 23100 | 84082 | 12671 | 18.9 | 22715 | 56.4 | 23119 | +191 | -37.4 | strong |
| Call | 23150 | 35495 | 7848 | 21.0 | 22714 | 42.9 | 23171 | +243 | -21.9 | strong |
| Call | 23200 | 103303 | 17992 | 11.3 | 22626 | 32.2 | 23211 | +284 | -20.9 | strong |
| Call | 23250 | 43647 | 20480 | 17.7 | 22821 | 24.1 | 23268 | +340 | -6.5 | strong |
| Put | 22600 | 141854 | 75367 | 77.2 | 22783 | 41.9 | 22523 | +405 | +35.3 | strong |
| Put | 22650 | 83768 | 63449 | 88.8 | 22788 | 49.9 | 22561 | +366 | +38.9 | strong |
| Put | 22700 | 201110 | 146043 | 100.8 | 22798 | 59.4 | 22599 | +329 | +41.4 | strong |
| Put | 22750 | 106250 | 97366 | 107.7 | 22829 | 70.8 | 22642 | +285 | +36.9 | strong |
| Put | 22800 | 157087 | 136800 | 115.7 | 22858 | 85.2 | 22684 | +243 | +30.6 | strong |
| Put | 22850 | 67048 | 62344 | 117.2 | 22895 | 101.8 | 22733 | +195 | +15.5 | strong |
| Put | 22900 | 111931 | 104874 | 131.3 | 22910 | 121.5 | 22769 | +159 | +9.9 | strong |
| Put | 22950 | 25626 | 23245 | 153.6 | 22913 | 144.4 | 22796 | +131 | +9.2 | strong |
| Put | 23000 | 47151 | 35186 | 192.2 | 22896 | 171.0 | 22808 | +120 | +21.2 | strong |
| Put | 23050 | 6006 | 4861 | 222.3 | 22899 | 200.0 | 22828 | +100 | +22.3 | medium |
| Put | 23100 | 9996 | 6583 | 246.3 | 22910 | 233.1 | 22854 | +74 | +13.2 | medium |
| Put | 23150 | 1257 | 923 | 306.4 | 22887 | 270.6 | 22844 | +84 | +35.7 | medium |
| Put | 23200 | 5872 | 4388 | 336.4 | 22897 | 309.5 | 22864 | +64 | +26.9 | medium |
| Put | 23250 | 651 | 266 | 462.0 | 22809 | 349.9 | 22788 | +140 | +112.0 | strong |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23200, strongest put writers at 22700; weakest call writers at 22700, weakest put writers at 23550. Covers 16% of near-money call OI and 13% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22600 | 35942 | 9497 | 245.7 | 22602 | 453.9 | 22846 | -86 | -208.2 | weak |
| Call | 22650 | 4755 | 1186 | 221.8 | 22596 | 417.6 | 22872 | -60 | -195.8 | weak |
| Call | 22700 | 59635 | 12203 | 208.3 | 22626 | 378.2 | 22908 | -24 | -170.0 | weak |
| Call | 22750 | 8526 | 1332 | 189.3 | 22635 | 345.0 | 22939 | +7 | -155.7 | weak |
| Call | 22800 | 59892 | 10159 | 175.6 | 22659 | 310.6 | 22976 | +43 | -135.0 | weak |
| Call | 22850 | 6273 | 567 | 163.9 | 22689 | 279.6 | 23014 | +82 | -115.7 | medium |
| Call | 22900 | 35890 | 11067 | 125.1 | 22640 | 250.0 | 23025 | +93 | -124.9 | medium |
| Call | 22950 | 5298 | 1609 | 181.0 | 22828 | 221.9 | 23131 | +199 | -40.9 | strong |
| Call | 23000 | 117215 | 17826 | 103.2 | 22659 | 196.8 | 23103 | +171 | -93.6 | strong |
| Call | 23050 | 5894 | 2086 | 95.7 | 22681 | 171.6 | 23146 | +214 | -75.9 | strong |
| Call | 23100 | 31805 | 3485 | 73.4 | 22651 | 149.8 | 23173 | +241 | -76.5 | strong |
| Call | 23150 | 4596 | 1083 | 90.9 | 22763 | 129.6 | 23241 | +309 | -38.7 | strong |
| Call | 23200 | 70774 | 17981 | 55.3 | 22647 | 112.4 | 23255 | +323 | -57.1 | strong |
| Call | 23250 | 6497 | 1995 | 56.8 | 22707 | 95.5 | 23307 | +375 | -38.7 | strong |
| Put | 22600 | 43216 | 8951 | 207.2 | 22628 | 102.6 | 22393 | +539 | +104.6 | strong |
| Put | 22650 | 6825 | 1940 | 182.1 | 22744 | 114.5 | 22468 | +464 | +67.6 | strong |
| Put | 22700 | 61102 | 15446 | 207.4 | 22733 | 128.8 | 22493 | +440 | +78.6 | strong |
| Put | 22750 | 9571 | 4608 | 196.2 | 22801 | 143.6 | 22554 | +378 | +52.6 | strong |
| Put | 22800 | 43228 | 9342 | 217.1 | 22808 | 159.9 | 22583 | +349 | +57.2 | strong |
| Put | 22850 | 5974 | 3283 | 246.5 | 22802 | 178.9 | 22603 | +329 | +67.6 | strong |
| Put | 22900 | 17371 | 7122 | 230.5 | 22872 | 198.8 | 22670 | +263 | +31.6 | strong |
| Put | 22950 | 2076 | 1079 | 255.1 | 22873 | 220.9 | 22695 | +237 | +34.1 | strong |
| Put | 23000 | 61337 | 9648 | 388.1 | 22708 | 244.0 | 22612 | +320 | +144.1 | strong |
| Put | 23050 | 999 | 285 | 286.2 | 22903 | 269.5 | 22764 | +168 | +16.7 | strong |
| Put | 23100 | 21037 | 141 | 460.6 | 22697 | 297.2 | 22639 | +293 | +163.3 | strong |
| Put | 23150 | 552 | 105 | 367.2 | 22878 | 326.0 | 22783 | +149 | +41.2 | strong |
| Put | 23200 | 27437 | 494 | 424.6 | 22848 | 359.4 | 22775 | +157 | +65.2 | strong |
| Put | 23250 | 790 | 35 | 480.4 | 22820 | 396.8 | 22770 | +162 | +83.6 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.74% | +0.74 to +0.74% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.44% | -0.44 to -0.44% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.73% | +0.73 to +0.73% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | -0.02% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.09% | too few (8/10) |
| intraday | weekly | put writers stronger · weak calls | 3 | 100% | +0.40% | too few (2/10) |
| intraday | monthly | writers even · weak calls | 2 | 100% | +0.09% | too few (1/10) |
| intraday | weekly | writers even · few weak writers | 2 | 0% | -0.43% | too few (2/10) |
| intraday | monthly | writers even · few weak writers | 1 | 100% | +0.74% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.37% | too few (1/10) |
| day | monthly | writers even · weak calls | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.37% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
