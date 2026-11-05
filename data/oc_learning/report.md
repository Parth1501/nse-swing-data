# Nifty option chain pattern log
Updated 2026-11-05 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 377 snapshots over 16 trading days
- 413 patterns logged; 149 different patterns so far

## Latest read (2026-11-05 09:44:49)

Nifty trend: weekly **bearish**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-09 (weekly) | 4.2 | 24392 | 0.506 | 24100 | 24300 | 25000 | ±1.22% (24095-24689) | 14.56 |
| 2026-11-23 (monthly) | 18.2 | 24392 | 0.631 | 23500 | 23000 | 25000 | ±2.32% (23825-24959) | 13.05 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls up · near put wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +1.03%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 8 times before; Nifty was up after it 71% of the time, average +0.32%. Too few outcomes (7/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 4 times before; Nifty was up after it 100% of the time, average +0.61%. Too few outcomes (4/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.02%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put writing · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 40 times before; Nifty was up after it 92% of the time, average +0.24%. History points to a bull call debit spread, ATM to about the call wall 25000.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 40 times before; Nifty was up after it 92% of the time, average +0.24%. History points to a bull call debit spread, ATM to about the call wall 25000.
- **Monthly, today vs previous day**: `PCR down · put writing · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 4 times before; Nifty was up after it 75% of the time, average +0.73%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 4 times before; Nifty was up after it 75% of the time, average +0.73%. Too few outcomes (4/20) to trade on.

## Strong vs weak writers, weekly 2026-11-09

Strongest call writers at 25000, strongest put writers at 24300; weakest call writers at 24300, weakest put writers at 24750. Covers 67% of near-money call OI and 91% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24050 | 14735 | 12782 | 107.5 | 23872 | 374.1 | 24157 | -234 | -266.7 | weak |
| Call | 24100 | 42923 | 26562 | 91.3 | 23877 | 333.2 | 24191 | -201 | -242.0 | weak |
| Call | 24150 | 25698 | 21241 | 83.8 | 23895 | 293.9 | 24234 | -158 | -210.1 | weak |
| Call | 24200 | 63413 | 30146 | 70.6 | 23885 | 257.1 | 24271 | -121 | -186.5 | weak |
| Call | 24250 | 27954 | 22190 | 61.4 | 23893 | 223.1 | 24311 | -81 | -161.7 | weak |
| Call | 24300 | 119694 | 80643 | 122.7 | 24144 | 192.2 | 24423 | +31 | -69.4 | weak |
| Call | 24350 | 89355 | 83380 | 136.5 | 24278 | 163.8 | 24486 | +95 | -27.4 | medium |
| Call | 24400 | 115156 | 82341 | 110.2 | 24255 | 137.3 | 24510 | +118 | -27.1 | strong |
| Call | 24450 | 44600 | 39515 | 85.5 | 24215 | 114.5 | 24536 | +144 | -29.0 | strong |
| Call | 24500 | 151744 | 72146 | 34.3 | 23949 | 94.2 | 24534 | +142 | -59.8 | strong |
| Call | 24550 | 34221 | 30153 | 40.0 | 24064 | 77.0 | 24590 | +198 | -37.0 | strong |
| Call | 24600 | 83007 | 45748 | 42.2 | 24153 | 62.5 | 24642 | +250 | -20.3 | strong |
| Call | 24650 | 39109 | 33393 | 33.6 | 24130 | 51.0 | 24684 | +292 | -17.3 | strong |
| Call | 24700 | 87087 | 39268 | 21.1 | 24027 | 41.4 | 24721 | +329 | -20.4 | strong |
| Call | 24750 | 40460 | 35973 | 20.4 | 24074 | 33.6 | 24770 | +378 | -13.3 | strong |
| Put | 24050 | 50498 | 50230 | 66.0 | 24351 | 48.1 | 23984 | +408 | +17.8 | strong |
| Put | 24100 | 32563 | 32119 | 118.8 | 24264 | 57.2 | 23981 | +411 | +61.6 | strong |
| Put | 24150 | 25092 | 24932 | 91.4 | 24348 | 68.1 | 24059 | +333 | +23.3 | strong |
| Put | 24200 | 61437 | 60113 | 98.7 | 24362 | 81.1 | 24101 | +291 | +17.6 | strong |
| Put | 24250 | 34555 | 34536 | 107.4 | 24375 | 96.5 | 24143 | +249 | +10.9 | strong |
| Put | 24300 | 127172 | 126638 | 119.4 | 24385 | 114.5 | 24181 | +211 | +4.9 | strong |
| Put | 24350 | 70311 | 70311 | 139.1 | 24388 | 136.2 | 24211 | +181 | +2.9 | strong |
| Put | 24400 | 62903 | 62764 | 168.2 | 24382 | 160.0 | 24232 | +160 | +8.2 | strong |
| Put | 24450 | 11366 | 11366 | 196.8 | 24381 | 187.3 | 24253 | +139 | +9.5 | strong |
| Put | 24500 | 26620 | 21609 | 247.0 | 24358 | 217.5 | 24253 | +139 | +29.5 | strong |
| Put | 24550 | 2518 | 2518 | 253.8 | 24388 | 250.1 | 24296 | +96 | +3.8 | medium |
| Put | 24600 | 4620 | 4516 | 291.1 | 24386 | 285.4 | 24309 | +83 | +5.7 | medium |
| Put | 24650 | 1155 | 1155 | 323.8 | 24392 | 323.8 | 24326 | +66 | +0.0 | medium |
| Put | 24700 | 1795 | 1748 | 384.8 | 24370 | 364.8 | 24315 | +77 | +20.0 | medium |
| Put | 24750 | 352 | 347 | 410.0 | 24388 | 406.1 | 24340 | +52 | +3.9 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 25000, strongest put writers at 24000; weakest call writers at 24000, weakest put writers at -. Covers 82% of near-money call OI and 85% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24050 | 2043 | 1922 | 113.7 | 23392 | 508.2 | 24164 | -228 | -394.5 | weak |
| Call | 24100 | 8620 | 7385 | 100.5 | 23277 | 478.2 | 24200 | -191 | -377.8 | weak |
| Call | 24150 | 1298 | 1210 | 98.9 | 23417 | 443.2 | 24249 | -143 | -344.4 | weak |
| Call | 24200 | 28306 | 26017 | 97.1 | 23476 | 407.1 | 24297 | -95 | -310.0 | weak |
| Call | 24250 | 1963 | 1866 | 61.1 | 23217 | 376.1 | 24311 | -81 | -315.1 | weak |
| Call | 24300 | 14776 | 13051 | 150.0 | 23600 | 347.2 | 24450 | +58 | -197.3 | medium |
| Call | 24350 | 3447 | 3343 | 155.1 | 23886 | 317.8 | 24505 | +113 | -162.7 | strong |
| Call | 24400 | 14155 | 13338 | 124.8 | 23704 | 289.6 | 24525 | +133 | -164.8 | strong |
| Call | 24450 | 1597 | 1525 | 82.8 | 23644 | 263.6 | 24533 | +141 | -180.8 | strong |
| Call | 24500 | 49705 | 38991 | 45.2 | 23385 | 239.4 | 24545 | +153 | -194.2 | strong |
| Call | 24550 | 1233 | 1165 | 59.9 | 23528 | 216.4 | 24610 | +218 | -156.6 | strong |
| Call | 24600 | 8844 | 8118 | 44.6 | 23604 | 192.8 | 24645 | +253 | -148.2 | strong |
| Call | 24650 | 907 | 863 | 67.0 | 23714 | 173.3 | 24717 | +325 | -106.3 | strong |
| Call | 24700 | 6783 | 6397 | 34.8 | 23541 | 155.2 | 24735 | +343 | -120.5 | strong |
| Call | 24750 | 752 | 708 | 41.9 | 23601 | 138.0 | 24792 | +400 | -96.1 | strong |
| Put | 24050 | 703 | 690 | 324.8 | 24007 | 153.2 | 23725 | +667 | +171.6 | strong |
| Put | 24100 | 4714 | 4608 | 409.2 | 23956 | 166.6 | 23691 | +701 | +242.6 | strong |
| Put | 24150 | 706 | 682 | 298.8 | 24157 | 181.2 | 23851 | +541 | +117.5 | strong |
| Put | 24200 | 8848 | 8642 | 497.4 | 23930 | 197.9 | 23703 | +689 | +299.4 | strong |
| Put | 24250 | 857 | 846 | 326.9 | 24216 | 216.0 | 23923 | +469 | +110.9 | strong |
| Put | 24300 | 11315 | 11141 | 387.9 | 24174 | 235.1 | 23912 | +480 | +152.8 | strong |
| Put | 24350 | 1755 | 1742 | 280.7 | 24355 | 255.7 | 24069 | +323 | +25.0 | strong |
| Put | 24400 | 6655 | 6551 | 377.7 | 24256 | 277.2 | 24022 | +370 | +100.5 | strong |
| Put | 24450 | 459 | 452 | 391.1 | 24264 | 299.2 | 24059 | +333 | +91.9 | strong |
| Put | 24500 | 31068 | 22166 | 1291.6 | 23184 | 325.4 | 23208 | +1184 | +966.2 | strong |
| Put | 24550 | 216 | 211 | 388.4 | 24341 | 352.0 | 24162 | +230 | +36.4 | strong |
| Put | 24600 | 2054 | 1990 | 1169.5 | 23415 | 379.6 | 23431 | +961 | +789.8 | strong |
| Put | 24650 | 149 | 146 | 442.4 | 24350 | 408.9 | 24208 | +184 | +33.5 | strong |
| Put | 24700 | 2538 | 1661 | 1434.6 | 23213 | 439.1 | 23265 | +1126 | +995.5 | strong |
| Put | 24750 | 115 | 113 | 485.4 | 24376 | 471.0 | 24265 | +127 | +14.4 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 34 | 73% | +0.26% | -0.44 to +0.97% | 100% of 1 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 12 | 100% | +0.54% | +0.09 to +1.02% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 12 | 100% | +0.32% | +0.03 to +0.62% | 33% of 3 | up |
| weekly | PCR up · put writing · walls same · near put wall | 11 | 64% | +0.05% | -0.47 to +0.42% | 33% of 3 | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near call wall | 9 | 100% | +0.41% | +0.20 to +0.68% |  | too few (9/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| weekly | PCR down · call writing · walls same · near put wall | 8 | 88% | +0.36% | -0.37 to +0.85% | 33% of 3 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 7 | 80% | +0.21% | -0.12 to +0.71% | 100% of 1 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 7 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR down · call writing · walls same · near call wall | 6 | 80% | +0.09% | -0.78 to +0.58% | 100% of 1 | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 6 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 6 | 80% | +0.04% | -0.18 to +0.19% |  | too few (5/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR up · put writing · walls same · mid walls | 6 | 100% | +0.65% | +0.24 to +0.85% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 6 | 50% | +0.08% | -0.74 to +0.62% | 100% of 1 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 6 | 67% | +0.13% | -0.07 to +0.32% | 33% of 3 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 6 | 50% | -0.19% | -0.71 to +0.45% | 100% of 1 | too few (6/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 6 | 50% | +0.17% | -0.78 to +0.90% | 100% of 1 | too few (6/10) |
| weekly | PCR down · call writing · walls down · mid walls | 5 | 80% | +0.31% | -0.07 to +0.54% | 50% of 2 | too few (5/10) |
| weekly | PCR up · put writing · walls up · near put wall | 5 | 60% | +0.15% | -0.13 to +0.35% | 0% of 2 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 5 | 75% | +0.21% | -0.05 to +0.63% | 50% of 2 | too few (4/10) |
| weekly | PCR down · call writing · walls same · mid walls | 5 | 100% | +0.46% | +0.04 to +0.75% | 33% of 3 | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 5 | 60% | +0.05% | -0.47 to +0.49% | 100% of 1 | too few (5/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | +0.10% | -0.68 to +0.75% | 50% of 2 | too few (4/10) |
| weekly | PCR down · call writing · walls same · near call wall | 4 | 75% | +0.49% | -0.02 to +0.91% | 50% of 2 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR up · put writing · walls up · mid walls | 4 | 75% | +0.33% | -0.16 to +0.65% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 3 | 100% | +0.33% | +0.13 to +0.59% | 0% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 3 | 33% | +0.13% | -0.02 to +0.43% | 0% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | +0.04% | -1.11 to +0.78% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 33% | -0.17% | -0.75 to +0.38% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near call wall | 3 | 100% | +0.45% | +0.30 to +0.58% | 100% of 1 | too few (3/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 3 | 100% | +0.50% | +0.37 to +0.62% |  | too few (3/10) |
| monthly | PCR up · put writing · walls same · near call wall | 3 | 33% | -0.01% | -0.40 to +0.43% | 100% of 1 | too few (3/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 3 | 67% | +0.24% | -0.22 to +0.68% | 100% of 2 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 3 | 67% | +0.16% | -0.11 to +0.50% | 50% of 2 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% |  | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 0% | -0.44% | -0.69 to -0.20% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 2 | 100% | +0.39% | +0.15 to +0.64% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 2 | 100% | +0.26% | +0.17 to +0.35% | 0% of 2 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 2 | 100% | +0.50% | +0.47 to +0.53% | 50% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 2 | 50% | +0.16% | -0.57 to +0.89% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.89% | +0.89 to +0.89% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.47% | +0.47 to +0.47% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 | 100% | +0.53% | +0.53 to +0.53% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
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
| monthly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.71% | -0.39 to +1.80% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR down · put writing · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 94 | 70% | +0.17% | up |
| intraday | weekly | writers even · few weak writers | 50 | 57% | +0.03% | no clear direction |
| intraday | weekly | put writers stronger · weak calls | 46 | 81% | +0.33% | up |
| intraday | monthly | writers even · weak calls | 41 | 92% | +0.24% | up |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | monthly | put writers stronger · weak calls | 28 | 89% | +0.51% | up |
| intraday | weekly | put writers stronger · few weak writers | 25 | 91% | +0.15% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | call writers stronger · few weak writers | 19 | 72% | +0.30% | no clear direction |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak calls | 9 | 71% | +0.32% | too few (7/10) |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | weekly | writers even · weak on both sides | 6 | 100% | +0.36% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| day | monthly | writers even · few weak writers | 8 | 50% | +0.34% | too few (8/10) |
| day | monthly | writers even · weak calls | 5 | 75% | +0.73% | too few (4/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls | 3 | 67% | +0.37% | too few (3/10) |
| day | weekly | writers even · few weak writers | 3 | 67% | +0.82% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak calls | 2 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |
| day | monthly | put writers stronger · weak calls | 1 | 100% | +0.63% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 46 | 81% | +0.33% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 41 | 92% | +0.24% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 28 | 89% | +0.51% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 26 | 75% | +0.18% | up |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 25 | 91% | +0.15% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 5 | 100% | +0.61% | too few (4/10) |
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
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 5 | 75% | +0.73% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.42% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 100% | +0.63% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m up | 1 |  |  | too few (0/10) |
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
