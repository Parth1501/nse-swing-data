# Nifty option chain pattern log
Updated 2026-10-21 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 115 snapshots over 5 trading days
- 123 patterns logged; 82 different patterns so far

## Latest read (2026-10-21 13:45:31)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 6.1 | 22696 | 0.867 | 22950 | 22000 | 23000 | ±1.54% (22347-23046) | 14.91 |
| 2026-11-23 (monthly) | 33.1 | 22697 | 1.207 | 23000 | 22000 | 23000 | ±3.66% (21866-23529) | 15.01 |

- **Weekly, last 30 min**: `PCR down · call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 9 times before; Nifty was up after it 25% of the time, average -0.15%. Too few outcomes (8/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.84%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR up · quiet OI · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.21%. Too few outcomes (1/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at -, weakest put writers at 23000. Covers 81% of near-money call OI and 77% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 10020 | 2292 | 549.3 | 22885 | 378.9 | 22949 | +253 | +170.3 | strong |
| Call | 22450 | 1634 | 760 | 403.5 | 22747 | 340.0 | 22854 | +157 | +63.5 | strong |
| Call | 22500 | 34512 | 13595 | 418.9 | 22818 | 305.1 | 22919 | +223 | +113.8 | strong |
| Call | 22550 | 5721 | 4333 | 390.9 | 22849 | 271.0 | 22941 | +245 | +119.9 | strong |
| Call | 22600 | 28617 | 15479 | 273.6 | 22717 | 237.8 | 22874 | +177 | +35.8 | strong |
| Call | 22650 | 11283 | 9152 | 245.8 | 22748 | 208.0 | 22896 | +200 | +37.8 | strong |
| Call | 22700 | 71979 | 53943 | 211.0 | 22739 | 180.7 | 22911 | +215 | +30.3 | strong |
| Call | 22750 | 46440 | 41969 | 182.1 | 22744 | 155.4 | 22932 | +236 | +26.7 | strong |
| Call | 22800 | 116507 | 100325 | 184.1 | 22790 | 133.9 | 22984 | +288 | +50.2 | strong |
| Call | 22850 | 46025 | 43673 | 170.5 | 22820 | 114.4 | 23021 | +324 | +56.1 | strong |
| Call | 22900 | 131111 | 118661 | 162.5 | 22848 | 97.0 | 23062 | +366 | +65.5 | strong |
| Call | 22950 | 61825 | 59911 | 164.5 | 22910 | 82.0 | 23115 | +418 | +82.6 | strong |
| Call | 23000 | 257738 | 198323 | 143.1 | 22898 | 69.2 | 23143 | +447 | +73.9 | strong |
| Put | 22400 | 70040 | 48182 | 42.5 | 22947 | 66.3 | 22357 | +339 | -23.8 | strong |
| Put | 22450 | 26848 | 25663 | 35.8 | 22978 | 78.2 | 22414 | +282 | -42.3 | strong |
| Put | 22500 | 148311 | 90109 | 52.1 | 22971 | 91.7 | 22448 | +248 | -39.6 | strong |
| Put | 22550 | 32601 | 30057 | 49.2 | 22981 | 107.5 | 22501 | +196 | -58.2 | strong |
| Put | 22600 | 95610 | 69579 | 68.0 | 22998 | 125.5 | 22532 | +164 | -57.5 | strong |
| Put | 22650 | 39182 | 35633 | 86.3 | 22928 | 146.2 | 22564 | +133 | -59.9 | strong |
| Put | 22700 | 120732 | 91032 | 102.8 | 22949 | 168.7 | 22597 | +99 | -65.9 | medium |
| Put | 22750 | 51765 | 50148 | 117.7 | 22922 | 194.6 | 22632 | +64 | -76.9 | medium |
| Put | 22800 | 88995 | 67455 | 117.4 | 22964 | 221.9 | 22683 | +14 | -104.6 | weak |
| Put | 22850 | 20758 | 19760 | 125.4 | 22979 | 251.8 | 22725 | -28 | -126.4 | weak |
| Put | 22900 | 66802 | 61516 | 131.1 | 23013 | 283.6 | 22769 | -73 | -152.6 | weak |
| Put | 22950 | 20429 | 20245 | 143.4 | 23012 | 318.3 | 22807 | -110 | -174.9 | weak |
| Put | 23000 | 105772 | 84565 | 156.2 | 23054 | 356.1 | 22844 | -147 | -199.8 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at -, weakest put writers at 23000. Covers 21% of near-money call OI and 18% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 1439 | 14 | 757.3 | 22852 | 663.0 | 23157 | +460 | +94.3 | strong |
| Call | 22450 | 105 | 26 | 751.8 | 22886 | 648.7 | 23202 | +505 | +103.1 | strong |
| Call | 22500 | 14284 | 2880 | 638.7 | 22771 | 601.8 | 23139 | +441 | +36.9 | strong |
| Call | 22550 | 309 | 60 | 597.5 | 22751 | 568.0 | 23148 | +450 | +29.5 | strong |
| Call | 22600 | 9007 | 63 | 555.0 | 22740 | 538.2 | 23155 | +458 | +16.8 | strong |
| Call | 22650 | 359 | 31 | 511.0 | 22730 | 512.0 | 23161 | +464 | -1.0 | strong |
| Call | 22700 | 4574 | 517 | 495.0 | 22748 | 475.0 | 23195 | +498 | +20.0 | strong |
| Call | 22750 | 1102 | 259 | 457.7 | 22729 | 448.2 | 23208 | +510 | +9.5 | strong |
| Call | 22800 | 8127 | 2219 | 439.8 | 22751 | 418.6 | 23240 | +543 | +21.2 | strong |
| Call | 22850 | 789 | 254 | 412.1 | 22754 | 395.0 | 23262 | +565 | +17.1 | strong |
| Call | 22900 | 7473 | 4135 | 386.4 | 22758 | 366.3 | 23286 | +589 | +20.1 | strong |
| Call | 22950 | 1218 | 244 | 389.8 | 22808 | 346.0 | 23340 | +643 | +43.8 | strong |
| Call | 23000 | 68635 | 16355 | 374.8 | 22845 | 320.1 | 23375 | +678 | +54.7 | strong |
| Put | 22400 | 13085 | 418 | 195.3 | 22899 | 252.3 | 22205 | +493 | -57.0 | strong |
| Put | 22450 | 552 | 62 | 249.8 | 22766 | 268.6 | 22200 | +497 | -18.7 | strong |
| Put | 22500 | 37034 | 8181 | 212.9 | 22927 | 284.8 | 22287 | +410 | -71.9 | strong |
| Put | 22550 | 726 | 218 | 199.4 | 23003 | 297.1 | 22351 | +347 | -97.8 | strong |
| Put | 22600 | 10087 | 451 | 272.0 | 22831 | 314.6 | 22328 | +369 | -42.6 | strong |
| Put | 22650 | 885 | 272 | 199.5 | 23076 | 335.0 | 22450 | +247 | -135.5 | strong |
| Put | 22700 | 8211 | 1020 | 277.8 | 22908 | 356.8 | 22422 | +275 | -79.0 | strong |
| Put | 22750 | 1024 | 431 | 277.7 | 22952 | 372.4 | 22472 | +225 | -94.7 | strong |
| Put | 22800 | 12135 | 2134 | 348.3 | 22819 | 401.4 | 22452 | +246 | -53.1 | strong |
| Put | 22850 | 2857 | 16 | 243.0 | 23094 | 415.8 | 22607 | +90 | -172.8 | medium |
| Put | 22900 | 5632 | 1591 | 362.1 | 22886 | 448.2 | 22538 | +159 | -86.2 | strong |
| Put | 22950 | 689 | 100 | 334.8 | 22956 | 464.9 | 22615 | +82 | -130.2 | medium |
| Put | 23000 | 52746 | 10893 | 341.5 | 23002 | 500.1 | 22659 | +39 | -158.7 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 86% | +0.16% | -0.08 to +0.37% | 0% of 1 | too few (7/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.98% | -1.17 to -0.71% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 3 | 67% | +0.02% | -0.21 to +0.17% |  | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 2 | 0% | -0.66% | -0.74 to -0.57% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 0% | -0.36% | -0.51 to -0.21% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 0% | -0.10% | -0.10 to -0.10% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.72% | -1.72 to -1.72% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -1.10% | -1.10 to -1.10% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -1.18% | -1.18 to -1.18% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
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
| weekly | PCR up · call writing · walls same · mid walls | 1 | 0% | -0.21% | -0.21 to -0.21% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 0% | -1.12% | -1.12 to -1.12% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.72% | -1.72 to -1.72% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -1.07% | -1.07 to -1.07% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.84% | -0.84 to -0.84% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.84% | -0.84 to -0.84% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 42% | -0.02% | no clear direction |
| intraday | monthly | writers even · few weak writers | 13 | 54% | -0.16% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 10 | 44% | -0.01% | too few (9/10) |
| intraday | weekly | call writers stronger · weak puts | 10 | 25% | -0.15% | too few (8/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · few weak writers | 10 | 10% | -0.71% | down |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.71% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak puts | 4 | 50% | -0.32% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 3 | 0% | -0.20% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 0% | -0.21% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.41% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.84% | too few (1/10) |
| day | monthly | call writers stronger · weak puts | 1 |  |  | too few (0/10) |
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
