# Nifty option chain pattern log
Updated 2026-10-22 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 147 snapshots over 6 trading days
- 159 patterns logged; 93 different patterns so far

## Latest read (2026-10-22 15:40:00)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 5.0 | 22688 | 0.905 | 22850 | 22000 | 24000 | ±1.35% (22381-22994) | 14.5 |
| 2026-11-23 (monthly) | 32.0 | 22688 | 1.181 | 23000 | 22000 | 23000 | ±3.56% (21880-23495) | 14.87 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls up · mid walls`. Seen 1 times before. Too few outcomes (0/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 12 times before; Nifty was up after it 25% of the time, average -0.45%. Too few outcomes (12/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · quiet OI · walls same · near call wall`. Seen 1 times before. Too few outcomes (0/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 26 times before; Nifty was up after it 64% of the time, average -0.00%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.54%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22600; weakest call writers at 22300, weakest put writers at 23000. Covers 86% of near-money call OI and 84% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22350 | 2608 | 2081 | 406.1 | 22690 | 408.6 | 22756 | +68 | -2.5 | medium |
| Call | 22400 | 11349 | 5257 | 410.9 | 22733 | 367.9 | 22811 | +123 | +43.0 | strong |
| Call | 22450 | 3768 | 3284 | 308.3 | 22655 | 326.1 | 22758 | +71 | -17.8 | medium |
| Call | 22500 | 46489 | 32832 | 300.7 | 22687 | 286.1 | 22801 | +113 | +14.7 | strong |
| Call | 22550 | 12423 | 11957 | 249.5 | 22671 | 252.9 | 22800 | +112 | -3.4 | strong |
| Call | 22600 | 58990 | 55045 | 200.2 | 22643 | 221.0 | 22800 | +113 | -20.8 | strong |
| Call | 22650 | 31880 | 31555 | 166.8 | 22636 | 188.8 | 22817 | +129 | -22.1 | strong |
| Call | 22700 | 96195 | 86912 | 166.0 | 22674 | 160.3 | 22866 | +178 | +5.7 | strong |
| Call | 22750 | 49131 | 46744 | 158.8 | 22708 | 135.3 | 22909 | +221 | +23.5 | strong |
| Call | 22800 | 117279 | 105954 | 158.4 | 22744 | 112.9 | 22958 | +271 | +45.5 | strong |
| Call | 22850 | 35427 | 34116 | 147.4 | 22772 | 93.0 | 22997 | +310 | +54.4 | strong |
| Call | 22900 | 90705 | 83248 | 151.7 | 22827 | 75.6 | 23052 | +364 | +76.1 | strong |
| Call | 22950 | 47384 | 46449 | 126.0 | 22812 | 61.8 | 23076 | +388 | +64.3 | strong |
| Call | 23000 | 246194 | 201659 | 118.5 | 22830 | 49.5 | 23119 | +431 | +69.1 | strong |
| Put | 22350 | 33437 | 31765 | 44.4 | 22759 | 41.9 | 22306 | +382 | +2.5 | strong |
| Put | 22400 | 87243 | 73153 | 53.6 | 22789 | 51.1 | 22346 | +341 | +2.5 | strong |
| Put | 22450 | 30989 | 30461 | 62.9 | 22781 | 61.0 | 22387 | +301 | +1.9 | strong |
| Put | 22500 | 143176 | 104850 | 69.6 | 22838 | 74.3 | 22430 | +257 | -4.8 | strong |
| Put | 22550 | 49116 | 47807 | 93.0 | 22762 | 88.0 | 22457 | +231 | +5.0 | strong |
| Put | 22600 | 132465 | 116092 | 107.8 | 22789 | 105.0 | 22492 | +195 | +2.8 | strong |
| Put | 22650 | 56218 | 54465 | 128.3 | 22746 | 124.9 | 22522 | +166 | +3.4 | strong |
| Put | 22700 | 119093 | 103957 | 126.4 | 22808 | 145.9 | 22574 | +114 | -19.5 | strong |
| Put | 22750 | 33078 | 32714 | 148.4 | 22782 | 169.6 | 22602 | +86 | -21.1 | medium |
| Put | 22800 | 62783 | 51182 | 137.9 | 22892 | 195.9 | 22662 | +26 | -58.0 | weak |
| Put | 22850 | 13219 | 12765 | 154.3 | 22894 | 228.5 | 22696 | -8 | -74.2 | weak |
| Put | 22900 | 47215 | 43770 | 142.5 | 22985 | 260.0 | 22758 | -70 | -117.5 | weak |
| Put | 22950 | 11049 | 10957 | 154.5 | 22989 | 298.0 | 22795 | -108 | -143.5 | weak |
| Put | 23000 | 72099 | 58507 | 169.0 | 23028 | 332.3 | 22831 | -143 | -163.3 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23200. Covers 46% of near-money call OI and 43% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22350 | 146 | 77 | 694.9 | 22713 | 675.4 | 23045 | +357 | +19.6 | strong |
| Call | 22400 | 1630 | 253 | 628.6 | 22684 | 638.5 | 23029 | +341 | -9.8 | strong |
| Call | 22450 | 238 | 160 | 607.7 | 22701 | 600.0 | 23058 | +370 | +7.8 | strong |
| Call | 22500 | 18154 | 7512 | 587.5 | 22702 | 570.1 | 23087 | +400 | +17.4 | strong |
| Call | 22550 | 447 | 238 | 541.2 | 22685 | 542.2 | 23091 | +404 | -1.1 | strong |
| Call | 22600 | 23687 | 15080 | 489.9 | 22663 | 510.0 | 23090 | +402 | -20.1 | strong |
| Call | 22650 | 2143 | 1829 | 462.7 | 22671 | 479.3 | 23113 | +425 | -16.6 | strong |
| Call | 22700 | 24680 | 20682 | 460.5 | 22708 | 451.2 | 23161 | +473 | +9.3 | strong |
| Call | 22750 | 1107 | 393 | 442.4 | 22702 | 423.1 | 23192 | +505 | +19.2 | strong |
| Call | 22800 | 18276 | 12736 | 404.8 | 22703 | 393.1 | 23205 | +517 | +11.7 | strong |
| Call | 22850 | 1278 | 762 | 378.8 | 22710 | 368.9 | 23229 | +541 | +9.9 | strong |
| Call | 22900 | 10695 | 7467 | 369.1 | 22729 | 343.6 | 23269 | +581 | +25.5 | strong |
| Call | 22950 | 1335 | 410 | 357.4 | 22750 | 317.2 | 23307 | +620 | +40.2 | strong |
| Call | 23000 | 76983 | 25562 | 343.9 | 22782 | 297.6 | 23344 | +656 | +46.2 | strong |
| Put | 22350 | 771 | 190 | 213.2 | 22797 | 234.2 | 22137 | +551 | -21.0 | strong |
| Put | 22400 | 15579 | 3344 | 238.2 | 22760 | 251.3 | 22162 | +526 | -13.1 | strong |
| Put | 22450 | 553 | 118 | 262.5 | 22732 | 264.4 | 22187 | +500 | -1.9 | strong |
| Put | 22500 | 43138 | 15796 | 250.8 | 22813 | 282.6 | 22249 | +438 | -31.7 | strong |
| Put | 22550 | 760 | 271 | 224.2 | 22932 | 298.6 | 22326 | +362 | -74.4 | strong |
| Put | 22600 | 24139 | 14995 | 338.6 | 22670 | 317.4 | 22261 | +426 | +21.1 | strong |
| Put | 22650 | 2360 | 1798 | 333.6 | 22729 | 336.1 | 22316 | +371 | -2.5 | strong |
| Put | 22700 | 26388 | 19408 | 348.4 | 22725 | 356.1 | 22352 | +336 | -7.7 | strong |
| Put | 22750 | 1118 | 624 | 315.1 | 22856 | 376.8 | 22435 | +253 | -61.7 | strong |
| Put | 22800 | 20146 | 10311 | 392.3 | 22725 | 402.6 | 22408 | +280 | -10.3 | strong |
| Put | 22850 | 2237 | 134 | 396.0 | 22770 | 423.6 | 22454 | +234 | -27.6 | strong |
| Put | 22900 | 7376 | 3414 | 409.5 | 22787 | 448.0 | 22490 | +197 | -38.5 | strong |
| Put | 22950 | 591 | 131 | 383.6 | 22865 | 472.1 | 22566 | +121 | -88.5 | strong |
| Put | 23000 | 66453 | 24971 | 441.2 | 22819 | 502.9 | 22559 | +129 | -61.8 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 4 | 75% | +0.04% | -0.21 to +0.17% |  | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 4 | 50% | +0.09% | -0.74 to +0.62% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 3 | 67% | +0.01% | -0.39 to +0.34% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| weekly | PCR up · put writing · walls same · near put wall | 3 | 33% | -0.27% | -0.47 to +0.06% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 2 | 100% | +0.28% | +0.27 to +0.29% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · mid walls | 2 | 100% | +0.20% | +0.04 to +0.36% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.40% | -0.40 to -0.40% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 2 | 100% | +0.21% | +0.13 to +0.29% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 27 | 64% | -0.00% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 22 | 80% | +0.23% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | writers even · few weak writers | 13 | 25% | -0.45% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | writers even · weak puts | 7 | 57% | +0.19% | too few (7/10) |
| intraday | weekly | writers even · weak puts | 6 | 50% | -0.18% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 100% | +0.39% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.54% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
