# Nifty option chain pattern log
Updated 2026-11-06 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 415 snapshots over 17 trading days
- 457 patterns logged; 151 different patterns so far

## Latest read (2026-11-06 13:45:38)

Nifty trend: weekly **bearish**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-09 (weekly) | 3.1 | 24800 | 0.973 | 24600 | 23000 | 25000 | ±1.25% (24490-25109) | 17.34 |
| 2026-11-23 (monthly) | 17.1 | 24804 | 0.643 | 24000 | 23000 | 25000 | ±2.73% (24127-25480) | 15.67 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls same · near call wall`. Seen 9 times before; Nifty was up after it 62% of the time, average +0.17%. Too few outcomes (8/20) to trade on.
  - Writers: `put writers stronger · weak calls`. Seen 53 times before; Nifty was up after it 76% of the time, average +0.30%. History points to a bull call debit spread, ATM to about the call wall 25000.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 53 times before; Nifty was up after it 76% of the time, average +0.30%. History points to a bull call debit spread, ATM to about the call wall 25000.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 3 times before; Nifty was up after it 67% of the time, average +0.37%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 3 times before; Nifty was up after it 67% of the time, average +0.37%. Too few outcomes (3/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · near call wall`. Seen 7 times before; Nifty was up after it 60% of the time, average +0.11%. Too few outcomes (5/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 41 times before; Nifty was up after it 92% of the time, average +0.26%. History points to a bull call debit spread, ATM to about the call wall 25000.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 41 times before; Nifty was up after it 92% of the time, average +0.26%. History points to a bull call debit spread, ATM to about the call wall 25000.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls same · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +1.58%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 4 times before; Nifty was up after it 75% of the time, average +0.88%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 4 times before; Nifty was up after it 75% of the time, average +0.88%. Too few outcomes (4/20) to trade on.

## Strong vs weak writers, weekly 2026-11-09

Strongest call writers at 25000, strongest put writers at 24500; weakest call writers at 24700, weakest put writers at -. Covers 87% of near-money call OI and 100% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24450 | 18639 | 18012 | 154.7 | 24435 | 391.9 | 24605 | -195 | -237.2 | weak |
| Call | 24500 | 68346 | 55286 | 148.9 | 24434 | 348.0 | 24649 | -151 | -199.1 | weak |
| Call | 24550 | 33220 | 32487 | 132.3 | 24470 | 311.7 | 24682 | -117 | -179.3 | weak |
| Call | 24600 | 81396 | 72758 | 132.1 | 24519 | 271.4 | 24732 | -68 | -139.3 | weak |
| Call | 24650 | 67298 | 65673 | 118.4 | 24534 | 238.3 | 24768 | -31 | -119.9 | weak |
| Call | 24700 | 148344 | 120920 | 91.3 | 24483 | 204.2 | 24791 | -8 | -112.8 | weak |
| Call | 24750 | 90944 | 88304 | 77.8 | 24475 | 175.2 | 24828 | +28 | -97.5 | weak |
| Call | 24800 | 153250 | 119790 | 56.0 | 24457 | 150.3 | 24856 | +56 | -94.3 | medium |
| Call | 24850 | 77158 | 75136 | 55.2 | 24454 | 125.0 | 24905 | +106 | -69.8 | medium |
| Call | 24900 | 90454 | 76779 | 40.9 | 24405 | 106.4 | 24941 | +141 | -65.5 | strong |
| Call | 24950 | 49914 | 47769 | 35.2 | 24459 | 86.3 | 24985 | +185 | -51.2 | strong |
| Call | 25000 | 221847 | 185471 | 21.2 | 24323 | 71.7 | 25021 | +221 | -50.5 | strong |
| Call | 25050 | 42725 | 41749 | 22.9 | 24425 | 57.8 | 25073 | +273 | -34.9 | strong |
| Call | 25100 | 87717 | 74779 | 18.6 | 24430 | 47.4 | 25119 | +319 | -28.7 | strong |
| Call | 25150 | 36399 | 35054 | 16.6 | 24479 | 38.7 | 25167 | +367 | -22.1 | strong |
| Put | 24450 | 94438 | 94438 | 133.5 | 24557 | 51.6 | 24317 | +483 | +81.9 | strong |
| Put | 24500 | 225776 | 223070 | 150.2 | 24561 | 60.7 | 24350 | +450 | +89.5 | strong |
| Put | 24550 | 135207 | 135207 | 154.2 | 24593 | 70.4 | 24396 | +404 | +83.8 | strong |
| Put | 24600 | 169732 | 169674 | 178.1 | 24604 | 83.8 | 24422 | +378 | +94.3 | strong |
| Put | 24650 | 115939 | 115939 | 181.2 | 24640 | 98.0 | 24469 | +331 | +83.1 | strong |
| Put | 24700 | 138734 | 138705 | 171.4 | 24696 | 116.7 | 24529 | +271 | +54.7 | strong |
| Put | 24750 | 73288 | 73284 | 164.6 | 24752 | 136.8 | 24585 | +214 | +27.9 | strong |
| Put | 24800 | 50012 | 49914 | 228.9 | 24699 | 158.9 | 24571 | +229 | +70.0 | strong |
| Put | 24850 | 10399 | 10369 | 248.1 | 24714 | 186.4 | 24602 | +198 | +61.7 | strong |
| Put | 24900 | 9097 | 9065 | 316.6 | 24670 | 214.1 | 24583 | +216 | +102.5 | strong |
| Put | 24950 | 2567 | 2550 | 345.1 | 24680 | 248.5 | 24605 | +195 | +96.6 | strong |
| Put | 25000 | 15437 | 14079 | 487.9 | 24551 | 282.1 | 24512 | +288 | +205.8 | strong |
| Put | 25050 | 1863 | 1860 | 438.7 | 24664 | 322.3 | 24611 | +188 | +116.4 | strong |
| Put | 25100 | 1612 | 1596 | 484.4 | 24659 | 359.1 | 24616 | +184 | +125.2 | strong |
| Put | 25150 | 443 | 443 | 534.4 | 24652 | 405.0 | 24616 | +184 | +129.4 | strong |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 25000, strongest put writers at 24500; weakest call writers at 24500, weakest put writers at -. Covers 91% of near-money call OI and 88% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24450 | 1792 | 1761 | 200.2 | 24117 | 568.0 | 24650 | -154 | -367.8 | weak |
| Call | 24500 | 49724 | 42592 | 168.5 | 23845 | 542.0 | 24669 | -135 | -373.5 | weak |
| Call | 24550 | 2031 | 1997 | 233.2 | 24234 | 502.0 | 24783 | -21 | -268.8 | weak |
| Call | 24600 | 22729 | 22087 | 220.5 | 24247 | 475.1 | 24821 | +17 | -254.6 | weak |
| Call | 24650 | 2022 | 1998 | 242.7 | 24395 | 440.4 | 24893 | +89 | -197.8 | medium |
| Call | 24700 | 15040 | 14705 | 194.9 | 24206 | 413.3 | 24895 | +91 | -218.4 | medium |
| Call | 24750 | 3650 | 3610 | 234.3 | 24459 | 381.9 | 24984 | +180 | -147.7 | strong |
| Call | 24800 | 12032 | 11422 | 103.0 | 24037 | 355.8 | 24903 | +99 | -252.8 | medium |
| Call | 24850 | 2894 | 2893 | 150.8 | 24181 | 327.6 | 25001 | +197 | -176.8 | strong |
| Call | 24900 | 7051 | 6992 | 89.0 | 24127 | 301.6 | 24989 | +185 | -212.6 | strong |
| Call | 24950 | 1326 | 1304 | 90.8 | 24121 | 277.6 | 25041 | +237 | -186.9 | strong |
| Call | 25000 | 80593 | 65126 | 60.5 | 23824 | 255.1 | 25060 | +257 | -194.6 | strong |
| Call | 25050 | 964 | 960 | 90.7 | 24284 | 232.0 | 25141 | +337 | -141.3 | strong |
| Call | 25100 | 9695 | 9501 | 93.3 | 24388 | 212.3 | 25193 | +390 | -119.0 | strong |
| Call | 25150 | 987 | 983 | 79.9 | 24366 | 190.8 | 25230 | +426 | -110.9 | strong |
| Put | 24450 | 2343 | 2336 | 288.4 | 24454 | 195.1 | 24162 | +642 | +93.4 | strong |
| Put | 24500 | 68790 | 60796 | 599.4 | 24118 | 207.8 | 23901 | +903 | +391.6 | strong |
| Put | 24550 | 3816 | 3771 | 282.9 | 24591 | 226.8 | 24267 | +537 | +56.1 | strong |
| Put | 24600 | 14961 | 14900 | 417.8 | 24433 | 241.0 | 24182 | +622 | +176.8 | strong |
| Put | 24650 | 1962 | 1955 | 343.4 | 24587 | 258.9 | 24307 | +497 | +84.5 | strong |
| Put | 24700 | 11794 | 10920 | 503.9 | 24420 | 279.0 | 24196 | +608 | +224.9 | strong |
| Put | 24750 | 1036 | 1030 | 356.7 | 24673 | 300.2 | 24393 | +411 | +56.5 | strong |
| Put | 24800 | 7571 | 7447 | 561.5 | 24352 | 320.9 | 24239 | +565 | +240.5 | strong |
| Put | 24850 | 274 | 268 | 505.0 | 24513 | 348.0 | 24345 | +459 | +157.0 | strong |
| Put | 24900 | 3281 | 3265 | 475.5 | 24581 | 369.2 | 24425 | +379 | +106.2 | strong |
| Put | 24950 | 184 | 184 | 560.3 | 24488 | 404.6 | 24390 | +414 | +155.7 | strong |
| Put | 25000 | 35206 | 24409 | 1753.0 | 23169 | 421.0 | 23247 | +1557 | +1332.0 | strong |
| Put | 25050 | 111 | 108 | 556.6 | 24617 | 455.9 | 24493 | +310 | +100.6 | strong |
| Put | 25100 | 448 | 436 | 1246.0 | 23864 | 485.1 | 23854 | +950 | +760.9 | strong |
| Put | 25150 | 37 | 34 | 719.0 | 24501 | 537.4 | 24431 | +373 | +181.6 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 34 | 73% | +0.26% | -0.44 to +0.97% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 15 | 93% | +0.31% | -0.02 to +0.62% | 33% of 3 | up |
| monthly | PCR flat · put and call writing · walls same · near call wall | 13 | 54% | +0.07% | -0.71 to +0.78% | 100% of 1 | no clear direction |
| monthly | PCR flat · put writing · walls same · mid walls | 12 | 100% | +0.54% | +0.09 to +1.02% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near put wall | 11 | 64% | +0.05% | -0.47 to +0.42% | 33% of 3 | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near call wall | 10 | 100% | +0.45% | +0.20 to +0.76% |  | up |
| weekly | PCR down · unwinding · walls same · near call wall | 10 | 62% | +0.17% | -0.07 to +0.59% | 33% of 3 | too few (8/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| weekly | PCR down · call writing · walls same · near put wall | 8 | 88% | +0.36% | -0.37 to +0.85% | 33% of 3 | too few (8/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 7 | 80% | +0.21% | -0.12 to +0.71% | 100% of 1 | too few (5/10) |
| monthly | PCR down · call writing · walls same · near call wall | 7 | 83% | +0.12% | -0.78 to +0.58% | 100% of 1 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 7 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| weekly | PCR up · put writing · walls up · near put wall | 7 | 57% | +0.20% | -0.13 to +0.72% | 0% of 2 | too few (7/10) |
| monthly | PCR up · put writing · walls same · near call wall | 6 | 50% | +0.23% | -0.40 to +0.73% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 6 | 80% | +0.04% | -0.18 to +0.19% |  | too few (5/10) |
| monthly | PCR flat · put writing · walls same · near call wall | 6 | 100% | +0.54% | +0.41 to +0.67% |  | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 6 | 50% | +0.08% | -0.74 to +0.62% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put writing · walls same · mid walls | 6 | 100% | +0.65% | +0.24 to +0.85% | 100% of 1 | too few (6/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 6 | 50% | +0.17% | -0.78 to +0.90% | 100% of 1 | too few (6/10) |
| weekly | PCR down · call writing · walls down · near call wall | 5 | 80% | +0.40% | -0.06 to +0.74% | 100% of 1 | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 5 | 60% | +0.05% | -0.47 to +0.49% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls down · mid walls | 5 | 80% | +0.31% | -0.07 to +0.54% | 50% of 2 | too few (5/10) |
| weekly | PCR down · call writing · walls same · mid walls | 5 | 100% | +0.46% | +0.04 to +0.75% | 33% of 3 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near call wall | 5 | 80% | +0.53% | -0.02 to +0.91% | 50% of 2 | too few (5/10) |
| weekly | PCR up · put writing · walls up · mid walls | 5 | 80% | +0.36% | -0.16 to +0.65% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 5 | 80% | +0.28% | -1.11 to +0.78% | 0% of 1 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 5 | 75% | +0.21% | -0.05 to +0.63% | 50% of 2 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.53% | +0.15 to +0.69% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 4 | 100% | +0.35% | +0.13 to +0.59% | 0% of 2 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | +0.10% | -0.68 to +0.75% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 33% | -0.17% | -0.75 to +0.38% | 0% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 3 | 33% | +0.13% | -0.02 to +0.43% | 0% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 3 | 67% | +0.24% | -0.22 to +0.68% | 100% of 2 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 3 | 67% | +0.16% | -0.11 to +0.50% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 3 | 100% | +0.84% | +0.59 to +1.03% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 2 | too few (3/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 3 | 100% | +0.50% | +0.37 to +0.62% |  | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 0% | -0.44% | -0.69 to -0.20% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 1 | too few (2/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 2 | 100% | +0.81% | +0.73 to +0.89% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 2 | 100% | +0.50% | +0.47 to +0.53% | 50% of 2 | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 2 | 50% | +0.16% | -0.57 to +0.89% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 2 | 100% | +0.15% | +0.01 to +0.29% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +0.93% | +0.93 to +0.93% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 | 100% | +0.53% | +0.53 to +0.53% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 100% | +0.58% | +0.58 to +0.58% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 2 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +1.01% | -0.39 to +2.40% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +1.09% | +1.09 to +1.09% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 94 | 70% | +0.17% | up |
| intraday | weekly | put writers stronger · weak calls | 54 | 76% | +0.30% | up |
| intraday | weekly | writers even · few weak writers | 52 | 59% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · weak calls | 49 | 85% | +0.50% | up |
| intraday | monthly | writers even · weak calls | 42 | 92% | +0.26% | up |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | weekly | put writers stronger · few weak writers | 28 | 92% | +0.22% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | call writers stronger · few weak writers | 19 | 72% | +0.30% | no clear direction |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | weekly | writers even · weak calls | 18 | 88% | +0.52% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | weekly | writers even · weak on both sides | 6 | 100% | +0.36% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| day | monthly | writers even · few weak writers | 8 | 50% | +0.34% | too few (8/10) |
| day | monthly | writers even · weak calls | 5 | 75% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · weak calls | 4 | 67% | +0.37% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | writers even · few weak writers | 3 | 67% | +1.02% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | put writers stronger · weak calls | 2 | 100% | +0.86% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak calls | 2 | 50% | +0.54% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 54 | 76% | +0.30% | up |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 49 | 85% | +0.50% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 42 | 92% | +0.26% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 28 | 92% | +0.22% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 28 | 77% | +0.22% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.66% | up |
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
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m up | 1 | 100% | +0.91% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 5 | 75% | +0.88% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 67% | +0.37% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +0.86% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m up | 1 | 100% | +1.09% | too few (1/10) |
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
