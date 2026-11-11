# Nifty option chain pattern log
Updated 2026-11-11 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 469 snapshots over 19 trading days
- 516 patterns logged; 158 different patterns so far

## Latest read (2026-11-11 14:46:05)

Nifty trend: weekly **sideways**, 125-min **up**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-17 (weekly) | 6.0 | 25202 | 0.807 | 25200 | 23000 | 26000 | ±1.83% (24740-25664) | 17.88 |
| 2026-11-23 (monthly) | 12.0 | 25201 | 1.078 | 24400 | 23000 | 26000 | ±2.43% (24590-25813) | 16.73 |

- **Weekly, last 30 min**: `PCR flat · put writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 22 times before; Nifty was up after it 62% of the time, average +0.23%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Nifty was up after it 0% of the time, average -0.15%. Too few outcomes (3/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. Seen 1 times before; Nifty was up after it 100% of the time, average +1.66%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls same · near call wall`. Seen 17 times before; Nifty was up after it 76% of the time, average +0.32%. Too few outcomes (17/20) to trade on.
  - Writers: `put writers stronger · weak calls`. Seen 56 times before; Nifty was up after it 83% of the time, average +0.62%. History points to a bull call debit spread, ATM to about the call wall 26000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 7 times before; Nifty was up after it 60% of the time, average +0.07%. Too few outcomes (5/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 4 times before; Nifty was up after it 100% of the time, average +0.83%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 2 times before; Nifty was up after it 100% of the time, average +0.34%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-17

Strongest call writers at 25400, strongest put writers at 25200; weakest call writers at -, weakest put writers at 25400. Covers 61% of near-money call OI and 64% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24850 | 2831 | 219 | 546.4 | 25302 | 482.9 | 25396 | +195 | +63.5 | strong |
| Call | 24950 | 3858 | 285 | 467.2 | 25302 | 401.8 | 25417 | +215 | +65.4 | strong |
| Call | 25000 | 46613 | 2106 | 365.9 | 25212 | 369.1 | 25366 | +164 | -3.2 | strong |
| Call | 25050 | 5628 | 488 | 388.9 | 25282 | 337.6 | 25439 | +237 | +51.2 | strong |
| Call | 25100 | 16723 | 1765 | 312.0 | 25220 | 307.4 | 25412 | +210 | +4.6 | strong |
| Call | 25150 | 11398 | 5041 | 300.0 | 25241 | 279.6 | 25450 | +248 | +20.3 | strong |
| Call | 25200 | 58062 | 30539 | 262.7 | 25228 | 252.6 | 25463 | +261 | +10.2 | strong |
| Call | 25250 | 39794 | 33422 | 256.8 | 25265 | 227.5 | 25507 | +305 | +29.3 | strong |
| Call | 25300 | 109263 | 87688 | 270.5 | 25343 | 204.8 | 25570 | +369 | +65.7 | strong |
| Call | 25350 | 71909 | 65982 | 255.6 | 25365 | 184.1 | 25606 | +404 | +71.5 | strong |
| Call | 25400 | 123765 | 93605 | 238.3 | 25382 | 164.6 | 25638 | +437 | +73.7 | strong |
| Call | 25450 | 37909 | 33397 | 216.0 | 25384 | 146.8 | 25666 | +464 | +69.2 | strong |
| Call | 25500 | 156219 | 70475 | 183.2 | 25357 | 131.0 | 25683 | +481 | +52.2 | strong |
| Call | 25550 | 37707 | 29324 | 163.1 | 25359 | 116.0 | 25713 | +511 | +47.1 | strong |
| Put | 24850 | 28152 | 20492 | 67.8 | 25327 | 83.7 | 24782 | +420 | -15.9 | strong |
| Put | 24900 | 55439 | 25482 | 62.8 | 25405 | 96.3 | 24837 | +365 | -33.6 | strong |
| Put | 24950 | 20483 | 12293 | 79.9 | 25367 | 111.0 | 24870 | +332 | -31.1 | strong |
| Put | 25000 | 100411 | 34103 | 83.7 | 25399 | 126.6 | 24916 | +285 | -42.9 | strong |
| Put | 25050 | 15636 | 11141 | 99.6 | 25385 | 144.6 | 24950 | +251 | -45.0 | strong |
| Put | 25100 | 46970 | 36810 | 116.4 | 25372 | 163.7 | 24984 | +218 | -47.3 | strong |
| Put | 25150 | 30754 | 29322 | 144.9 | 25332 | 185.7 | 25005 | +197 | -40.8 | strong |
| Put | 25200 | 80234 | 76012 | 169.1 | 25324 | 209.7 | 25031 | +171 | -40.6 | strong |
| Put | 25250 | 33607 | 32723 | 177.9 | 25355 | 234.7 | 25072 | +130 | -56.8 | strong |
| Put | 25300 | 68762 | 67305 | 176.6 | 25406 | 260.6 | 25123 | +78 | -84.0 | medium |
| Put | 25350 | 37288 | 37117 | 200.7 | 25400 | 289.4 | 25149 | +52 | -88.7 | weak |
| Put | 25400 | 40531 | 40140 | 223.9 | 25399 | 320.3 | 25176 | +26 | -96.3 | weak |
| Put | 25450 | 7132 | 7015 | 244.8 | 25406 | 352.9 | 25205 | -3 | -108.1 | weak |
| Put | 25500 | 29947 | 21578 | 273.6 | 25405 | 385.8 | 25226 | -25 | -112.2 | weak |
| Put | 25550 | 2528 | 2449 | 308.1 | 25395 | 422.0 | 25242 | -40 | -113.9 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 25500, strongest put writers at 25000; weakest call writers at 25000, weakest put writers at 25850. Covers 94% of near-money call OI and 93% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24850 | 1196 | 1196 | 204.3 | 24370 | 575.1 | 25054 | -147 | -370.8 | weak |
| Call | 24900 | 12844 | 12801 | 257.2 | 24631 | 516.0 | 25157 | -44 | -258.8 | weak |
| Call | 24950 | 1274 | 1269 | 269.2 | 24728 | 490.4 | 25219 | +18 | -221.1 | weak |
| Call | 25000 | 60260 | 50252 | 101.8 | 24011 | 448.5 | 25102 | -100 | -346.7 | weak |
| Call | 25050 | 1170 | 1169 | 273.5 | 24871 | 419.9 | 25324 | +122 | -146.3 | strong |
| Call | 25100 | 11545 | 11470 | 222.4 | 24797 | 390.0 | 25322 | +121 | -167.6 | strong |
| Call | 25150 | 1899 | 1898 | 245.8 | 24903 | 362.3 | 25396 | +194 | -116.5 | strong |
| Call | 25200 | 24477 | 24394 | 227.8 | 24863 | 332.9 | 25428 | +226 | -105.2 | strong |
| Call | 25250 | 3056 | 3054 | 223.2 | 24945 | 308.6 | 25473 | +272 | -85.5 | strong |
| Call | 25300 | 26412 | 26392 | 287.3 | 25120 | 285.2 | 25587 | +386 | +2.0 | strong |
| Call | 25350 | 3977 | 3977 | 276.8 | 25193 | 261.4 | 25627 | +425 | +15.4 | strong |
| Call | 25400 | 19280 | 19215 | 241.5 | 25156 | 240.2 | 25642 | +440 | +1.3 | strong |
| Call | 25450 | 2865 | 2851 | 215.8 | 25129 | 221.2 | 25666 | +464 | -5.4 | strong |
| Call | 25500 | 59191 | 55042 | 77.5 | 24631 | 201.2 | 25577 | +376 | -123.7 | strong |
| Call | 25550 | 2337 | 2279 | 137.1 | 24969 | 184.2 | 25687 | +486 | -47.1 | strong |
| Put | 24850 | 2003 | 2001 | 278.0 | 24937 | 149.2 | 24572 | +629 | +128.8 | strong |
| Put | 24900 | 18981 | 18966 | 294.8 | 24957 | 163.9 | 24605 | +596 | +130.9 | strong |
| Put | 24950 | 1813 | 1813 | 328.7 | 24940 | 179.0 | 24621 | +580 | +149.7 | strong |
| Put | 25000 | 105818 | 95613 | 610.0 | 24687 | 195.4 | 24390 | +811 | +414.6 | strong |
| Put | 25050 | 1345 | 1343 | 316.7 | 25060 | 214.7 | 24733 | +468 | +102.0 | strong |
| Put | 25100 | 10751 | 10743 | 340.3 | 25076 | 233.7 | 24760 | +442 | +106.6 | strong |
| Put | 25150 | 1587 | 1585 | 267.0 | 25237 | 255.1 | 24883 | +318 | +11.9 | strong |
| Put | 25200 | 17887 | 17858 | 292.4 | 25247 | 278.9 | 24908 | +294 | +13.5 | strong |
| Put | 25250 | 3575 | 3572 | 276.9 | 25283 | 303.0 | 24973 | +228 | -26.1 | strong |
| Put | 25300 | 20537 | 20527 | 260.3 | 25370 | 327.4 | 25040 | +162 | -67.1 | strong |
| Put | 25350 | 2510 | 2500 | 293.0 | 25352 | 355.3 | 25057 | +144 | -62.3 | strong |
| Put | 25400 | 13236 | 13216 | 299.4 | 25376 | 382.9 | 25101 | +101 | -83.5 | medium |
| Put | 25450 | 1067 | 1060 | 340.2 | 25352 | 413.1 | 25110 | +92 | -73.0 | medium |
| Put | 25500 | 30830 | 22916 | 886.2 | 24718 | 445.4 | 24614 | +588 | +440.9 | strong |
| Put | 25550 | 410 | 405 | 425.8 | 25319 | 479.3 | 25124 | +77 | -53.5 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 34 | 73% | +0.26% | -0.44 to +0.97% | 100% of 1 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 18 | 76% | +0.32% | -0.71 to +1.68% |  | up |
| weekly | PCR up · put writing · walls same · near call wall | 17 | 94% | +0.34% | -0.02 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · put and call writing · walls same · near call wall | 15 | 60% | +0.32% | -0.71 to +1.70% | 100% of 1 | no clear direction |
| monthly | PCR flat · put writing · walls same · mid walls | 14 | 100% | +0.49% | +0.09 to +1.02% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near put wall | 12 | 58% | +0.05% | -0.47 to +0.42% | 33% of 3 | no clear direction |
| weekly | PCR down · call writing · walls same · near put wall | 12 | 75% | +0.27% | -0.37 to +0.85% | 33% of 3 | no clear direction |
| weekly | PCR down · unwinding · walls same · near call wall | 11 | 70% | +0.39% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| monthly | PCR flat · put writing · walls same · near call wall | 11 | 78% | +0.41% | -0.71 to +1.56% |  | too few (9/10) |
| monthly | PCR up · put writing · walls same · near call wall | 10 | 50% | +0.14% | -0.56 to +0.93% | 100% of 1 | no clear direction |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 8 | 38% | -0.00% | -0.78 to +0.90% | 100% of 1 | too few (8/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% |  | too few (6/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.05% | -0.84 to +0.62% | 100% of 1 | too few (7/10) |
| weekly | PCR up · put writing · walls up · near put wall | 7 | 57% | +0.34% | -0.13 to +1.65% | 0% of 3 | too few (7/10) |
| monthly | PCR down · call writing · walls same · near call wall | 7 | 83% | +0.27% | -0.78 to +1.18% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 7 | 80% | +0.21% | -0.12 to +0.71% | 100% of 1 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 7 | 33% | +0.07% | -0.40 to +0.90% | 67% of 3 | too few (3/10) |
| weekly | PCR up · put writing · walls up · mid walls | 6 | 83% | +0.48% | -0.16 to +1.40% | 33% of 3 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| weekly | PCR down · call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.64 to +0.75% | 33% of 3 | too few (6/10) |
| monthly | PCR up · put writing · walls same · mid walls | 6 | 100% | +0.65% | +0.24 to +0.85% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 6 | 80% | +0.04% | -0.18 to +0.19% |  | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| weekly | PCR down · call writing · walls same · near call wall | 5 | 80% | +0.53% | -0.02 to +0.91% | 33% of 3 | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 5 | 60% | +0.05% | -0.47 to +0.49% | 100% of 1 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 5 | 80% | +0.46% | -1.11 to +1.69% | 0% of 2 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near call wall | 5 | 80% | +0.59% | -0.06 to +1.68% | 50% of 2 | too few (5/10) |
| weekly | PCR down · call writing · walls down · mid walls | 5 | 80% | +0.31% | -0.07 to +0.54% | 50% of 2 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 5 | 75% | +0.21% | -0.05 to +0.63% | 50% of 2 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 75% | +0.74% | -0.07 to +1.65% |  | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 4 | 100% | +0.35% | +0.13 to +0.59% | 0% of 3 | too few (4/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 4 | 75% | +0.24% | -0.11 to +0.50% | 50% of 2 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put writing · walls same · mid walls | 4 | 25% | -0.27% | -0.70 to +0.89% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls down · near put wall | 4 | 50% | +0.05% | -0.51 to +0.73% | 0% of 1 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | +0.10% | -0.68 to +0.75% | 50% of 2 | too few (4/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 3 | 33% | +0.13% | -0.02 to +0.43% | 0% of 2 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 3 |  |  |  | 100% of 3 | too few (0/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 3 | 67% | +0.06% | -0.84 to +0.58% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 3 | 100% | +1.15% | +0.59 to +1.82% | 0% of 2 | too few (3/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 3 | 67% | +0.24% | -0.22 to +0.68% | 67% of 3 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 33% | -0.17% | -0.75 to +0.38% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 3 | 100% | +0.54% | +0.47 to +0.61% | 50% of 2 | too few (3/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 3 | 100% | +0.50% | +0.37 to +0.62% |  | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% |  | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 0% | -0.44% | -0.69 to -0.20% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 2 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 2 | 100% | +0.15% | +0.14 to +0.16% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 2 | 50% | -0.03% | -0.08 to +0.03% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 2 | 100% | +0.61% | +0.01 to +1.22% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +1.86% | +1.86 to +1.86% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 | 100% | +0.53% | +0.53 to +0.53% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +1.01% | -0.39 to +2.40% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% |  | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 100% | +0.35% | +0.06 to +0.65% | 100% of 2 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 94 | 70% | +0.17% | up |
| intraday | monthly | writers even · weak calls | 64 | 80% | +0.20% | up |
| intraday | weekly | writers even · few weak writers | 64 | 56% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · weak calls | 59 | 78% | +0.39% | up |
| intraday | monthly | put writers stronger · weak calls | 57 | 83% | +0.62% | up |
| intraday | weekly | call writers stronger · weak puts | 34 | 88% | +0.40% | up |
| intraday | weekly | put writers stronger · few weak writers | 28 | 92% | +0.34% | up |
| intraday | weekly | call writers stronger · few weak writers | 23 | 62% | +0.23% | no clear direction |
| intraday | weekly | writers even · weak calls | 23 | 90% | +0.51% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak on both sides | 7 | 100% | +0.39% | too few (7/10) |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| day | monthly | writers even · few weak writers | 8 | 50% | +0.34% | too few (8/10) |
| day | monthly | put writers stronger · weak calls | 5 | 100% | +0.83% | too few (4/10) |
| day | weekly | put writers stronger · weak calls | 5 | 80% | +0.36% | too few (5/10) |
| day | monthly | writers even · weak calls | 4 | 75% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | writers even · few weak writers | 3 | 67% | +1.02% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 2 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak calls | 2 | 50% | +1.00% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |

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
| intraday | monthly | writers even · weak calls · weekly sideways · 125m up | 19 | 53% | -0.02% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.73% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 12 | 42% | -0.19% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 8 | 60% | +0.07% | too few (5/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 5 | 100% | +0.26% | too few (5/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 4 | 0% | -0.15% | too few (3/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 2 | 100% | +0.67% | too few (2/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 2 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m up | 1 | 100% | +0.91% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 100% | +0.55% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 3 | 100% | +0.34% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +1.32% | too few (2/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.34% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
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
