# Nifty option chain pattern log
Updated 2026-11-03 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 349 snapshots over 14 trading days
- 382 patterns logged; 141 different patterns so far

## Latest read (2026-11-03 15:40:00)

Nifty trend: weekly **bearish**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-03 (weekly) | 0.0 | 23811 | 1.165 | 23700 | 23700 | 23850 | ±0.05% (23800-23822) | 0.58 |
| 2026-11-23 (monthly) | 20.0 | 23811 | 0.686 | 23500 | 23000 | 24000 | ±2.54% (23205-24416) | 13.54 |

- **Weekly, last 30 min**: `PCR up · unwinding · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 45 times before; Nifty was up after it 81% of the time, average +0.33%. History points to a bull call debit spread, ATM to about the call wall 23850.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 45 times before; Nifty was up after it 81% of the time, average +0.33%. History points to a bull call debit spread, ATM to about the call wall 23850.
- **Weekly, today vs previous day**: `PCR up · put writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 2 times before; Nifty was up after it 50% of the time, average +0.23%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 2 times before; Nifty was up after it 50% of the time, average +0.23%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR down · call writing · walls same · near call wall`. Seen 4 times before; Nifty was up after it 75% of the time, average -0.03%. Too few outcomes (4/20) to trade on.
  - Writers: `put writers stronger · weak calls`. Seen 24 times before; Nifty was up after it 88% of the time, average +0.52%. History points to a bull call debit spread, ATM to about the call wall 24000.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 24 times before; Nifty was up after it 88% of the time, average +0.52%. History points to a bull call debit spread, ATM to about the call wall 24000.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly bearish · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-03

Strongest call writers at 24000, strongest put writers at 23700; weakest call writers at 23850, weakest put writers at -. Covers 95% of near-money call OI and 100% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 23500 | 22392 | 16381 | 14.2 | 23076 | 311.6 | 23514 | -297 | -297.4 | weak |
| Call | 23550 | 22861 | 22480 | 58.6 | 23423 | 260.2 | 23609 | -202 | -201.6 | weak |
| Call | 23600 | 46206 | 44983 | 46.1 | 23469 | 210.3 | 23646 | -165 | -164.2 | weak |
| Call | 23650 | 50669 | 50351 | 47.2 | 23599 | 160.8 | 23697 | -114 | -113.6 | weak |
| Call | 23700 | 90262 | 88962 | 29.7 | 23597 | 110.9 | 23730 | -81 | -81.2 | weak |
| Call | 23750 | 96791 | 96347 | 16.7 | 23623 | 60.9 | 23767 | -44 | -44.1 | weak |
| Call | 23800 | 185977 | 182908 | 7.2 | 23554 | 10.8 | 23807 | -4 | -3.6 | weak |
| Call | 23850 | 244100 | 243615 | 4.2 | 23616 | 0.1 | 23854 | +43 | +4.2 | weak |
| Call | 23900 | 115883 | 113472 | 2.4 | 23546 | 0.1 | 23902 | +92 | +2.4 | medium |
| Call | 23950 | 52744 | 52072 | 1.6 | 23603 | 0.1 | 23952 | +141 | +1.6 | strong |
| Call | 24000 | 146258 | 125391 | 1.6 | 23223 | 0.1 | 24002 | +191 | +1.6 | strong |
| Call | 24050 | 67428 | 66381 | 1.0 | 23551 | 0.1 | 24051 | +240 | +0.9 | strong |
| Call | 24100 | 86230 | 84069 | 1.0 | 23519 | 0.1 | 24101 | +290 | +0.9 | strong |
| Call | 24150 | 42068 | 41549 | 0.8 | 23525 | 0.1 | 24151 | +340 | +0.7 | strong |
| Put | 23500 | 158731 | 158118 | 31.2 | 23612 | 0.1 | 23469 | +342 | +31.2 | strong |
| Put | 23550 | 140620 | 140618 | 37.5 | 23626 | 0.1 | 23512 | +298 | +37.5 | strong |
| Put | 23600 | 213737 | 213609 | 53.9 | 23631 | 0.1 | 23546 | +265 | +53.8 | strong |
| Put | 23650 | 212346 | 212331 | 58.6 | 23655 | 0.1 | 23591 | +219 | +58.5 | strong |
| Put | 23700 | 326325 | 326230 | 61.0 | 23688 | 0.1 | 23639 | +172 | +60.9 | strong |
| Put | 23750 | 207125 | 207120 | 51.0 | 23738 | 0.1 | 23699 | +112 | +51.0 | strong |
| Put | 23800 | 175622 | 175333 | 61.0 | 23753 | 0.1 | 23739 | +72 | +60.9 | medium |
| Put | 23850 | 31991 | 31987 | 105.3 | 23749 | 39.0 | 23745 | +66 | +66.2 | medium |
| Put | 23900 | 14085 | 13920 | 180.6 | 23725 | 89.0 | 23719 | +91 | +91.6 | medium |
| Put | 23950 | 3819 | 3812 | 195.6 | 23757 | 139.2 | 23754 | +56 | +56.5 | medium |
| Put | 24000 | 6644 | 5821 | 325.4 | 23678 | 188.7 | 23675 | +136 | +136.8 | strong |
| Put | 24050 | 916 | 914 | 361.1 | 23696 | 238.8 | 23689 | +122 | +122.3 | strong |
| Put | 24100 | 761 | 721 | 463.1 | 23644 | 288.4 | 23637 | +174 | +174.7 | strong |
| Put | 24150 | 447 | 402 | 441.3 | 23713 | 338.8 | 23709 | +102 | +102.5 | medium |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 24000, strongest put writers at 23500; weakest call writers at 23500, weakest put writers at -. Covers 74% of near-money call OI and 84% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 23500 | 94181 | 66500 | 139.8 | 22713 | 478.0 | 23640 | -171 | -338.1 | weak |
| Call | 23550 | 1645 | 932 | 162.1 | 22954 | 440.9 | 23712 | -99 | -278.8 | weak |
| Call | 23600 | 15738 | 11322 | 219.4 | 23155 | 412.4 | 23819 | +9 | -192.9 | weak |
| Call | 23650 | 2672 | 2500 | 247.8 | 23359 | 382.9 | 23898 | +87 | -135.1 | medium |
| Call | 23700 | 17550 | 11832 | 157.8 | 23079 | 350.0 | 23858 | +47 | -192.2 | weak |
| Call | 23750 | 8022 | 7564 | 146.2 | 23322 | 321.6 | 23896 | +85 | -175.5 | medium |
| Call | 23800 | 30740 | 24677 | 100.5 | 22960 | 291.5 | 23901 | +90 | -191.0 | medium |
| Call | 23850 | 1593 | 1277 | 125.5 | 23145 | 266.1 | 23976 | +165 | -140.6 | strong |
| Call | 23900 | 12572 | 10048 | 119.3 | 23184 | 243.7 | 24019 | +208 | -124.4 | strong |
| Call | 23950 | 1938 | 1701 | 117.6 | 23289 | 218.7 | 24068 | +257 | -101.0 | strong |
| Call | 24000 | 76517 | 50833 | 73.3 | 22993 | 198.0 | 24073 | +262 | -124.7 | strong |
| Call | 24050 | 2538 | 2377 | 105.5 | 23357 | 176.4 | 24155 | +345 | -70.9 | strong |
| Call | 24100 | 9007 | 7297 | 57.0 | 23024 | 159.9 | 24157 | +346 | -102.9 | strong |
| Call | 24150 | 1411 | 1287 | 67.5 | 23257 | 141.3 | 24218 | +407 | -73.8 | strong |
| Put | 23500 | 92819 | 80561 | 626.0 | 23005 | 201.2 | 22874 | +937 | +424.9 | strong |
| Put | 23550 | 1137 | 1065 | 338.5 | 23506 | 216.8 | 23211 | +599 | +121.8 | strong |
| Put | 23600 | 16982 | 16227 | 336.5 | 23549 | 233.8 | 23264 | +547 | +102.7 | strong |
| Put | 23650 | 2648 | 2549 | 365.3 | 23545 | 252.3 | 23285 | +526 | +113.0 | strong |
| Put | 23700 | 14020 | 13397 | 402.0 | 23526 | 272.9 | 23298 | +513 | +129.1 | strong |
| Put | 23750 | 1576 | 1493 | 394.1 | 23589 | 292.5 | 23356 | +455 | +101.6 | strong |
| Put | 23800 | 12391 | 8514 | 455.6 | 23532 | 314.1 | 23344 | +466 | +141.6 | strong |
| Put | 23850 | 596 | 548 | 435.0 | 23598 | 339.2 | 23415 | +396 | +95.8 | strong |
| Put | 23900 | 2619 | 2339 | 726.4 | 23235 | 365.6 | 23174 | +637 | +360.7 | strong |
| Put | 23950 | 255 | 241 | 459.3 | 23639 | 390.9 | 23491 | +320 | +68.4 | strong |
| Put | 24000 | 37237 | 29429 | 1209.7 | 22703 | 419.9 | 22790 | +1021 | +789.9 | strong |
| Put | 24050 | 192 | 174 | 539.0 | 23612 | 451.0 | 23511 | +300 | +88.0 | strong |
| Put | 24100 | 939 | 832 | 1085.5 | 22951 | 478.2 | 23015 | +796 | +607.3 | strong |
| Put | 24150 | 114 | 85 | 639.4 | 23576 | 509.9 | 23511 | +300 | +129.5 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 34 | 73% | +0.26% | -0.44 to +0.97% | 100% of 1 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 12 | 100% | +0.54% | +0.09 to +1.02% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 11 | 100% | +0.32% | +0.03 to +0.62% | 33% of 3 | up |
| weekly | PCR up · put writing · walls same · near put wall | 11 | 64% | +0.05% | -0.47 to +0.42% | 33% of 3 | no clear direction |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| weekly | PCR down · call writing · walls same · near put wall | 8 | 88% | +0.36% | -0.37 to +0.85% | 33% of 3 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 7 | 80% | +0.21% | -0.12 to +0.71% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 6 | 80% | +0.04% | -0.18 to +0.19% |  | too few (5/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 6 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put writing · walls same · mid walls | 6 | 100% | +0.65% | +0.24 to +0.85% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 6 | 50% | +0.17% | -0.78 to +0.90% | 100% of 1 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 5 | 100% | +0.46% | +0.04 to +0.75% | 33% of 3 | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 5 | 60% | +0.05% | -0.47 to +0.49% | 100% of 1 | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 5 | 100% | +0.43% | +0.26 to +0.59% |  | too few (5/10) |
| monthly | PCR down · call writing · walls same · near call wall | 5 | 75% | -0.03% | -0.78 to +0.33% | 100% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls down · mid walls | 5 | 80% | +0.31% | -0.07 to +0.54% | 50% of 2 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 5 | 60% | +0.12% | -0.07 to +0.32% | 33% of 3 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 5 | 75% | +0.21% | -0.05 to +0.63% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put writing · walls up · near put wall | 5 | 60% | +0.15% | -0.13 to +0.35% | 0% of 2 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | +0.10% | -0.68 to +0.75% | 50% of 2 | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 4 | 25% | -0.38% | -0.71 to +0.45% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put writing · walls up · mid walls | 4 | 75% | +0.33% | -0.16 to +0.65% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls same · near call wall | 4 | 75% | +0.49% | -0.02 to +0.91% | 50% of 2 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 3 | 100% | +0.33% | +0.13 to +0.59% | 0% of 2 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put writing · walls same · near call wall | 3 | 33% | -0.01% | -0.40 to +0.43% | 100% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 3 | 67% | +0.16% | -0.11 to +0.50% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 33% | -0.17% | -0.75 to +0.38% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 3 | 33% | +0.13% | -0.02 to +0.43% | 0% of 2 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.30 to +0.45% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · near call wall | 2 | 100% | +0.39% | +0.15 to +0.64% | 50% of 2 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 2 | 100% | +0.26% | +0.17 to +0.35% | 0% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% | 0% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 0% | -0.44% | -0.69 to -0.20% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 2 | 100% | +0.50% | +0.47 to +0.53% | 50% of 2 | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 1 | 100% | +0.85% | +0.85 to +0.85% | 0% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.47% | +0.47 to +0.47% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 | 100% | +0.53% | +0.53 to +0.53% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 100% | +0.58% | +0.58 to +0.58% | 0% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.32% | +0.32 to +0.32% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
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
| weekly | PCR up · put writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 94 | 70% | +0.17% | up |
| intraday | weekly | put writers stronger · weak calls | 46 | 81% | +0.33% | up |
| intraday | weekly | writers even · few weak writers | 41 | 49% | -0.02% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | monthly | writers even · weak calls | 28 | 88% | +0.14% | up |
| intraday | monthly | put writers stronger · weak calls | 25 | 88% | +0.52% | up |
| intraday | weekly | put writers stronger · few weak writers | 25 | 91% | +0.15% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | weekly | call writers stronger · few weak writers | 15 | 64% | +0.18% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak calls | 7 | 67% | +0.34% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | weekly | writers even · weak on both sides | 6 | 100% | +0.36% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| day | monthly | writers even · few weak writers | 8 | 50% | +0.34% | too few (8/10) |
| day | monthly | writers even · weak calls | 3 | 67% | +0.37% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls | 3 | 50% | +0.23% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · few weak writers | 2 | 50% | +0.33% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |
| day | monthly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.02% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 46 | 81% | +0.33% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 28 | 88% | +0.14% | up |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 25 | 88% | +0.52% | up |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 25 | 91% | +0.15% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 17 | 62% | +0.13% | no clear direction |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 12 | 73% | +0.32% | no clear direction |
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
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 50% | +0.23% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.05% | too few (1/10) |
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
