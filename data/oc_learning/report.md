# Nifty option chain pattern log
Updated 2026-10-27 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 217 snapshots over 9 trading days
- 235 patterns logged; 110 different patterns so far

## Latest read (2026-10-27 13:45:19)

Nifty trend: weekly **bearish**, 125-min **sideways**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 0.1 | 22700 | 0.919 | 22700 | 22600 | 22800 | ±0.36% (22618-22781) | 9.08 |
| 2026-11-23 (monthly) | 27.1 | 22700 | 1.232 | 23000 | 22000 | 23000 | ±3.51% (21903-23498) | 16.09 |

- **Weekly, last 30 min**: `PCR down · call writing · walls down · mid walls`. Seen 2 times before; Nifty was up after it 50% of the time, average +0.24%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · weak on both sides`. Seen 3 times before; Nifty was up after it 100% of the time, average +0.22%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 2 times before; Nifty was up after it 100% of the time, average +0.15%. Too few outcomes (2/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak on both sides`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly bearish · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 51 times before; Nifty was up after it 60% of the time, average +0.06%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 25 times before; Nifty was up after it 58% of the time, average +0.09%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Nifty was up after it 25% of the time, average -0.12%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 1 times before; Nifty was up after it 0% of the time, average -0.23%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 22800, strongest put writers at 22600; weakest call writers at 22650, weakest put writers at 22750. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 17638 | 17154 | 217.3 | 22482 | 299.4 | 22617 | -82 | -82.1 | weak |
| Call | 22450 | 9408 | 9395 | 182.6 | 22484 | 250.8 | 22633 | -67 | -68.2 | weak |
| Call | 22500 | 51399 | 50294 | 168.6 | 22507 | 201.0 | 22669 | -31 | -32.4 | weak |
| Call | 22550 | 20245 | 20228 | 154.7 | 22577 | 154.2 | 22705 | +5 | +0.5 | weak |
| Call | 22600 | 84437 | 84137 | 126.8 | 22611 | 109.2 | 22727 | +27 | +17.6 | weak |
| Call | 22650 | 97128 | 97114 | 96.6 | 22694 | 70.2 | 22747 | +47 | +26.4 | weak |
| Call | 22700 | 381924 | 380758 | 71.3 | 22697 | 39.9 | 22771 | +72 | +31.4 | medium |
| Call | 22750 | 369754 | 369480 | 52.4 | 22715 | 20.2 | 22802 | +103 | +32.2 | strong |
| Call | 22800 | 507587 | 504903 | 50.1 | 22708 | 10.1 | 22850 | +151 | +40.0 | strong |
| Call | 22850 | 251384 | 251073 | 37.5 | 22714 | 5.0 | 22888 | +188 | +32.6 | strong |
| Call | 22900 | 270489 | 267944 | 45.8 | 22710 | 2.8 | 22946 | +246 | +43.0 | strong |
| Call | 22950 | 120504 | 120235 | 32.6 | 22731 | 1.8 | 22983 | +283 | +30.9 | strong |
| Call | 23000 | 363710 | 346921 | 40.4 | 22706 | 1.3 | 23040 | +341 | +39.1 | strong |
| Put | 22400 | 226731 | 222329 | 55.8 | 22601 | 1.3 | 22344 | +355 | +54.5 | strong |
| Put | 22450 | 140404 | 140297 | 49.2 | 22634 | 2.1 | 22401 | +299 | +47.1 | strong |
| Put | 22500 | 350556 | 337841 | 56.6 | 22671 | 3.4 | 22443 | +256 | +53.3 | strong |
| Put | 22550 | 186652 | 186492 | 40.2 | 22693 | 5.8 | 22510 | +190 | +34.4 | strong |
| Put | 22600 | 373693 | 370239 | 51.6 | 22700 | 11.1 | 22548 | +151 | +40.5 | strong |
| Put | 22650 | 287791 | 287698 | 41.2 | 22722 | 22.4 | 22609 | +91 | +18.8 | medium |
| Put | 22700 | 435039 | 433119 | 63.8 | 22732 | 42.0 | 22636 | +63 | +21.8 | medium |
| Put | 22750 | 180138 | 180118 | 66.6 | 22749 | 73.0 | 22683 | +16 | -6.4 | weak |
| Put | 22800 | 114160 | 113234 | 83.4 | 22769 | 111.8 | 22717 | -17 | -28.4 | weak |
| Put | 22850 | 26565 | 26545 | 100.6 | 22777 | 157.6 | 22749 | -50 | -57.0 | weak |
| Put | 22900 | 38466 | 37560 | 157.1 | 22821 | 204.7 | 22743 | -43 | -47.6 | weak |
| Put | 22950 | 11296 | 11271 | 181.4 | 22821 | 254.6 | 22769 | -69 | -73.2 | weak |
| Put | 23000 | 35925 | 32343 | 231.6 | 22858 | 303.6 | 22768 | -69 | -72.0 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23150. Covers 66% of near-money call OI and 64% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 3152 | 2166 | 554.3 | 22492 | 649.2 | 22954 | +254 | -94.9 | strong |
| Call | 22450 | 605 | 550 | 585.2 | 22598 | 606.2 | 23035 | +335 | -21.0 | strong |
| Call | 22500 | 27416 | 18693 | 552.4 | 22605 | 577.7 | 23052 | +352 | -25.3 | strong |
| Call | 22550 | 796 | 715 | 518.9 | 22591 | 547.2 | 23069 | +368 | -28.3 | strong |
| Call | 22600 | 20958 | 15504 | 486.9 | 22630 | 513.5 | 23087 | +386 | -26.5 | strong |
| Call | 22650 | 3816 | 3610 | 469.9 | 22611 | 482.2 | 23120 | +419 | -12.3 | strong |
| Call | 22700 | 38773 | 35957 | 469.8 | 22706 | 450.8 | 23170 | +469 | +19.0 | strong |
| Call | 22750 | 1738 | 1192 | 432.3 | 22658 | 425.0 | 23182 | +482 | +7.3 | strong |
| Call | 22800 | 26495 | 22502 | 411.1 | 22697 | 396.9 | 23211 | +511 | +14.2 | strong |
| Call | 22850 | 1357 | 965 | 387.6 | 22713 | 374.4 | 23238 | +537 | +13.2 | strong |
| Call | 22900 | 13598 | 11065 | 368.6 | 22709 | 344.0 | 23269 | +568 | +24.6 | strong |
| Call | 22950 | 1640 | 928 | 349.6 | 22726 | 319.9 | 23300 | +599 | +29.7 | strong |
| Call | 23000 | 97147 | 53136 | 308.5 | 22669 | 298.7 | 23308 | +608 | +9.8 | strong |
| Put | 22400 | 19907 | 8295 | 264.9 | 22663 | 240.9 | 22135 | +565 | +24.0 | strong |
| Put | 22450 | 1092 | 757 | 291.4 | 22626 | 252.7 | 22159 | +542 | +38.7 | strong |
| Put | 22500 | 59509 | 34007 | 288.3 | 22693 | 271.7 | 22212 | +489 | +16.6 | strong |
| Put | 22550 | 1371 | 1075 | 310.0 | 22669 | 286.9 | 22240 | +460 | +23.0 | strong |
| Put | 22600 | 22827 | 16583 | 339.0 | 22657 | 307.2 | 22261 | +439 | +31.7 | strong |
| Put | 22650 | 4386 | 3942 | 355.4 | 22641 | 325.6 | 22295 | +406 | +29.8 | strong |
| Put | 22700 | 44511 | 38644 | 345.6 | 22724 | 347.0 | 22354 | +346 | -1.4 | strong |
| Put | 22750 | 1897 | 1545 | 354.3 | 22746 | 364.4 | 22396 | +305 | -10.1 | strong |
| Put | 22800 | 29155 | 21126 | 395.0 | 22706 | 388.8 | 22405 | +296 | +6.3 | strong |
| Put | 22850 | 2094 | 690 | 390.2 | 22748 | 406.9 | 22460 | +241 | -16.7 | strong |
| Put | 22900 | 16095 | 12824 | 436.1 | 22709 | 435.1 | 22464 | +237 | +1.1 | strong |
| Put | 22950 | 757 | 441 | 429.5 | 22756 | 455.1 | 22520 | +180 | -25.6 | strong |
| Put | 23000 | 86313 | 49510 | 483.4 | 22733 | 488.4 | 22517 | +184 | -5.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 16 | 56% | +0.02% | -0.46 to +0.76% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 50% of 2 | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 7 | 71% | +0.29% | -0.39 to +0.91% | 100% of 1 | too few (7/10) |
| weekly | PCR up · put writing · walls same · near put wall | 7 | 43% | -0.09% | -0.47 to +0.41% | 50% of 2 | too few (7/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 6 | 100% | +0.46% | +0.27 to +0.70% |  | too few (4/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 6 | 67% | +0.07% | -0.21 to +0.46% | 100% of 1 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | -0.01% | -0.51 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 5 | 40% | -0.01% | -0.78 to +0.90% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near put wall | 5 | 60% | +0.31% | -0.37 to +0.85% | 50% of 2 | too few (5/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 5 | 100% | +0.44% | +0.09 to +1.02% | 100% of 1 | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 4 | 67% | -0.08% | -0.34 to +0.08% | 100% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% | 100% of 1 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 75% | +0.15% | -0.24 to +0.56% | 100% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 100% | +0.57% | +0.24 to +0.85% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 3 | 50% | +0.24% | -0.07 to +0.54% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 50% of 2 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% | 100% of 1 | too few (3/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.11% | +0.01 to +0.21% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 50% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 2 | 50% | +0.06% | -0.25 to +0.37% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% | 100% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 2 | 0% | -0.46% | -0.68 to -0.24% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.45% | +0.15 to +0.76% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 1 | 100% | +0.72% | +0.72 to +0.72% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.12% | +0.12 to +0.12% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.36% | +0.36 to +0.36% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 52 | 60% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 31 | 86% | +0.38% | up |
| intraday | weekly | writers even · few weak writers | 23 | 23% | -0.33% | down |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | weekly | writers even · weak puts | 18 | 76% | +0.29% | up |
| intraday | monthly | writers even · weak puts | 17 | 82% | +0.42% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides | 4 | 100% | +0.22% | too few (3/10) |
| intraday | weekly | writers even · weak calls | 3 | 50% | -0.17% | too few (2/10) |
| day | monthly | writers even · few weak writers | 5 | 25% | -0.12% | too few (4/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.23% | too few (1/10) |
| day | weekly | writers even · weak on both sides | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +0.68% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 26 | 58% | +0.09% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 11 | 90% | +0.32% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 11 | 18% | -0.33% | down |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 8 | 57% | +0.20% | too few (7/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 75% | +0.28% | too few (8/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 7 | 43% | -0.11% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 7 | 14% | -0.40% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 3 | 0% | -0.20% | too few (3/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 3 | 50% | -0.17% | too few (2/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 3 | 100% | +0.15% | too few (2/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.27% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.23% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.23% | too few (1/10) |
| day | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
