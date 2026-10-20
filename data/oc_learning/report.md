# Nifty option chain pattern log
Updated 2026-10-20 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 95 snapshots over 4 trading days
- 104 patterns logged; 68 different patterns so far

## Latest read (2026-10-19 15:40:00)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 0.0 | 22889 | 0.849 | 22900 | 22850 | 22900 | ±0.05% (22878-22900) | 0.99 |
| 2026-10-27 (monthly) | 8.0 | 22889 | 0.883 | 23000 | 22000 | 24000 | ±1.5% (22547-23231) | 12.62 |

- **Weekly, last 30 min**: `PCR flat · unwinding · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 4 times before; Nifty was up after it 50% of the time, average -0.03%. Too few outcomes (4/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 11 times before; Nifty was up after it 50% of the time, average +0.00%. Too few outcomes (10/20) to trade on.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 1 times before; Nifty was up after it 100% of the time, average +1.66%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23000, strongest put writers at 22800; weakest call writers at 22850, weakest put writers at 22900. Covers 93% of near-money call OI and 92% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22550 | 2853 | 2301 | 244.1 | 22720 | 339.0 | 22794 | -95 | -95.0 | weak |
| Call | 22600 | 9669 | 6475 | 146.3 | 22604 | 289.2 | 22746 | -143 | -142.9 | weak |
| Call | 22650 | 4928 | 3119 | 134.7 | 22622 | 238.7 | 22785 | -104 | -104.0 | weak |
| Call | 22700 | 18399 | 11075 | 160.9 | 22805 | 188.8 | 22861 | -28 | -27.9 | weak |
| Call | 22750 | 10418 | 8505 | 128.5 | 22854 | 139.2 | 22879 | -10 | -10.7 | weak |
| Call | 22800 | 33161 | 30770 | 109.8 | 22891 | 88.9 | 22910 | +21 | +20.9 | weak |
| Call | 22850 | 92128 | 91137 | 60.0 | 22884 | 39.0 | 22910 | +21 | +21.0 | weak |
| Call | 22900 | 364200 | 357580 | 44.0 | 22896 | 0.1 | 22944 | +55 | +44.0 | medium |
| Call | 22950 | 228352 | 227454 | 44.1 | 22937 | 0.1 | 22994 | +105 | +44.1 | strong |
| Call | 23000 | 253115 | 242646 | 50.3 | 22971 | 0.1 | 23050 | +161 | +50.2 | strong |
| Call | 23050 | 171835 | 170278 | 54.5 | 23022 | 0.1 | 23105 | +216 | +54.5 | strong |
| Call | 23100 | 202765 | 194218 | 53.7 | 23049 | 0.1 | 23154 | +265 | +53.6 | strong |
| Call | 23150 | 139273 | 135837 | 54.4 | 23096 | 0.1 | 23204 | +315 | +54.3 | strong |
| Call | 23200 | 156200 | 142685 | 36.5 | 23085 | 0.1 | 23236 | +348 | +36.5 | strong |
| Put | 22550 | 46728 | 39391 | 18.7 | 23034 | 0.1 | 22531 | +358 | +18.6 | strong |
| Put | 22600 | 110913 | 89438 | 27.6 | 22998 | 0.1 | 22572 | +316 | +27.5 | strong |
| Put | 22650 | 95913 | 89532 | 26.1 | 22991 | 0.1 | 22624 | +265 | +26.1 | strong |
| Put | 22700 | 154758 | 138395 | 40.5 | 22970 | 0.1 | 22659 | +229 | +40.5 | strong |
| Put | 22750 | 124705 | 123218 | 24.2 | 22950 | 0.1 | 22726 | +163 | +24.2 | strong |
| Put | 22800 | 155602 | 152586 | 32.5 | 22975 | 0.1 | 22767 | +122 | +32.5 | strong |
| Put | 22850 | 243501 | 242329 | 34.8 | 22961 | 0.1 | 22815 | +74 | +34.7 | medium |
| Put | 22900 | 207245 | 206063 | 53.0 | 23007 | 11.0 | 22847 | +42 | +42.0 | weak |
| Put | 22950 | 73310 | 73085 | 58.9 | 23048 | 60.9 | 22891 | -2 | -1.9 | weak |
| Put | 23000 | 76162 | 75536 | 62.4 | 23088 | 110.8 | 22938 | -49 | -48.4 | weak |
| Put | 23050 | 30635 | 30616 | 62.0 | 23095 | 160.6 | 22988 | -99 | -98.5 | weak |
| Put | 23100 | 61960 | 61776 | 91.2 | 23111 | 210.8 | 23009 | -120 | -119.7 | weak |
| Put | 23150 | 48390 | 48373 | 103.5 | 23132 | 260.6 | 23047 | -158 | -157.1 | weak |
| Put | 23200 | 18655 | 18591 | 149.4 | 23113 | 310.1 | 23051 | -162 | -160.7 | weak |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at 22600, weakest put writers at 23100. Covers 58% of near-money call OI and 54% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22550 | 6233 | 4395 | 417.5 | 22881 | 406.4 | 22968 | +79 | +11.1 | medium |
| Call | 22600 | 20581 | 6668 | 282.6 | 22680 | 367.6 | 22883 | -6 | -85.0 | weak |
| Call | 22650 | 3236 | 1051 | 264.6 | 22697 | 324.0 | 22915 | +26 | -59.4 | weak |
| Call | 22700 | 27906 | 8533 | 254.9 | 22744 | 292.0 | 22955 | +66 | -37.1 | medium |
| Call | 22750 | 6786 | 2251 | 253.6 | 22819 | 255.1 | 23004 | +115 | -1.5 | strong |
| Call | 22800 | 36638 | 18706 | 251.8 | 22879 | 223.2 | 23052 | +163 | +28.5 | strong |
| Call | 22850 | 13176 | 9836 | 211.6 | 22890 | 195.0 | 23062 | +173 | +16.6 | strong |
| Call | 22900 | 75381 | 60775 | 179.6 | 22874 | 169.9 | 23080 | +191 | +9.7 | strong |
| Call | 22950 | 20278 | 17971 | 173.4 | 22918 | 145.9 | 23123 | +234 | +27.4 | strong |
| Call | 23000 | 150021 | 88970 | 159.7 | 22922 | 122.1 | 23160 | +271 | +37.6 | strong |
| Call | 23050 | 17744 | 15359 | 160.4 | 22981 | 102.8 | 23210 | +321 | +57.6 | strong |
| Call | 23100 | 76578 | 54760 | 146.4 | 23000 | 87.0 | 23246 | +357 | +59.4 | strong |
| Call | 23150 | 30164 | 27528 | 119.3 | 22989 | 72.4 | 23269 | +380 | +46.9 | strong |
| Call | 23200 | 115545 | 68674 | 92.9 | 22919 | 58.3 | 23293 | +404 | +34.6 | strong |
| Put | 22550 | 13054 | 9652 | 65.3 | 22978 | 56.2 | 22485 | +404 | +9.1 | strong |
| Put | 22600 | 64569 | 36935 | 91.6 | 22966 | 66.0 | 22508 | +381 | +25.6 | strong |
| Put | 22650 | 11269 | 7569 | 88.2 | 22981 | 78.3 | 22562 | +327 | +9.8 | strong |
| Put | 22700 | 81156 | 42993 | 118.2 | 22964 | 92.0 | 22582 | +307 | +26.2 | strong |
| Put | 22750 | 18286 | 16339 | 94.5 | 23031 | 110.5 | 22656 | +233 | -16.1 | strong |
| Put | 22800 | 65705 | 38891 | 133.4 | 22944 | 127.5 | 22667 | +222 | +5.9 | strong |
| Put | 22850 | 16856 | 14688 | 155.4 | 22937 | 149.5 | 22695 | +194 | +5.9 | strong |
| Put | 22900 | 59689 | 50713 | 156.1 | 22984 | 172.5 | 22744 | +145 | -16.4 | strong |
| Put | 22950 | 13153 | 12529 | 177.3 | 22997 | 196.8 | 22773 | +116 | -19.5 | strong |
| Put | 23000 | 106920 | 65969 | 204.9 | 22999 | 224.7 | 22795 | +94 | -19.7 | medium |
| Put | 23050 | 5860 | 5576 | 179.3 | 23077 | 255.3 | 22871 | +18 | -76.0 | weak |
| Put | 23100 | 41384 | 28677 | 198.9 | 23094 | 286.4 | 22901 | -12 | -87.5 | weak |
| Put | 23150 | 7105 | 6619 | 243.0 | 23058 | 324.9 | 22907 | -18 | -81.9 | weak |
| Put | 23200 | 37750 | 14113 | 247.9 | 23101 | 355.8 | 22952 | -63 | -107.9 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% | 0% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 3 | 67% | +0.02% | -0.21 to +0.17% |  | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 1 | 0% | -0.51% | -0.51 to -0.51% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.74% | -0.74 to -0.74% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.71% | -0.71 to -0.71% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 12 | 50% | +0.00% | no clear direction |
| intraday | monthly | writers even · few weak writers | 11 | 64% | -0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | weekly | writers even · few weak writers | 7 | 14% | -0.40% | too few (7/10) |
| intraday | weekly | call writers stronger · weak puts | 5 | 50% | -0.03% | too few (4/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 3 | 0% | -0.20% | too few (3/10) |
| intraday | weekly | writers even · weak puts | 3 | 67% | -0.06% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.23% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
