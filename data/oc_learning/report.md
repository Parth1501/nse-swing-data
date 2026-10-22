# Nifty option chain pattern log
Updated 2026-10-22 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 130 snapshots over 6 trading days
- 139 patterns logged; 88 different patterns so far

## Latest read (2026-10-22 10:45:33)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 5.2 | 22707 | 0.924 | 22850 | 22500 | 23000 | ±1.41% (22386-23027) | 15.02 |
| 2026-11-23 (monthly) | 32.2 | 22720 | 1.114 | 23000 | 22000 | 23000 | ±3.58% (21908-23532) | 14.73 |

- **Weekly, last 30 min**: `PCR down · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 17 times before; Nifty was up after it 80% of the time, average +0.24%. Too few outcomes (15/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.40%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · near call wall`. Seen 3 times before; Nifty was up after it 100% of the time, average +0.28%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 17 times before; Nifty was up after it 62% of the time, average -0.02%. Too few outcomes (16/20) to trade on.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.46%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22600; weakest call writers at 22250, weakest put writers at 23000. Covers 84% of near-money call OI and 82% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 12833 | 5462 | 424.6 | 22752 | 384.9 | 22825 | +118 | +39.8 | strong |
| Call | 22450 | 4037 | 3308 | 322.0 | 22677 | 341.3 | 22772 | +65 | -19.3 | medium |
| Call | 22500 | 45748 | 27729 | 332.1 | 22728 | 305.8 | 22832 | +126 | +26.3 | strong |
| Call | 22550 | 14373 | 13495 | 266.3 | 22697 | 270.3 | 22816 | +110 | -4.0 | strong |
| Call | 22600 | 66634 | 58328 | 216.8 | 22670 | 235.5 | 22817 | +110 | -18.7 | strong |
| Call | 22650 | 34456 | 33494 | 186.4 | 22672 | 202.8 | 22836 | +130 | -16.4 | strong |
| Call | 22700 | 106261 | 92012 | 182.1 | 22701 | 173.9 | 22882 | +176 | +8.2 | strong |
| Call | 22750 | 63032 | 59584 | 163.2 | 22717 | 149.2 | 22913 | +207 | +14.0 | strong |
| Call | 22800 | 135252 | 120681 | 166.5 | 22760 | 124.5 | 22967 | +260 | +42.0 | strong |
| Call | 22850 | 43717 | 41926 | 154.9 | 22788 | 105.5 | 23005 | +298 | +49.4 | strong |
| Call | 22900 | 122066 | 111613 | 154.2 | 22831 | 88.0 | 23054 | +348 | +66.2 | strong |
| Call | 22950 | 59036 | 57612 | 143.1 | 22857 | 72.6 | 23093 | +387 | +70.5 | strong |
| Call | 23000 | 261144 | 207234 | 132.0 | 22868 | 59.5 | 23132 | +425 | +72.5 | strong |
| Put | 22400 | 87553 | 68711 | 54.3 | 22835 | 54.4 | 22346 | +361 | -0.1 | strong |
| Put | 22450 | 36049 | 35266 | 62.0 | 22813 | 65.2 | 22388 | +318 | -3.2 | strong |
| Put | 22500 | 164488 | 114402 | 67.4 | 22872 | 76.6 | 22433 | +274 | -9.2 | strong |
| Put | 22550 | 56187 | 54425 | 92.6 | 22782 | 89.7 | 22457 | +249 | +2.9 | strong |
| Put | 22600 | 163043 | 140826 | 105.6 | 22807 | 106.0 | 22494 | +212 | -0.4 | strong |
| Put | 22650 | 54329 | 52084 | 123.9 | 22782 | 125.7 | 22526 | +180 | -1.8 | strong |
| Put | 22700 | 139551 | 115616 | 120.1 | 22860 | 147.0 | 22580 | +127 | -26.9 | strong |
| Put | 22750 | 46359 | 45480 | 138.9 | 22840 | 169.9 | 22611 | +95 | -31.1 | medium |
| Put | 22800 | 78909 | 62405 | 131.2 | 22920 | 197.7 | 22669 | +38 | -66.5 | weak |
| Put | 22850 | 15405 | 14778 | 143.3 | 22933 | 224.9 | 22707 | -0 | -81.5 | weak |
| Put | 22900 | 55720 | 51478 | 136.4 | 23000 | 255.5 | 22764 | -57 | -119.1 | weak |
| Put | 22950 | 12516 | 12405 | 145.9 | 23007 | 291.9 | 22804 | -98 | -146.1 | weak |
| Put | 23000 | 92122 | 74547 | 166.6 | 23033 | 329.4 | 22833 | -127 | -162.7 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23200. Covers 42% of near-money call OI and 38% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 1619 | 209 | 634.5 | 22697 | 663.0 | 23034 | +315 | -28.6 | strong |
| Call | 22450 | 210 | 131 | 611.8 | 22712 | 623.5 | 23062 | +342 | -11.7 | strong |
| Call | 22500 | 17129 | 6058 | 595.2 | 22718 | 586.0 | 23095 | +375 | +9.2 | strong |
| Call | 22550 | 469 | 235 | 545.9 | 22695 | 576.2 | 23096 | +376 | -30.3 | strong |
| Call | 22600 | 23429 | 14630 | 490.7 | 22665 | 525.4 | 23091 | +371 | -34.6 | strong |
| Call | 22650 | 2030 | 1705 | 461.7 | 22673 | 494.1 | 23112 | +392 | -32.3 | strong |
| Call | 22700 | 23872 | 19855 | 461.4 | 22710 | 462.1 | 23161 | +442 | -0.7 | strong |
| Call | 22750 | 1129 | 356 | 447.6 | 22711 | 432.9 | 23198 | +478 | +14.7 | strong |
| Call | 22800 | 16449 | 10802 | 407.1 | 22708 | 407.9 | 23207 | +487 | -0.8 | strong |
| Call | 22850 | 1275 | 743 | 378.9 | 22711 | 378.7 | 23229 | +509 | +0.2 | strong |
| Call | 22900 | 10548 | 7210 | 370.4 | 22731 | 354.1 | 23270 | +551 | +16.3 | strong |
| Call | 22950 | 1307 | 355 | 368.3 | 22770 | 332.1 | 23318 | +598 | +36.2 | strong |
| Call | 23000 | 74369 | 22089 | 355.1 | 22809 | 307.9 | 23355 | +635 | +47.2 | strong |
| Call | 23050 | 1534 | 91 | 309.5 | 22764 | 281.3 | 23360 | +640 | +28.2 | strong |
| Put | 22400 | 13737 | 1395 | 244.4 | 22750 | 246.2 | 22156 | +564 | -1.8 | strong |
| Put | 22450 | 581 | 108 | 261.9 | 22729 | 255.9 | 22188 | +532 | +6.0 | strong |
| Put | 22500 | 39546 | 12157 | 240.5 | 22852 | 276.3 | 22259 | +460 | -35.8 | strong |
| Put | 22550 | 758 | 258 | 218.3 | 22950 | 291.9 | 22332 | +388 | -73.5 | strong |
| Put | 22600 | 23715 | 14354 | 338.4 | 22672 | 311.6 | 22262 | +458 | +26.8 | strong |
| Put | 22650 | 2402 | 1813 | 333.7 | 22731 | 325.8 | 22316 | +403 | +7.9 | strong |
| Put | 22700 | 25765 | 18597 | 348.3 | 22726 | 350.1 | 22352 | +368 | -1.9 | strong |
| Put | 22750 | 1076 | 531 | 302.9 | 22891 | 369.5 | 22447 | +273 | -66.6 | strong |
| Put | 22800 | 19415 | 9446 | 392.1 | 22728 | 392.4 | 22408 | +312 | -0.3 | strong |
| Put | 22850 | 2440 | 125 | 395.4 | 22776 | 412.1 | 22455 | +265 | -16.7 | strong |
| Put | 22900 | 6980 | 2980 | 403.0 | 22802 | 438.8 | 22497 | +223 | -35.8 | strong |
| Put | 22950 | 631 | 127 | 375.7 | 22878 | 458.9 | 22574 | +146 | -83.2 | strong |
| Put | 23000 | 61853 | 20151 | 424.1 | 22853 | 491.4 | 22576 | +144 | -67.3 | strong |
| Put | 23050 | 532 | 113 | 340.9 | 23048 | 511.4 | 22709 | +11 | -170.4 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 4 | 50% | +0.09% | -0.74 to +0.62% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 4 | 75% | +0.08% | -0.21 to +0.24% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 4 | 100% | +0.28% | +0.22 to +0.32% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.14% | +0.11 to +0.16% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.46% | -0.46 to -0.46% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · few weak writers | 18 | 62% | -0.02% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 18 | 80% | +0.24% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 10 | 44% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · few weak writers | 10 | 10% | -0.56% | down |
| intraday | monthly | writers even · weak puts | 6 | 50% | +0.18% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak puts | 4 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 100% | +0.39% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 3 | 0% | -0.40% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.46% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
