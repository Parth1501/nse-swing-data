# Nifty option chain pattern log
Updated 2026-10-23 17:17 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 172 snapshots over 7 trading days
- 187 patterns logged; 98 different patterns so far

## Latest read (2026-10-23 15:40:00)

Nifty trend: weekly **bearish**, 125-min **down**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 4.0 | 22600 | 0.824 | 22700 | 21500 | 24000 | ±1.2% (22330-22870) | 14.48 |
| 2026-11-23 (monthly) | 31.0 | 22600 | 1.326 | 23000 | 22000 | 23000 | ±3.74% (21756-23444) | 15.83 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls same · mid walls`. Seen 3 times before; Nifty was up after it 50% of the time, average +0.25%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 9 times before; Nifty was up after it 67% of the time, average -0.04%. Too few outcomes (9/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m down`: Seen 5 times before; Nifty was up after it 80% of the time, average +0.08%. Too few outcomes (5/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly bearish · 125m down`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · quiet OI · walls same · mid walls`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.28%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 29 times before; Nifty was up after it 59% of the time, average -0.04%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m down`: Seen 15 times before; Nifty was up after it 62% of the time, average -0.03%. Too few outcomes (13/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.46%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m down`: Seen 2 times before; Nifty was up after it 0% of the time, average -0.46%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at 22400, weakest put writers at 22700. Covers 93% of near-money call OI and 90% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 16012 | 11359 | 298.3 | 22473 | 335.4 | 22598 | -2 | -37.1 | weak |
| Call | 22350 | 7802 | 7563 | 257.2 | 22465 | 297.6 | 22607 | +7 | -40.4 | weak |
| Call | 22400 | 38690 | 36161 | 222.3 | 22462 | 254.2 | 22622 | +22 | -32.0 | weak |
| Call | 22450 | 23985 | 23849 | 192.7 | 22467 | 224.8 | 22643 | +43 | -32.2 | weak |
| Call | 22500 | 130851 | 124228 | 190.1 | 22511 | 190.0 | 22690 | +90 | +0.1 | medium |
| Call | 22550 | 43026 | 42823 | 168.8 | 22517 | 157.0 | 22719 | +119 | +11.8 | strong |
| Call | 22600 | 97159 | 95108 | 151.1 | 22525 | 132.4 | 22751 | +151 | +18.6 | strong |
| Call | 22650 | 48407 | 48248 | 131.0 | 22534 | 110.9 | 22781 | +181 | +20.1 | strong |
| Call | 22700 | 155338 | 149797 | 135.5 | 22595 | 88.8 | 22836 | +236 | +46.7 | strong |
| Call | 22750 | 53920 | 52778 | 139.8 | 22663 | 71.0 | 22890 | +290 | +68.8 | strong |
| Call | 22800 | 158097 | 151580 | 121.5 | 22655 | 58.5 | 22922 | +322 | +63.0 | strong |
| Call | 22850 | 50549 | 49918 | 95.3 | 22627 | 45.2 | 22945 | +345 | +50.1 | strong |
| Call | 22900 | 117374 | 113006 | 102.2 | 22696 | 37.5 | 23002 | +402 | +64.7 | strong |
| Put | 22300 | 95271 | 77423 | 45.2 | 22701 | 41.9 | 22255 | +345 | +3.4 | strong |
| Put | 22350 | 39601 | 38880 | 67.7 | 22581 | 51.3 | 22282 | +318 | +16.4 | strong |
| Put | 22400 | 121474 | 113644 | 74.5 | 22624 | 64.2 | 22325 | +275 | +10.4 | strong |
| Put | 22450 | 55861 | 55603 | 92.1 | 22601 | 76.2 | 22358 | +242 | +15.9 | strong |
| Put | 22500 | 190206 | 168729 | 85.7 | 22680 | 95.0 | 22414 | +186 | -9.3 | strong |
| Put | 22550 | 39161 | 38837 | 106.0 | 22634 | 115.0 | 22444 | +156 | -9.0 | strong |
| Put | 22600 | 101779 | 94478 | 112.2 | 22716 | 137.7 | 22488 | +112 | -25.5 | strong |
| Put | 22650 | 26500 | 26129 | 126.5 | 22701 | 167.2 | 22524 | +76 | -40.8 | medium |
| Put | 22700 | 79551 | 75022 | 136.3 | 22728 | 190.2 | 22564 | +36 | -53.8 | weak |
| Put | 22750 | 22651 | 22559 | 156.3 | 22726 | 228.0 | 22594 | +6 | -71.7 | weak |
| Put | 22800 | 68148 | 62503 | 164.9 | 22774 | 262.0 | 22635 | -35 | -97.1 | weak |
| Put | 22850 | 9696 | 9518 | 182.1 | 22800 | 301.0 | 22668 | -68 | -118.9 | weak |
| Put | 22900 | 43991 | 41601 | 169.9 | 22907 | 339.9 | 22730 | -130 | -170.0 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22000; weakest call writers at -, weakest put writers at 23200. Covers 57% of near-money call OI and 50% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 1416 | 648 | 675.7 | 22608 | 650.6 | 22976 | +376 | +25.1 | strong |
| Call | 22350 | 167 | 117 | 621.9 | 22576 | 616.8 | 22972 | +372 | +5.2 | strong |
| Call | 22400 | 2902 | 1678 | 530.6 | 22464 | 583.7 | 22931 | +331 | -53.1 | strong |
| Call | 22450 | 401 | 336 | 549.7 | 22563 | 550.8 | 23000 | +400 | -1.1 | strong |
| Call | 22500 | 25964 | 15722 | 540.0 | 22597 | 517.8 | 23040 | +440 | +22.3 | strong |
| Call | 22550 | 541 | 373 | 490.9 | 22566 | 487.0 | 23041 | +441 | +3.9 | strong |
| Call | 22600 | 27890 | 19320 | 478.3 | 22625 | 461.2 | 23078 | +478 | +17.1 | strong |
| Call | 22650 | 4356 | 4060 | 456.0 | 22603 | 433.1 | 23106 | +506 | +22.9 | strong |
| Call | 22700 | 28941 | 25259 | 450.1 | 22674 | 402.4 | 23150 | +550 | +47.7 | strong |
| Call | 22750 | 1285 | 622 | 408.9 | 22612 | 378.5 | 23159 | +559 | +30.4 | strong |
| Call | 22800 | 20794 | 15679 | 399.2 | 22678 | 352.9 | 23199 | +599 | +46.3 | strong |
| Call | 22850 | 1187 | 731 | 376.0 | 22696 | 330.6 | 23226 | +626 | +45.3 | strong |
| Call | 22900 | 10150 | 7182 | 365.8 | 22719 | 306.8 | 23266 | +666 | +59.1 | strong |
| Put | 22300 | 17311 | 10364 | 233.5 | 22679 | 277.1 | 22066 | +534 | -43.6 | strong |
| Put | 22350 | 824 | 322 | 249.5 | 22680 | 286.9 | 22100 | +500 | -37.4 | strong |
| Put | 22400 | 17160 | 5106 | 267.6 | 22666 | 307.0 | 22132 | +468 | -39.4 | strong |
| Put | 22450 | 626 | 248 | 294.9 | 22628 | 321.9 | 22155 | +445 | -27.1 | strong |
| Put | 22500 | 50294 | 23259 | 282.1 | 22723 | 343.9 | 22218 | +382 | -61.8 | strong |
| Put | 22550 | 802 | 392 | 280.3 | 22769 | 369.3 | 22270 | +330 | -89.0 | strong |
| Put | 22600 | 27170 | 18146 | 350.1 | 22640 | 382.9 | 22250 | +350 | -32.9 | strong |
| Put | 22650 | 4664 | 4134 | 360.6 | 22630 | 403.4 | 22289 | +311 | -42.8 | strong |
| Put | 22700 | 29304 | 22672 | 355.1 | 22712 | 424.6 | 22345 | +255 | -69.5 | strong |
| Put | 22750 | 1134 | 713 | 343.9 | 22791 | 448.6 | 22406 | +194 | -104.6 | strong |
| Put | 22800 | 20884 | 12146 | 401.2 | 22708 | 476.4 | 22399 | +201 | -75.3 | strong |
| Put | 22850 | 1716 | 115 | 399.6 | 22763 | 496.7 | 22450 | +150 | -97.1 | strong |
| Put | 22900 | 7129 | 3389 | 417.9 | 22770 | 525.6 | 22482 | +118 | -107.8 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 9 | 78% | +0.07% | -0.44 to +0.28% |  | too few (9/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 6 | 83% | +0.35% | -0.39 to +0.91% |  | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 5 | 80% | +0.41% | -0.37 to +0.89% |  | too few (5/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 5 | 100% | +0.44% | +0.09 to +1.02% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 5 | 80% | +0.13% | -0.21 to +0.46% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% |  | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| weekly | PCR up · put writing · walls same · near put wall | 4 | 50% | -0.15% | -0.47 to +0.19% | 0% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 50% | +0.25% | -0.40 to +0.90% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 75% | +0.15% | -0.24 to +0.56% |  | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 4 | 50% | +0.08% | -0.78 to +0.90% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% |  | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 3 | 100% | +0.28% | +0.27 to +0.29% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 2 | 50% | +0.24% | -0.07 to +0.54% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.11% | +0.01 to +0.21% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 30 | 59% | -0.04% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 30 | 86% | +0.35% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · weak puts | 15 | 80% | +0.32% | up |
| intraday | weekly | writers even · few weak writers | 15 | 21% | -0.46% | down |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts | 10 | 67% | -0.04% | too few (9/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| day | monthly | writers even · few weak writers | 3 | 0% | -0.46% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 18 | 76% | +0.13% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 17 | 94% | +0.43% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 16 | 62% | -0.03% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 11 | 90% | +0.32% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 10 | 100% | +0.42% | up |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 8 | 57% | +0.20% | too few (7/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 7 | 71% | +0.00% | too few (7/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 7 | 43% | -0.11% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 7 | 14% | -0.40% | too few (7/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 6 | 80% | +0.08% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 3 | 0% | -0.20% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.92% | too few (3/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 3 | 67% | -0.18% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.27% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 0% | -0.46% | too few (2/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
