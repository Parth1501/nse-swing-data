# Nifty option chain pattern log
Updated 2026-11-20 13:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 636 snapshots over 26 trading days
- 707 patterns logged; 186 different patterns so far

## Latest read (2026-11-20 13:45:03)

Nifty trend: weekly **sideways**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-23 (weekly) | 3.1 | 25732 | 1.113 | 25500 | 25500 | 26000 | ±0.95% (25487-25978) | 13.25 |
| 2026-12-29 (monthly) | 39.1 | 25732 | 0.962 | 25400 | 25500 | 27000 | ±3.7% (24780-26684) | 14.13 |

- **Weekly, last 30 min**: `PCR down · call writing · walls same · mid walls`. Seen 10 times before; Nifty was up after it 80% of the time, average +0.21%. Too few outcomes (10/20) to trade on.
  - Writers: `put writers stronger · weak calls`. Seen 73 times before; Nifty was up after it 76% of the time, average +0.35%. History points to a bull call debit spread, ATM to about the call wall 26000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 16 times before; Nifty was up after it 69% of the time, average +0.17%. Too few outcomes (13/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls up · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +1.58%. Too few outcomes (1/20) to trade on.
  - Writers: `put writers stronger · weak calls`. Seen 6 times before; Nifty was up after it 83% of the time, average +0.47%. Too few outcomes (6/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Nifty was up after it 100% of the time, average +0.58%. Too few outcomes (3/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · near put wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.04%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 144 times before; Nifty was up after it 70% of the time, average +0.21%. History points to a bull call debit spread, ATM to about the call wall 27000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 35 times before; Nifty was up after it 72% of the time, average +0.26%. History points to a bull call debit spread, ATM to about the call wall 27000.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 12 times before; Nifty was up after it 58% of the time, average +0.37%. Too few outcomes (12/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Nifty was up after it 67% of the time, average +0.20%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-11-23

Strongest call writers at 26000, strongest put writers at 25500; weakest call writers at 25700, weakest put writers at -. Covers 100% of near-money call OI and 99% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25350 | 15506 | 15497 | 153.7 | 25368 | 404.8 | 25504 | -229 | -251.2 | weak |
| Call | 25400 | 63785 | 63728 | 143.2 | 25405 | 360.0 | 25543 | -189 | -216.8 | weak |
| Call | 25450 | 28542 | 28541 | 128.6 | 25452 | 316.5 | 25579 | -154 | -187.9 | weak |
| Call | 25500 | 130048 | 129389 | 106.6 | 25368 | 276.6 | 25607 | -126 | -170.0 | weak |
| Call | 25550 | 41961 | 41948 | 94.8 | 25467 | 237.4 | 25645 | -88 | -142.7 | weak |
| Call | 25600 | 85001 | 84990 | 81.5 | 25428 | 201.7 | 25682 | -51 | -120.1 | weak |
| Call | 25650 | 59937 | 59937 | 65.0 | 25464 | 170.2 | 25715 | -17 | -105.2 | weak |
| Call | 25700 | 187938 | 187869 | 68.6 | 25451 | 140.5 | 25769 | +36 | -71.9 | weak |
| Call | 25750 | 126712 | 126618 | 78.7 | 25589 | 114.8 | 25829 | +96 | -36.0 | medium |
| Call | 25800 | 164101 | 163857 | 51.9 | 25466 | 92.7 | 25852 | +120 | -40.8 | strong |
| Call | 25850 | 62227 | 62140 | 31.3 | 25462 | 73.7 | 25881 | +149 | -42.4 | strong |
| Call | 25900 | 102795 | 102794 | 26.8 | 25437 | 58.4 | 25927 | +194 | -31.6 | strong |
| Call | 25950 | 56030 | 55896 | 21.9 | 25464 | 45.6 | 25972 | +240 | -23.7 | strong |
| Call | 26000 | 258605 | 253657 | 27.0 | 25146 | 35.4 | 26027 | +295 | -8.4 | strong |
| Call | 26050 | 44266 | 44264 | 13.8 | 25468 | 27.2 | 26064 | +331 | -13.4 | strong |
| Call | 26100 | 84971 | 84920 | 10.0 | 25414 | 20.7 | 26110 | +378 | -10.7 | strong |
| Put | 25350 | 114265 | 114265 | 117.2 | 25416 | 22.1 | 25233 | +500 | +95.1 | strong |
| Put | 25400 | 224657 | 224190 | 131.6 | 25449 | 27.4 | 25268 | +464 | +104.2 | strong |
| Put | 25450 | 122014 | 122013 | 138.1 | 25482 | 34.5 | 25312 | +420 | +103.6 | strong |
| Put | 25500 | 316676 | 312775 | 167.7 | 25488 | 43.2 | 25332 | +400 | +124.5 | strong |
| Put | 25550 | 116547 | 116545 | 144.2 | 25550 | 54.2 | 25406 | +327 | +89.9 | strong |
| Put | 25600 | 158609 | 158589 | 141.3 | 25604 | 68.6 | 25459 | +274 | +72.7 | strong |
| Put | 25650 | 108389 | 108387 | 126.1 | 25667 | 85.3 | 25524 | +208 | +40.7 | strong |
| Put | 25700 | 175318 | 175302 | 142.6 | 25684 | 105.7 | 25557 | +175 | +36.9 | strong |
| Put | 25750 | 58307 | 58306 | 161.1 | 25696 | 130.3 | 25589 | +144 | +30.8 | strong |
| Put | 25800 | 31805 | 31727 | 234.1 | 25643 | 158.9 | 25566 | +167 | +75.2 | strong |
| Put | 25850 | 6708 | 6705 | 240.2 | 25679 | 190.0 | 25610 | +123 | +50.2 | strong |
| Put | 25900 | 9831 | 9807 | 304.7 | 25650 | 224.9 | 25595 | +137 | +79.8 | strong |
| Put | 25950 | 3331 | 3330 | 302.3 | 25690 | 262.1 | 25648 | +85 | +40.2 | medium |
| Put | 26000 | 29440 | 25713 | 1271.7 | 24692 | 300.0 | 24728 | +1004 | +971.7 | strong |
| Put | 26050 | 661 | 659 | 486.0 | 25584 | 341.4 | 25564 | +168 | +144.6 | strong |
| Put | 26100 | 1684 | 1676 | 1279.5 | 24788 | 383.5 | 24820 | +912 | +896.0 | strong |

## Strong vs weak writers, monthly 2026-12-29

Strongest call writers at 26500, strongest put writers at 25500; weakest call writers at 25200, weakest put writers at -. Covers 34% of near-money call OI and 35% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25350 | 645 | 262 | 484.9 | 25249 | 803.4 | 25835 | +102 | -318.6 | medium |
| Call | 25400 | 6514 | 3349 | 467.1 | 25276 | 766.3 | 25867 | +135 | -299.2 | strong |
| Call | 25450 | 1244 | 623 | 442.8 | 25276 | 733.0 | 25893 | +160 | -290.2 | strong |
| Call | 25500 | 67184 | 25131 | 476.8 | 25374 | 697.0 | 25977 | +244 | -220.2 | strong |
| Call | 25550 | 1289 | 847 | 413.0 | 25307 | 662.8 | 25963 | +231 | -249.8 | strong |
| Call | 25600 | 9376 | 5906 | 448.6 | 25437 | 634.5 | 26049 | +316 | -185.9 | strong |
| Call | 25650 | 922 | 456 | 422.6 | 25407 | 608.0 | 26073 | +340 | -185.3 | strong |
| Call | 25700 | 4967 | 2471 | 440.3 | 25495 | 576.0 | 26140 | +408 | -135.7 | strong |
| Call | 25750 | 650 | 447 | 433.1 | 25533 | 548.5 | 26183 | +451 | -115.3 | strong |
| Call | 25800 | 7494 | 4379 | 332.2 | 25346 | 519.1 | 26132 | +400 | -187.0 | strong |
| Call | 25850 | 278 | 154 | 395.5 | 25545 | 489.5 | 26245 | +513 | -94.0 | strong |
| Call | 25900 | 2213 | 927 | 295.2 | 25382 | 463.7 | 26195 | +463 | -168.5 | strong |
| Call | 25950 | 241 | 106 | 286.3 | 25416 | 441.9 | 26236 | +504 | -155.6 | strong |
| Call | 26000 | 79952 | 18334 | 250.4 | 25357 | 414.1 | 26250 | +518 | -163.6 | strong |
| Call | 26050 | 400 | 212 | 241.1 | 25385 | 379.9 | 26291 | +559 | -138.9 | strong |
| Call | 26100 | 3060 | 1007 | 225.9 | 25394 | 368.4 | 26326 | +594 | -142.5 | strong |
| Put | 25350 | 712 | 369 | 400.3 | 25310 | 260.1 | 24950 | +783 | +140.3 | strong |
| Put | 25400 | 18552 | 10153 | 428.2 | 25310 | 277.4 | 24972 | +761 | +150.7 | strong |
| Put | 25450 | 1055 | 685 | 423.9 | 25364 | 290.6 | 25026 | +706 | +133.4 | strong |
| Put | 25500 | 92440 | 38459 | 431.0 | 25430 | 310.6 | 25069 | +663 | +120.5 | strong |
| Put | 25550 | 1411 | 1078 | 471.8 | 25386 | 326.4 | 25078 | +654 | +145.3 | strong |
| Put | 25600 | 12658 | 8985 | 459.8 | 25492 | 346.1 | 25140 | +592 | +113.8 | strong |
| Put | 25650 | 782 | 627 | 460.0 | 25468 | 362.0 | 25190 | +542 | +98.0 | strong |
| Put | 25700 | 3546 | 2873 | 448.2 | 25587 | 384.9 | 25252 | +481 | +63.3 | strong |
| Put | 25750 | 409 | 258 | 475.8 | 25583 | 403.5 | 25274 | +458 | +72.3 | strong |
| Put | 25800 | 2213 | 1473 | 496.2 | 25572 | 427.3 | 25304 | +429 | +68.9 | strong |
| Put | 25850 | 214 | 129 | 524.7 | 25558 | 444.2 | 25325 | +407 | +80.5 | strong |
| Put | 25900 | 757 | 452 | 543.6 | 25588 | 472.1 | 25356 | +376 | +71.5 | strong |
| Put | 25950 | 161 | 86 | 622.4 | 25516 | 498.1 | 25328 | +405 | +124.2 | strong |
| Put | 26000 | 55916 | 5004 | 674.7 | 25442 | 517.5 | 25325 | +407 | +157.2 | strong |
| Put | 26050 | 172 | 79 | 671.1 | 25538 | 562.2 | 25379 | +354 | +108.9 | strong |
| Put | 26100 | 2951 | 2525 | 665.1 | 25548 | 570.0 | 25435 | +297 | +95.1 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 39 | 68% | +0.26% | -0.44 to +0.97% | 100% of 1 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 22 | 86% | +0.39% | -0.50 to +1.68% |  | up |
| weekly | PCR up · put writing · walls same · near call wall | 20 | 85% | +0.28% | -0.27 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 19 | 83% | +0.37% | -0.42 to +1.02% | 100% of 1 | up |
| weekly | PCR down · call writing · walls same · near put wall | 18 | 67% | +0.24% | -0.37 to +0.85% | 50% of 4 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near call wall | 16 | 56% | +0.28% | -0.71 to +1.70% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 16 | 62% | +0.11% | -0.47 to +0.80% | 50% of 4 | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near put wall | 14 | 83% | +0.12% | -0.18 to +0.63% |  | up |
| monthly | PCR flat · put writing · walls same · near call wall | 13 | 73% | +0.36% | -0.50 to +1.56% |  | no clear direction |
| weekly | PCR up · put writing · walls same · mid walls | 12 | 67% | +0.15% | -0.57 to +0.89% | 67% of 3 | no clear direction |
| monthly | PCR up · put and call writing · walls same · mid walls | 11 | 73% | +0.15% | -0.24 to +0.63% | 100% of 1 | no clear direction |
| monthly | PCR up · put writing · walls same · near call wall | 11 | 50% | +0.18% | -0.40 to +0.93% | 100% of 1 | no clear direction |
| weekly | PCR down · call writing · walls same · mid walls | 11 | 80% | +0.21% | -0.43 to +0.75% | 50% of 4 | no clear direction |
| weekly | PCR down · unwinding · walls same · near call wall | 11 | 70% | +0.39% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| weekly | PCR down · unwinding · walls same · mid walls | 11 | 57% | +0.04% | -0.40 to +0.90% | 75% of 4 | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 10 | 80% | +0.24% | -0.39 to +0.91% | 100% of 1 | no clear direction |
| monthly | PCR down · put and call writing · walls same · mid walls | 10 | 80% | +0.28% | -0.21 to +1.13% | 100% of 1 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · mid walls | 10 | 57% | +0.11% | -0.16 to +0.71% | 100% of 1 | too few (7/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 10 | 40% | +0.03% | -0.78 to +0.90% | 100% of 2 | no clear direction |
| weekly | PCR up · put and call writing · walls same · near put wall | 9 | 78% | +0.28% | -1.22 to +1.24% | 50% of 2 | too few (9/10) |
| weekly | PCR down · call writing · walls down · mid walls | 9 | 78% | +0.24% | -0.07 to +0.54% | 67% of 3 | too few (9/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% |  | too few (6/10) |
| monthly | PCR down · call writing · walls same · near call wall | 8 | 83% | +0.27% | -0.78 to +1.18% | 100% of 1 | too few (6/10) |
| monthly | PCR down · call writing · walls same · mid walls | 8 | 38% | +0.01% | -0.47 to +0.49% | 100% of 1 | too few (8/10) |
| weekly | PCR up · put writing · walls up · near put wall | 8 | 62% | +0.33% | -0.13 to +1.65% | 0% of 4 | too few (8/10) |
| monthly | PCR up · put writing · walls same · mid walls | 8 | 75% | +0.42% | -0.29 to +0.85% | 100% of 1 | too few (8/10) |
| weekly | PCR up · put writing · walls up · mid walls | 8 | 62% | +0.31% | -0.26 to +1.40% | 33% of 3 | too few (8/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (7/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 7 | 86% | +0.25% | -0.11 to +0.62% | 33% of 3 | too few (7/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 7 | 86% | +0.50% | -0.37 to +1.25% | 100% of 1 | too few (7/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 6 | 100% | +0.43% | +0.10 to +0.85% |  | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near call wall | 6 | 83% | +0.53% | -0.06 to +1.68% | 67% of 3 | too few (6/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 6 | 80% | +0.23% | -0.05 to +0.63% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 5 | 80% | +0.21% | -0.02 to +0.63% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 5 | 100% | +0.19% | +0.16 to +0.25% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 5 | 40% | +0.06% | -0.75 to +0.90% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 5 | 100% | +0.29% | +0.04 to +0.59% | 0% of 4 | too few (5/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 5 | 40% | +0.06% | -0.68 to +0.75% | 50% of 2 | too few (5/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 5 | 80% | +0.20% | -0.13 to +0.71% |  | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 100% of 1 | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 5 | 60% | +0.15% | -0.07 to +0.33% |  | too few (5/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 5 | 80% | +0.12% | -0.05 to +0.28% |  | too few (5/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 5 | 80% | +0.90% | -0.07 to +1.82% | 33% of 3 | too few (5/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 5 | 100% | +0.54% | +0.47 to +0.61% | 67% of 3 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 5 | 25% | +0.07% | -0.10 to +0.43% | 33% of 3 | too few (4/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 5 | 80% | +0.46% | -1.11 to +1.69% | 0% of 2 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near put wall | 5 | 60% | +0.09% | -0.51 to +0.73% | 0% of 2 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near call wall | 5 | 80% | +0.53% | -0.02 to +0.91% | 33% of 3 | too few (5/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 4 | 100% | +0.44% | +0.13 to +0.91% | 100% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 4 | 100% | +0.50% | +0.37 to +0.62% |  | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 4 |  |  |  | 100% of 4 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 4 | 75% | +0.22% | -0.22 to +0.68% | 75% of 4 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 4 | 50% | +0.06% | -0.63 to +0.58% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 100% | +0.79% | +0.14 to +1.65% |  | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 4 | 25% | -0.09% | -0.69 to +0.72% | 0% of 1 | too few (4/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 3 | 50% | -0.03% | -0.43 to +0.37% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 3 | 100% | +0.61% | +0.01 to +1.22% | 50% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 3 | 67% | +0.08% | -0.04 to +0.18% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 3 | 100% | +0.12% | +0.05 to +0.16% | 100% of 2 | too few (3/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 3 | 67% | +0.38% | -0.18 to +0.91% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 3 | 33% | -0.01% | -0.37 to +0.53% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 3 | 100% | +0.28% | +0.07 to +0.50% | 100% of 2 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · quiet OI · walls up · near put wall | 3 | 0% | -0.07% | -0.09 to -0.05% |  | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 2 | 100% | +0.30% | +0.29 to +0.31% | 100% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 2 | 100% | +0.20% | +0.20 to +0.20% | 100% of 2 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| monthly | PCR up · call writing · walls same · mid walls | 2 | 50% | +0.04% | -0.19 to +0.28% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 2 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 2 | 50% | +0.05% | -0.20 to +0.30% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 2 | 100% | +0.15% | +0.10 to +0.21% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near put wall | 2 | 100% | +0.21% | +0.18 to +0.24% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near put wall | 2 | 50% | -0.59% | -1.22 to +0.05% |  | too few (2/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.87% | +0.87 to +0.87% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +1.86% | +1.86 to +1.86% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · quiet OI · walls down · near call wall | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| weekly | PCR down · quiet OI · walls same · mid walls | 1 | 100% | +0.49% | +0.49 to +0.49% |  | too few (1/10) |
| weekly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · near put wall | 1 | 100% | +0.76% | +0.76 to +0.76% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near put wall | 1 | 0% | -0.29% | -0.29 to -0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · mid walls | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | +0.21% | -0.61 to +0.85% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | +0.73% | -0.39 to +2.40% |  | too few (3/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 100% | +0.52% | +0.06 to +0.85% | 100% of 2 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 2 | 50% | +0.02% | -0.63 to +0.68% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 100% | +0.55% | +0.51 to +0.58% | 50% of 2 | too few (2/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 2 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.53% | -0.63 to +1.68% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.58% | +0.58 to +0.58% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.38% | +0.38 to +0.38% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +1.14% | +1.14 to +1.14% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 145 | 70% | +0.21% | up |
| intraday | weekly | writers even · few weak writers | 115 | 57% | +0.10% | no clear direction |
| intraday | monthly | writers even · weak calls | 101 | 74% | +0.17% | up |
| intraday | weekly | put writers stronger · weak calls | 74 | 76% | +0.35% | up |
| intraday | monthly | put writers stronger · weak calls | 63 | 85% | +0.57% | up |
| intraday | weekly | call writers stronger · weak puts | 38 | 89% | +0.40% | up |
| intraday | weekly | put writers stronger · few weak writers | 35 | 94% | +0.42% | up |
| intraday | weekly | call writers stronger · few weak writers | 33 | 81% | +0.25% | up |
| intraday | weekly | writers even · weak calls | 26 | 83% | +0.44% | up |
| intraday | weekly | writers even · weak puts | 20 | 82% | +0.31% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | monthly | call writers stronger · few weak writers | 15 | 62% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak on both sides | 11 | 73% | +0.20% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | weekly | put writers stronger · weak on both sides | 1 | 0% | -0.29% | too few (1/10) |
| day | monthly | writers even · few weak writers | 13 | 58% | +0.37% | no clear direction |
| day | monthly | writers even · weak calls | 7 | 71% | +0.52% | too few (7/10) |
| day | weekly | put writers stronger · weak calls | 7 | 83% | +0.47% | too few (6/10) |
| day | weekly | writers even · few weak writers | 7 | 71% | +0.65% | too few (7/10) |
| day | monthly | put writers stronger · weak calls | 4 | 100% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | writers even · weak puts | 3 | 33% | -0.06% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 2 | 100% | +0.92% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak calls | 2 | 50% | +1.00% | too few (2/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 57 | 78% | +0.39% | up |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 49 | 85% | +0.68% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 45 | 93% | +0.31% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 40 | 50% | +0.02% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m up | 39 | 49% | +0.04% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 36 | 72% | +0.26% | up |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 28 | 77% | +0.29% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 23 | 67% | +0.27% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m sideways | 17 | 88% | +0.14% | up |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 17 | 69% | +0.17% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 15 | 64% | +0.39% | no clear direction |
| intraday | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 14 | 83% | +0.16% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.73% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 8 | 100% | +0.19% | too few (8/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 8 | 75% | +0.16% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly sideways · 125m up | 7 | 100% | +0.71% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 6 | 80% | +0.16% | too few (5/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 5 | 100% | +0.53% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 5 | 40% | +0.00% | too few (5/10) |
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
| intraday | monthly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.02% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 1 | 100% | +0.28% | too few (1/10) |
| intraday | weekly | put writers stronger · weak on both sides · weekly sideways · 125m up | 1 | 0% | -0.29% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m up | 1 | 100% | +0.91% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 4 | 67% | +0.20% | too few (3/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 4 | 100% | +0.58% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +1.32% | too few (2/10) |
| day | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m up | 2 | 50% | -0.22% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +0.86% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.12% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 | 100% | +1.14% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.58% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.18% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
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
