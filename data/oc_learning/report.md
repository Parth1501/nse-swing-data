# Nifty option chain pattern log
Updated 2026-11-04 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 372 snapshots over 15 trading days
- 405 patterns logged; 145 different patterns so far

## Latest read (2026-11-04 14:44:52)

Nifty trend: weekly **bearish**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-09 (weekly) | 5.0 | 23914 | 0.736 | 23800 | 23000 | 24000 | ±1.38% (23585-24243) | 14.68 |
| 2026-11-23 (monthly) | 19.0 | 23910 | 0.732 | 23500 | 23000 | 24000 | ±2.47% (23320-24500) | 13.46 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls same · near call wall`. Seen 5 times before; Nifty was up after it 60% of the time, average +0.12%. Too few outcomes (5/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 47 times before; Nifty was up after it 51% of the time, average +0.00%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 23 times before; Nifty was up after it 64% of the time, average +0.13%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 2 times before; Nifty was up after it 50% of the time, average +0.33%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 1 times before; Nifty was up after it 100% of the time, average +1.05%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · call writing · walls same · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.40%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 36 times before; Nifty was up after it 88% of the time, average +0.19%. History points to a bull call debit spread, ATM to about the call wall 24000.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 36 times before; Nifty was up after it 88% of the time, average +0.19%. History points to a bull call debit spread, ATM to about the call wall 24000.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · near call wall`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.39%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 3 times before; Nifty was up after it 67% of the time, average +0.37%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 3 times before; Nifty was up after it 67% of the time, average +0.37%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-11-09

Strongest call writers at 23900, strongest put writers at 23900; weakest call writers at 23750, weakest put writers at 24550. Covers 56% of near-money call OI and 63% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 23600 | 38673 | 666 | 247.2 | 23761 | 374.9 | 23847 | -67 | -127.8 | weak |
| Call | 23650 | 13772 | 2839 | 242.8 | 23791 | 335.8 | 23893 | -21 | -93.0 | weak |
| Call | 23700 | 41602 | 6620 | 207.2 | 23784 | 299.0 | 23907 | -7 | -91.8 | weak |
| Call | 23750 | 32202 | 16399 | 183.9 | 23785 | 263.5 | 23934 | +20 | -79.6 | weak |
| Call | 23800 | 80808 | 50017 | 182.3 | 23820 | 232.3 | 23982 | +68 | -50.0 | medium |
| Call | 23850 | 61528 | 53527 | 178.3 | 23853 | 202.7 | 24028 | +114 | -24.4 | strong |
| Call | 23900 | 152584 | 109062 | 173.3 | 23888 | 176.0 | 24073 | +159 | -2.7 | strong |
| Call | 23950 | 76658 | 68461 | 163.2 | 23910 | 150.8 | 24113 | +199 | +12.4 | strong |
| Call | 24000 | 162987 | 91570 | 123.0 | 23869 | 128.9 | 24123 | +209 | -5.9 | strong |
| Call | 24050 | 58099 | 50398 | 107.5 | 23872 | 108.9 | 24157 | +243 | -1.4 | strong |
| Call | 24100 | 105087 | 65030 | 91.3 | 23877 | 91.4 | 24191 | +277 | -0.1 | strong |
| Call | 24150 | 46660 | 38568 | 83.8 | 23895 | 76.8 | 24234 | +320 | +7.1 | strong |
| Call | 24200 | 98746 | 46563 | 70.7 | 23885 | 63.9 | 24271 | +357 | +6.8 | strong |
| Call | 24250 | 36709 | 29139 | 61.4 | 23893 | 53.4 | 24311 | +397 | +8.0 | strong |
| Put | 23600 | 105734 | 45055 | 83.3 | 23893 | 54.1 | 23517 | +397 | +29.2 | strong |
| Put | 23650 | 33388 | 20447 | 91.0 | 23909 | 65.3 | 23559 | +355 | +25.7 | strong |
| Put | 23700 | 99179 | 55188 | 102.0 | 23910 | 77.8 | 23598 | +316 | +24.2 | strong |
| Put | 23750 | 48618 | 38146 | 137.0 | 23880 | 93.1 | 23613 | +301 | +43.9 | strong |
| Put | 23800 | 103628 | 79285 | 145.0 | 23900 | 110.4 | 23655 | +259 | +34.6 | strong |
| Put | 23850 | 56223 | 54866 | 157.9 | 23898 | 130.4 | 23692 | +222 | +27.5 | strong |
| Put | 23900 | 104882 | 102394 | 176.0 | 23911 | 153.2 | 23724 | +190 | +22.8 | strong |
| Put | 23950 | 19752 | 19365 | 202.9 | 23915 | 178.4 | 23747 | +167 | +24.5 | strong |
| Put | 24000 | 43046 | 34059 | 230.3 | 23912 | 205.9 | 23770 | +144 | +24.4 | strong |
| Put | 24050 | 4854 | 4558 | 260.7 | 23913 | 235.9 | 23789 | +125 | +24.7 | strong |
| Put | 24100 | 8915 | 8446 | 293.5 | 23907 | 268.7 | 23807 | +108 | +24.8 | medium |
| Put | 24150 | 1838 | 1678 | 336.8 | 23904 | 303.8 | 23813 | +101 | +33.0 | medium |
| Put | 24200 | 4833 | 3463 | 381.1 | 23894 | 340.5 | 23819 | +95 | +40.6 | medium |
| Put | 24250 | 759 | 740 | 422.6 | 23900 | 382.0 | 23827 | +87 | +40.6 | medium |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 24000, strongest put writers at 23500; weakest call writers at 23500, weakest put writers at -. Covers 79% of near-money call OI and 88% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 23600 | 12601 | 9102 | 222.9 | 23165 | 521.5 | 23823 | -87 | -298.6 | weak |
| Call | 23650 | 1356 | 1270 | 249.7 | 23365 | 474.0 | 23900 | -10 | -224.3 | weak |
| Call | 23700 | 15847 | 10717 | 160.0 | 23086 | 451.8 | 23860 | -50 | -291.8 | weak |
| Call | 23750 | 7857 | 7423 | 152.3 | 23337 | 411.4 | 23902 | -8 | -259.1 | weak |
| Call | 23800 | 34658 | 28981 | 147.4 | 23136 | 384.7 | 23947 | +37 | -237.3 | weak |
| Call | 23850 | 4973 | 4680 | 257.1 | 23653 | 353.1 | 24107 | +197 | -96.0 | strong |
| Call | 23900 | 32539 | 30369 | 252.0 | 23678 | 324.7 | 24152 | +242 | -72.7 | strong |
| Call | 23950 | 3485 | 3256 | 207.4 | 23593 | 297.9 | 24157 | +247 | -90.5 | strong |
| Call | 24000 | 84373 | 60755 | 113.2 | 23192 | 272.2 | 24113 | +203 | -159.1 | strong |
| Call | 24050 | 2346 | 2207 | 113.7 | 23392 | 247.7 | 24164 | +254 | -133.9 | strong |
| Call | 24100 | 9396 | 7839 | 78.5 | 23149 | 223.6 | 24179 | +268 | -145.1 | strong |
| Call | 24150 | 1553 | 1440 | 90.3 | 23372 | 201.9 | 24240 | +330 | -111.6 | strong |
| Call | 24200 | 27900 | 25592 | 92.5 | 23459 | 181.3 | 24293 | +382 | -88.8 | strong |
| Call | 24250 | 2165 | 2055 | 57.9 | 23194 | 163.0 | 24308 | +398 | -105.1 | strong |
| Put | 23600 | 16251 | 15578 | 326.0 | 23573 | 162.5 | 23274 | +636 | +163.5 | strong |
| Put | 23650 | 3453 | 3366 | 307.8 | 23663 | 177.8 | 23342 | +568 | +130.0 | strong |
| Put | 23700 | 14704 | 14125 | 378.8 | 23569 | 191.4 | 23321 | +589 | +187.4 | strong |
| Put | 23750 | 2229 | 2149 | 353.4 | 23662 | 206.9 | 23397 | +513 | +146.4 | strong |
| Put | 23800 | 20167 | 16290 | 368.5 | 23690 | 225.0 | 23432 | +479 | +143.5 | strong |
| Put | 23850 | 5155 | 5108 | 321.2 | 23810 | 244.8 | 23529 | +381 | +76.4 | strong |
| Put | 23900 | 30455 | 30205 | 338.1 | 23836 | 265.4 | 23562 | +348 | +72.7 | strong |
| Put | 23950 | 1328 | 1306 | 347.9 | 23842 | 287.1 | 23602 | +308 | +60.7 | strong |
| Put | 24000 | 48487 | 40693 | 972.3 | 23029 | 310.1 | 23028 | +882 | +662.2 | strong |
| Put | 24050 | 427 | 414 | 413.9 | 23816 | 340.0 | 23636 | +274 | +73.8 | strong |
| Put | 24100 | 2076 | 1970 | 678.0 | 23502 | 362.1 | 23422 | +488 | +315.9 | strong |
| Put | 24150 | 275 | 251 | 471.4 | 23817 | 394.6 | 23679 | +231 | +76.8 | strong |
| Put | 24200 | 3476 | 3270 | 962.9 | 23224 | 418.1 | 23237 | +673 | +544.7 | strong |
| Put | 24250 | 198 | 187 | 703.8 | 23622 | 462.2 | 23546 | +364 | +241.6 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 34 | 73% | +0.26% | -0.44 to +0.97% | 100% of 1 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 12 | 100% | +0.54% | +0.09 to +1.02% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 12 | 100% | +0.30% | +0.03 to +0.62% | 33% of 3 | up |
| weekly | PCR up · put writing · walls same · near put wall | 11 | 64% | +0.05% | -0.47 to +0.42% | 33% of 3 | no clear direction |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| weekly | PCR down · call writing · walls same · near put wall | 8 | 88% | +0.36% | -0.37 to +0.85% | 33% of 3 | too few (8/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 8 | 100% | +0.36% | +0.05 to +0.59% |  | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 7 | 80% | +0.21% | -0.12 to +0.71% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 6 | 80% | +0.04% | -0.18 to +0.19% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put writing · walls same · mid walls | 6 | 100% | +0.65% | +0.24 to +0.85% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 6 | 50% | +0.05% | -0.74 to +0.62% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR down · call writing · walls same · near call wall | 6 | 80% | +0.05% | -0.78 to +0.37% | 100% of 1 | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 6 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 6 | 17% | -0.26% | -0.71 to +0.45% | 100% of 1 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 6 | 60% | +0.12% | -0.07 to +0.32% | 33% of 3 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 6 | 50% | +0.17% | -0.78 to +0.90% | 100% of 1 | too few (6/10) |
| weekly | PCR up · put writing · walls up · near put wall | 5 | 60% | +0.15% | -0.13 to +0.35% | 0% of 2 | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 5 | 60% | +0.05% | -0.47 to +0.49% | 100% of 1 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 5 | 75% | +0.21% | -0.05 to +0.63% | 50% of 2 | too few (4/10) |
| weekly | PCR down · call writing · walls same · mid walls | 5 | 100% | +0.46% | +0.04 to +0.75% | 33% of 3 | too few (5/10) |
| weekly | PCR down · call writing · walls down · mid walls | 5 | 80% | +0.31% | -0.07 to +0.54% | 50% of 2 | too few (5/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls same · near call wall | 4 | 75% | +0.49% | -0.02 to +0.91% | 50% of 2 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | +0.10% | -0.68 to +0.75% | 50% of 2 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR up · put writing · walls up · mid walls | 4 | 75% | +0.33% | -0.16 to +0.65% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 3 | 100% | +0.33% | +0.13 to +0.59% | 0% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near call wall | 3 | 100% | +0.38% | +0.30 to +0.45% | 100% of 1 | too few (3/10) |
| monthly | PCR up · put writing · walls same · near call wall | 3 | 33% | -0.01% | -0.40 to +0.43% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 3 | 33% | +0.13% | -0.02 to +0.43% | 0% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 3 | 67% | +0.17% | -0.22 to +0.48% | 100% of 2 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 3 | 67% | +0.16% | -0.11 to +0.50% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | -0.02% | -1.11 to +0.78% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 33% | -0.17% | -0.75 to +0.38% | 0% of 1 | too few (3/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 3 | 100% | +0.36% | +0.16 to +0.50% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 0% | -0.44% | -0.69 to -0.20% | 0% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 2 | 100% | +0.39% | +0.15 to +0.64% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 50% | +0.29% | -0.05 to +0.63% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 2 | 100% | +0.26% | +0.17 to +0.35% | 0% of 2 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.64% | +0.42 to +0.85% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 2 | 50% | +0.06% | -0.57 to +0.69% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 2 | 100% | +0.50% | +0.47 to +0.53% | 50% of 2 | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.67% | +0.67 to +0.67% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.47% | +0.47 to +0.47% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 | 100% | +0.53% | +0.53 to +0.53% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 100% | +0.58% | +0.58 to +0.58% | 0% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.32% | +0.32 to +0.32% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 2 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.42% | +0.42 to +0.42% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.42% | +0.42 to +0.42% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 94 | 70% | +0.17% | up |
| intraday | weekly | writers even · few weak writers | 48 | 51% | +0.00% | no clear direction |
| intraday | weekly | put writers stronger · weak calls | 46 | 81% | +0.33% | up |
| intraday | monthly | writers even · weak calls | 37 | 88% | +0.19% | up |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | monthly | put writers stronger · weak calls | 28 | 85% | +0.48% | up |
| intraday | weekly | put writers stronger · few weak writers | 25 | 91% | +0.15% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | call writers stronger · few weak writers | 19 | 72% | +0.25% | no clear direction |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 67% | +0.34% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | weekly | writers even · weak on both sides | 6 | 100% | +0.36% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| day | monthly | writers even · few weak writers | 8 | 50% | +0.34% | too few (8/10) |
| day | monthly | writers even · weak calls | 4 | 67% | +0.37% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls | 3 | 67% | +0.29% | too few (3/10) |
| day | weekly | writers even · few weak writers | 3 | 50% | +0.33% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |
| day | monthly | put writers stronger · weak calls | 1 | 100% | +0.42% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.02% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 46 | 81% | +0.33% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 37 | 88% | +0.19% | up |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 28 | 85% | +0.48% | up |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 25 | 91% | +0.15% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 24 | 64% | +0.13% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.37% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 67% | +0.09% | too few (3/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 3 | 100% | +0.73% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m up | 1 | 100% | +0.91% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 67% | +0.37% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.29% | too few (3/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.05% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 100% | +0.42% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.22% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
