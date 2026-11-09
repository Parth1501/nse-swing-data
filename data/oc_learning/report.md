# Nifty option chain pattern log
Updated 2026-11-09 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 427 snapshots over 18 trading days
- 473 patterns logged; 154 different patterns so far

## Latest read (2026-11-09 10:45:28)

Nifty trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-09 (weekly) | 0.2 | 24862 | 0.81 | 24900 | 24800 | 25000 | ±0.59% (24715-25009) | 14.3 |
| 2026-11-23 (monthly) | 14.2 | 24862 | 0.729 | 24000 | 23000 | 25000 | ±2.5% (24241-25483) | 16.0 |

- **Weekly, last 30 min**: `PCR down · call writing · walls down · near put wall`. Seen 3 times before; Nifty was up after it 33% of the time, average -0.17%. Too few outcomes (3/20) to trade on.
  - Writers: `call writers stronger · weak puts`. Seen 32 times before; Nifty was up after it 87% of the time, average +0.38%. History points to a bull call debit spread, ATM to about the call wall 25000.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.44%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls same · near call wall`. Seen 11 times before; Nifty was up after it 91% of the time, average +0.46%. Too few outcomes (11/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 48 times before; Nifty was up after it 86% of the time, average +0.26%. History points to a bull call debit spread, ATM to about the call wall 25000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Nifty was up after it 0% of the time, average -0.40%. Too few outcomes (3/20) to trade on.
- **Monthly, today vs previous day**: `PCR flat · call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 4 times before; Nifty was up after it 75% of the time, average +0.88%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-09

Strongest call writers at 25000, strongest put writers at 24800; weakest call writers at 24800, weakest put writers at 24900. Covers 97% of near-money call OI and 100% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24500 | 26676 | 21579 | 148.9 | 24434 | 352.8 | 24649 | -213 | -203.9 | weak |
| Call | 24550 | 10348 | 10120 | 132.3 | 24470 | 304.9 | 24682 | -180 | -172.6 | weak |
| Call | 24600 | 25605 | 22888 | 132.1 | 24519 | 257.2 | 24732 | -130 | -125.1 | weak |
| Call | 24650 | 11571 | 11292 | 118.4 | 24534 | 212.7 | 24768 | -94 | -94.3 | weak |
| Call | 24700 | 31521 | 26452 | 104.8 | 24543 | 172.0 | 24805 | -57 | -67.2 | weak |
| Call | 24750 | 23622 | 23074 | 90.1 | 24555 | 133.2 | 24840 | -22 | -43.1 | weak |
| Call | 24800 | 75698 | 66443 | 90.2 | 24665 | 99.5 | 24890 | +28 | -9.3 | weak |
| Call | 24850 | 96904 | 96568 | 92.3 | 24832 | 71.5 | 24942 | +80 | +20.8 | medium |
| Call | 24900 | 273437 | 268208 | 87.7 | 24863 | 50.4 | 24988 | +125 | +37.3 | strong |
| Call | 24950 | 258981 | 258135 | 80.5 | 24912 | 34.4 | 25031 | +168 | +46.1 | strong |
| Call | 25000 | 445455 | 421662 | 52.1 | 24766 | 24.2 | 25052 | +190 | +27.9 | strong |
| Call | 25050 | 197240 | 196612 | 53.7 | 24876 | 16.9 | 25104 | +241 | +36.8 | strong |
| Call | 25100 | 348822 | 338945 | 46.6 | 24875 | 12.2 | 25147 | +284 | +34.3 | strong |
| Call | 25150 | 164107 | 163025 | 36.6 | 24881 | 8.9 | 25187 | +324 | +27.7 | strong |
| Call | 25200 | 272177 | 257387 | 23.7 | 24796 | 6.8 | 25224 | +361 | +16.9 | strong |
| Put | 24500 | 269889 | 268274 | 76.9 | 24765 | 5.3 | 24423 | +439 | +71.5 | strong |
| Put | 24550 | 98005 | 98005 | 83.3 | 24766 | 7.5 | 24467 | +396 | +75.8 | strong |
| Put | 24600 | 171094 | 171063 | 99.0 | 24769 | 11.2 | 24501 | +361 | +87.8 | strong |
| Put | 24650 | 102431 | 102431 | 82.4 | 24818 | 16.2 | 24568 | +295 | +66.1 | strong |
| Put | 24700 | 187455 | 187436 | 93.9 | 24824 | 23.9 | 24606 | +256 | +70.0 | strong |
| Put | 24750 | 142396 | 142393 | 81.9 | 24872 | 36.0 | 24668 | +194 | +45.8 | strong |
| Put | 24800 | 294034 | 293980 | 75.5 | 24896 | 53.0 | 24725 | +138 | +22.4 | strong |
| Put | 24850 | 175022 | 175005 | 76.4 | 24920 | 75.2 | 24774 | +89 | +1.2 | medium |
| Put | 24900 | 270953 | 270932 | 86.6 | 24938 | 102.4 | 24813 | +49 | -15.8 | weak |
| Put | 24950 | 161931 | 161921 | 103.4 | 24946 | 138.2 | 24847 | +16 | -34.8 | weak |
| Put | 25000 | 156110 | 154975 | 171.0 | 24914 | 177.8 | 24829 | +33 | -6.8 | weak |
| Put | 25050 | 28404 | 28402 | 162.5 | 24961 | 219.7 | 24888 | -25 | -57.2 | weak |
| Put | 25100 | 30435 | 30425 | 197.3 | 24969 | 266.3 | 24903 | -40 | -69.0 | weak |
| Put | 25150 | 8733 | 8733 | 211.0 | 24968 | 312.7 | 24939 | -77 | -101.7 | weak |
| Put | 25200 | 10745 | 10727 | 300.0 | 24924 | 359.8 | 24900 | -38 | -59.8 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 25500, strongest put writers at 24500; weakest call writers at 24500, weakest put writers at 25450. Covers 92% of near-money call OI and 90% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24500 | 41323 | 35419 | 170.6 | 23850 | 525.2 | 24671 | -192 | -354.6 | weak |
| Call | 24550 | 1216 | 1196 | 233.2 | 24234 | 492.8 | 24783 | -79 | -259.6 | weak |
| Call | 24600 | 12041 | 11701 | 220.5 | 24247 | 457.3 | 24821 | -42 | -236.8 | weak |
| Call | 24650 | 1245 | 1231 | 247.3 | 24406 | 424.4 | 24897 | +35 | -177.1 | weak |
| Call | 24700 | 9497 | 9289 | 199.6 | 24219 | 393.9 | 24900 | +37 | -194.2 | weak |
| Call | 24750 | 1749 | 1730 | 234.3 | 24459 | 366.2 | 24984 | +122 | -131.9 | strong |
| Call | 24800 | 11784 | 11313 | 162.2 | 24208 | 338.1 | 24962 | +100 | -175.9 | medium |
| Call | 24850 | 2069 | 2068 | 183.5 | 24288 | 311.7 | 25034 | +171 | -128.2 | strong |
| Call | 24900 | 11177 | 11122 | 196.5 | 24447 | 285.6 | 25096 | +234 | -89.1 | strong |
| Call | 24950 | 2848 | 2834 | 248.8 | 24664 | 263.0 | 25199 | +337 | -14.2 | strong |
| Call | 25000 | 84971 | 70180 | 89.1 | 23953 | 239.8 | 25089 | +227 | -150.7 | strong |
| Call | 25050 | 2300 | 2297 | 248.5 | 24805 | 219.6 | 25299 | +436 | +28.9 | strong |
| Call | 25100 | 15122 | 14978 | 195.5 | 24701 | 200.8 | 25296 | +433 | -5.2 | strong |
| Call | 25150 | 3069 | 3066 | 213.6 | 24807 | 183.1 | 25364 | +501 | +30.5 | strong |
| Call | 25200 | 19014 | 18896 | 141.6 | 24588 | 165.9 | 25342 | +479 | -24.4 | strong |
| Put | 24500 | 76729 | 69624 | 502.0 | 24297 | 173.3 | 23998 | +864 | +328.7 | strong |
| Put | 24550 | 5278 | 5235 | 250.4 | 24699 | 190.8 | 24300 | +563 | +59.6 | strong |
| Put | 24600 | 11079 | 11034 | 414.7 | 24439 | 206.1 | 24185 | +677 | +208.7 | strong |
| Put | 24650 | 1869 | 1732 | 336.4 | 24604 | 224.4 | 24314 | +549 | +112.0 | strong |
| Put | 24700 | 11729 | 10981 | 467.8 | 24481 | 244.1 | 24232 | +630 | +223.8 | strong |
| Put | 24750 | 1653 | 1647 | 317.0 | 24756 | 263.6 | 24433 | +429 | +53.4 | strong |
| Put | 24800 | 15607 | 15483 | 423.2 | 24608 | 286.1 | 24377 | +485 | +137.0 | strong |
| Put | 24850 | 2105 | 2099 | 332.9 | 24817 | 309.4 | 24517 | +345 | +23.6 | strong |
| Put | 24900 | 10193 | 10177 | 363.1 | 24814 | 333.1 | 24537 | +325 | +29.9 | strong |
| Put | 24950 | 2019 | 2019 | 342.9 | 24913 | 360.4 | 24607 | +255 | -17.5 | strong |
| Put | 25000 | 57615 | 46818 | 1079.4 | 24027 | 385.5 | 23921 | +942 | +693.9 | strong |
| Put | 25050 | 902 | 900 | 385.2 | 24942 | 426.1 | 24665 | +197 | -40.9 | strong |
| Put | 25100 | 3812 | 3801 | 478.0 | 24868 | 447.4 | 24622 | +240 | +30.6 | strong |
| Put | 25150 | 453 | 450 | 447.2 | 24925 | 477.6 | 24703 | +160 | -30.3 | strong |
| Put | 25200 | 3324 | 3292 | 627.4 | 24731 | 511.8 | 24573 | +290 | +115.6 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 34 | 73% | +0.26% | -0.44 to +0.97% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 16 | 94% | +0.34% | -0.02 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · put and call writing · walls same · near call wall | 14 | 57% | +0.31% | -0.71 to +1.70% | 100% of 1 | no clear direction |
| monthly | PCR flat · put writing · walls same · mid walls | 12 | 100% | +0.54% | +0.09 to +1.02% | 100% of 1 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 12 | 91% | +0.46% | -0.28 to +1.68% |  | up |
| weekly | PCR down · unwinding · walls same · near call wall | 11 | 70% | +0.39% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 11 | 64% | +0.05% | -0.47 to +0.42% | 33% of 3 | no clear direction |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| weekly | PCR down · call writing · walls same · near put wall | 8 | 88% | +0.36% | -0.37 to +0.85% | 33% of 3 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% |  | too few (6/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| monthly | PCR up · put writing · walls same · near call wall | 7 | 57% | +0.33% | -0.40 to +0.93% | 100% of 1 | too few (7/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 7 | 80% | +0.21% | -0.12 to +0.71% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · put writing · walls same · near call wall | 7 | 100% | +0.69% | +0.41 to +1.56% |  | too few (6/10) |
| monthly | PCR down · call writing · walls same · near call wall | 7 | 83% | +0.27% | -0.78 to +1.18% | 100% of 1 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 7 | 33% | +0.07% | -0.40 to +0.90% | 67% of 3 | too few (3/10) |
| weekly | PCR up · put writing · walls up · near put wall | 7 | 57% | +0.34% | -0.13 to +1.65% | 0% of 3 | too few (7/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put writing · walls same · mid walls | 6 | 100% | +0.65% | +0.24 to +0.85% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 6 | 50% | +0.08% | -0.74 to +0.62% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 6 | 80% | +0.04% | -0.18 to +0.19% |  | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 6 | 50% | +0.17% | -0.78 to +0.90% | 100% of 1 | too few (6/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 5 | 80% | +0.46% | -1.11 to +1.69% | 0% of 2 | too few (5/10) |
| weekly | PCR up · put writing · walls up · mid walls | 5 | 80% | +0.55% | -0.16 to +1.40% | 67% of 3 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near call wall | 5 | 80% | +0.59% | -0.06 to +1.68% | 50% of 2 | too few (5/10) |
| weekly | PCR down · call writing · walls same · mid walls | 5 | 100% | +0.46% | +0.04 to +0.75% | 33% of 3 | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 5 | 60% | +0.05% | -0.47 to +0.49% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near call wall | 5 | 80% | +0.53% | -0.02 to +0.91% | 33% of 3 | too few (5/10) |
| weekly | PCR down · call writing · walls down · mid walls | 5 | 80% | +0.31% | -0.07 to +0.54% | 50% of 2 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 5 | 75% | +0.21% | -0.05 to +0.63% | 50% of 2 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | +0.10% | -0.68 to +0.75% | 50% of 2 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls down · near put wall | 4 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 4 | 100% | +0.35% | +0.13 to +0.59% | 0% of 3 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 3 | 33% | +0.13% | -0.02 to +0.43% | 0% of 2 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 3 |  |  |  | 100% of 3 | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 3 | 67% | +0.24% | -0.22 to +0.68% | 67% of 3 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 33% | -0.17% | -0.75 to +0.38% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 3 | 67% | +0.16% | -0.11 to +0.50% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 3 | 100% | +0.50% | +0.37 to +0.62% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 3 | 100% | +1.15% | +0.59 to +1.82% | 0% of 2 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 2 | 100% | +1.27% | +0.89 to +1.65% |  | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 2 | 50% | +0.15% | -0.28 to +0.58% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 0% | -0.44% | -0.69 to -0.20% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 50% | -0.07% | -0.36 to +0.22% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 2 | 100% | +0.37% | +0.37 to +0.37% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 2 | 100% | +0.50% | +0.47 to +0.53% | 50% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · put writing · walls same · mid walls | 2 | 50% | +0.16% | -0.57 to +0.89% | 50% of 2 | too few (2/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 2 | 100% | +0.61% | +0.01 to +1.22% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +1.86% | +1.86 to +1.86% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 | 100% | +0.53% | +0.53 to +0.53% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 50% | -0.02% | -0.67 to +0.63% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +1.01% | -0.39 to +2.40% |  | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 50% | -0.01% | -0.67 to +0.65% | 100% of 2 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% |  | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 94 | 70% | +0.17% | up |
| intraday | weekly | put writers stronger · weak calls | 58 | 78% | +0.39% | up |
| intraday | weekly | writers even · few weak writers | 54 | 57% | +0.08% | no clear direction |
| intraday | monthly | put writers stronger · weak calls | 50 | 85% | +0.68% | up |
| intraday | monthly | writers even · weak calls | 49 | 86% | +0.26% | up |
| intraday | weekly | call writers stronger · weak puts | 33 | 87% | +0.38% | up |
| intraday | weekly | put writers stronger · few weak writers | 28 | 92% | +0.34% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | call writers stronger · few weak writers | 19 | 72% | +0.30% | no clear direction |
| intraday | weekly | writers even · weak calls | 19 | 82% | +0.52% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | weekly | writers even · weak on both sides | 6 | 100% | +0.36% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| day | monthly | writers even · few weak writers | 8 | 50% | +0.34% | too few (8/10) |
| day | monthly | writers even · weak calls | 5 | 75% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · weak calls | 4 | 50% | +0.11% | too few (4/10) |
| day | monthly | put writers stronger · weak calls | 3 | 67% | +0.66% | too few (3/10) |
| day | weekly | call writers stronger · weak puts | 3 | 0% | -0.44% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | writers even · few weak writers | 3 | 67% | +1.02% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | writers even · weak calls | 2 | 50% | +1.00% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 57 | 78% | +0.39% | up |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 49 | 85% | +0.68% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 45 | 93% | +0.31% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 28 | 77% | +0.29% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.73% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m up | 4 | 0% | -0.40% | too few (3/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 0% | -0.34% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 1 | 0% | -0.51% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m up | 1 | 100% | +0.91% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +1.32% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 1 | 0% | -0.67% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 1 | 0% | -0.67% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m up | 1 | 100% | +2.01% | too few (1/10) |
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
