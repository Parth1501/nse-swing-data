# Nifty option chain pattern log
Updated 2026-11-19 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 616 snapshots over 25 trading days
- 683 patterns logged; 182 different patterns so far

## Latest read (2026-11-19 14:45:28)

Nifty trend: weekly **sideways**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-23 (weekly) | 4.0 | 25458 | 1.211 | 25300 | 25000 | 26000 | ±1.07% (25184-25731) | 12.8 |
| 2026-12-29 (monthly) | 40.0 | 25450 | 1.117 | 25300 | 24000 | 26000 | ±3.64% (24524-26376) | 13.65 |

- **Weekly, last 30 min**: `PCR up · put writing · walls same · mid walls`. Seen 10 times before; Nifty was up after it 60% of the time, average +0.08%. Too few outcomes (10/20) to trade on.
  - Writers: `put writers stronger · few weak writers`. Seen 31 times before; Nifty was up after it 93% of the time, average +0.34%. History points to a bull call debit spread, ATM to about the call wall 26000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Nifty was up after it 100% of the time, average +0.35%. Too few outcomes (3/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put writing · walls up · mid walls`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.35%. Too few outcomes (2/20) to trade on.
  - Writers: `put writers stronger · few weak writers`. Seen 3 times before; Nifty was up after it 100% of the time, average +0.95%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put writing · walls same · near call wall`. Seen 12 times before; Nifty was up after it 70% of the time, average +0.38%. Too few outcomes (10/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 132 times before; Nifty was up after it 67% of the time, average +0.16%. History points to a bull call debit spread, ATM to about the call wall 26000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 23 times before; Nifty was up after it 57% of the time, average +0.05%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR down · put and call writing · walls same · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +1.58%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 11 times before; Nifty was up after it 55% of the time, average +0.31%. Too few outcomes (11/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Nifty was up after it 50% of the time, average -0.12%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-23

Strongest call writers at 26000, strongest put writers at 25000; weakest call writers at 25300, weakest put writers at -. Covers 99% of near-money call OI and 99% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25100 | 22737 | 22724 | 226.5 | 25173 | 416.9 | 25326 | -131 | -190.4 | weak |
| Call | 25150 | 12335 | 12334 | 184.6 | 25213 | 373.4 | 25335 | -123 | -188.8 | weak |
| Call | 25200 | 54956 | 54949 | 176.7 | 25204 | 331.4 | 25377 | -81 | -154.8 | weak |
| Call | 25250 | 25124 | 25124 | 159.1 | 25233 | 291.3 | 25409 | -48 | -132.2 | weak |
| Call | 25300 | 86599 | 86596 | 151.7 | 25235 | 252.2 | 25452 | -6 | -100.6 | weak |
| Call | 25350 | 36651 | 36608 | 125.5 | 25249 | 217.7 | 25476 | +18 | -92.2 | weak |
| Call | 25400 | 98247 | 98023 | 125.4 | 25270 | 185.1 | 25525 | +68 | -59.7 | medium |
| Call | 25450 | 47775 | 47771 | 120.9 | 25299 | 155.6 | 25571 | +113 | -34.7 | medium |
| Call | 25500 | 159654 | 157733 | 98.0 | 25172 | 128.8 | 25598 | +140 | -30.8 | strong |
| Call | 25550 | 36456 | 36401 | 74.8 | 25259 | 105.5 | 25625 | +167 | -30.7 | strong |
| Call | 25600 | 75906 | 75879 | 82.7 | 25261 | 85.1 | 25683 | +225 | -2.4 | strong |
| Call | 25650 | 32902 | 32902 | 52.9 | 25269 | 68.2 | 25703 | +245 | -15.3 | strong |
| Call | 25700 | 88785 | 88707 | 52.4 | 25257 | 54.0 | 25752 | +295 | -1.6 | strong |
| Call | 25750 | 29764 | 29633 | 37.2 | 25284 | 41.9 | 25787 | +330 | -4.6 | strong |
| Call | 25800 | 77716 | 77444 | 40.9 | 25265 | 32.5 | 25841 | +383 | +8.3 | strong |
| Put | 25100 | 115061 | 114435 | 100.7 | 25270 | 29.0 | 24999 | +458 | +71.7 | strong |
| Put | 25150 | 68070 | 68070 | 118.7 | 25246 | 35.6 | 25031 | +426 | +83.1 | strong |
| Put | 25200 | 188351 | 188342 | 139.0 | 25268 | 43.8 | 25061 | +397 | +95.2 | strong |
| Put | 25250 | 94583 | 94581 | 143.5 | 25280 | 53.5 | 25107 | +351 | +90.0 | strong |
| Put | 25300 | 200339 | 200313 | 156.3 | 25302 | 65.3 | 25144 | +314 | +90.9 | strong |
| Put | 25350 | 116925 | 116924 | 137.1 | 25354 | 79.6 | 25213 | +245 | +57.5 | strong |
| Put | 25400 | 134142 | 133475 | 160.6 | 25372 | 97.0 | 25239 | +218 | +63.7 | strong |
| Put | 25450 | 52150 | 52148 | 155.7 | 25418 | 117.5 | 25294 | +163 | +38.2 | strong |
| Put | 25500 | 104666 | 100000 | 288.7 | 25321 | 141.1 | 25211 | +246 | +147.6 | strong |
| Put | 25550 | 10422 | 10420 | 223.1 | 25400 | 167.8 | 25327 | +131 | +55.3 | strong |
| Put | 25600 | 17273 | 17251 | 289.1 | 25386 | 196.8 | 25311 | +147 | +92.2 | strong |
| Put | 25650 | 2670 | 2668 | 302.5 | 25388 | 229.2 | 25347 | +110 | +73.3 | medium |
| Put | 25700 | 7612 | 7595 | 382.9 | 25356 | 265.9 | 25317 | +140 | +116.9 | strong |
| Put | 25750 | 1647 | 1646 | 382.6 | 25407 | 303.8 | 25367 | +90 | +78.8 | medium |
| Put | 25800 | 5308 | 5200 | 481.1 | 25342 | 344.0 | 25319 | +139 | +137.1 | strong |

## Strong vs weak writers, monthly 2026-12-29

Strongest call writers at 25500, strongest put writers at 25500; weakest call writers at -, weakest put writers at -. Covers 21% of near-money call OI and 21% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25100 | 1908 | 389 | 601.4 | 25229 | 790.0 | 25701 | +251 | -188.6 | strong |
| Call | 25150 | 257 | 81 | 566.5 | 25205 | 756.0 | 25717 | +266 | -189.5 | strong |
| Call | 25200 | 7801 | 2158 | 548.2 | 25228 | 723.6 | 25748 | +298 | -175.4 | strong |
| Call | 25250 | 677 | 440 | 521.8 | 25233 | 703.9 | 25772 | +321 | -182.1 | strong |
| Call | 25300 | 7485 | 2896 | 497.3 | 25237 | 656.2 | 25797 | +347 | -158.9 | strong |
| Call | 25350 | 854 | 335 | 474.7 | 25231 | 630.0 | 25825 | +374 | -155.3 | strong |
| Call | 25400 | 7130 | 3469 | 452.4 | 25248 | 595.0 | 25852 | +402 | -142.6 | strong |
| Call | 25450 | 1338 | 602 | 418.4 | 25223 | 561.4 | 25868 | +418 | -143.0 | strong |
| Call | 25500 | 58276 | 15779 | 412.8 | 25252 | 532.5 | 25913 | +462 | -119.7 | strong |
| Call | 25550 | 1328 | 798 | 382.6 | 25246 | 509.1 | 25933 | +482 | -126.6 | strong |
| Call | 25600 | 6581 | 2422 | 374.2 | 25266 | 477.3 | 25974 | +524 | -103.1 | strong |
| Call | 25650 | 868 | 301 | 349.4 | 25252 | 449.5 | 25999 | +549 | -100.2 | strong |
| Call | 25700 | 3915 | 1065 | 336.9 | 25291 | 423.9 | 26037 | +587 | -86.9 | strong |
| Call | 25750 | 361 | 137 | 326.4 | 25307 | 403.9 | 26076 | +626 | -77.5 | strong |
| Call | 25800 | 6775 | 3430 | 277.1 | 25228 | 376.9 | 26077 | +627 | -99.8 | strong |
| Put | 25100 | 2819 | 501 | 318.4 | 25257 | 245.9 | 24782 | +669 | +72.4 | strong |
| Put | 25150 | 421 | 146 | 335.1 | 25267 | 259.6 | 24815 | +635 | +75.5 | strong |
| Put | 25200 | 10327 | 4251 | 365.9 | 25240 | 277.4 | 24834 | +616 | +88.4 | strong |
| Put | 25250 | 1032 | 524 | 379.9 | 25254 | 290.6 | 24870 | +580 | +89.3 | strong |
| Put | 25300 | 10566 | 2720 | 397.2 | 25264 | 309.0 | 24903 | +548 | +88.2 | strong |
| Put | 25350 | 901 | 455 | 405.4 | 25293 | 325.2 | 24945 | +506 | +80.1 | strong |
| Put | 25400 | 17811 | 9122 | 439.6 | 25274 | 347.7 | 24960 | +490 | +91.9 | strong |
| Put | 25450 | 1037 | 609 | 447.2 | 25300 | 364.7 | 25003 | +448 | +82.5 | strong |
| Put | 25500 | 75724 | 20393 | 478.8 | 25282 | 386.9 | 25021 | +429 | +92.0 | strong |
| Put | 25550 | 1133 | 733 | 515.3 | 25263 | 405.9 | 25035 | +416 | +109.3 | strong |
| Put | 25600 | 5884 | 1896 | 514.9 | 25303 | 430.1 | 25085 | +365 | +84.9 | strong |
| Put | 25650 | 383 | 219 | 529.1 | 25247 | 451.1 | 25121 | +330 | +78.1 | strong |
| Put | 25700 | 1424 | 689 | 549.3 | 25329 | 474.0 | 25151 | +300 | +75.3 | strong |
| Put | 25750 | 191 | 43 | 582.8 | 25310 | 496.1 | 25167 | +283 | +86.6 | strong |
| Put | 25800 | 1188 | 433 | 598.6 | 25338 | 524.2 | 25201 | +249 | +74.3 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 39 | 68% | +0.25% | -0.44 to +0.97% | 100% of 1 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 22 | 86% | +0.34% | -0.50 to +1.68% |  | up |
| weekly | PCR up · put writing · walls same · near call wall | 20 | 85% | +0.28% | -0.27 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 19 | 83% | +0.36% | -0.42 to +1.02% | 100% of 1 | up |
| weekly | PCR down · call writing · walls same · near put wall | 18 | 67% | +0.24% | -0.37 to +0.85% | 50% of 4 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near call wall | 16 | 56% | +0.28% | -0.71 to +1.70% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 15 | 60% | +0.08% | -0.47 to +0.58% | 50% of 4 | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 | 82% | +0.08% | -0.18 to +0.20% |  | up |
| monthly | PCR flat · put writing · walls same · near call wall | 13 | 70% | +0.38% | -0.50 to +1.56% |  | no clear direction |
| weekly | PCR down · unwinding · walls same · near call wall | 11 | 70% | +0.39% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| monthly | PCR up · put writing · walls same · near call wall | 11 | 50% | +0.18% | -0.40 to +0.93% | 100% of 1 | no clear direction |
| monthly | PCR up · put and call writing · walls same · mid walls | 11 | 73% | +0.15% | -0.24 to +0.63% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · mid walls | 11 | 60% | +0.08% | -0.57 to +0.89% | 67% of 3 | no clear direction |
| weekly | PCR down · call writing · walls same · mid walls | 10 | 80% | +0.21% | -0.43 to +0.75% | 50% of 4 | no clear direction |
| monthly | PCR up · quiet OI · walls same · mid walls | 10 | 80% | +0.24% | -0.39 to +0.91% | 100% of 1 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · mid walls | 10 | 57% | +0.11% | -0.16 to +0.71% | 100% of 1 | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 10 | 80% | +0.26% | -0.21 to +0.90% | 100% of 1 | no clear direction |
| weekly | PCR up · put and call writing · walls same · mid walls | 10 | 40% | +0.03% | -0.78 to +0.90% | 100% of 2 | no clear direction |
| weekly | PCR down · unwinding · walls same · mid walls | 10 | 50% | +0.04% | -0.40 to +0.90% | 75% of 4 | too few (6/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| weekly | PCR down · call writing · walls down · mid walls | 9 | 78% | +0.24% | -0.07 to +0.54% | 67% of 3 | too few (9/10) |
| monthly | PCR down · call writing · walls same · near call wall | 8 | 83% | +0.27% | -0.78 to +1.18% | 100% of 1 | too few (6/10) |
| monthly | PCR down · call writing · walls same · mid walls | 8 | 38% | +0.01% | -0.47 to +0.49% | 100% of 1 | too few (8/10) |
| weekly | PCR up · put writing · walls up · mid walls | 8 | 62% | +0.31% | -0.26 to +1.40% | 33% of 3 | too few (8/10) |
| monthly | PCR up · put writing · walls same · mid walls | 8 | 75% | +0.42% | -0.29 to +0.85% | 100% of 1 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% |  | too few (6/10) |
| weekly | PCR up · put writing · walls up · near put wall | 8 | 62% | +0.33% | -0.13 to +1.65% | 0% of 4 | too few (8/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 8 | 75% | +0.21% | -1.22 to +1.24% | 50% of 2 | too few (8/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (7/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 7 | 86% | +0.50% | -0.37 to +1.25% | 100% of 1 | too few (7/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 6 | 83% | +0.25% | -0.11 to +0.50% | 33% of 3 | too few (6/10) |
| weekly | PCR down · call writing · walls down · near call wall | 6 | 83% | +0.53% | -0.06 to +1.68% | 67% of 3 | too few (6/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 6 | 80% | +0.18% | -0.05 to +0.63% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 5 | 100% | +0.29% | +0.04 to +0.59% | 0% of 4 | too few (5/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 5 | 80% | +0.86% | -0.07 to +1.82% | 33% of 3 | too few (5/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 5 | 80% | +0.12% | -0.05 to +0.28% |  | too few (5/10) |
| weekly | PCR down · call writing · walls down · near put wall | 5 | 60% | +0.09% | -0.51 to +0.73% | 0% of 2 | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 5 | 60% | +0.15% | -0.07 to +0.33% |  | too few (5/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 5 | 100% | +0.54% | +0.47 to +0.61% | 67% of 3 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 5 | 40% | +0.06% | -0.68 to +0.75% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 5 | 40% | +0.02% | -0.75 to +0.67% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 5 | 80% | +0.46% | -1.11 to +1.69% | 0% of 2 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 5 | 25% | +0.07% | -0.10 to +0.43% | 33% of 3 | too few (4/10) |
| weekly | PCR down · call writing · walls same · near call wall | 5 | 80% | +0.53% | -0.02 to +0.91% | 33% of 3 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 100% of 1 | too few (5/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 100% | +0.79% | +0.14 to +1.65% |  | too few (4/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 4 | 50% | +0.06% | -0.63 to +0.58% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 4 | 75% | +0.22% | -0.22 to +0.68% | 75% of 4 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 4 |  |  |  | 100% of 4 | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 4 | 75% | +0.10% | -0.02 to +0.28% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 4 | 100% | +0.19% | +0.16 to +0.25% | 50% of 2 | too few (3/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 4 | 100% | +0.50% | +0.37 to +0.62% |  | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 4 | 100% | +0.24% | +0.10 to +0.28% |  | too few (4/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 3 | 100% | +0.28% | +0.07 to +0.50% | 100% of 2 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 3 | 67% | +0.08% | -0.04 to +0.18% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 3 | 100% | +0.12% | +0.05 to +0.16% | 100% of 2 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 3 | 50% | -0.03% | -0.43 to +0.37% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 3 | 67% | +0.31% | -0.18 to +0.69% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 3 | 33% | -0.01% | -0.37 to +0.53% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 3 | 100% | +0.61% | +0.01 to +1.22% | 50% of 2 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 3 | 0% | -0.36% | -0.69 to -0.18% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 3 | 67% | +0.06% | -0.13 to +0.17% |  | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls same · mid walls | 2 | 100% | +0.30% | +0.29 to +0.31% | 100% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 2 | 100% | +0.20% | +0.20 to +0.20% | 100% of 2 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 2 | 100% | +0.15% | +0.10 to +0.21% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near put wall | 2 | 100% | +0.21% | +0.18 to +0.24% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · mid walls | 2 | 50% | +0.04% | -0.19 to +0.28% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% |  | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · near put wall | 2 | 0% | -0.07% | -0.09 to -0.05% |  | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +1.86% | +1.86 to +1.86% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near call wall | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| weekly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls same · mid walls | 1 | 100% | +0.27% | +0.27 to +0.27% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
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
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | +0.73% | -0.39 to +2.40% |  | too few (3/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 100% | +0.35% | +0.06 to +0.65% | 100% of 2 | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.12% | -0.61 to +0.38% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 2 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 2 | 50% | +0.02% | -0.63 to +0.68% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.53% | -0.63 to +1.68% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 100% | +0.55% | +0.51 to +0.58% | 50% of 2 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.58% | +0.58 to +0.58% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.38% | +0.38 to +0.38% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.88% | +0.88 to +0.88% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 133 | 67% | +0.16% | up |
| intraday | weekly | writers even · few weak writers | 115 | 57% | +0.09% | no clear direction |
| intraday | monthly | writers even · weak calls | 101 | 74% | +0.17% | up |
| intraday | weekly | put writers stronger · weak calls | 65 | 73% | +0.34% | up |
| intraday | monthly | put writers stronger · weak calls | 63 | 85% | +0.57% | up |
| intraday | weekly | call writers stronger · weak puts | 38 | 89% | +0.40% | up |
| intraday | weekly | call writers stronger · few weak writers | 33 | 81% | +0.25% | up |
| intraday | weekly | put writers stronger · few weak writers | 32 | 93% | +0.34% | up |
| intraday | weekly | writers even · weak calls | 26 | 83% | +0.44% | up |
| intraday | weekly | writers even · weak puts | 20 | 82% | +0.31% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | monthly | call writers stronger · few weak writers | 15 | 62% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak on both sides | 11 | 73% | +0.20% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | weekly | put writers stronger · weak on both sides | 1 | 0% | -0.29% | too few (1/10) |
| day | monthly | writers even · few weak writers | 12 | 55% | +0.31% | no clear direction |
| day | monthly | writers even · weak calls | 7 | 71% | +0.52% | too few (7/10) |
| day | weekly | writers even · few weak writers | 7 | 71% | +0.61% | too few (7/10) |
| day | weekly | put writers stronger · weak calls | 5 | 80% | +0.40% | too few (5/10) |
| day | monthly | put writers stronger · weak calls | 4 | 100% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · few weak writers | 4 | 100% | +0.95% | too few (3/10) |
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
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 40 | 50% | +0.00% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m up | 39 | 49% | +0.04% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 28 | 77% | +0.29% | up |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 24 | 57% | +0.05% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 23 | 67% | +0.22% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m sideways | 17 | 88% | +0.14% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 15 | 64% | +0.30% | no clear direction |
| intraday | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 14 | 83% | +0.16% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.73% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 8 | 100% | +0.19% | too few (8/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 8 | 33% | -0.12% | too few (6/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 8 | 75% | +0.16% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 6 | 80% | +0.16% | too few (5/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 5 | 100% | +0.53% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 5 | 40% | +0.00% | too few (5/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly sideways · 125m up | 4 | 100% | +0.35% | too few (3/10) |
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
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 3 | 50% | -0.12% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +1.32% | too few (2/10) |
| day | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m up | 2 | 50% | -0.22% | too few (2/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +0.73% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.12% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 | 100% | +0.88% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.58% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.18% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
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
