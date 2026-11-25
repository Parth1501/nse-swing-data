# Nifty option chain pattern log
Updated 2026-11-25 11:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 679 snapshots over 28 trading days
- 754 patterns logged; 193 different patterns so far

## Latest read (2026-11-25 11:45:02)

Nifty trend: weekly **sideways**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-01 (weekly) | 6.2 | 25948 | 0.92 | 25800 | 25500 | 26000 | ±1.86% (25466-26429) | 18.27 |
| 2026-12-29 (monthly) | 34.2 | 25946 | 0.875 | 25500 | 25000 | 27000 | ±3.73% (24978-26914) | 15.24 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls down · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.34%. Too few outcomes (1/20) to trade on.
  - Writers: `put writers stronger · few weak writers`. Seen 39 times before; Nifty was up after it 94% of the time, average +0.45%. History points to a bull call debit spread, ATM to about the call wall 26000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 7 times before; Nifty was up after it 100% of the time, average +0.83%. Too few outcomes (7/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `put writers stronger · few weak writers`. Seen 3 times before; Nifty was up after it 100% of the time, average +0.95%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put writing · walls same · mid walls`. Seen 19 times before; Nifty was up after it 83% of the time, average +0.37%. Too few outcomes (18/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 102 times before; Nifty was up after it 74% of the time, average +0.15%. History points to a bull call debit spread, ATM to about the call wall 27000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 40 times before; Nifty was up after it 47% of the time, average -0.02%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR down · put writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.65%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 7 times before; Nifty was up after it 71% of the time, average +0.52%. Too few outcomes (7/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Nifty was up after it 50% of the time, average -0.22%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-12-01

Strongest call writers at 25900, strongest put writers at 25700; weakest call writers at 25700, weakest put writers at 26600. Covers 40% of near-money call OI and 69% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25650 | 8835 | 851 | 306.3 | 25758 | 464.1 | 25956 | +9 | -157.8 | weak |
| Call | 25700 | 53066 | 22256 | 278.5 | 25756 | 427.0 | 25978 | +31 | -148.5 | weak |
| Call | 25750 | 27948 | 22222 | 250.9 | 25757 | 392.9 | 26001 | +53 | -142.0 | weak |
| Call | 25800 | 79788 | 33559 | 225.1 | 25757 | 359.3 | 26025 | +78 | -134.2 | medium |
| Call | 25850 | 33187 | 24756 | 214.7 | 25780 | 328.7 | 26065 | +117 | -114.0 | strong |
| Call | 25900 | 62386 | 30172 | 217.4 | 25818 | 298.6 | 26117 | +170 | -81.2 | strong |
| Call | 25950 | 42722 | 30054 | 230.8 | 25879 | 270.9 | 26181 | +233 | -40.1 | strong |
| Call | 26000 | 141102 | 27712 | 168.6 | 25808 | 243.7 | 26169 | +221 | -75.0 | strong |
| Call | 26050 | 23918 | 16840 | 161.9 | 25834 | 219.1 | 26212 | +264 | -57.1 | strong |
| Call | 26100 | 49180 | 14379 | 155.6 | 25860 | 195.6 | 26256 | +308 | -39.9 | strong |
| Call | 26150 | 22868 | 15079 | 115.1 | 25805 | 174.1 | 26265 | +318 | -59.0 | strong |
| Call | 26200 | 80360 | 26772 | 98.4 | 25801 | 154.3 | 26298 | +351 | -56.0 | strong |
| Call | 26250 | 19859 | 8584 | 78.3 | 25783 | 136.0 | 26328 | +381 | -57.7 | strong |
| Call | 26300 | 52923 | 18015 | 80.3 | 25819 | 119.7 | 26380 | +433 | -39.4 | strong |
| Put | 25600 | 69014 | 44517 | 138.9 | 25789 | 93.8 | 25461 | +486 | +45.1 | strong |
| Put | 25650 | 33290 | 29536 | 162.6 | 25772 | 106.3 | 25487 | +460 | +56.3 | strong |
| Put | 25700 | 122039 | 100717 | 183.8 | 25772 | 120.2 | 25516 | +431 | +63.7 | strong |
| Put | 25750 | 64876 | 61397 | 208.3 | 25765 | 134.9 | 25542 | +406 | +73.4 | strong |
| Put | 25800 | 113656 | 89014 | 211.7 | 25807 | 151.9 | 25588 | +359 | +59.8 | strong |
| Put | 25850 | 41182 | 39434 | 208.6 | 25863 | 169.8 | 25641 | +306 | +38.8 | strong |
| Put | 25900 | 62336 | 55479 | 222.7 | 25883 | 190.0 | 25677 | +270 | +32.7 | strong |
| Put | 25950 | 18054 | 17388 | 233.4 | 25907 | 210.9 | 25717 | +231 | +22.5 | strong |
| Put | 26000 | 57490 | 33981 | 276.7 | 25877 | 234.5 | 25723 | +224 | +42.2 | strong |
| Put | 26050 | 4562 | 4237 | 287.5 | 25903 | 259.2 | 25762 | +185 | +28.3 | strong |
| Put | 26100 | 8197 | 6307 | 338.5 | 25872 | 286.3 | 25762 | +186 | +52.2 | strong |
| Put | 26150 | 2300 | 1855 | 336.1 | 25918 | 314.8 | 25814 | +134 | +21.3 | strong |
| Put | 26200 | 8875 | 2949 | 374.7 | 25907 | 344.8 | 25825 | +122 | +29.9 | strong |
| Put | 26250 | 774 | 672 | 433.0 | 25879 | 377.9 | 25817 | +131 | +55.1 | strong |
| Put | 26300 | 13151 | 640 | 445.4 | 25902 | 411.0 | 25855 | +93 | +34.4 | medium |

## Strong vs weak writers, monthly 2026-12-29

Strongest call writers at 26000, strongest put writers at 25500; weakest call writers at 25500, weakest put writers at -. Covers 55% of near-money call OI and 56% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25600 | 16748 | 13660 | 486.1 | 25500 | 787.8 | 26086 | +140 | -301.7 | strong |
| Call | 25650 | 795 | 505 | 448.9 | 25468 | 747.4 | 26099 | +153 | -298.5 | strong |
| Call | 25700 | 15609 | 13198 | 483.5 | 25591 | 721.9 | 26184 | +237 | -238.3 | strong |
| Call | 25750 | 1633 | 1452 | 476.7 | 25622 | 682.0 | 26227 | +280 | -205.3 | strong |
| Call | 25800 | 24873 | 22311 | 395.1 | 25509 | 655.2 | 26195 | +249 | -260.1 | strong |
| Call | 25850 | 1095 | 972 | 443.5 | 25656 | 625.1 | 26294 | +347 | -181.6 | strong |
| Call | 25900 | 9166 | 7918 | 441.8 | 25693 | 594.8 | 26342 | +395 | -153.0 | strong |
| Call | 25950 | 727 | 597 | 421.4 | 25704 | 566.2 | 26371 | +425 | -144.8 | strong |
| Call | 26000 | 89035 | 31059 | 302.5 | 25481 | 533.5 | 26302 | +356 | -231.0 | strong |
| Call | 26050 | 628 | 462 | 315.5 | 25572 | 507.2 | 26365 | +419 | -191.7 | strong |
| Call | 26100 | 7746 | 5829 | 282.8 | 25518 | 478.0 | 26383 | +436 | -195.2 | strong |
| Call | 26150 | 523 | 309 | 272.8 | 25544 | 452.4 | 26423 | +476 | -179.7 | strong |
| Call | 26200 | 7646 | 3828 | 253.6 | 25545 | 427.4 | 26454 | +507 | -173.8 | strong |
| Call | 26250 | 707 | 476 | 223.3 | 25516 | 405.4 | 26473 | +527 | -182.2 | strong |
| Call | 26300 | 7129 | 4622 | 179.9 | 25420 | 381.2 | 26480 | +534 | -201.3 | strong |
| Put | 25600 | 21833 | 18430 | 439.0 | 25552 | 276.5 | 25161 | +785 | +162.5 | strong |
| Put | 25650 | 879 | 820 | 440.5 | 25587 | 293.0 | 25209 | +737 | +147.5 | strong |
| Put | 25700 | 15116 | 14459 | 438.2 | 25642 | 307.9 | 25262 | +685 | +130.2 | strong |
| Put | 25750 | 5672 | 5521 | 415.9 | 25738 | 326.6 | 25334 | +612 | +89.3 | strong |
| Put | 25800 | 17817 | 17089 | 476.3 | 25669 | 342.4 | 25324 | +623 | +134.0 | strong |
| Put | 25850 | 658 | 606 | 430.2 | 25775 | 361.9 | 25420 | +527 | +68.3 | strong |
| Put | 25900 | 7233 | 6963 | 471.6 | 25773 | 380.6 | 25428 | +518 | +90.9 | strong |
| Put | 25950 | 417 | 368 | 478.8 | 25791 | 401.9 | 25471 | +475 | +76.9 | strong |
| Put | 26000 | 67575 | 18288 | 557.9 | 25680 | 419.8 | 25442 | +504 | +138.1 | strong |
| Put | 26050 | 256 | 175 | 567.0 | 25719 | 444.3 | 25483 | +463 | +122.7 | strong |
| Put | 26100 | 4189 | 3823 | 651.0 | 25611 | 465.2 | 25449 | +497 | +185.8 | strong |
| Put | 26150 | 254 | 223 | 683.6 | 25610 | 491.3 | 25466 | +480 | +192.3 | strong |
| Put | 26200 | 1726 | 1484 | 681.4 | 25659 | 513.0 | 25519 | +428 | +168.5 | strong |
| Put | 26250 | 170 | 131 | 746.2 | 25623 | 547.8 | 25504 | +443 | +198.5 | strong |
| Put | 26300 | 1123 | 909 | 736.2 | 25672 | 564.1 | 25564 | +383 | +172.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 39 | 68% | +0.26% | -0.44 to +0.97% | 50% of 2 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 22 | 86% | +0.39% | -0.50 to +1.68% | 0% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 21 | 86% | +0.27% | -0.27 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 20 | 83% | +0.37% | -0.42 to +1.02% | 50% of 2 | up |
| weekly | PCR down · call writing · walls same · near put wall | 20 | 60% | +0.13% | -1.00 to +0.85% | 60% of 5 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 18 | 56% | +0.06% | -0.61 to +0.80% | 60% of 5 | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near put wall | 16 | 79% | +0.15% | -0.28 to +0.90% | 0% of 1 | up |
| monthly | PCR flat · put and call writing · walls same · near call wall | 16 | 56% | +0.28% | -0.71 to +1.70% | 50% of 2 | no clear direction |
| monthly | PCR flat · put writing · walls same · near call wall | 13 | 73% | +0.36% | -0.50 to +1.56% | 0% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · mid walls | 13 | 69% | +0.19% | -0.57 to +0.89% | 75% of 4 | no clear direction |
| weekly | PCR down · unwinding · walls same · mid walls | 12 | 62% | +0.04% | -0.40 to +0.90% | 80% of 5 | too few (8/10) |
| weekly | PCR down · call writing · walls same · mid walls | 11 | 82% | +0.21% | -0.43 to +0.75% | 40% of 5 | up |
| monthly | PCR up · put writing · walls same · near call wall | 11 | 50% | +0.18% | -0.40 to +0.93% | 50% of 2 | no clear direction |
| weekly | PCR down · unwinding · walls same · near call wall | 11 | 70% | +0.39% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| monthly | PCR up · put and call writing · walls same · mid walls | 11 | 73% | +0.15% | -0.24 to +0.63% | 50% of 2 | no clear direction |
| monthly | PCR flat · put writing · walls same · near put wall | 10 | 75% | +0.13% | -0.83 to +0.98% | 0% of 1 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 10 | 80% | +0.28% | -0.21 to +1.13% | 50% of 2 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · mid walls | 10 | 57% | +0.11% | -0.16 to +0.71% | 50% of 2 | too few (7/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 10 | 40% | +0.03% | -0.78 to +0.90% | 100% of 2 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 10 | 60% | +0.01% | -1.01 to +1.12% | 100% of 1 | no clear direction |
| monthly | PCR up · quiet OI · walls same · mid walls | 10 | 80% | +0.24% | -0.39 to +0.91% | 50% of 2 | no clear direction |
| weekly | PCR up · put and call writing · walls same · near put wall | 9 | 78% | +0.31% | -1.22 to +1.24% | 67% of 3 | too few (9/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% | 0% of 1 | too few (7/10) |
| weekly | PCR down · call writing · walls down · mid walls | 9 | 78% | +0.24% | -0.07 to +0.54% | 67% of 3 | too few (9/10) |
| weekly | PCR up · put writing · walls up · near put wall | 8 | 62% | +0.33% | -0.13 to +1.65% | 0% of 4 | too few (8/10) |
| monthly | PCR up · put writing · walls same · mid walls | 8 | 75% | +0.42% | -0.29 to +0.85% | 50% of 2 | too few (8/10) |
| weekly | PCR up · put writing · walls up · mid walls | 8 | 62% | +0.31% | -0.26 to +1.40% | 33% of 3 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% | 0% of 1 | too few (6/10) |
| monthly | PCR down · call writing · walls same · mid walls | 8 | 38% | +0.01% | -0.47 to +0.49% | 50% of 2 | too few (8/10) |
| monthly | PCR down · call writing · walls same · near call wall | 8 | 83% | +0.27% | -0.78 to +1.18% | 50% of 2 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 7 | 86% | +0.50% | -0.37 to +1.25% | 50% of 2 | too few (7/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 7 | 43% | +0.02% | -0.89 to +0.90% | 67% of 3 | too few (7/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.02% | -0.74 to +0.62% | 50% of 2 | too few (7/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 7 | 86% | +0.29% | -0.11 to +0.62% | 50% of 4 | too few (7/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 7 | 71% | +0.60% | -1.02 to +1.82% | 50% of 4 | too few (7/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 7 | 83% | +0.23% | -0.05 to +0.63% | 67% of 3 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 6 | 20% | +0.00% | -0.29 to +0.43% | 33% of 3 | too few (5/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 50% of 2 | too few (5/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 6 | 67% | -0.08% | -1.07 to +0.28% | 100% of 1 | too few (6/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 6 | 100% | +0.54% | +0.47 to +0.61% | 67% of 3 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near call wall | 6 | 83% | +0.53% | -0.06 to +1.68% | 67% of 3 | too few (6/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 5 | 80% | +0.26% | -0.02 to +0.90% | 33% of 3 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 5 | 80% | +0.46% | -1.11 to +1.69% | 0% of 2 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 50% of 2 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near put wall | 5 | 60% | +0.09% | -0.51 to +0.73% | 0% of 2 | too few (5/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 5 | 40% | +0.06% | -0.68 to +0.75% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 5 | 100% | +0.19% | +0.16 to +0.25% | 67% of 3 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 5 | 60% | +0.15% | -0.07 to +0.33% | 100% of 1 | too few (5/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 5 | 80% | +0.21% | -0.22 to +0.68% | 60% of 5 | too few (5/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 5 | 100% | +0.29% | +0.04 to +0.59% | 0% of 4 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near call wall | 5 | 80% | +0.53% | -0.02 to +0.91% | 33% of 3 | too few (5/10) |
| monthly | PCR flat · quiet OI · walls up · near put wall | 4 | 0% | -0.25% | -0.61 to -0.05% | 100% of 1 | too few (3/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 4 | 100% | +0.28% | +0.06 to +0.74% | 100% of 1 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 50% of 2 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 4 | 25% | -0.02% | -0.69 to +0.99% | 50% of 2 | too few (4/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 4 | 100% | +0.50% | +0.37 to +0.62% | 0% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 4 | 100% | +0.61% | +0.01 to +1.22% | 67% of 3 | too few (2/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 100% | +0.79% | +0.14 to +1.65% | 0% of 1 | too few (4/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 4 | 100% | +0.51% | +0.13 to +1.17% | 50% of 2 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 4 |  |  |  | 100% of 4 | too few (0/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 4 | 50% | +0.06% | -0.63 to +0.58% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 3 | 100% | +0.12% | +0.05 to +0.16% | 100% of 2 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 3 | 67% | +0.38% | -0.18 to +0.91% | 50% of 2 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 3 | 100% | +0.24% | +0.04 to +0.42% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 3 | 50% | -0.03% | -0.43 to +0.37% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 3 | 67% | +0.08% | -0.04 to +0.18% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 3 | 50% | -0.15% | -0.33 to +0.03% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 3 | 100% | +0.28% | +0.07 to +0.50% | 100% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 3 | 67% | -0.03% | -0.44 to +0.19% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 3 | 33% | -0.01% | -0.37 to +0.53% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 2 | 50% | -0.57% | -1.32 to +0.18% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls same · near put wall | 2 | 0% | -0.07% | -0.07 to -0.07% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 2 | 50% | +0.18% | -0.20 to +0.57% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls same · mid walls | 2 | 100% | +0.30% | +0.29 to +0.31% | 100% of 2 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 2 | 100% | +0.20% | +0.20 to +0.20% | 100% of 2 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 50% of 2 | too few (2/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 2 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 50% of 2 | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · mid walls | 2 | 50% | +0.04% | -0.19 to +0.28% | 100% of 2 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near put wall | 2 | 50% | -0.45% | -1.22 to +0.31% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near put wall | 2 | 100% | +0.21% | +0.18 to +0.24% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 2 | 50% | -0.10% | -0.29 to +0.09% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.20% | -0.20 to -0.20% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls up · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.14% | +1.14 to +1.14% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near put wall | 1 | 0% | -0.44% | -0.44 to -0.44% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls down · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near call wall | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.40% | +0.40 to +0.40% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% | 0% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +1.86% | +1.86 to +1.86% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -1.33% | -1.33 to -1.33% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls same · mid walls | 1 | 100% | +0.49% | +0.49 to +0.49% | 100% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% | 0% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · near put wall | 1 | 100% | +1.02% | +1.02 to +1.02% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near put wall | 1 | 0% | -0.29% | -0.29 to -0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near put wall | 1 | 0% | -0.83% | -0.83 to -0.83% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · mid walls | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 50% of 2 | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | +0.30% | -0.61 to +1.12% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | +0.73% | -0.39 to +2.40% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 100% | +0.61% | +0.06 to +1.12% | 100% of 3 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.53% | -0.63 to +1.68% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 100% | +0.55% | +0.51 to +0.58% | 50% of 2 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 2 | 50% | +0.02% | -0.63 to +0.68% | 0% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 2 | 0% | -1.15% | -1.75 to -0.54% | 100% of 2 | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -1.75% | -1.75 to -1.75% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 | 100% | +2.35% | +2.35 to +2.35% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.58% | +0.58 to +0.58% | 100% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +2.35% | +2.35 to +2.35% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.84% | +0.84 to +0.84% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.38% | +0.38 to +0.38% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +1.14% | +1.14 to +1.14% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 164 | 67% | +0.18% | up |
| intraday | weekly | writers even · few weak writers | 118 | 56% | +0.07% | no clear direction |
| intraday | monthly | writers even · weak calls | 103 | 74% | +0.15% | up |
| intraday | weekly | put writers stronger · weak calls | 79 | 76% | +0.32% | up |
| intraday | monthly | put writers stronger · weak calls | 63 | 85% | +0.57% | up |
| intraday | weekly | call writers stronger · weak puts | 43 | 80% | +0.33% | up |
| intraday | weekly | put writers stronger · few weak writers | 40 | 94% | +0.45% | up |
| intraday | weekly | call writers stronger · few weak writers | 36 | 74% | +0.17% | up |
| intraday | weekly | writers even · weak calls | 27 | 80% | +0.38% | up |
| intraday | monthly | writers even · weak puts | 21 | 80% | +0.42% | up |
| intraday | weekly | writers even · weak puts | 21 | 78% | +0.24% | up |
| intraday | monthly | call writers stronger · few weak writers | 15 | 62% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak on both sides | 11 | 73% | +0.20% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 7 | 29% | -0.51% | too few (7/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | weekly | put writers stronger · weak on both sides | 1 | 0% | -0.29% | too few (1/10) |
| day | monthly | writers even · few weak writers | 13 | 54% | +0.23% | no clear direction |
| day | monthly | writers even · weak calls | 8 | 71% | +0.52% | too few (7/10) |
| day | weekly | put writers stronger · weak calls | 7 | 71% | +0.20% | too few (7/10) |
| day | weekly | writers even · few weak writers | 7 | 71% | +0.65% | too few (7/10) |
| day | monthly | put writers stronger · weak calls | 4 | 100% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · few weak writers | 4 | 100% | +0.95% | too few (3/10) |
| day | weekly | call writers stronger · weak puts | 3 | 33% | +0.49% | too few (3/10) |
| day | weekly | writers even · weak puts | 3 | 33% | -0.06% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 2 | 100% | +0.92% | too few (2/10) |
| day | weekly | writers even · weak calls | 2 | 50% | +1.00% | too few (2/10) |
| day | monthly | writers even · weak puts | 1 | 100% | +2.35% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 57 | 78% | +0.39% | up |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 49 | 85% | +0.68% | up |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 47 | 63% | +0.14% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 45 | 93% | +0.31% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 43 | 46% | -0.06% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m up | 41 | 47% | -0.02% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 28 | 77% | +0.29% | up |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 23 | 64% | +0.34% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 23 | 67% | +0.27% | no clear direction |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 22 | 72% | +0.11% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m sideways | 17 | 88% | +0.14% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 14 | 83% | +0.16% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.73% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 9 | 50% | -0.12% | too few (8/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 9 | 67% | +0.03% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 8 | 100% | +0.19% | too few (8/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly sideways · 125m up | 8 | 100% | +0.83% | too few (7/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 6 | 20% | -0.14% | too few (5/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 5 | 100% | +0.53% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 5 | 40% | +0.00% | too few (5/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 4 | 100% | +0.51% | too few (4/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 2 | 0% | -0.07% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 0% | -0.89% | too few (1/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.02% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 1 | 0% | -1.33% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | put writers stronger · weak on both sides · weekly sideways · 125m up | 1 | 0% | -0.29% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m up | 1 | 100% | +0.91% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 50% | -0.22% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 4 | 75% | +0.07% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m up | 3 | 50% | -0.22% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +1.32% | too few (2/10) |
| day | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +0.86% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.12% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 | 100% | +1.14% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.58% | too few (1/10) |
| day | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 100% | +2.35% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.18% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 1 | 100% | +2.35% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m up | 1 | 100% | +2.01% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.22% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 0% | -0.63% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
