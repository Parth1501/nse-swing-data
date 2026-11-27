# Nifty option chain pattern log
Updated 2026-11-27 11:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 730 snapshots over 30 trading days
- 808 patterns logged; 198 different patterns so far

## Latest read (2026-11-27 11:45:09)

Nifty trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-01 (weekly) | 4.2 | 25688 | 0.839 | 25750 | 25000 | 26000 | ±1.28% (25360-26017) | 15.23 |
| 2026-12-29 (monthly) | 32.2 | 25692 | 1.186 | 25500 | 25000 | 26000 | ±3.45% (24806-26578) | 14.48 |

- **Weekly, last 30 min**: `PCR up · call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 142 times before; Nifty was up after it 56% of the time, average +0.06%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 23 times before; Nifty was up after it 67% of the time, average +0.27%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · near call wall`. Seen 2 times before; Nifty was up after it 50% of the time, average +0.53%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 9 times before; Nifty was up after it 67% of the time, average +0.45%. Too few outcomes (9/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 2 times before; Nifty was up after it 100% of the time, average +0.86%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR up · call writing · walls same · near call wall`. Seen 3 times before; Nifty was up after it 33% of the time, average -0.13%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 190 times before; Nifty was up after it 64% of the time, average +0.14%. History points to a bull call debit spread, ATM to about the call wall 26000.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 23 times before; Nifty was up after it 55% of the time, average +0.22%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 15 times before; Nifty was up after it 53% of the time, average +0.17%. Too few outcomes (15/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 1 times before; Nifty was up after it 100% of the time, average +1.14%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-12-01

Strongest call writers at 26000, strongest put writers at 25700; weakest call writers at 25000, weakest put writers at 25900. Covers 84% of near-money call OI and 88% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25350 | 3471 | 202 | 480.9 | 25765 | 375.0 | 25831 | +143 | +105.9 | strong |
| Call | 25400 | 25967 | 672 | 432.7 | 25729 | 336.9 | 25833 | +144 | +95.8 | strong |
| Call | 25450 | 3532 | 324 | 439.9 | 25818 | 301.4 | 25890 | +202 | +138.4 | strong |
| Call | 25500 | 42213 | 6669 | 372.7 | 25798 | 266.4 | 25873 | +184 | +106.2 | strong |
| Call | 25550 | 8646 | 5361 | 275.3 | 25709 | 235.2 | 25825 | +137 | +40.1 | strong |
| Call | 25600 | 36407 | 22697 | 252.2 | 25736 | 205.4 | 25852 | +164 | +46.7 | strong |
| Call | 25650 | 29149 | 27047 | 213.8 | 25730 | 177.6 | 25864 | +175 | +36.2 | strong |
| Call | 25700 | 111934 | 103331 | 195.6 | 25740 | 152.9 | 25896 | +207 | +42.7 | strong |
| Call | 25750 | 83618 | 82670 | 186.2 | 25775 | 130.6 | 25936 | +248 | +55.6 | strong |
| Call | 25800 | 237678 | 225954 | 174.1 | 25794 | 110.8 | 25974 | +286 | +63.4 | strong |
| Call | 25850 | 170871 | 169575 | 162.5 | 25827 | 92.5 | 26012 | +324 | +69.9 | strong |
| Call | 25900 | 225927 | 209871 | 158.1 | 25838 | 77.5 | 26058 | +370 | +80.7 | strong |
| Call | 25950 | 101959 | 97889 | 142.2 | 25841 | 64.0 | 26092 | +404 | +78.1 | strong |
| Call | 26000 | 323877 | 248838 | 107.7 | 25805 | 53.1 | 26108 | +419 | +54.6 | strong |
| Call | 26050 | 75341 | 72386 | 98.1 | 25836 | 43.4 | 26148 | +460 | +54.8 | strong |
| Put | 25350 | 39308 | 30074 | 43.6 | 25824 | 50.2 | 25306 | +382 | -6.6 | strong |
| Put | 25400 | 104520 | 87859 | 62.4 | 25805 | 61.3 | 25338 | +351 | +1.1 | strong |
| Put | 25450 | 51893 | 48252 | 62.7 | 25830 | 74.7 | 25387 | +301 | -12.0 | strong |
| Put | 25500 | 154828 | 122168 | 76.7 | 25828 | 90.3 | 25423 | +265 | -13.6 | strong |
| Put | 25550 | 57108 | 55242 | 84.1 | 25804 | 107.5 | 25466 | +222 | -23.4 | strong |
| Put | 25600 | 117556 | 105731 | 97.0 | 25861 | 128.3 | 25503 | +185 | -31.3 | strong |
| Put | 25650 | 80986 | 79911 | 117.5 | 25803 | 150.7 | 25533 | +156 | -33.2 | strong |
| Put | 25700 | 158407 | 150799 | 134.6 | 25817 | 175.8 | 25565 | +123 | -41.3 | strong |
| Put | 25750 | 70723 | 70128 | 155.3 | 25810 | 202.9 | 25595 | +94 | -47.6 | medium |
| Put | 25800 | 117162 | 112220 | 170.5 | 25830 | 233.2 | 25629 | +59 | -62.7 | medium |
| Put | 25850 | 57138 | 57039 | 173.2 | 25856 | 265.1 | 25677 | +12 | -91.9 | weak |
| Put | 25900 | 65438 | 64399 | 208.4 | 25861 | 300.1 | 25692 | -3 | -91.8 | weak |
| Put | 25950 | 17707 | 17643 | 211.6 | 25900 | 337.2 | 25738 | -50 | -125.6 | weak |
| Put | 26000 | 51637 | 42927 | 259.0 | 25876 | 376.3 | 25741 | -53 | -117.3 | weak |
| Put | 26050 | 4036 | 3977 | 273.7 | 25893 | 417.6 | 25776 | -88 | -143.9 | weak |

## Strong vs weak writers, monthly 2026-12-29

Strongest call writers at 26000, strongest put writers at 25500; weakest call writers at -, weakest put writers at 26350. Covers 59% of near-money call OI and 59% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25350 | 460 | 308 | 545.1 | 25348 | 702.0 | 25895 | +203 | -156.8 | strong |
| Call | 25400 | 7014 | 4810 | 526.6 | 25378 | 661.8 | 25927 | +235 | -135.2 | strong |
| Call | 25450 | 887 | 574 | 485.6 | 25354 | 636.9 | 25936 | +244 | -151.3 | strong |
| Call | 25500 | 59945 | 29983 | 519.8 | 25455 | 597.4 | 26020 | +328 | -77.6 | strong |
| Call | 25550 | 817 | 626 | 471.9 | 25422 | 580.8 | 26022 | +330 | -108.8 | strong |
| Call | 25600 | 15651 | 13003 | 500.6 | 25530 | 539.4 | 26101 | +409 | -38.8 | strong |
| Call | 25650 | 843 | 607 | 480.9 | 25548 | 511.6 | 26131 | +439 | -30.7 | strong |
| Call | 25700 | 15837 | 13740 | 492.2 | 25617 | 482.8 | 26192 | +500 | +9.4 | strong |
| Call | 25750 | 1608 | 1481 | 489.9 | 25668 | 460.4 | 26240 | +548 | +29.6 | strong |
| Call | 25800 | 28975 | 26638 | 414.1 | 25567 | 429.9 | 26214 | +522 | -15.8 | strong |
| Call | 25850 | 1976 | 1890 | 470.9 | 25765 | 410.4 | 26321 | +629 | +60.5 | strong |
| Call | 25900 | 16329 | 15227 | 446.9 | 25741 | 381.4 | 26347 | +655 | +65.5 | strong |
| Call | 25950 | 1532 | 1450 | 453.7 | 25788 | 362.3 | 26404 | +712 | +91.4 | strong |
| Call | 26000 | 106063 | 51509 | 347.3 | 25618 | 338.9 | 26347 | +655 | +8.3 | strong |
| Call | 26050 | 1313 | 1178 | 398.2 | 25784 | 320.2 | 26448 | +756 | +78.0 | strong |
| Put | 25350 | 748 | 583 | 334.1 | 25523 | 258.9 | 25016 | +676 | +75.2 | strong |
| Put | 25400 | 18006 | 10857 | 408.7 | 25373 | 283.1 | 24991 | +701 | +125.6 | strong |
| Put | 25450 | 1238 | 974 | 396.6 | 25461 | 294.5 | 25053 | +639 | +102.1 | strong |
| Put | 25500 | 97599 | 51626 | 402.7 | 25512 | 318.5 | 25097 | +595 | +84.2 | strong |
| Put | 25550 | 1115 | 954 | 403.4 | 25557 | 334.9 | 25147 | +545 | +68.5 | strong |
| Put | 25600 | 21542 | 18517 | 424.3 | 25582 | 358.4 | 25176 | +516 | +66.0 | strong |
| Put | 25650 | 1454 | 1403 | 376.0 | 25714 | 375.4 | 25274 | +418 | +0.6 | strong |
| Put | 25700 | 15850 | 15255 | 427.2 | 25662 | 402.9 | 25273 | +419 | +24.3 | strong |
| Put | 25750 | 2180 | 2127 | 413.0 | 25744 | 424.4 | 25337 | +355 | -11.4 | strong |
| Put | 25800 | 20917 | 20257 | 454.2 | 25707 | 450.2 | 25346 | +346 | +4.0 | strong |
| Put | 25850 | 1300 | 1282 | 426.6 | 25793 | 467.4 | 25423 | +269 | -40.9 | strong |
| Put | 25900 | 14437 | 14202 | 454.9 | 25790 | 500.9 | 25445 | +247 | -46.0 | strong |
| Put | 25950 | 653 | 619 | 461.1 | 25829 | 521.6 | 25489 | +203 | -60.5 | strong |
| Put | 26000 | 77663 | 30718 | 520.9 | 25747 | 553.9 | 25479 | +213 | -33.0 | strong |
| Put | 26050 | 697 | 632 | 488.8 | 25842 | 570.5 | 25561 | +131 | -81.8 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 47 | 67% | +0.22% | -0.44 to +0.97% | 50% of 2 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 27 | 77% | +0.30% | -0.64 to +1.68% | 0% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 25 | 75% | +0.22% | -0.36 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 20 | 79% | +0.33% | -0.49 to +1.02% | 50% of 2 | up |
| weekly | PCR down · call writing · walls same · near put wall | 20 | 60% | +0.13% | -1.00 to +0.85% | 60% of 5 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 18 | 56% | +0.06% | -0.61 to +0.80% | 60% of 5 | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near put wall | 16 | 79% | +0.12% | -0.28 to +0.90% | 0% of 1 | up |
| monthly | PCR flat · put and call writing · walls same · near call wall | 16 | 56% | +0.28% | -0.71 to +1.70% | 50% of 2 | no clear direction |
| monthly | PCR flat · put writing · walls same · near call wall | 13 | 73% | +0.36% | -0.50 to +1.56% | 0% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · mid walls | 13 | 62% | +0.16% | -0.57 to +0.89% | 75% of 4 | no clear direction |
| weekly | PCR down · unwinding · walls same · near call wall | 13 | 75% | +0.34% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| weekly | PCR down · unwinding · walls same · mid walls | 13 | 67% | +0.06% | -0.40 to +0.90% | 80% of 5 | too few (9/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 12 | 80% | +0.24% | -0.19 to +0.70% | 0% of 1 | no clear direction |
| monthly | PCR up · put and call writing · walls same · mid walls | 12 | 75% | +0.18% | -0.24 to +0.63% | 50% of 2 | no clear direction |
| monthly | PCR up · quiet OI · walls same · mid walls | 11 | 82% | +0.23% | -0.39 to +0.91% | 50% of 2 | up |
| weekly | PCR down · call writing · walls same · mid walls | 11 | 82% | +0.21% | -0.43 to +0.75% | 40% of 5 | up |
| weekly | PCR up · put and call writing · walls same · mid walls | 11 | 45% | +0.08% | -0.78 to +0.90% | 100% of 2 | no clear direction |
| monthly | PCR up · put writing · walls same · near call wall | 11 | 50% | +0.18% | -0.40 to +0.93% | 50% of 2 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near put wall | 10 | 60% | +0.01% | -1.01 to +1.12% | 100% of 1 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · mid walls | 10 | 57% | +0.11% | -0.16 to +0.71% | 50% of 2 | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 10 | 80% | +0.28% | -0.21 to +1.13% | 50% of 2 | no clear direction |
| weekly | PCR down · call writing · walls down · mid walls | 10 | 70% | +0.18% | -0.39 to +0.54% | 67% of 3 | no clear direction |
| weekly | PCR up · put and call writing · walls same · near put wall | 10 | 70% | +0.21% | -1.22 to +1.24% | 67% of 3 | no clear direction |
| monthly | PCR flat · put writing · walls same · near put wall | 10 | 75% | +0.13% | -0.83 to +0.98% | 0% of 1 | too few (8/10) |
| monthly | PCR down · call writing · walls same · mid walls | 9 | 44% | +0.02% | -0.47 to +0.49% | 50% of 2 | too few (9/10) |
| weekly | PCR up · put writing · walls up · mid walls | 8 | 62% | +0.31% | -0.26 to +1.40% | 33% of 3 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% | 0% of 1 | too few (6/10) |
| weekly | PCR up · put writing · walls up · near put wall | 8 | 62% | +0.33% | -0.13 to +1.65% | 0% of 4 | too few (8/10) |
| monthly | PCR up · put writing · walls same · mid walls | 8 | 75% | +0.42% | -0.29 to +0.85% | 50% of 2 | too few (8/10) |
| monthly | PCR down · call writing · walls same · near call wall | 8 | 83% | +0.27% | -0.78 to +1.18% | 50% of 2 | too few (6/10) |
| weekly | PCR down · call writing · walls same · near call wall | 7 | 71% | +0.41% | -0.15 to +0.91% | 33% of 3 | too few (7/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 7 | 71% | +0.53% | -1.02 to +1.82% | 50% of 4 | too few (7/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 7 | 86% | +0.50% | -0.37 to +1.25% | 50% of 2 | too few (7/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 7 | 43% | -0.05% | -0.89 to +0.90% | 67% of 3 | too few (7/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 7 | 83% | +0.23% | -0.05 to +0.63% | 67% of 3 | too few (6/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 7 | 86% | +0.29% | -0.11 to +0.62% | 50% of 4 | too few (7/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.02% | -0.74 to +0.62% | 50% of 2 | too few (7/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 6 | 20% | +0.00% | -0.29 to +0.43% | 33% of 3 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near call wall | 6 | 83% | +0.53% | -0.06 to +1.68% | 67% of 3 | too few (6/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 6 | 83% | +0.25% | -0.68 to +1.17% | 50% of 2 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 6 | 67% | -0.08% | -1.07 to +0.28% | 100% of 1 | too few (6/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 6 | 67% | +0.37% | -1.11 to +1.69% | 0% of 2 | too few (6/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 6 | 100% | +0.54% | +0.47 to +0.61% | 67% of 3 | too few (3/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 6 | 100% | +0.24% | +0.02 to +0.59% | 0% of 4 | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 5 | 80% | +0.26% | -0.02 to +0.90% | 33% of 3 | too few (5/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 5 | 40% | +0.06% | -0.68 to +0.75% | 50% of 2 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near put wall | 5 | 60% | +0.09% | -0.51 to +0.73% | 0% of 2 | too few (5/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 5 | 100% | +0.19% | +0.16 to +0.25% | 67% of 3 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 5 | 60% | +0.15% | -0.07 to +0.33% | 100% of 1 | too few (5/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 5 | 80% | +0.21% | -0.22 to +0.68% | 60% of 5 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 50% of 2 | too few (5/10) |
| monthly | PCR flat · quiet OI · walls up · near put wall | 4 | 0% | -0.25% | -0.61 to -0.05% | 100% of 1 | too few (3/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 4 | 100% | +0.15% | +0.06 to +0.25% | 100% of 1 | too few (4/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 4 | 50% | +0.06% | -0.15 to +0.26% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 50% of 2 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 4 |  |  |  | 100% of 4 | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 4 | 100% | +0.60% | +0.23 to +0.85% | 0% of 1 | too few (4/10) |
| monthly | PCR up · call writing · walls same · near call wall | 4 | 33% | -0.13% | -0.51 to +0.29% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 4 | 25% | -0.02% | -0.69 to +0.99% | 50% of 2 | too few (4/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 4 | 100% | +0.61% | +0.01 to +1.22% | 67% of 3 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 4 | 50% | +0.06% | -0.63 to +0.58% | 50% of 2 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 100% | +0.79% | +0.14 to +1.65% | 0% of 1 | too few (4/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 4 | 100% | +0.50% | +0.37 to +0.62% | 0% of 1 | too few (4/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 3 | 67% | -0.01% | -0.63 to +0.40% | 0% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 3 | 67% | +0.08% | -0.07 to +0.27% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 3 | 50% | -0.03% | -0.43 to +0.37% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near put wall | 3 | 67% | -0.09% | -1.22 to +0.65% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 3 | 33% | -0.01% | -0.37 to +0.53% | 50% of 2 | too few (3/10) |
| weekly | PCR up · call writing · walls down · mid walls | 3 | 67% | +0.18% | -0.61 to +0.64% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 3 | 67% | -0.03% | -0.44 to +0.19% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 3 | 67% | +0.08% | -0.04 to +0.18% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 3 | 100% | +0.28% | +0.07 to +0.50% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 3 | 100% | +0.12% | +0.05 to +0.16% | 100% of 2 | too few (3/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 3 | 50% | -0.15% | -0.33 to +0.03% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 3 | 67% | +0.38% | -0.18 to +0.91% | 50% of 2 | too few (3/10) |
| monthly | PCR down · call writing · walls same · near put wall | 2 | 0% | -0.07% | -0.07 to -0.07% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 2 | 50% | -0.57% | -1.32 to +0.18% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · call writing · walls up · near put wall | 2 | 50% | +0.40% | -0.23 to +1.02% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls same · mid walls | 2 | 100% | +0.30% | +0.29 to +0.31% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.29% | +0.19 to +0.40% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 2 | 50% | -0.15% | -0.30 to +0.01% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 2 | 50% | -0.01% | -0.24 to +0.21% | 100% of 1 | too few (2/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 2 | 50% | -0.10% | -0.29 to +0.09% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% | 0% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 50% of 2 | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 2 | 50% | +0.18% | -0.20 to +0.57% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · mid walls | 2 | 50% | +0.04% | -0.19 to +0.28% | 100% of 2 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near put wall | 2 | 100% | +0.21% | +0.18 to +0.24% | 100% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 2 | 50% | -0.08% | -0.49 to +0.34% |  | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls down · near call wall | 2 | 100% | +0.09% | +0.02 to +0.16% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 2 | 100% | +0.20% | +0.20 to +0.20% | 100% of 2 | too few (1/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.20% | -0.20 to -0.20% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.14% | +1.14 to +1.14% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near put wall | 1 | 0% | -0.44% | -0.44 to -0.44% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +1.86% | +1.86 to +1.86% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls down · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -1.33% | -1.33 to -1.33% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% | 0% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls same · mid walls | 1 | 100% | +0.49% | +0.49 to +0.49% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.40% | +0.40 to +0.40% | 100% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near put wall | 1 | 0% | -0.29% | -0.29 to -0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · quiet OI · walls same · near put wall | 1 | 0% | -0.83% | -0.83 to -0.83% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · mid walls | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | +0.30% | -0.61 to +1.12% | 100% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 3 | 50% | +0.53% | -0.63 to +1.68% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 100% | +0.61% | +0.06 to +1.12% | 100% of 3 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | +0.73% | -0.39 to +2.40% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 2 | 0% | -1.15% | -1.75 to -0.54% | 100% of 2 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 100% | +0.55% | +0.51 to +0.58% | 50% of 2 | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.45% | +0.25 to +0.65% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 2 | 50% | +0.02% | -0.63 to +0.68% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -1.75% | -1.75 to -1.75% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 | 100% | +1.85% | +1.85 to +1.85% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 | 0% | -0.74% | -0.74 to -0.74% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.58% | +0.58 to +0.58% | 100% of 1 | too few (1/10) |
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
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 0% | -0.74% | -0.74 to -0.74% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 191 | 64% | +0.14% | up |
| intraday | weekly | writers even · few weak writers | 143 | 56% | +0.06% | no clear direction |
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
| day | monthly | writers even · few weak writers | 16 | 53% | +0.17% | no clear direction |
| day | weekly | writers even · few weak writers | 10 | 67% | +0.45% | too few (9/10) |
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
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 73 | 60% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 67 | 51% | -0.04% | no clear direction |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 57 | 78% | +0.39% | up |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 49 | 85% | +0.68% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 45 | 93% | +0.31% | up |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m up | 41 | 46% | -0.03% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 28 | 77% | +0.29% | up |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 24 | 55% | +0.22% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 24 | 67% | +0.27% | no clear direction |
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
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 6 | 50% | -0.23% | too few (6/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 4 | 75% | +0.07% | too few (4/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 4 | 50% | -0.18% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 3 | 100% | +0.86% | too few (2/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +1.32% | too few (2/10) |
| day | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +1.14% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m up | 2 | 50% | -0.22% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
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
