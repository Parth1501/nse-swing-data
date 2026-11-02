# Nifty option chain pattern log
Updated 2026-11-02 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 302 snapshots over 13 trading days
- 330 patterns logged; 131 different patterns so far

## Latest read (2026-11-02 09:45:39)

Nifty trend: weekly **bearish**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-03 (weekly) | 1.2 | 23306 | 0.95 | 23250 | 23000 | 23500 | ±0.83% (23112-23500) | 19.91 |
| 2026-11-23 (monthly) | 21.2 | 23323 | 0.763 | 23200 | 23000 | 23500 | ±2.8% (22670-23977) | 14.5 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 24 times before; Nifty was up after it 65% of the time, average +0.09%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 24 times before; Nifty was up after it 65% of the time, average +0.09%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 1 times before; Nifty was up after it 0% of the time, average -1.11%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 1 times before; Nifty was up after it 0% of the time, average -1.11%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put writing · walls same · mid walls`. Seen 3 times before; Nifty was up after it 67% of the time, average +0.06%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 21 times before; Nifty was up after it 84% of the time, average +0.03%. Too few outcomes (19/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 21 times before; Nifty was up after it 84% of the time, average +0.03%. Too few outcomes (19/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.65%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 2 times before; Nifty was up after it 50% of the time, average -0.23%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 2 times before; Nifty was up after it 50% of the time, average -0.23%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-03

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 23250, weakest put writers at 23600. Covers 86% of near-money call OI and 97% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 23000 | 80289 | 71999 | 106.0 | 22919 | 333.8 | 23106 | -200 | -227.8 | weak |
| Call | 23050 | 28203 | 26792 | 94.5 | 22964 | 289.1 | 23144 | -162 | -194.6 | weak |
| Call | 23100 | 59082 | 51888 | 75.8 | 22954 | 247.8 | 23176 | -130 | -172.0 | weak |
| Call | 23150 | 43605 | 40536 | 58.7 | 22948 | 205.5 | 23209 | -97 | -146.8 | weak |
| Call | 23200 | 118646 | 95184 | 45.2 | 22916 | 167.8 | 23245 | -61 | -122.5 | weak |
| Call | 23250 | 132013 | 127494 | 97.8 | 23165 | 133.6 | 23348 | +42 | -35.8 | weak |
| Call | 23300 | 230419 | 207937 | 75.0 | 23163 | 103.4 | 23375 | +69 | -28.4 | medium |
| Call | 23350 | 116628 | 112822 | 53.4 | 23139 | 77.4 | 23403 | +97 | -24.0 | medium |
| Call | 23400 | 194034 | 161005 | 25.9 | 23017 | 55.6 | 23426 | +120 | -29.6 | strong |
| Call | 23450 | 89703 | 84811 | 19.6 | 23043 | 39.3 | 23470 | +164 | -19.8 | strong |
| Call | 23500 | 255512 | 174955 | 13.5 | 23024 | 26.5 | 23514 | +208 | -13.0 | strong |
| Call | 23550 | 85049 | 80358 | 10.5 | 23116 | 17.6 | 23560 | +254 | -7.1 | strong |
| Call | 23600 | 155940 | 139050 | 8.6 | 23134 | 11.4 | 23609 | +303 | -2.9 | strong |
| Call | 23650 | 76372 | 72043 | 6.3 | 23160 | 7.8 | 23656 | +350 | -1.5 | strong |
| Put | 23000 | 257857 | 253764 | 89.0 | 23141 | 21.4 | 22911 | +395 | +67.6 | strong |
| Put | 23050 | 125419 | 125184 | 85.5 | 23172 | 26.6 | 22965 | +341 | +58.9 | strong |
| Put | 23100 | 140139 | 139102 | 73.2 | 23229 | 33.6 | 23027 | +279 | +39.5 | strong |
| Put | 23150 | 78598 | 78465 | 58.4 | 23280 | 43.1 | 23092 | +214 | +15.3 | strong |
| Put | 23200 | 228130 | 227062 | 65.5 | 23291 | 55.5 | 23135 | +171 | +10.0 | strong |
| Put | 23250 | 220213 | 219908 | 73.0 | 23303 | 71.0 | 23177 | +129 | +2.0 | strong |
| Put | 23300 | 210644 | 209787 | 95.8 | 23299 | 90.4 | 23204 | +102 | +5.3 | medium |
| Put | 23350 | 48922 | 48865 | 120.2 | 23300 | 114.7 | 23230 | +76 | +5.6 | medium |
| Put | 23400 | 44456 | 43426 | 159.4 | 23289 | 143.8 | 23241 | +65 | +15.6 | medium |
| Put | 23450 | 9972 | 9944 | 233.3 | 23243 | 176.1 | 23217 | +89 | +57.2 | medium |
| Put | 23500 | 22118 | 16785 | 264.9 | 23254 | 214.8 | 23235 | +71 | +50.1 | medium |
| Put | 23550 | 2119 | 2107 | 288.6 | 23272 | 254.8 | 23261 | +45 | +33.8 | weak |
| Put | 23600 | 4611 | 3670 | 332.2 | 23273 | 299.6 | 23268 | +38 | +32.6 | weak |
| Put | 23650 | 439 | 379 | 365.7 | 23286 | 345.6 | 23284 | +22 | +20.1 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 23000, weakest put writers at -. Covers 69% of near-money call OI and 77% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 23000 | 85180 | 53552 | 293.6 | 22669 | 583.8 | 23294 | -30 | -290.2 | weak |
| Call | 23050 | 2560 | 1755 | 316.3 | 22888 | 546.9 | 23366 | +43 | -230.6 | weak |
| Call | 23100 | 17229 | 10987 | 302.6 | 22863 | 511.0 | 23403 | +79 | -208.4 | medium |
| Call | 23150 | 2142 | 1544 | 272.4 | 22893 | 475.6 | 23422 | +99 | -203.3 | medium |
| Call | 23200 | 21497 | 11582 | 237.4 | 22761 | 443.4 | 23437 | +114 | -206.1 | strong |
| Call | 23250 | 2609 | 1694 | 239.0 | 22891 | 410.6 | 23489 | +166 | -171.5 | strong |
| Call | 23300 | 24066 | 18870 | 199.6 | 22715 | 381.7 | 23500 | +176 | -182.1 | strong |
| Call | 23350 | 2967 | 2422 | 210.2 | 22947 | 350.9 | 23560 | +237 | -140.8 | strong |
| Call | 23400 | 15237 | 10111 | 174.8 | 22794 | 322.5 | 23575 | +252 | -147.7 | strong |
| Call | 23450 | 1577 | 1147 | 148.9 | 22740 | 293.0 | 23599 | +276 | -144.1 | strong |
| Call | 23500 | 103115 | 70979 | 120.7 | 22643 | 268.9 | 23621 | +297 | -148.3 | strong |
| Call | 23550 | 1726 | 803 | 114.8 | 22748 | 243.4 | 23665 | +342 | -128.6 | strong |
| Call | 23600 | 13873 | 8139 | 117.7 | 22781 | 221.0 | 23718 | +394 | -103.3 | strong |
| Call | 23650 | 1210 | 994 | 101.4 | 22810 | 199.0 | 23751 | +428 | -97.6 | strong |
| Put | 23000 | 97747 | 65038 | 445.1 | 22793 | 176.2 | 22555 | +768 | +269.0 | strong |
| Put | 23050 | 1835 | 1546 | 365.6 | 22947 | 190.1 | 22684 | +639 | +175.5 | strong |
| Put | 23100 | 15614 | 11012 | 375.1 | 22996 | 203.6 | 22725 | +598 | +171.6 | strong |
| Put | 23150 | 1845 | 1024 | 384.1 | 23008 | 220.8 | 22766 | +557 | +163.3 | strong |
| Put | 23200 | 20777 | 14682 | 454.3 | 22953 | 234.9 | 22746 | +578 | +219.4 | strong |
| Put | 23250 | 1552 | 1305 | 368.2 | 23127 | 252.6 | 22882 | +442 | +115.6 | strong |
| Put | 23300 | 17092 | 15122 | 584.8 | 22830 | 271.6 | 22715 | +608 | +313.1 | strong |
| Put | 23350 | 763 | 691 | 476.1 | 23024 | 288.9 | 22874 | +449 | +187.2 | strong |
| Put | 23400 | 6220 | 4653 | 572.0 | 22927 | 311.3 | 22828 | +495 | +260.7 | strong |
| Put | 23450 | 518 | 464 | 580.7 | 22928 | 336.0 | 22869 | +454 | +244.7 | strong |
| Put | 23500 | 64819 | 52102 | 845.5 | 22648 | 359.0 | 22654 | +669 | +486.5 | strong |
| Put | 23550 | 282 | 204 | 742.9 | 22808 | 385.9 | 22807 | +516 | +357.0 | strong |
| Put | 23600 | 2631 | 1809 | 787.4 | 22818 | 410.9 | 22813 | +511 | +376.6 | strong |
| Put | 23650 | 371 | 301 | 891.6 | 22729 | 446.9 | 22758 | +565 | +444.7 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 30 | 69% | +0.19% | -0.44 to +0.76% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near put wall | 10 | 60% | +0.02% | -0.47 to +0.41% | 50% of 2 | no clear direction |
| weekly | PCR up · put writing · walls same · near call wall | 10 | 100% | +0.31% | +0.03 to +0.62% | 50% of 2 | up |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 7 | 80% | +0.21% | -0.12 to +0.71% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near put wall | 7 | 86% | +0.33% | -0.37 to +0.85% | 50% of 2 | too few (7/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 6 | 80% | +0.04% | -0.18 to +0.19% |  | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 6 | 100% | +0.47% | +0.09 to +1.02% | 100% of 1 | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 5 | 40% | +0.04% | -0.78 to +0.90% | 100% of 1 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 5 | 60% | +0.12% | -0.07 to +0.32% | 50% of 2 | too few (5/10) |
| weekly | PCR up · put writing · walls up · near put wall | 5 | 60% | +0.15% | -0.13 to +0.35% | 0% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls down · mid walls | 4 | 75% | +0.28% | -0.07 to +0.54% | 100% of 1 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 67% | +0.06% | -0.05 to +0.21% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 4 | 100% | +0.39% | +0.04 to +0.73% | 50% of 2 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 4 | 67% | +0.06% | -0.05 to +0.15% | 50% of 2 | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% | 100% of 1 | too few (4/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 100% | +0.57% | +0.24 to +0.85% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 3 | 33% | -0.12% | -0.68 to +0.34% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · near call wall | 3 | 67% | +0.35% | -0.02 to +0.55% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 3 | 67% | +0.16% | -0.02 to +0.37% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 3 | 67% | +0.16% | -0.11 to +0.50% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 2 | 0% | -0.01% | -0.02 to -0.01% | 0% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% |  | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 2 | 100% | +0.26% | +0.17 to +0.35% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 2 | 100% | +0.19% | +0.13 to +0.26% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 50% | +0.10% | -0.16 to +0.36% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 0% | -0.44% | -0.69 to -0.20% |  | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 2 | 100% | +0.78% | +0.70 to +0.85% |  | too few (2/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% | 100% of 1 | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% | 100% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.17% | +1.17 to +1.17% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +1.17% | +1.17 to +1.17% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 94 | 70% | +0.17% | up |
| intraday | weekly | writers even · few weak writers | 40 | 47% | -0.04% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | weekly | put writers stronger · few weak writers | 25 | 91% | +0.15% | up |
| intraday | weekly | put writers stronger · weak calls | 25 | 65% | +0.09% | no clear direction |
| intraday | monthly | writers even · weak calls | 22 | 84% | +0.03% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | weekly | call writers stronger · few weak writers | 15 | 64% | +0.18% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 5 | 40% | -0.01% | too few (5/10) |
| intraday | weekly | writers even · weak on both sides | 5 | 100% | +0.25% | too few (5/10) |
| intraday | weekly | writers even · weak calls | 4 | 33% | -0.06% | too few (3/10) |
| day | monthly | writers even · few weak writers | 8 | 50% | +0.28% | too few (8/10) |
| day | monthly | writers even · weak calls | 3 | 50% | -0.23% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.78% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | put writers stronger · weak calls | 2 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 2 | 50% | +0.33% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.02% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 25 | 91% | +0.15% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 25 | 65% | +0.09% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 22 | 84% | +0.03% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 16 | 60% | +0.09% | no clear direction |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 12 | 73% | +0.32% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 5 | 40% | -0.01% | too few (5/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
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
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.63% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 3 | 50% | -0.23% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.78% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 0% | -1.11% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.05% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.22% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
