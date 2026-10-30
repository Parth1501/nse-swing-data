# Nifty option chain pattern log
Updated 2026-10-30 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 277 snapshots over 12 trading days
- 302 patterns logged; 122 different patterns so far

## Latest read (2026-10-30 09:44:39)

Nifty trend: weekly **bearish**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-03 (weekly) | 4.2 | 22973 | 1.063 | 22950 | 22900 | 23000 | ±1.24% (22688-23258) | 14.75 |
| 2026-11-23 (monthly) | 24.2 | 22973 | 1.043 | 23000 | 22000 | 23500 | ±3.06% (22270-23676) | 14.77 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.17%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 35 times before; Nifty was up after it 39% of the time, average -0.09%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 11 times before; Nifty was up after it 40% of the time, average -0.02%. Too few outcomes (10/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Nifty was up after it 50% of the time, average +0.33%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 1 times before; Nifty was up after it 100% of the time, average +1.05%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls same · mid walls`. Seen 6 times before; Nifty was up after it 75% of the time, average +0.17%. Too few outcomes (4/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 83 times before; Nifty was up after it 67% of the time, average +0.16%. History points to a bull call debit spread, ATM to about the call wall 23500.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 27 times before; Nifty was up after it 75% of the time, average +0.24%. History points to a bull call debit spread, ATM to about the call wall 23500.
- **Monthly, today vs previous day**: `PCR flat · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 7 times before; Nifty was up after it 43% of the time, average +0.10%. Too few outcomes (7/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 3 times before; Nifty was up after it 67% of the time, average +0.33%. Too few outcomes (3/20) to trade on.

## Strong vs weak writers, weekly 2026-11-03

Strongest call writers at 23000, strongest put writers at 22900; weakest call writers at 22800, weakest put writers at 23500. Covers 78% of near-money call OI and 90% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 8496 | 7995 | 192.0 | 22668 | 351.1 | 22842 | -131 | -159.1 | weak |
| Call | 22700 | 37717 | 30495 | 166.2 | 22676 | 309.6 | 22866 | -107 | -143.4 | weak |
| Call | 22750 | 14069 | 12370 | 161.8 | 22732 | 272.9 | 22912 | -61 | -111.1 | weak |
| Call | 22800 | 60802 | 42380 | 137.1 | 22729 | 235.8 | 22937 | -36 | -98.7 | weak |
| Call | 22850 | 27817 | 25916 | 149.0 | 22825 | 203.3 | 22999 | +26 | -54.4 | weak |
| Call | 22900 | 109492 | 98506 | 139.2 | 22863 | 172.8 | 23039 | +66 | -33.6 | medium |
| Call | 22950 | 102859 | 100482 | 127.0 | 22902 | 144.4 | 23077 | +104 | -17.4 | strong |
| Call | 23000 | 249075 | 207754 | 95.5 | 22858 | 118.8 | 23095 | +123 | -23.4 | strong |
| Call | 23050 | 82612 | 73721 | 82.1 | 22894 | 96.5 | 23132 | +159 | -14.3 | strong |
| Call | 23100 | 129758 | 102392 | 64.0 | 22879 | 76.5 | 23164 | +191 | -12.4 | strong |
| Call | 23150 | 61640 | 52733 | 48.3 | 22854 | 59.5 | 23198 | +226 | -11.3 | strong |
| Call | 23200 | 125727 | 88385 | 35.2 | 22827 | 45.8 | 23235 | +262 | -10.6 | strong |
| Call | 23250 | 71556 | 61667 | 27.6 | 22826 | 34.4 | 23278 | +305 | -6.8 | strong |
| Call | 23300 | 144944 | 105398 | 22.6 | 22869 | 25.4 | 23323 | +350 | -2.8 | strong |
| Put | 22650 | 76303 | 72798 | 112.0 | 22803 | 47.5 | 22538 | +435 | +64.5 | strong |
| Put | 22700 | 181108 | 155844 | 112.2 | 22827 | 57.6 | 22588 | +385 | +54.6 | strong |
| Put | 22750 | 106267 | 101873 | 112.5 | 22859 | 69.3 | 22638 | +335 | +43.1 | strong |
| Put | 22800 | 205521 | 183060 | 116.6 | 22887 | 84.0 | 22683 | +289 | +32.5 | strong |
| Put | 22850 | 102512 | 101214 | 125.2 | 22907 | 100.5 | 22725 | +248 | +24.7 | strong |
| Put | 22900 | 208311 | 204069 | 132.3 | 22936 | 119.2 | 22768 | +205 | +13.1 | strong |
| Put | 22950 | 147840 | 147087 | 145.4 | 22955 | 140.8 | 22805 | +168 | +4.6 | strong |
| Put | 23000 | 174785 | 162733 | 191.7 | 22926 | 166.1 | 22808 | +164 | +25.6 | strong |
| Put | 23050 | 26527 | 25878 | 207.5 | 22945 | 193.6 | 22843 | +130 | +13.9 | strong |
| Put | 23100 | 38581 | 33709 | 245.1 | 22936 | 223.7 | 22855 | +118 | +21.4 | strong |
| Put | 23150 | 8242 | 7549 | 278.7 | 22937 | 257.4 | 22871 | +101 | +21.3 | medium |
| Put | 23200 | 14762 | 10866 | 342.9 | 22903 | 293.4 | 22857 | +116 | +49.4 | strong |
| Put | 23250 | 2590 | 1660 | 353.0 | 22930 | 330.9 | 22897 | +76 | +22.2 | medium |
| Put | 23300 | 5708 | 3025 | 418.2 | 22898 | 371.7 | 22882 | +91 | +46.5 | medium |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 22400, weakest put writers at -. Covers 71% of near-money call OI and 73% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 3829 | 3661 | 456.9 | 22612 | 580.5 | 23107 | +134 | -123.6 | strong |
| Call | 22700 | 31463 | 29735 | 449.6 | 22691 | 549.6 | 23150 | +177 | -100.0 | strong |
| Call | 22750 | 3950 | 3541 | 394.6 | 22691 | 509.2 | 23145 | +172 | -114.6 | strong |
| Call | 22800 | 25262 | 22351 | 396.6 | 22699 | 483.7 | 23197 | +224 | -87.0 | strong |
| Call | 22850 | 1559 | 1276 | 367.1 | 22712 | 444.8 | 23217 | +244 | -77.7 | strong |
| Call | 22900 | 13808 | 11823 | 355.4 | 22714 | 420.7 | 23255 | +282 | -65.3 | strong |
| Call | 22950 | 3339 | 2685 | 339.8 | 22805 | 389.2 | 23290 | +317 | -49.4 | strong |
| Call | 23000 | 96936 | 60885 | 293.3 | 22668 | 363.0 | 23293 | +320 | -69.7 | strong |
| Call | 23050 | 1872 | 962 | 286.6 | 22761 | 334.5 | 23337 | +364 | -47.9 | strong |
| Call | 23100 | 16492 | 8541 | 277.8 | 22736 | 308.6 | 23378 | +405 | -30.7 | strong |
| Call | 23150 | 1404 | 754 | 237.6 | 22733 | 282.9 | 23388 | +415 | -45.3 | strong |
| Call | 23200 | 20445 | 10194 | 228.2 | 22709 | 260.9 | 23428 | +455 | -32.8 | strong |
| Call | 23250 | 2076 | 1131 | 207.5 | 22768 | 234.6 | 23458 | +485 | -27.1 | strong |
| Call | 23300 | 21716 | 16431 | 177.0 | 22628 | 216.8 | 23477 | +504 | -39.8 | strong |
| Put | 22650 | 5336 | 4919 | 349.0 | 22654 | 206.6 | 22301 | +672 | +142.4 | strong |
| Put | 22700 | 44106 | 39777 | 353.7 | 22707 | 220.2 | 22346 | +627 | +133.5 | strong |
| Put | 22750 | 3610 | 3394 | 336.3 | 22760 | 236.7 | 22414 | +559 | +99.7 | strong |
| Put | 22800 | 33182 | 26610 | 382.4 | 22723 | 253.4 | 22418 | +555 | +129.0 | strong |
| Put | 22850 | 2950 | 1718 | 352.4 | 22805 | 273.9 | 22498 | +475 | +78.5 | strong |
| Put | 22900 | 18836 | 15922 | 411.8 | 22748 | 291.8 | 22488 | +485 | +120.0 | strong |
| Put | 22950 | 1870 | 1614 | 356.0 | 22857 | 313.8 | 22594 | +379 | +42.3 | strong |
| Put | 23000 | 96455 | 62467 | 461.2 | 22763 | 334.7 | 22539 | +434 | +126.5 | strong |
| Put | 23050 | 951 | 661 | 429.7 | 22825 | 355.6 | 22620 | +353 | +74.1 | strong |
| Put | 23100 | 9982 | 5245 | 469.0 | 22836 | 379.2 | 22631 | +342 | +89.7 | strong |
| Put | 23150 | 1175 | 329 | 448.0 | 22896 | 404.9 | 22702 | +271 | +43.1 | strong |
| Put | 23200 | 16210 | 9634 | 556.8 | 22785 | 429.6 | 22643 | +330 | +127.2 | strong |
| Put | 23250 | 692 | 429 | 575.4 | 22779 | 454.9 | 22675 | +298 | +120.5 | strong |
| Put | 23300 | 12261 | 10252 | 732.6 | 22598 | 483.6 | 22567 | +406 | +249.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 28 | 67% | +0.17% | -0.44 to +0.76% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · near call wall | 10 | 100% | +0.31% | +0.03 to +0.62% | 50% of 2 | up |
| weekly | PCR up · put writing · walls same · near put wall | 9 | 56% | +0.01% | -0.47 to +0.41% | 50% of 2 | too few (9/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 7 | 75% | +0.17% | -0.12 to +0.71% | 100% of 1 | too few (4/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| weekly | PCR down · call writing · walls same · near put wall | 6 | 83% | +0.37% | -0.37 to +0.85% | 50% of 2 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 6 | 100% | +0.47% | +0.09 to +1.02% | 100% of 1 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 5 | 60% | +0.12% | -0.07 to +0.32% | 50% of 2 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 5 | 40% | +0.04% | -0.78 to +0.90% | 100% of 1 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 4 | 67% | +0.06% | -0.05 to +0.15% | 50% of 2 | too few (3/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls down · mid walls | 4 | 75% | +0.28% | -0.07 to +0.54% | 100% of 1 | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% | 100% of 1 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 3 | 67% | +0.06% | -0.05 to +0.21% | 100% of 1 | too few (3/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 100% | +0.57% | +0.24 to +0.85% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 50% of 2 | too few (3/10) |
| weekly | PCR down · call writing · walls same · near call wall | 3 | 67% | +0.35% | -0.02 to +0.55% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 3 | 33% | -0.12% | -0.68 to +0.34% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put writing · walls up · near put wall | 3 | 67% | +0.23% | -0.01 to +0.35% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 3 | 67% | +0.16% | -0.02 to +0.37% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% | 100% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 50% | +0.10% | -0.16 to +0.36% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 2 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 2 | 0% | -0.01% | -0.02 to -0.01% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 2 | 100% | +0.78% | +0.70 to +0.85% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 2 | 100% | +0.19% | +0.13 to +0.26% | 0% of 1 | too few (2/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 1 | 100% | +0.42% | +0.42 to +0.42% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% | 100% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 84 | 67% | +0.16% | up |
| intraday | weekly | writers even · few weak writers | 36 | 39% | -0.09% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · few weak writers | 20 | 89% | +0.14% | up |
| intraday | weekly | put writers stronger · weak calls | 20 | 74% | +0.12% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | weekly | call writers stronger · few weak writers | 15 | 64% | +0.18% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | weekly | writers even · weak on both sides | 5 | 100% | +0.25% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak calls | 4 | 33% | -0.06% | too few (3/10) |
| day | monthly | writers even · few weak writers | 8 | 43% | +0.10% | too few (7/10) |
| day | weekly | writers even · few weak writers | 3 | 50% | +0.33% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers | 2 | 100% | +0.40% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.02% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 28 | 75% | +0.24% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 20 | 89% | +0.14% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 20 | 74% | +0.12% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 12 | 73% | +0.32% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 12 | 40% | -0.02% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 67% | +0.33% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.40% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.05% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
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
