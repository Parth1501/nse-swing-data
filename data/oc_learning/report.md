# Nifty option chain pattern log
Updated 2026-10-30 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 281 snapshots over 12 trading days
- 306 patterns logged; 122 different patterns so far

## Latest read (2026-10-30 10:44:49)

Nifty trend: weekly **bearish**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-03 (weekly) | 4.2 | 22955 | 0.895 | 22900 | 22900 | 23000 | ±1.17% (22687-23224) | 14.11 |
| 2026-11-23 (monthly) | 24.2 | 22954 | 1.057 | 23050 | 22000 | 23500 | ±3.02% (22261-23648) | 14.7 |

- **Weekly, last 30 min**: `PCR down · call writing · walls same · mid walls`. Seen 3 times before; Nifty was up after it 100% of the time, average +0.38%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 37 times before; Nifty was up after it 40% of the time, average -0.09%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 13 times before; Nifty was up after it 42% of the time, average -0.01%. Too few outcomes (12/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Nifty was up after it 50% of the time, average +0.33%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 1 times before; Nifty was up after it 100% of the time, average +1.05%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls same · mid walls`. Seen 29 times before; Nifty was up after it 68% of the time, average +0.17%. No direction and the walls have not held reliably: no structure.
  - Writers: `writers even · few weak writers`. Seen 85 times before; Nifty was up after it 67% of the time, average +0.16%. History points to a bull call debit spread, ATM to about the call wall 23500.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 29 times before; Nifty was up after it 73% of the time, average +0.22%. History points to a bull call debit spread, ATM to about the call wall 23500.
- **Monthly, today vs previous day**: `PCR flat · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 7 times before; Nifty was up after it 43% of the time, average +0.09%. Too few outcomes (7/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 3 times before; Nifty was up after it 67% of the time, average +0.30%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-11-03

Strongest call writers at 23000, strongest put writers at 22900; weakest call writers at 22800, weakest put writers at 23500. Covers 81% of near-money call OI and 90% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 8194 | 7713 | 192.5 | 22669 | 326.4 | 22843 | -113 | -133.9 | weak |
| Call | 22700 | 37010 | 29937 | 166.5 | 22677 | 287.9 | 22866 | -89 | -121.5 | weak |
| Call | 22750 | 13967 | 12323 | 164.3 | 22739 | 250.0 | 22914 | -41 | -85.7 | weak |
| Call | 22800 | 63154 | 44890 | 142.1 | 22744 | 215.4 | 22942 | -13 | -73.3 | weak |
| Call | 22850 | 30597 | 28696 | 152.2 | 22837 | 182.2 | 23002 | +47 | -30.0 | weak |
| Call | 22900 | 146985 | 135999 | 143.0 | 22887 | 153.2 | 23043 | +88 | -10.2 | medium |
| Call | 22950 | 146285 | 143908 | 126.8 | 22916 | 125.8 | 23077 | +121 | +0.9 | strong |
| Call | 23000 | 299175 | 257854 | 96.9 | 22875 | 102.5 | 23097 | +142 | -5.6 | strong |
| Call | 23050 | 108908 | 100017 | 82.1 | 22906 | 81.3 | 23132 | +177 | +0.8 | strong |
| Call | 23100 | 157425 | 130059 | 63.9 | 22895 | 63.6 | 23164 | +209 | +0.3 | strong |
| Call | 23150 | 86064 | 77157 | 48.4 | 22884 | 48.7 | 23198 | +243 | -0.3 | strong |
| Call | 23200 | 151483 | 114141 | 35.6 | 22854 | 36.5 | 23236 | +280 | -1.0 | strong |
| Call | 23250 | 73931 | 64561 | 27.6 | 22838 | 27.1 | 23278 | +322 | +0.4 | strong |
| Put | 22650 | 75373 | 72005 | 110.1 | 22808 | 44.5 | 22540 | +415 | +65.6 | strong |
| Put | 22700 | 180550 | 156543 | 109.3 | 22833 | 55.0 | 22591 | +365 | +54.3 | strong |
| Put | 22750 | 100323 | 96194 | 112.3 | 22860 | 67.2 | 22638 | +318 | +45.1 | strong |
| Put | 22800 | 197584 | 176924 | 115.1 | 22890 | 82.0 | 22685 | +270 | +33.1 | strong |
| Put | 22850 | 96976 | 95846 | 123.4 | 22909 | 99.5 | 22727 | +229 | +23.9 | strong |
| Put | 22900 | 202223 | 198260 | 131.9 | 22936 | 119.4 | 22768 | +187 | +12.5 | strong |
| Put | 22950 | 131752 | 131103 | 145.4 | 22955 | 142.8 | 22805 | +151 | +2.6 | strong |
| Put | 23000 | 120070 | 111791 | 191.7 | 22926 | 168.5 | 22808 | +147 | +23.2 | strong |
| Put | 23050 | 20115 | 19623 | 207.5 | 22945 | 198.6 | 22843 | +113 | +8.9 | strong |
| Put | 23100 | 31722 | 27779 | 244.9 | 22936 | 230.9 | 22855 | +100 | +14.0 | medium |
| Put | 23150 | 5954 | 5454 | 278.7 | 22937 | 265.9 | 22871 | +84 | +12.7 | medium |
| Put | 23200 | 12213 | 8990 | 342.9 | 22903 | 304.0 | 22857 | +98 | +38.9 | medium |
| Put | 23250 | 2488 | 1598 | 353.0 | 22930 | 345.2 | 22897 | +58 | +7.8 | medium |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 22400, weakest put writers at -. Covers 71% of near-money call OI and 73% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 3736 | 3572 | 456.9 | 22612 | 556.5 | 23107 | +153 | -99.6 | strong |
| Call | 22700 | 31358 | 29636 | 449.6 | 22691 | 535.0 | 23150 | +195 | -85.5 | strong |
| Call | 22750 | 4019 | 3610 | 396.4 | 22695 | 495.0 | 23146 | +192 | -98.6 | strong |
| Call | 22800 | 24234 | 21441 | 396.6 | 22699 | 470.0 | 23197 | +242 | -73.3 | strong |
| Call | 22850 | 1574 | 1293 | 368.1 | 22717 | 436.9 | 23218 | +264 | -68.8 | strong |
| Call | 22900 | 14306 | 12321 | 357.2 | 22723 | 406.1 | 23257 | +303 | -48.8 | strong |
| Call | 22950 | 3522 | 2868 | 342.0 | 22814 | 376.6 | 23292 | +338 | -34.6 | strong |
| Call | 23000 | 95495 | 60014 | 293.4 | 22669 | 348.2 | 23293 | +339 | -54.8 | strong |
| Call | 23050 | 2239 | 1329 | 296.2 | 22813 | 322.1 | 23346 | +392 | -25.8 | strong |
| Call | 23100 | 16969 | 9018 | 278.7 | 22747 | 296.3 | 23379 | +424 | -17.6 | strong |
| Call | 23150 | 1717 | 1067 | 247.6 | 22797 | 272.1 | 23398 | +443 | -24.4 | strong |
| Call | 23200 | 20454 | 10205 | 228.2 | 22709 | 249.6 | 23428 | +474 | -21.4 | strong |
| Call | 23250 | 2073 | 1131 | 207.6 | 22768 | 227.0 | 23458 | +503 | -19.4 | strong |
| Put | 22650 | 5300 | 4885 | 349.0 | 22654 | 209.3 | 22301 | +653 | +139.6 | strong |
| Put | 22700 | 44674 | 40345 | 352.0 | 22710 | 224.9 | 22348 | +606 | +127.0 | strong |
| Put | 22750 | 3884 | 3668 | 329.5 | 22773 | 240.4 | 22420 | +534 | +89.0 | strong |
| Put | 22800 | 33318 | 26747 | 381.8 | 22724 | 258.4 | 22418 | +536 | +123.4 | strong |
| Put | 22850 | 2962 | 1733 | 351.6 | 22807 | 277.9 | 22498 | +456 | +73.7 | strong |
| Put | 22900 | 18988 | 16074 | 410.8 | 22750 | 297.2 | 22489 | +465 | +113.6 | strong |
| Put | 22950 | 2019 | 1763 | 353.1 | 22864 | 316.9 | 22597 | +358 | +36.3 | strong |
| Put | 23000 | 96576 | 62766 | 460.1 | 22765 | 339.0 | 22540 | +414 | +121.1 | strong |
| Put | 23050 | 1078 | 788 | 418.5 | 22846 | 359.9 | 22631 | +323 | +58.7 | strong |
| Put | 23100 | 10228 | 5503 | 464.9 | 22842 | 386.2 | 22635 | +319 | +78.6 | strong |
| Put | 23150 | 1278 | 440 | 439.4 | 22911 | 414.8 | 22711 | +244 | +24.6 | strong |
| Put | 23200 | 16002 | 9511 | 556.8 | 22785 | 436.8 | 22643 | +311 | +120.0 | strong |
| Put | 23250 | 692 | 430 | 574.9 | 22780 | 474.0 | 22675 | +279 | +100.8 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 30 | 68% | +0.17% | -0.44 to +0.76% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · near call wall | 10 | 100% | +0.31% | +0.03 to +0.62% | 50% of 2 | up |
| weekly | PCR up · put writing · walls same · near put wall | 9 | 56% | +0.01% | -0.47 to +0.41% | 50% of 2 | too few (9/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 7 | 60% | +0.12% | -0.12 to +0.71% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| weekly | PCR down · call writing · walls same · near put wall | 6 | 83% | +0.37% | -0.37 to +0.85% | 50% of 2 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 6 | 100% | +0.47% | +0.09 to +1.02% | 100% of 1 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 5 | 60% | +0.12% | -0.07 to +0.32% | 50% of 2 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 5 | 40% | +0.04% | -0.78 to +0.90% | 100% of 1 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls same · mid walls | 4 | 100% | +0.38% | +0.04 to +0.73% | 50% of 2 | too few (3/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls down · mid walls | 4 | 75% | +0.28% | -0.07 to +0.54% | 100% of 1 | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% | 100% of 1 | too few (4/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 4 | 67% | +0.06% | -0.05 to +0.15% | 50% of 2 | too few (3/10) |
| monthly | PCR down · put writing · walls same · mid walls | 3 | 67% | +0.06% | -0.05 to +0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · near call wall | 3 | 67% | +0.35% | -0.02 to +0.55% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 3 | 33% | -0.12% | -0.68 to +0.34% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 3 | 67% | +0.16% | -0.02 to +0.37% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls up · near put wall | 3 | 67% | +0.23% | -0.01 to +0.35% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 3 | 67% | +0.02% | -0.11 to +0.09% | 100% of 1 | too few (3/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 100% | +0.57% | +0.24 to +0.85% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 2 | 50% | +0.05% | -0.08 to +0.17% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 2 | 0% | -0.01% | -0.02 to -0.01% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 50% | +0.10% | -0.16 to +0.36% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 2 | 100% | +0.78% | +0.70 to +0.85% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 2 | 100% | +0.19% | +0.13 to +0.26% | 0% of 1 | too few (2/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 1 | 100% | +0.42% | +0.42 to +0.42% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% | 100% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.08% | +0.08 to +0.08% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.08% | +0.08 to +0.08% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 86 | 67% | +0.16% | up |
| intraday | weekly | writers even · few weak writers | 38 | 40% | -0.09% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · few weak writers | 20 | 89% | +0.14% | up |
| intraday | weekly | put writers stronger · weak calls | 20 | 74% | +0.12% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | weekly | call writers stronger · few weak writers | 15 | 64% | +0.18% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | weekly | writers even · weak on both sides | 5 | 100% | +0.25% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak calls | 4 | 33% | -0.06% | too few (3/10) |
| day | monthly | writers even · few weak writers | 8 | 43% | +0.09% | too few (7/10) |
| day | weekly | writers even · few weak writers | 3 | 50% | +0.33% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers | 2 | 100% | +0.36% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.02% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 30 | 73% | +0.22% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 20 | 89% | +0.14% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 20 | 74% | +0.12% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 14 | 42% | -0.01% | no clear direction |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 12 | 73% | +0.32% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 67% | +0.30% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.36% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.05% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
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
