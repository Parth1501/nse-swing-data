# Nifty option chain pattern log
Updated 2026-10-19 13:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 88 snapshots over 4 trading days
- 96 patterns logged; 64 different patterns so far

## Latest read (2026-10-19 13:45:38)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 0.1 | 22861 | 0.821 | 22900 | 22800 | 23000 | ±0.38% (22774-22947) | 8.71 |
| 2026-10-27 (monthly) | 8.1 | 22860 | 0.994 | 23100 | 22500 | 23500 | ±1.57% (22500-23219) | 13.1 |

- **Weekly, last 30 min**: `PCR flat · unwinding · walls down · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.29%. Too few outcomes (2/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put and call writing · walls same · mid walls`. Seen 2 times before; Nifty was up after it 50% of the time, average -0.11%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 7 times before; Nifty was up after it 43% of the time, average -0.18%. Too few outcomes (7/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23000, strongest put writers at 22750; weakest call writers at 22700, weakest put writers at 22850. Covers 93% of near-money call OI and 92% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22550 | 4792 | 3865 | 244.1 | 22720 | 307.3 | 22794 | -67 | -63.2 | weak |
| Call | 22600 | 11560 | 7675 | 143.3 | 22598 | 257.2 | 22743 | -117 | -113.9 | weak |
| Call | 22650 | 7539 | 4753 | 133.6 | 22620 | 207.2 | 22784 | -77 | -73.7 | weak |
| Call | 22700 | 30051 | 15647 | 156.1 | 22778 | 161.3 | 22856 | -5 | -5.3 | weak |
| Call | 22750 | 18571 | 13747 | 126.9 | 22840 | 117.0 | 22877 | +16 | +9.9 | weak |
| Call | 22800 | 88207 | 79531 | 118.1 | 22896 | 77.7 | 22918 | +57 | +40.4 | medium |
| Call | 22850 | 147769 | 144777 | 67.8 | 22888 | 46.4 | 22918 | +57 | +21.4 | medium |
| Call | 22900 | 438011 | 427278 | 51.3 | 22903 | 25.1 | 22951 | +91 | +26.2 | medium |
| Call | 22950 | 405311 | 403560 | 47.7 | 22943 | 12.9 | 22998 | +137 | +34.8 | strong |
| Call | 23000 | 555595 | 532253 | 51.0 | 22973 | 6.8 | 23051 | +190 | +44.2 | strong |
| Call | 23050 | 324038 | 321102 | 54.5 | 23022 | 3.8 | 23105 | +244 | +50.8 | strong |
| Call | 23100 | 434243 | 415940 | 53.7 | 23049 | 2.6 | 23154 | +293 | +51.0 | strong |
| Call | 23150 | 259311 | 252914 | 54.4 | 23096 | 1.8 | 23204 | +344 | +52.6 | strong |
| Call | 23200 | 340573 | 311106 | 36.5 | 23085 | 1.5 | 23236 | +376 | +35.0 | strong |
| Put | 22550 | 95157 | 80198 | 18.7 | 23034 | 1.1 | 22531 | +329 | +17.6 | strong |
| Put | 22600 | 216635 | 173658 | 28.4 | 23002 | 1.6 | 22572 | +289 | +26.8 | strong |
| Put | 22650 | 167011 | 155899 | 26.1 | 22991 | 2.4 | 22624 | +237 | +23.7 | strong |
| Put | 22700 | 288227 | 256802 | 41.9 | 22973 | 5.0 | 22658 | +203 | +36.9 | strong |
| Put | 22750 | 273510 | 269822 | 27.0 | 22960 | 10.2 | 22723 | +138 | +16.8 | strong |
| Put | 22800 | 421445 | 411837 | 36.4 | 22993 | 21.1 | 22764 | +97 | +15.2 | medium |
| Put | 22850 | 319462 | 317510 | 36.8 | 22986 | 40.1 | 22813 | +48 | -3.3 | weak |
| Put | 22900 | 311173 | 309293 | 52.6 | 23015 | 69.1 | 22847 | +13 | -16.5 | weak |
| Put | 22950 | 128141 | 127748 | 58.9 | 23048 | 107.0 | 22891 | -30 | -48.0 | weak |
| Put | 23000 | 138486 | 137347 | 62.4 | 23088 | 150.2 | 22938 | -77 | -87.8 | weak |
| Put | 23050 | 51844 | 51812 | 62.0 | 23095 | 198.5 | 22988 | -127 | -136.4 | weak |
| Put | 23100 | 94226 | 93946 | 91.2 | 23111 | 245.2 | 23009 | -148 | -154.1 | weak |
| Put | 23150 | 57781 | 57761 | 103.5 | 23132 | 295.9 | 23047 | -186 | -192.4 | weak |
| Put | 23200 | 32079 | 31968 | 146.4 | 23117 | 345.5 | 23054 | -193 | -199.1 | weak |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at 22600, weakest put writers at 23100. Covers 52% of near-money call OI and 51% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22550 | 5578 | 3740 | 419.7 | 22880 | 401.4 | 22970 | +110 | +18.3 | strong |
| Call | 22600 | 20234 | 6270 | 277.6 | 22667 | 361.2 | 22878 | +18 | -83.7 | weak |
| Call | 22650 | 3039 | 854 | 251.7 | 22656 | 326.4 | 22902 | +42 | -74.8 | weak |
| Call | 22700 | 26998 | 7625 | 251.1 | 22729 | 291.4 | 22951 | +92 | -40.2 | medium |
| Call | 22750 | 6005 | 1469 | 252.8 | 22786 | 256.8 | 23003 | +143 | -4.0 | strong |
| Call | 22800 | 31163 | 13231 | 263.9 | 22880 | 225.8 | 23064 | +204 | +38.1 | strong |
| Call | 22850 | 8250 | 4694 | 233.7 | 22911 | 197.8 | 23084 | +224 | +36.0 | strong |
| Call | 22900 | 45976 | 31370 | 190.2 | 22869 | 170.9 | 23090 | +231 | +19.4 | strong |
| Call | 22950 | 18190 | 15758 | 179.9 | 22927 | 147.7 | 23130 | +270 | +32.2 | strong |
| Call | 23000 | 139477 | 75839 | 168.2 | 22933 | 125.5 | 23168 | +309 | +42.7 | strong |
| Call | 23050 | 16448 | 14060 | 165.9 | 22991 | 106.5 | 23216 | +356 | +59.4 | strong |
| Call | 23100 | 73198 | 50633 | 153.3 | 23015 | 89.7 | 23253 | +394 | +63.6 | strong |
| Call | 23150 | 32168 | 29249 | 121.3 | 22994 | 74.5 | 23271 | +412 | +46.8 | strong |
| Call | 23200 | 106518 | 59647 | 98.0 | 22925 | 62.3 | 23298 | +439 | +35.7 | strong |
| Put | 22550 | 10748 | 7346 | 67.7 | 23010 | 64.8 | 22482 | +377 | +2.9 | strong |
| Put | 22600 | 62605 | 34921 | 93.1 | 22970 | 76.3 | 22507 | +353 | +16.8 | strong |
| Put | 22650 | 10529 | 6680 | 89.5 | 22999 | 89.5 | 22560 | +299 | +0.0 | strong |
| Put | 22700 | 80251 | 42048 | 118.6 | 22966 | 103.8 | 22581 | +278 | +14.8 | strong |
| Put | 22750 | 14581 | 12634 | 89.6 | 23074 | 121.2 | 22660 | +199 | -31.6 | strong |
| Put | 22800 | 51341 | 24527 | 134.9 | 22982 | 139.6 | 22665 | +194 | -4.7 | strong |
| Put | 22850 | 12631 | 10463 | 155.5 | 22961 | 162.1 | 22694 | +165 | -6.5 | strong |
| Put | 22900 | 43391 | 34415 | 147.2 | 23032 | 185.0 | 22753 | +107 | -37.8 | strong |
| Put | 22950 | 15326 | 14599 | 177.3 | 22997 | 210.9 | 22773 | +87 | -33.6 | medium |
| Put | 23000 | 114498 | 69965 | 204.1 | 23002 | 240.0 | 22796 | +64 | -35.9 | medium |
| Put | 23050 | 7173 | 6825 | 179.3 | 23077 | 270.2 | 22871 | -11 | -90.9 | weak |
| Put | 23100 | 41825 | 28853 | 197.4 | 23097 | 304.4 | 22903 | -43 | -106.9 | weak |
| Put | 23150 | 5768 | 5250 | 214.2 | 23117 | 337.8 | 22936 | -76 | -123.6 | weak |
| Put | 23200 | 38177 | 14214 | 247.1 | 23103 | 376.0 | 22953 | -93 | -128.9 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% | 0% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | -0.11% | -0.37 to +0.15% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · mid walls | 3 | 33% | -0.11% | -0.47 to +0.14% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.26% | -0.63 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 3 | 67% | -0.02% | -0.34 to +0.17% |  | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.23% | -1.24 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.57% | -0.87 to -0.26% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 2 | 100% | +0.14% | +0.07 to +0.21% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.84% | -0.84 to -0.84% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 1 | 0% | -0.63% | -0.63 to -0.63% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.26% | -1.26 to -1.26% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.91% | -0.91 to -0.91% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.27% | -0.27 to -0.27% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.87% | -0.87 to -0.87% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.81% | -0.81 to -0.81% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.31% | -0.31 to -0.31% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.90% | -0.90 to -0.90% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.24% | -1.24 to -1.24% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.24% | -1.24 to -1.24% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.03% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.12% | up |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.03% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | monthly | writers even · few weak writers | 8 | 43% | -0.18% | too few (7/10) |
| intraday | weekly | writers even · few weak writers | 7 | 14% | -0.47% | too few (7/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 3 | 0% | -0.32% | too few (3/10) |
| intraday | weekly | call writers stronger · weak puts | 3 | 0% | -0.29% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.23% | too few (2/10) |
| intraday | weekly | writers even · weak puts | 1 | 0% | -0.39% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.30% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.24% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
