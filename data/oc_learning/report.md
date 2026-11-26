# Nifty option chain pattern log
Updated 2026-11-26 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 707 snapshots over 29 trading days
- 784 patterns logged; 194 different patterns so far

## Latest read (2026-11-26 12:48:38)

Nifty trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-01 (weekly) | 5.1 | 25908 | 0.938 | 25800 | 25000 | 26000 | ±1.5% (25520-26295) | 15.96 |
| 2026-12-29 (monthly) | 33.1 | 25908 | 0.891 | 25500 | 25000 | 27000 | ±3.55% (24988-26827) | 14.7 |

- **Weekly, last 30 min**: `PCR flat · put and call writing · walls same · near call wall`. Seen 5 times before; Nifty was up after it 80% of the time, average +0.46%. Too few outcomes (5/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 130 times before; Nifty was up after it 59% of the time, average +0.09%. History points to a bull call debit spread, ATM to about the call wall 26000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 55 times before; Nifty was up after it 56% of the time, average +0.01%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 8 times before; Nifty was up after it 75% of the time, average +0.61%. Too few outcomes (8/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Nifty was up after it 67% of the time, average +0.04%. Too few outcomes (3/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls same · mid walls`. Seen 45 times before; Nifty was up after it 67% of the time, average +0.24%. History points to a bull call debit spread, ATM to about the call wall 27000.
  - Writers: `writers even · few weak writers`. Seen 178 times before; Nifty was up after it 66% of the time, average +0.17%. History points to a bull call debit spread, ATM to about the call wall 27000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 61 times before; Nifty was up after it 66% of the time, average +0.15%. History points to a bull call debit spread, ATM to about the call wall 27000.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · mid walls`. Seen 3 times before; Nifty was up after it 33% of the time, average +0.16%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 14 times before; Nifty was up after it 57% of the time, average +0.24%. Too few outcomes (14/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 5 times before; Nifty was up after it 60% of the time, average -0.11%. Too few outcomes (5/20) to trade on.

## Strong vs weak writers, weekly 2026-12-01

Strongest call writers at 26000, strongest put writers at 25800; weakest call writers at 25700, weakest put writers at 26600. Covers 61% of near-money call OI and 83% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25550 | 5227 | 1683 | 316.1 | 25677 | 445.6 | 25866 | -42 | -129.6 | weak |
| Call | 25600 | 20320 | 4663 | 308.2 | 25724 | 409.1 | 25908 | +0 | -100.9 | weak |
| Call | 25650 | 7776 | 4977 | 270.4 | 25713 | 368.4 | 25920 | +13 | -98.0 | weak |
| Call | 25700 | 29826 | 19157 | 257.7 | 25719 | 335.9 | 25958 | +50 | -78.3 | weak |
| Call | 25750 | 18812 | 17339 | 233.3 | 25738 | 301.2 | 25983 | +76 | -68.0 | medium |
| Call | 25800 | 70211 | 52734 | 197.6 | 25738 | 269.9 | 25998 | +90 | -72.4 | medium |
| Call | 25850 | 33542 | 30955 | 184.7 | 25776 | 240.3 | 26035 | +127 | -55.6 | strong |
| Call | 25900 | 100382 | 79671 | 179.9 | 25799 | 212.0 | 26080 | +172 | -32.1 | strong |
| Call | 25950 | 61408 | 55372 | 186.2 | 25857 | 186.1 | 26136 | +229 | +0.1 | strong |
| Call | 26000 | 164899 | 81997 | 137.3 | 25772 | 162.7 | 26137 | +230 | -25.3 | strong |
| Call | 26050 | 31462 | 27021 | 133.1 | 25815 | 141.2 | 26183 | +275 | -8.1 | strong |
| Call | 26100 | 61053 | 38978 | 108.7 | 25798 | 121.2 | 26209 | +301 | -12.5 | strong |
| Call | 26150 | 28206 | 23635 | 101.6 | 25803 | 103.8 | 26252 | +344 | -2.2 | strong |
| Call | 26200 | 91442 | 58486 | 79.2 | 25748 | 88.7 | 26279 | +371 | -9.5 | strong |
| Call | 26250 | 37247 | 27875 | 68.8 | 25752 | 74.8 | 26319 | +411 | -6.0 | strong |
| Put | 25550 | 25395 | 22997 | 110.2 | 25803 | 62.7 | 25440 | +468 | +47.5 | strong |
| Put | 25600 | 115822 | 100661 | 104.8 | 25867 | 73.0 | 25495 | +413 | +31.8 | strong |
| Put | 25650 | 37401 | 35950 | 153.7 | 25783 | 85.5 | 25496 | +411 | +68.1 | strong |
| Put | 25700 | 97786 | 87268 | 170.6 | 25790 | 99.7 | 25529 | +378 | +70.9 | strong |
| Put | 25750 | 46930 | 45934 | 201.1 | 25766 | 115.5 | 25549 | +359 | +85.6 | strong |
| Put | 25800 | 113172 | 102092 | 218.0 | 25784 | 133.6 | 25582 | +326 | +84.4 | strong |
| Put | 25850 | 48242 | 47826 | 219.7 | 25826 | 153.0 | 25630 | +277 | +66.7 | strong |
| Put | 25900 | 91941 | 89299 | 233.0 | 25848 | 175.6 | 25667 | +241 | +57.4 | strong |
| Put | 25950 | 41215 | 41012 | 210.8 | 25912 | 199.3 | 25739 | +169 | +11.5 | strong |
| Put | 26000 | 63588 | 49444 | 270.0 | 25875 | 225.4 | 25730 | +178 | +44.5 | strong |
| Put | 26050 | 6697 | 6552 | 276.6 | 25902 | 254.0 | 25773 | +134 | +22.6 | strong |
| Put | 26100 | 10083 | 8891 | 321.3 | 25885 | 284.3 | 25779 | +129 | +37.0 | strong |
| Put | 26150 | 2128 | 1927 | 342.8 | 25901 | 316.2 | 25807 | +100 | +26.6 | medium |
| Put | 26200 | 8026 | 4485 | 390.0 | 25881 | 352.2 | 25810 | +98 | +37.8 | medium |
| Put | 26250 | 1561 | 1463 | 452.1 | 25851 | 391.1 | 25798 | +110 | +61.0 | medium |

## Strong vs weak writers, monthly 2026-12-29

Strongest call writers at 26000, strongest put writers at 25500; weakest call writers at 25400, weakest put writers at -. Covers 58% of near-money call OI and 60% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25550 | 807 | 610 | 463.9 | 25404 | 753.4 | 26014 | +106 | -289.4 | medium |
| Call | 25600 | 15340 | 12605 | 494.3 | 25514 | 715.4 | 26094 | +187 | -221.1 | strong |
| Call | 25650 | 776 | 520 | 466.0 | 25502 | 677.8 | 26116 | +209 | -211.8 | strong |
| Call | 25700 | 14564 | 12420 | 488.2 | 25599 | 652.0 | 26188 | +281 | -163.7 | strong |
| Call | 25750 | 1581 | 1427 | 486.9 | 25641 | 614.4 | 26237 | +329 | -127.5 | strong |
| Call | 25800 | 24628 | 22257 | 402.7 | 25526 | 589.2 | 26203 | +295 | -186.5 | strong |
| Call | 25850 | 1225 | 1124 | 457.5 | 25698 | 558.0 | 26307 | +400 | -100.5 | strong |
| Call | 25900 | 12917 | 11741 | 450.8 | 25723 | 530.5 | 26351 | +443 | -79.6 | strong |
| Call | 25950 | 1883 | 1767 | 458.4 | 25783 | 503.8 | 26408 | +501 | -45.4 | strong |
| Call | 26000 | 92653 | 37496 | 326.1 | 25543 | 474.5 | 26326 | +419 | -148.4 | strong |
| Call | 26050 | 816 | 656 | 352.8 | 25661 | 446.9 | 26403 | +495 | -94.1 | strong |
| Call | 26100 | 8095 | 6257 | 294.3 | 25550 | 423.6 | 26394 | +487 | -129.3 | strong |
| Call | 26150 | 529 | 335 | 289.8 | 25590 | 401.0 | 26440 | +532 | -111.2 | strong |
| Call | 26200 | 7995 | 4594 | 279.2 | 25615 | 373.7 | 26479 | +572 | -94.5 | strong |
| Call | 26250 | 1142 | 922 | 270.4 | 25634 | 356.9 | 26520 | +613 | -86.5 | strong |
| Put | 25550 | 931 | 765 | 429.4 | 25503 | 263.0 | 25121 | +787 | +166.4 | strong |
| Put | 25600 | 20261 | 17227 | 433.1 | 25566 | 279.8 | 25167 | +741 | +153.3 | strong |
| Put | 25650 | 950 | 894 | 426.6 | 25619 | 290.9 | 25223 | +684 | +135.7 | strong |
| Put | 25700 | 15113 | 14505 | 432.9 | 25652 | 312.6 | 25267 | +640 | +120.2 | strong |
| Put | 25750 | 5501 | 5363 | 413.8 | 25743 | 329.0 | 25336 | +571 | +84.8 | strong |
| Put | 25800 | 18533 | 17854 | 466.9 | 25687 | 348.0 | 25333 | +574 | +118.9 | strong |
| Put | 25850 | 1122 | 1097 | 451.5 | 25754 | 369.4 | 25398 | +509 | +82.1 | strong |
| Put | 25900 | 11321 | 11054 | 460.1 | 25792 | 388.9 | 25440 | +468 | +71.2 | strong |
| Put | 25950 | 625 | 587 | 467.1 | 25822 | 410.0 | 25483 | +425 | +57.0 | strong |
| Put | 26000 | 74141 | 25326 | 540.3 | 25718 | 430.8 | 25460 | +448 | +109.6 | strong |
| Put | 26050 | 446 | 372 | 524.9 | 25802 | 458.1 | 25525 | +382 | +66.8 | strong |
| Put | 26100 | 4484 | 4135 | 633.7 | 25644 | 481.4 | 25466 | +441 | +152.4 | strong |
| Put | 26150 | 235 | 209 | 668.3 | 25636 | 502.5 | 25482 | +426 | +165.8 | strong |
| Put | 26200 | 2699 | 2461 | 629.5 | 25752 | 534.1 | 25571 | +337 | +95.3 | strong |
| Put | 26250 | 216 | 180 | 706.5 | 25684 | 562.2 | 25544 | +364 | +144.2 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 46 | 67% | +0.24% | -0.44 to +0.97% | 50% of 2 | up |
| weekly | PCR up · put writing · walls same · near call wall | 23 | 78% | +0.24% | -0.36 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 22 | 86% | +0.39% | -0.50 to +1.68% | 0% of 1 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 20 | 79% | +0.33% | -0.49 to +1.02% | 50% of 2 | up |
| weekly | PCR down · call writing · walls same · near put wall | 20 | 60% | +0.13% | -1.00 to +0.85% | 60% of 5 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 18 | 56% | +0.06% | -0.61 to +0.80% | 60% of 5 | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near put wall | 16 | 79% | +0.12% | -0.28 to +0.90% | 0% of 1 | up |
| monthly | PCR flat · put and call writing · walls same · near call wall | 16 | 56% | +0.28% | -0.71 to +1.70% | 50% of 2 | no clear direction |
| monthly | PCR flat · put writing · walls same · near call wall | 13 | 73% | +0.36% | -0.50 to +1.56% | 0% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · mid walls | 13 | 62% | +0.16% | -0.57 to +0.89% | 75% of 4 | no clear direction |
| weekly | PCR down · unwinding · walls same · mid walls | 13 | 67% | +0.06% | -0.40 to +0.90% | 80% of 5 | too few (9/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 12 | 75% | +0.19% | -0.24 to +0.63% | 50% of 2 | no clear direction |
| monthly | PCR down · quiet OI · walls same · mid walls | 12 | 80% | +0.26% | -0.10 to +0.70% | 0% of 1 | no clear direction |
| weekly | PCR down · unwinding · walls same · near call wall | 12 | 73% | +0.37% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| monthly | PCR up · put writing · walls same · near call wall | 11 | 50% | +0.18% | -0.40 to +0.93% | 50% of 2 | no clear direction |
| weekly | PCR down · call writing · walls same · mid walls | 11 | 82% | +0.21% | -0.43 to +0.75% | 40% of 5 | up |
| monthly | PCR up · quiet OI · walls same · mid walls | 11 | 82% | +0.23% | -0.39 to +0.91% | 50% of 2 | up |
| weekly | PCR up · put and call writing · walls same · mid walls | 11 | 45% | +0.09% | -0.78 to +0.90% | 100% of 2 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · mid walls | 10 | 57% | +0.11% | -0.16 to +0.71% | 50% of 2 | too few (7/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 10 | 75% | +0.13% | -0.83 to +0.98% | 0% of 1 | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 10 | 60% | +0.01% | -1.01 to +1.12% | 100% of 1 | no clear direction |
| monthly | PCR down · put and call writing · walls same · mid walls | 10 | 80% | +0.28% | -0.21 to +1.13% | 50% of 2 | no clear direction |
| monthly | PCR down · call writing · walls same · mid walls | 9 | 44% | +0.02% | -0.47 to +0.49% | 50% of 2 | too few (9/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 9 | 78% | +0.31% | -1.22 to +1.24% | 67% of 3 | too few (9/10) |
| weekly | PCR down · call writing · walls down · mid walls | 9 | 78% | +0.24% | -0.07 to +0.54% | 67% of 3 | too few (9/10) |
| monthly | PCR up · put writing · walls same · mid walls | 8 | 75% | +0.42% | -0.29 to +0.85% | 50% of 2 | too few (8/10) |
| weekly | PCR up · put writing · walls up · mid walls | 8 | 62% | +0.31% | -0.26 to +1.40% | 33% of 3 | too few (8/10) |
| weekly | PCR up · put writing · walls up · near put wall | 8 | 62% | +0.33% | -0.13 to +1.65% | 0% of 4 | too few (8/10) |
| monthly | PCR down · call writing · walls same · near call wall | 8 | 83% | +0.27% | -0.78 to +1.18% | 50% of 2 | too few (6/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% | 0% of 1 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 7 | 86% | +0.50% | -0.37 to +1.25% | 50% of 2 | too few (7/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 7 | 43% | -0.05% | -0.89 to +0.90% | 67% of 3 | too few (7/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.02% | -0.74 to +0.62% | 50% of 2 | too few (7/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 7 | 86% | +0.29% | -0.11 to +0.62% | 50% of 4 | too few (7/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 7 | 71% | +0.53% | -1.02 to +1.82% | 50% of 4 | too few (7/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 7 | 83% | +0.23% | -0.05 to +0.63% | 67% of 3 | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 50% of 2 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near call wall | 6 | 83% | +0.50% | -0.02 to +0.91% | 33% of 3 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 6 | 67% | -0.08% | -1.07 to +0.28% | 100% of 1 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 6 | 20% | +0.00% | -0.29 to +0.43% | 33% of 3 | too few (5/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 6 | 100% | +0.54% | +0.47 to +0.61% | 67% of 3 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 6 | 80% | +0.46% | -1.11 to +1.69% | 0% of 2 | too few (5/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 6 | 100% | +0.26% | +0.04 to +0.59% | 0% of 4 | too few (6/10) |
| weekly | PCR down · call writing · walls down · near call wall | 6 | 83% | +0.53% | -0.06 to +1.68% | 67% of 3 | too few (6/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 5 | 100% | +0.19% | +0.16 to +0.25% | 67% of 3 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 5 | 40% | +0.06% | -0.68 to +0.75% | 50% of 2 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near put wall | 5 | 60% | +0.09% | -0.51 to +0.73% | 0% of 2 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 50% of 2 | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 5 | 60% | +0.15% | -0.07 to +0.33% | 100% of 1 | too few (5/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 5 | 80% | +0.26% | -0.02 to +0.90% | 33% of 3 | too few (5/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 5 | 80% | +0.21% | -0.22 to +0.68% | 60% of 5 | too few (5/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 5 | 100% | +0.46% | +0.13 to +1.17% | 50% of 2 | too few (5/10) |
| monthly | PCR flat · quiet OI · walls up · near put wall | 4 | 0% | -0.25% | -0.61 to -0.05% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 50% of 2 | too few (4/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 4 | 100% | +0.15% | +0.06 to +0.25% | 100% of 1 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 4 | 25% | -0.02% | -0.69 to +0.99% | 50% of 2 | too few (4/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 4 | 100% | +0.61% | +0.01 to +1.22% | 67% of 3 | too few (2/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 100% | +0.79% | +0.14 to +1.65% | 0% of 1 | too few (4/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 4 | 100% | +0.50% | +0.37 to +0.62% | 0% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 4 |  |  |  | 100% of 4 | too few (0/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 4 | 50% | +0.06% | -0.63 to +0.58% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 4 | 100% | +0.60% | +0.23 to +0.85% | 0% of 1 | too few (4/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 3 | 67% | +0.08% | -0.07 to +0.27% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 3 | 50% | -0.03% | -0.43 to +0.37% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near put wall | 3 | 67% | -0.09% | -1.22 to +0.65% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 3 | 67% | -0.03% | -0.44 to +0.19% | 0% of 1 | too few (3/10) |
| weekly | PCR up · call writing · walls down · mid walls | 3 | 67% | +0.18% | -0.61 to +0.64% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 3 | 67% | +0.38% | -0.18 to +0.91% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 3 | 33% | -0.01% | -0.37 to +0.53% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 3 | 50% | -0.15% | -0.33 to +0.03% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 3 | 100% | +0.28% | +0.07 to +0.50% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 3 | 100% | +0.12% | +0.05 to +0.16% | 100% of 2 | too few (3/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 3 | 67% | +0.08% | -0.04 to +0.18% | 50% of 2 | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls same · near put wall | 2 | 0% | -0.07% | -0.07 to -0.07% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 2 | 50% | +0.18% | -0.20 to +0.57% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 2 | 50% | -0.57% | -1.32 to +0.18% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 2 | 50% | -0.15% | -0.30 to +0.01% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 2 | 50% | +0.03% | -0.15 to +0.21% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 2 | 100% | +0.20% | +0.20 to +0.20% | 100% of 2 | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 50% of 2 | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · mid walls | 2 | 50% | +0.04% | -0.19 to +0.28% | 100% of 2 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 50% of 2 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% | 0% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 2 | 50% | -0.08% | -0.49 to +0.34% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near put wall | 2 | 100% | +0.21% | +0.18 to +0.24% | 100% of 1 | too few (2/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 2 | 50% | -0.10% | -0.29 to +0.09% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls same · mid walls | 2 | 100% | +0.30% | +0.29 to +0.31% | 100% of 2 | too few (2/10) |
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
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls down · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near call wall | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
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
| monthly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.40% | +0.40 to +0.40% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · near put wall | 1 | 100% | +1.02% | +1.02 to +1.02% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near put wall | 1 | 0% | -0.29% | -0.29 to -0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near put wall | 1 | 0% | -0.83% | -0.83 to -0.83% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · mid walls | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 4 | 33% | +0.16% | -0.34 to +1.05% | 50% of 2 | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | +0.30% | -0.61 to +1.12% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | +0.73% | -0.39 to +2.40% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 100% | +0.61% | +0.06 to +1.12% | 100% of 3 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.53% | -0.63 to +1.68% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 100% | +0.55% | +0.51 to +0.58% | 50% of 2 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 2 | 50% | +0.02% | -0.63 to +0.68% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.49% | +0.34 to +0.65% | 100% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 2 | 0% | -1.15% | -1.75 to -0.54% | 100% of 2 | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -1.75% | -1.75 to -1.75% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 | 100% | +1.85% | +1.85 to +1.85% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.58% | +0.58 to +0.58% | 100% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +1.85% | +1.85 to +1.85% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.84% | +0.84 to +0.84% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.38% | +0.38 to +0.38% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +1.14% | +1.14 to +1.14% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 179 | 66% | +0.17% | up |
| intraday | weekly | writers even · few weak writers | 131 | 59% | +0.09% | up |
| intraday | monthly | writers even · weak calls | 103 | 73% | +0.14% | up |
| intraday | weekly | put writers stronger · weak calls | 79 | 76% | +0.32% | up |
| intraday | monthly | put writers stronger · weak calls | 63 | 85% | +0.57% | up |
| intraday | weekly | call writers stronger · weak puts | 43 | 80% | +0.33% | up |
| intraday | weekly | put writers stronger · few weak writers | 42 | 82% | +0.34% | up |
| intraday | weekly | call writers stronger · few weak writers | 36 | 74% | +0.17% | up |
| intraday | weekly | writers even · weak calls | 27 | 80% | +0.38% | up |
| intraday | monthly | writers even · weak puts | 21 | 80% | +0.42% | up |
| intraday | weekly | writers even · weak puts | 21 | 78% | +0.24% | up |
| intraday | monthly | call writers stronger · few weak writers | 15 | 62% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak on both sides | 11 | 73% | +0.20% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 7 | 29% | -0.51% | too few (7/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | weekly | put writers stronger · weak on both sides | 1 | 0% | -0.29% | too few (1/10) |
| day | monthly | writers even · few weak writers | 15 | 57% | +0.24% | no clear direction |
| day | weekly | writers even · few weak writers | 9 | 75% | +0.61% | too few (8/10) |
| day | monthly | writers even · weak calls | 7 | 71% | +0.52% | too few (7/10) |
| day | weekly | put writers stronger · weak calls | 7 | 71% | +0.20% | too few (7/10) |
| day | monthly | put writers stronger · weak calls | 4 | 100% | +0.88% | too few (4/10) |
| day | weekly | call writers stronger · weak puts | 3 | 33% | +0.32% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | writers even · weak puts | 3 | 33% | -0.06% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 2 | 100% | +0.92% | too few (2/10) |
| day | weekly | writers even · weak calls | 2 | 50% | +1.00% | too few (2/10) |
| day | monthly | writers even · weak puts | 1 | 100% | +1.85% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 62 | 66% | +0.15% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 57 | 78% | +0.39% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 56 | 56% | +0.01% | no clear direction |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 49 | 85% | +0.68% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 45 | 93% | +0.31% | up |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m up | 41 | 46% | -0.03% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 28 | 77% | +0.29% | up |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 23 | 55% | +0.22% | no clear direction |
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
| intraday | weekly | put writers stronger · few weak writers · weekly sideways · 125m up | 10 | 70% | +0.49% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 9 | 50% | -0.12% | too few (8/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 9 | 67% | +0.03% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 8 | 100% | +0.19% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 6 | 20% | -0.14% | too few (5/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 5 | 100% | +0.53% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 5 | 40% | +0.00% | too few (5/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 4 | 50% | +0.01% | too few (4/10) |
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
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 6 | 60% | -0.11% | too few (5/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 4 | 75% | +0.07% | too few (4/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 4 | 67% | +0.04% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +1.32% | too few (2/10) |
| day | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m up | 2 | 50% | -0.22% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +0.86% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 | 100% | +1.14% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.58% | too few (1/10) |
| day | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 100% | +1.85% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.18% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 1 | 100% | +1.85% | too few (1/10) |
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
