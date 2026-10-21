# Nifty option chain pattern log
Updated 2026-10-21 12:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 111 snapshots over 5 trading days
- 119 patterns logged; 79 different patterns so far

## Latest read (2026-10-21 12:44:55)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 6.1 | 22742 | 0.834 | 22950 | 22000 | 23000 | ±1.58% (22383-23102) | 15.49 |
| 2026-11-23 (monthly) | 33.1 | 22740 | 1.196 | 23000 | 22000 | 23000 | ±3.68% (21903-23577) | 15.08 |

- **Weekly, last 30 min**: `PCR down · call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 7 times before; Nifty was up after it 33% of the time, average -0.08%. Too few outcomes (6/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.64%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 12 times before; Nifty was up after it 50% of the time, average +0.00%. Too few outcomes (10/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. Seen 2 times before; Nifty was up after it 50% of the time, average +0.51%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at -, weakest put writers at 23000. Covers 80% of near-money call OI and 75% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22450 | 1411 | 537 | 429.3 | 22766 | 369.9 | 22879 | +137 | +59.3 | strong |
| Call | 22500 | 33955 | 13038 | 423.7 | 22823 | 333.8 | 22924 | +181 | +90.0 | strong |
| Call | 22550 | 5617 | 4206 | 396.6 | 22857 | 298.6 | 22947 | +204 | +98.1 | strong |
| Call | 22600 | 25599 | 12461 | 281.9 | 22720 | 264.4 | 22882 | +140 | +17.5 | strong |
| Call | 22650 | 9175 | 7044 | 257.0 | 22762 | 233.7 | 22907 | +165 | +23.3 | strong |
| Call | 22700 | 55500 | 37464 | 223.9 | 22755 | 204.8 | 22924 | +182 | +19.0 | strong |
| Call | 22750 | 35779 | 31308 | 190.8 | 22758 | 178.2 | 22941 | +199 | +12.7 | strong |
| Call | 22800 | 105307 | 89125 | 190.2 | 22801 | 154.1 | 22990 | +248 | +36.2 | strong |
| Call | 22850 | 43384 | 41032 | 174.1 | 22827 | 132.8 | 23024 | +282 | +41.2 | strong |
| Call | 22900 | 124225 | 111775 | 166.4 | 22857 | 113.2 | 23066 | +324 | +53.2 | strong |
| Call | 22950 | 60350 | 58436 | 166.6 | 22915 | 96.4 | 23117 | +374 | +70.2 | strong |
| Call | 23000 | 254425 | 194796 | 144.7 | 22902 | 81.7 | 23145 | +402 | +63.0 | strong |
| Call | 23050 | 80635 | 78282 | 158.1 | 22994 | 68.5 | 23208 | +466 | +89.6 | strong |
| Put | 22450 | 25203 | 24003 | 32.3 | 23001 | 74.8 | 22418 | +325 | -42.4 | strong |
| Put | 22500 | 145963 | 87761 | 51.0 | 22979 | 87.2 | 22449 | +293 | -36.1 | strong |
| Put | 22550 | 31250 | 28706 | 46.5 | 22995 | 102.0 | 22504 | +239 | -55.5 | strong |
| Put | 22600 | 92870 | 66839 | 65.6 | 23010 | 118.2 | 22534 | +208 | -52.6 | strong |
| Put | 22650 | 36642 | 33093 | 81.6 | 22946 | 137.6 | 22568 | +174 | -56.0 | strong |
| Put | 22700 | 110105 | 80405 | 94.1 | 22981 | 158.6 | 22606 | +136 | -64.5 | strong |
| Put | 22750 | 52753 | 50980 | 111.7 | 22938 | 181.2 | 22638 | +104 | -69.5 | strong |
| Put | 22800 | 90871 | 68214 | 113.2 | 22974 | 207.7 | 22687 | +55 | -94.5 | medium |
| Put | 22850 | 24317 | 23148 | 125.4 | 22979 | 235.1 | 22725 | +18 | -109.7 | weak |
| Put | 22900 | 69628 | 64119 | 131.1 | 23013 | 266.5 | 22769 | -27 | -135.4 | weak |
| Put | 22950 | 21684 | 21489 | 143.4 | 23012 | 299.2 | 22807 | -64 | -155.8 | weak |
| Put | 23000 | 109410 | 87473 | 156.2 | 23054 | 334.8 | 22844 | -102 | -178.5 | weak |
| Put | 23050 | 20952 | 20865 | 145.0 | 23091 | 372.5 | 22905 | -163 | -227.5 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at -, weakest put writers at 23100. Covers 18% of near-money call OI and 16% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 1434 | 9 | 810.7 | 22937 | 684.5 | 23211 | +470 | +126.2 | strong |
| Call | 22450 | 104 | 25 | 756.0 | 22894 | 656.2 | 23206 | +466 | +99.8 | strong |
| Call | 22500 | 14240 | 2836 | 639.3 | 22772 | 615.5 | 23139 | +399 | +23.8 | strong |
| Call | 22550 | 277 | 28 | 631.3 | 22788 | 589.6 | 23181 | +441 | +41.6 | strong |
| Call | 22600 | 8956 | 12 | 629.9 | 22875 | 550.9 | 23230 | +490 | +79.0 | strong |
| Call | 22650 | 335 | 5 | 547.6 | 22781 | 525.0 | 23198 | +457 | +22.6 | strong |
| Call | 22700 | 4362 | 305 | 508.1 | 22772 | 489.6 | 23208 | +468 | +18.5 | strong |
| Call | 22750 | 998 | 155 | 463.6 | 22741 | 463.2 | 23214 | +473 | +0.5 | strong |
| Call | 22800 | 7436 | 1528 | 449.0 | 22771 | 431.0 | 23249 | +509 | +18.0 | strong |
| Call | 22850 | 675 | 140 | 428.5 | 22788 | 403.1 | 23278 | +538 | +25.4 | strong |
| Call | 22900 | 6046 | 2708 | 397.0 | 22781 | 377.1 | 23297 | +557 | +19.8 | strong |
| Call | 22950 | 1170 | 196 | 401.1 | 22831 | 361.9 | 23351 | +611 | +39.2 | strong |
| Call | 23000 | 66845 | 14565 | 381.5 | 22861 | 331.4 | 23381 | +641 | +50.0 | strong |
| Call | 23050 | 1607 | 39 | 371.9 | 22905 | 311.1 | 23422 | +682 | +60.8 | strong |
| Put | 22400 | 13069 | 304 | 173.4 | 22976 | 248.1 | 22227 | +514 | -74.7 | strong |
| Put | 22450 | 528 | 37 | 236.1 | 22797 | 257.0 | 22214 | +526 | -20.9 | strong |
| Put | 22500 | 36297 | 7444 | 205.8 | 22948 | 279.8 | 22294 | +446 | -74.0 | strong |
| Put | 22550 | 705 | 197 | 188.7 | 23034 | 298.4 | 22361 | +379 | -109.7 | strong |
| Put | 22600 | 9937 | 301 | 249.8 | 22892 | 312.9 | 22350 | +390 | -63.1 | strong |
| Put | 22650 | 873 | 260 | 193.2 | 23093 | 333.4 | 22457 | +284 | -140.2 | strong |
| Put | 22700 | 8107 | 916 | 268.8 | 22932 | 353.6 | 22431 | +309 | -84.8 | strong |
| Put | 22750 | 957 | 360 | 256.8 | 22999 | 373.9 | 22493 | +247 | -117.1 | strong |
| Put | 22800 | 11837 | 1762 | 336.6 | 22845 | 395.1 | 22463 | +277 | -58.5 | strong |
| Put | 22850 | 3031 | 17 | 243.0 | 23094 | 417.5 | 22607 | +133 | -174.5 | strong |
| Put | 22900 | 5255 | 1214 | 335.2 | 22940 | 440.2 | 22565 | +176 | -105.0 | strong |
| Put | 22950 | 792 | 109 | 326.5 | 22972 | 457.0 | 22624 | +117 | -130.5 | strong |
| Put | 23000 | 52669 | 10816 | 340.3 | 23004 | 491.9 | 22660 | +81 | -151.5 | medium |
| Put | 23050 | 645 | 132 | 330.0 | 23069 | 515.0 | 22720 | +20 | -185.0 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% | 0% of 1 | too few (6/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.86% | -0.98 to -0.71% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 3 | 67% | +0.02% | -0.21 to +0.17% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 2 | 0% | -0.56% | -0.74 to -0.38% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 0% | -0.27% | -0.51 to -0.03% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.53% | -1.53 to -1.53% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.92% | -0.92 to -0.92% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.98% | -0.98 to -0.98% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 0% | -0.92% | -0.92 to -0.92% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.52% | -1.52 to -1.52% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.87% | -0.87 to -0.87% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 13 | 50% | +0.00% | no clear direction |
| intraday | monthly | writers even · few weak writers | 13 | 54% | -0.13% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 10 | 44% | +0.02% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · few weak writers | 10 | 10% | -0.65% | down |
| intraday | weekly | call writers stronger · weak puts | 8 | 33% | -0.08% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.59% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak puts | 4 | 50% | -0.27% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 3 | 0% | -0.20% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts | 1 | 0% | -0.03% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 3 | 50% | +0.51% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.64% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
