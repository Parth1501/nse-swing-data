# Nifty option chain pattern log
Updated 2026-11-26 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 711 snapshots over 29 trading days
- 788 patterns logged; 196 different patterns so far

## Latest read (2026-11-26 13:49:35)

Nifty trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-01 (weekly) | 5.1 | 25836 | 0.891 | 25800 | 25000 | 26000 | ±1.44% (25464-26208) | 15.38 |
| 2026-12-29 (monthly) | 33.1 | 25842 | 0.898 | 25500 | 25000 | 26000 | ±3.51% (24935-26749) | 14.43 |

- **Weekly, last 30 min**: `PCR flat · call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 132 times before; Nifty was up after it 56% of the time, average +0.07%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 57 times before; Nifty was up after it 48% of the time, average -0.03%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 8 times before; Nifty was up after it 75% of the time, average +0.58%. Too few outcomes (8/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Nifty was up after it 67% of the time, average -0.06%. Too few outcomes (3/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls down · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.02%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 180 times before; Nifty was up after it 64% of the time, average +0.16%. History points to a bull call debit spread, ATM to about the call wall 26000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 63 times before; Nifty was up after it 60% of the time, average +0.12%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 14 times before; Nifty was up after it 57% of the time, average +0.22%. Too few outcomes (14/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 5 times before; Nifty was up after it 60% of the time, average -0.16%. Too few outcomes (5/20) to trade on.

## Strong vs weak writers, weekly 2026-12-01

Strongest call writers at 25900, strongest put writers at 25600; weakest call writers at 25550, weakest put writers at 26200. Covers 64% of near-money call OI and 83% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25450 | 4223 | 295 | 450.2 | 25819 | 452.7 | 25900 | +64 | -2.5 | medium |
| Call | 25500 | 41457 | 3499 | 426.5 | 25839 | 415.4 | 25926 | +91 | +11.1 | medium |
| Call | 25550 | 5202 | 1699 | 318.0 | 25681 | 375.4 | 25868 | +32 | -57.4 | weak |
| Call | 25600 | 19818 | 4548 | 308.2 | 25724 | 341.4 | 25908 | +72 | -33.2 | medium |
| Call | 25650 | 7991 | 5192 | 273.0 | 25720 | 306.8 | 25923 | +87 | -33.8 | medium |
| Call | 25700 | 30826 | 20157 | 258.7 | 25725 | 273.9 | 25959 | +123 | -15.3 | strong |
| Call | 25750 | 20389 | 18916 | 234.3 | 25746 | 243.1 | 25984 | +148 | -8.8 | strong |
| Call | 25800 | 80498 | 63021 | 201.5 | 25756 | 214.9 | 26001 | +166 | -13.4 | strong |
| Call | 25850 | 51762 | 49175 | 188.1 | 25803 | 187.7 | 26038 | +202 | +0.4 | strong |
| Call | 25900 | 114839 | 94609 | 177.1 | 25806 | 164.3 | 26077 | +241 | +12.8 | strong |
| Call | 25950 | 60549 | 54689 | 185.5 | 25857 | 141.9 | 26135 | +300 | +43.5 | strong |
| Call | 26000 | 174200 | 92641 | 135.4 | 25780 | 122.2 | 26135 | +299 | +13.2 | strong |
| Call | 26050 | 34356 | 30375 | 127.2 | 25819 | 103.8 | 26177 | +341 | +23.4 | strong |
| Call | 26100 | 67534 | 45459 | 106.3 | 25805 | 88.5 | 26206 | +370 | +17.8 | strong |
| Call | 26150 | 35930 | 31373 | 94.8 | 25811 | 74.2 | 26245 | +409 | +20.6 | strong |
| Call | 26200 | 88352 | 57534 | 78.3 | 25752 | 62.5 | 26278 | +442 | +15.9 | strong |
| Put | 25450 | 30253 | 26440 | 80.7 | 25822 | 53.5 | 25369 | +467 | +27.2 | strong |
| Put | 25500 | 119611 | 82265 | 96.7 | 25809 | 63.9 | 25403 | +433 | +32.9 | strong |
| Put | 25550 | 24970 | 22614 | 110.1 | 25803 | 74.9 | 25440 | +396 | +35.2 | strong |
| Put | 25600 | 116754 | 101632 | 104.5 | 25867 | 88.1 | 25495 | +340 | +16.4 | strong |
| Put | 25650 | 35266 | 33939 | 151.8 | 25786 | 103.5 | 25498 | +338 | +48.3 | strong |
| Put | 25700 | 84675 | 75567 | 170.6 | 25790 | 121.0 | 25529 | +307 | +49.7 | strong |
| Put | 25750 | 43187 | 42270 | 201.1 | 25766 | 140.6 | 25549 | +287 | +60.6 | strong |
| Put | 25800 | 111470 | 100557 | 218.0 | 25784 | 161.0 | 25582 | +254 | +57.0 | strong |
| Put | 25850 | 45355 | 44968 | 219.2 | 25826 | 184.2 | 25631 | +205 | +35.0 | strong |
| Put | 25900 | 69229 | 67240 | 233.0 | 25848 | 209.9 | 25667 | +169 | +23.1 | strong |
| Put | 25950 | 26647 | 26516 | 210.8 | 25912 | 237.7 | 25739 | +97 | -26.9 | medium |
| Put | 26000 | 51629 | 40145 | 270.0 | 25875 | 267.9 | 25730 | +106 | +2.1 | medium |
| Put | 26050 | 4827 | 4722 | 276.6 | 25902 | 302.1 | 25773 | +63 | -25.4 | medium |
| Put | 26100 | 8709 | 7679 | 321.3 | 25885 | 335.0 | 25779 | +57 | -13.7 | medium |
| Put | 26150 | 1926 | 1750 | 343.9 | 25899 | 373.9 | 25806 | +30 | -30.0 | weak |
| Put | 26200 | 6479 | 3620 | 390.0 | 25881 | 409.6 | 25810 | +26 | -19.6 | weak |

## Strong vs weak writers, monthly 2026-12-29

Strongest call writers at 26000, strongest put writers at 25500; weakest call writers at 25300, weakest put writers at -. Covers 59% of near-money call OI and 60% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25500 | 60932 | 30273 | 518.0 | 25451 | 729.8 | 26018 | +176 | -211.8 | strong |
| Call | 25550 | 805 | 609 | 463.9 | 25404 | 673.1 | 26014 | +172 | -209.2 | strong |
| Call | 25600 | 15376 | 12641 | 494.8 | 25515 | 661.3 | 26095 | +253 | -166.5 | strong |
| Call | 25650 | 768 | 515 | 466.0 | 25502 | 626.0 | 26116 | +274 | -160.0 | strong |
| Call | 25700 | 14560 | 12416 | 488.2 | 25599 | 600.0 | 26188 | +346 | -111.8 | strong |
| Call | 25750 | 1611 | 1457 | 488.7 | 25645 | 573.1 | 26239 | +397 | -84.4 | strong |
| Call | 25800 | 24694 | 22324 | 403.2 | 25527 | 539.7 | 26203 | +361 | -136.5 | strong |
| Call | 25850 | 1317 | 1216 | 462.0 | 25710 | 513.5 | 26312 | +470 | -51.4 | strong |
| Call | 25900 | 12623 | 11485 | 451.4 | 25725 | 486.0 | 26351 | +509 | -34.6 | strong |
| Call | 25950 | 1824 | 1712 | 458.4 | 25783 | 457.4 | 26408 | +566 | +0.9 | strong |
| Call | 26000 | 94042 | 38885 | 330.2 | 25554 | 432.1 | 26330 | +488 | -101.9 | strong |
| Call | 26050 | 807 | 651 | 353.9 | 25664 | 413.9 | 26404 | +562 | -60.1 | strong |
| Call | 26100 | 8515 | 6677 | 300.1 | 25569 | 385.0 | 26400 | +558 | -84.9 | strong |
| Call | 26150 | 520 | 334 | 292.9 | 25599 | 361.6 | 26443 | +601 | -68.8 | strong |
| Call | 26200 | 9253 | 5852 | 295.6 | 25669 | 340.4 | 26496 | +653 | -44.9 | strong |
| Put | 25500 | 98924 | 52147 | 403.5 | 25510 | 263.2 | 25097 | +746 | +140.3 | strong |
| Put | 25550 | 937 | 773 | 425.8 | 25510 | 276.4 | 25124 | +718 | +149.4 | strong |
| Put | 25600 | 20380 | 17349 | 432.0 | 25568 | 297.1 | 25168 | +674 | +135.0 | strong |
| Put | 25650 | 982 | 926 | 421.9 | 25628 | 308.4 | 25228 | +614 | +113.4 | strong |
| Put | 25700 | 15074 | 14468 | 432.7 | 25652 | 332.5 | 25267 | +575 | +100.2 | strong |
| Put | 25750 | 5513 | 5376 | 413.5 | 25744 | 349.2 | 25336 | +506 | +64.3 | strong |
| Put | 25800 | 18425 | 17752 | 466.5 | 25688 | 372.8 | 25333 | +509 | +93.8 | strong |
| Put | 25850 | 1079 | 1055 | 451.0 | 25755 | 393.4 | 25399 | +443 | +57.6 | strong |
| Put | 25900 | 10957 | 10701 | 459.4 | 25793 | 416.1 | 25441 | +402 | +43.3 | strong |
| Put | 25950 | 679 | 641 | 464.5 | 25826 | 440.0 | 25485 | +357 | +24.5 | strong |
| Put | 26000 | 74685 | 25870 | 538.6 | 25721 | 460.9 | 25461 | +381 | +77.7 | strong |
| Put | 26050 | 449 | 376 | 523.9 | 25802 | 479.7 | 25526 | +316 | +44.2 | strong |
| Put | 26100 | 4759 | 4415 | 623.7 | 25659 | 502.1 | 25476 | +366 | +121.7 | strong |
| Put | 26150 | 236 | 210 | 667.8 | 25637 | 549.2 | 25482 | +360 | +118.6 | strong |
| Put | 26200 | 2908 | 2670 | 624.3 | 25759 | 564.9 | 25576 | +267 | +59.5 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 47 | 62% | +0.21% | -0.44 to +0.97% | 50% of 2 | no clear direction |
| weekly | PCR up · put writing · walls same · near call wall | 23 | 78% | +0.22% | -0.36 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 22 | 86% | +0.39% | -0.50 to +1.68% | 0% of 1 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 20 | 79% | +0.33% | -0.49 to +1.02% | 50% of 2 | up |
| weekly | PCR down · call writing · walls same · near put wall | 20 | 60% | +0.13% | -1.00 to +0.85% | 60% of 5 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 18 | 56% | +0.06% | -0.61 to +0.80% | 60% of 5 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near call wall | 16 | 56% | +0.28% | -0.71 to +1.70% | 50% of 2 | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near put wall | 16 | 79% | +0.12% | -0.28 to +0.90% | 0% of 1 | up |
| monthly | PCR flat · put writing · walls same · near call wall | 13 | 73% | +0.36% | -0.50 to +1.56% | 0% of 1 | no clear direction |
| weekly | PCR down · unwinding · walls same · near call wall | 13 | 67% | +0.32% | -0.17 to +1.52% | 25% of 4 | no clear direction |
| weekly | PCR up · put writing · walls same · mid walls | 13 | 62% | +0.16% | -0.57 to +0.89% | 75% of 4 | no clear direction |
| weekly | PCR down · unwinding · walls same · mid walls | 13 | 67% | +0.06% | -0.40 to +0.90% | 80% of 5 | too few (9/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 12 | 75% | +0.17% | -0.24 to +0.63% | 50% of 2 | no clear direction |
| monthly | PCR down · quiet OI · walls same · mid walls | 12 | 70% | +0.21% | -0.36 to +0.70% | 0% of 1 | no clear direction |
| monthly | PCR up · quiet OI · walls same · mid walls | 11 | 82% | +0.23% | -0.39 to +0.91% | 50% of 2 | up |
| weekly | PCR up · put and call writing · walls same · mid walls | 11 | 45% | +0.06% | -0.78 to +0.90% | 100% of 2 | no clear direction |
| weekly | PCR down · call writing · walls same · mid walls | 11 | 82% | +0.21% | -0.43 to +0.75% | 40% of 5 | up |
| monthly | PCR up · put writing · walls same · near call wall | 11 | 50% | +0.18% | -0.40 to +0.93% | 50% of 2 | no clear direction |
| monthly | PCR down · put and call writing · walls same · mid walls | 10 | 80% | +0.28% | -0.21 to +1.13% | 50% of 2 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · mid walls | 10 | 57% | +0.11% | -0.16 to +0.71% | 50% of 2 | too few (7/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 10 | 60% | +0.01% | -1.01 to +1.12% | 100% of 1 | no clear direction |
| monthly | PCR flat · put writing · walls same · near put wall | 10 | 75% | +0.13% | -0.83 to +0.98% | 0% of 1 | too few (8/10) |
| monthly | PCR down · call writing · walls same · mid walls | 9 | 44% | +0.02% | -0.47 to +0.49% | 50% of 2 | too few (9/10) |
| weekly | PCR down · call writing · walls down · mid walls | 9 | 78% | +0.24% | -0.07 to +0.54% | 67% of 3 | too few (9/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 9 | 78% | +0.31% | -1.22 to +1.24% | 67% of 3 | too few (9/10) |
| monthly | PCR up · put writing · walls same · mid walls | 8 | 75% | +0.42% | -0.29 to +0.85% | 50% of 2 | too few (8/10) |
| weekly | PCR up · put writing · walls up · near put wall | 8 | 62% | +0.33% | -0.13 to +1.65% | 0% of 4 | too few (8/10) |
| weekly | PCR up · put writing · walls up · mid walls | 8 | 62% | +0.31% | -0.26 to +1.40% | 33% of 3 | too few (8/10) |
| monthly | PCR down · call writing · walls same · near call wall | 8 | 83% | +0.27% | -0.78 to +1.18% | 50% of 2 | too few (6/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% | 0% of 1 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.02% | -0.74 to +0.62% | 50% of 2 | too few (7/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 7 | 86% | +0.50% | -0.37 to +1.25% | 50% of 2 | too few (7/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 7 | 43% | -0.05% | -0.89 to +0.90% | 67% of 3 | too few (7/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 7 | 83% | +0.23% | -0.05 to +0.63% | 67% of 3 | too few (6/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 7 | 86% | +0.29% | -0.11 to +0.62% | 50% of 4 | too few (7/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 7 | 71% | +0.53% | -1.02 to +1.82% | 50% of 4 | too few (7/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 6 | 20% | +0.00% | -0.29 to +0.43% | 33% of 3 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near call wall | 6 | 83% | +0.53% | -0.06 to +1.68% | 67% of 3 | too few (6/10) |
| weekly | PCR down · call writing · walls same · near call wall | 6 | 83% | +0.50% | -0.02 to +0.91% | 33% of 3 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 6 | 67% | -0.08% | -1.07 to +0.28% | 100% of 1 | too few (6/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 6 | 67% | +0.34% | -1.11 to +1.69% | 0% of 2 | too few (6/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 6 | 100% | +0.54% | +0.47 to +0.61% | 67% of 3 | too few (3/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 6 | 83% | +0.21% | -0.17 to +0.59% | 0% of 4 | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 5 | 80% | +0.26% | -0.02 to +0.90% | 33% of 3 | too few (5/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 5 | 80% | +0.40% | -0.02 to +1.17% | 50% of 2 | too few (5/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 5 | 40% | +0.06% | -0.68 to +0.75% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 5 | 100% | +0.19% | +0.16 to +0.25% | 67% of 3 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 5 | 60% | +0.15% | -0.07 to +0.33% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near put wall | 5 | 60% | +0.09% | -0.51 to +0.73% | 0% of 2 | too few (5/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 5 | 80% | +0.21% | -0.22 to +0.68% | 60% of 5 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 50% of 2 | too few (5/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 4 | 25% | -0.02% | -0.69 to +0.99% | 50% of 2 | too few (4/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 4 | 100% | +0.15% | +0.06 to +0.25% | 100% of 1 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 50% of 2 | too few (4/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 4 | 100% | +0.61% | +0.01 to +1.22% | 67% of 3 | too few (2/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 100% | +0.79% | +0.14 to +1.65% | 0% of 1 | too few (4/10) |
| monthly | PCR flat · quiet OI · walls up · near put wall | 4 | 0% | -0.25% | -0.61 to -0.05% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 4 | 100% | +0.60% | +0.23 to +0.85% | 0% of 1 | too few (4/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 4 | 100% | +0.50% | +0.37 to +0.62% | 0% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 4 |  |  |  | 100% of 4 | too few (0/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 4 | 50% | +0.06% | -0.63 to +0.58% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 3 | 50% | -0.03% | -0.43 to +0.37% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 3 | 100% | +0.12% | +0.05 to +0.16% | 100% of 2 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 3 | 67% | +0.08% | -0.07 to +0.27% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 3 | 67% | -0.09% | -1.22 to +0.65% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 3 | 67% | -0.03% | -0.44 to +0.19% | 0% of 1 | too few (3/10) |
| weekly | PCR up · call writing · walls down · mid walls | 3 | 67% | +0.18% | -0.61 to +0.64% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 3 | 67% | +0.38% | -0.18 to +0.91% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 3 | 33% | -0.01% | -0.37 to +0.53% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 3 | 50% | -0.15% | -0.33 to +0.03% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 3 | 100% | +0.28% | +0.07 to +0.50% | 100% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 3 | 67% | +0.08% | -0.04 to +0.18% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| monthly | PCR down · call writing · walls same · near put wall | 2 | 0% | -0.07% | -0.07 to -0.07% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 2 | 50% | +0.18% | -0.20 to +0.57% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 2 | 100% | +0.20% | +0.20 to +0.20% | 100% of 2 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 2 | 50% | -0.15% | -0.30 to +0.01% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 2 | 50% | -0.57% | -1.32 to +0.18% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 2 | 50% | -0.11% | -0.42 to +0.21% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 2 | 50% | -0.08% | -0.49 to +0.34% |  | too few (2/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 2 | 50% | -0.10% | -0.29 to +0.09% | 0% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 50% of 2 | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near put wall | 2 | 100% | +0.21% | +0.18 to +0.24% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 50% of 2 | too few (2/10) |
| monthly | PCR up · call writing · walls same · mid walls | 2 | 50% | +0.04% | -0.19 to +0.28% | 100% of 2 | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls down · near call wall | 2 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 2 | 100% | +0.30% | +0.29 to +0.31% | 100% of 2 | too few (2/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.20% | -0.20 to -0.20% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.14% | +1.14 to +1.14% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near put wall | 1 | 0% | -0.44% | -0.44 to -0.44% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls down · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -1.33% | -1.33 to -1.33% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +1.86% | +1.86 to +1.86% | 0% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls same · mid walls | 1 | 100% | +0.49% | +0.49 to +0.49% | 100% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.40% | +0.40 to +0.40% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · near put wall | 1 | 100% | +1.02% | +1.02 to +1.02% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
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
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | +0.30% | -0.61 to +1.12% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 100% | +0.61% | +0.06 to +1.12% | 100% of 3 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 50% of 2 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | +0.73% | -0.39 to +2.40% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.53% | -0.63 to +1.68% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 100% | +0.55% | +0.51 to +0.58% | 50% of 2 | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.36% | +0.06 to +0.65% | 100% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 2 | 0% | -1.15% | -1.75 to -0.54% | 100% of 2 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 2 | 50% | +0.02% | -0.63 to +0.68% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -1.75% | -1.75 to -1.75% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.58% | +0.58 to +0.58% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 | 100% | +1.85% | +1.85 to +1.85% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
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
| intraday | monthly | writers even · few weak writers | 181 | 64% | +0.16% | up |
| intraday | weekly | writers even · few weak writers | 133 | 56% | +0.07% | no clear direction |
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
| day | monthly | writers even · few weak writers | 15 | 57% | +0.22% | no clear direction |
| day | weekly | writers even · few weak writers | 9 | 75% | +0.58% | too few (8/10) |
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
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 64 | 60% | +0.12% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 58 | 48% | -0.03% | no clear direction |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 57 | 78% | +0.39% | up |
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
| intraday | weekly | put writers stronger · few weak writers · weekly sideways · 125m up | 10 | 70% | +0.47% | no clear direction |
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
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 6 | 60% | -0.16% | too few (5/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 4 | 75% | +0.07% | too few (4/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 4 | 67% | -0.06% | too few (3/10) |
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
