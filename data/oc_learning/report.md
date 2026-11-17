# Nifty option chain pattern log
Updated 2026-11-17 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 548 snapshots over 23 trading days
- 608 patterns logged; 177 different patterns so far

## Latest read (2026-11-17 09:45:39)

Nifty trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-17 (weekly) | 0.2 | 25360 | 0.957 | 25300 | 25300 | 25400 | ±0.43% (25250-25469) | 10.26 |
| 2026-11-23 (monthly) | 6.2 | 25361 | 0.828 | 24900 | 25000 | 26000 | ±1.45% (24993-25729) | 14.35 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · mid walls`. Seen 9 times before; Nifty was up after it 33% of the time, average +0.02%. Too few outcomes (9/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 23 times before; Nifty was up after it 90% of the time, average +0.51%. History points to a bull call debit spread, ATM to about the call wall 25400.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 5 times before; Nifty was up after it 100% of the time, average +0.26%. Too few outcomes (5/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.55%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 2 times before; Nifty was up after it 50% of the time, average +1.00%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put and call writing · walls same · mid walls`. Seen 6 times before; Nifty was up after it 83% of the time, average +0.28%. Too few outcomes (6/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 99 times before; Nifty was up after it 70% of the time, average +0.16%. History points to a bull call debit spread, ATM to about the call wall 26000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 4 times before; Nifty was up after it 100% of the time, average +0.08%. Too few outcomes (3/20) to trade on.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · mid walls`. Seen 3 times before; Nifty was up after it 33% of the time, average +0.16%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 9 times before; Nifty was up after it 56% of the time, average +0.34%. Too few outcomes (9/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Nifty was up after it 100% of the time, average +0.27%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-11-17

Strongest call writers at 25500, strongest put writers at 25200; weakest call writers at 25300, weakest put writers at 25400. Covers 93% of near-money call OI and 97% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25000 | 21620 | 12157 | 230.7 | 25140 | 364.6 | 25231 | -129 | -133.9 | weak |
| Call | 25050 | 5780 | 5487 | 200.4 | 25158 | 314.9 | 25250 | -109 | -114.4 | weak |
| Call | 25100 | 25043 | 24650 | 170.3 | 25165 | 266.9 | 25270 | -89 | -96.7 | weak |
| Call | 25150 | 21818 | 21737 | 140.6 | 25180 | 218.6 | 25291 | -69 | -77.9 | weak |
| Call | 25200 | 103393 | 102569 | 126.2 | 25225 | 173.6 | 25326 | -33 | -47.4 | weak |
| Call | 25250 | 100022 | 99854 | 109.4 | 25259 | 131.3 | 25359 | -0 | -21.9 | weak |
| Call | 25300 | 336776 | 334063 | 102.6 | 25315 | 92.1 | 25403 | +43 | +10.5 | weak |
| Call | 25350 | 364309 | 363224 | 74.5 | 25338 | 60.9 | 25424 | +65 | +13.6 | medium |
| Call | 25400 | 360960 | 353072 | 62.2 | 25327 | 37.5 | 25462 | +103 | +24.7 | medium |
| Call | 25450 | 192654 | 191237 | 44.1 | 25321 | 21.2 | 25494 | +134 | +22.9 | strong |
| Call | 25500 | 350869 | 318074 | 40.7 | 25309 | 11.7 | 25541 | +181 | +29.1 | strong |
| Call | 25550 | 171058 | 167832 | 26.8 | 25316 | 6.0 | 25577 | +217 | +20.8 | strong |
| Call | 25600 | 218668 | 206360 | 29.7 | 25305 | 3.1 | 25630 | +270 | +26.6 | strong |
| Call | 25650 | 104821 | 103462 | 19.2 | 25280 | 1.8 | 25669 | +310 | +17.5 | strong |
| Call | 25700 | 177555 | 154919 | 27.9 | 25283 | 1.2 | 25728 | +368 | +26.6 | strong |
| Put | 25000 | 308954 | 294288 | 28.2 | 25305 | 2.3 | 24972 | +388 | +25.9 | strong |
| Put | 25050 | 142214 | 141926 | 24.7 | 25314 | 3.0 | 25025 | +334 | +21.7 | strong |
| Put | 25100 | 232422 | 230602 | 40.9 | 25309 | 4.5 | 25059 | +301 | +36.5 | strong |
| Put | 25150 | 150608 | 150509 | 41.5 | 25309 | 6.9 | 25109 | +251 | +34.5 | strong |
| Put | 25200 | 400603 | 400447 | 41.1 | 25318 | 11.2 | 25159 | +201 | +29.9 | strong |
| Put | 25250 | 257658 | 257645 | 36.9 | 25338 | 18.4 | 25213 | +147 | +18.6 | strong |
| Put | 25300 | 456589 | 456551 | 43.6 | 25348 | 30.6 | 25256 | +103 | +13.1 | medium |
| Put | 25350 | 209264 | 209260 | 59.6 | 25352 | 48.9 | 25290 | +69 | +10.7 | medium |
| Put | 25400 | 117839 | 117820 | 94.8 | 25349 | 75.5 | 25305 | +54 | +19.2 | weak |
| Put | 25450 | 32574 | 32570 | 120.0 | 25353 | 110.0 | 25330 | +30 | +10.0 | weak |
| Put | 25500 | 35890 | 34348 | 190.9 | 25348 | 150.7 | 25309 | +51 | +40.2 | weak |
| Put | 25550 | 5509 | 5502 | 236.8 | 25332 | 194.7 | 25313 | +46 | +42.2 | weak |
| Put | 25600 | 9214 | 9185 | 287.6 | 25327 | 241.8 | 25312 | +47 | +45.8 | weak |
| Put | 25650 | 1699 | 1690 | 338.4 | 25335 | 290.4 | 25312 | +48 | +48.0 | weak |
| Put | 25700 | 2300 | 2264 | 414.9 | 25341 | 340.0 | 25285 | +75 | +75.0 | medium |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 26000, strongest put writers at 25000; weakest call writers at 25000, weakest put writers at -. Covers 97% of near-money call OI and 96% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25000 | 59719 | 51232 | 148.4 | 24215 | 444.7 | 25148 | -213 | -296.3 | weak |
| Call | 25050 | 1292 | 1292 | 303.6 | 25072 | 404.0 | 25354 | -7 | -100.4 | weak |
| Call | 25100 | 21652 | 21597 | 263.2 | 25025 | 368.3 | 25363 | +2 | -105.1 | weak |
| Call | 25150 | 4088 | 4088 | 255.4 | 25123 | 331.6 | 25405 | +44 | -76.2 | weak |
| Call | 25200 | 60759 | 60699 | 254.4 | 25123 | 298.0 | 25454 | +93 | -43.6 | medium |
| Call | 25250 | 9380 | 9378 | 230.5 | 25198 | 265.6 | 25481 | +119 | -35.1 | strong |
| Call | 25300 | 66167 | 66153 | 244.4 | 25233 | 235.0 | 25544 | +183 | +9.4 | strong |
| Call | 25350 | 14486 | 14486 | 213.3 | 25289 | 206.0 | 25563 | +202 | +7.3 | strong |
| Call | 25400 | 36270 | 36228 | 201.5 | 25230 | 180.0 | 25602 | +240 | +21.5 | strong |
| Call | 25450 | 6387 | 6377 | 174.4 | 25198 | 156.8 | 25624 | +263 | +17.6 | strong |
| Call | 25500 | 77350 | 74239 | 105.0 | 24899 | 134.9 | 25605 | +244 | -29.9 | strong |
| Call | 25550 | 7819 | 7771 | 120.2 | 25178 | 115.5 | 25670 | +309 | +4.7 | strong |
| Call | 25600 | 26845 | 26807 | 124.2 | 25185 | 97.6 | 25724 | +363 | +26.6 | strong |
| Call | 25650 | 5824 | 5824 | 89.2 | 25228 | 82.5 | 25739 | +378 | +6.7 | strong |
| Call | 25700 | 34167 | 34072 | 91.2 | 25152 | 69.4 | 25791 | +430 | +21.8 | strong |
| Put | 25000 | 152530 | 144262 | 372.0 | 24967 | 53.2 | 24628 | +733 | +318.8 | strong |
| Put | 25050 | 10243 | 10239 | 109.9 | 25294 | 63.4 | 24940 | +421 | +46.5 | strong |
| Put | 25100 | 35685 | 35679 | 202.6 | 25191 | 75.0 | 24897 | +464 | +127.6 | strong |
| Put | 25150 | 6439 | 6438 | 199.7 | 25230 | 88.7 | 24950 | +411 | +111.0 | strong |
| Put | 25200 | 60242 | 60220 | 207.8 | 25266 | 103.9 | 24992 | +369 | +103.9 | strong |
| Put | 25250 | 11395 | 11388 | 190.1 | 25295 | 121.5 | 25060 | +301 | +68.6 | strong |
| Put | 25300 | 70458 | 70359 | 210.6 | 25313 | 140.4 | 25089 | +272 | +70.1 | strong |
| Put | 25350 | 18901 | 18898 | 219.5 | 25295 | 162.2 | 25131 | +231 | +57.3 | strong |
| Put | 25400 | 23514 | 23505 | 258.7 | 25332 | 186.2 | 25141 | +220 | +72.5 | strong |
| Put | 25450 | 2391 | 2387 | 267.1 | 25330 | 212.6 | 25183 | +178 | +54.5 | strong |
| Put | 25500 | 35894 | 29118 | 702.3 | 24911 | 241.5 | 24798 | +563 | +460.8 | strong |
| Put | 25550 | 717 | 714 | 378.7 | 25288 | 275.0 | 25171 | +190 | +103.7 | strong |
| Put | 25600 | 3949 | 3937 | 511.2 | 25215 | 303.9 | 25089 | +272 | +207.3 | strong |
| Put | 25650 | 322 | 320 | 433.1 | 25307 | 342.1 | 25217 | +144 | +91.0 | strong |
| Put | 25700 | 1746 | 1725 | 596.5 | 25172 | 376.8 | 25104 | +258 | +219.7 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 35 | 71% | +0.25% | -0.44 to +0.97% | 100% of 1 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 18 | 83% | +0.36% | -0.50 to +1.68% |  | up |
| weekly | PCR up · put writing · walls same · near call wall | 17 | 94% | +0.34% | -0.02 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · put and call writing · walls same · near call wall | 16 | 56% | +0.28% | -0.71 to +1.70% | 100% of 1 | no clear direction |
| weekly | PCR down · call writing · walls same · near put wall | 14 | 71% | +0.28% | -0.37 to +0.85% | 50% of 4 | no clear direction |
| monthly | PCR flat · put writing · walls same · mid walls | 14 | 100% | +0.49% | +0.09 to +1.02% | 100% of 1 | up |
| monthly | PCR flat · quiet OI · walls same · near put wall | 12 | 80% | +0.08% | -0.18 to +0.20% |  | no clear direction |
| monthly | PCR flat · put writing · walls same · near call wall | 12 | 70% | +0.38% | -0.50 to +1.56% |  | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 12 | 67% | +0.06% | -0.47 to +0.42% | 50% of 4 | no clear direction |
| weekly | PCR down · unwinding · walls same · near call wall | 11 | 70% | +0.39% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| monthly | PCR up · put writing · walls same · near call wall | 11 | 50% | +0.18% | -0.40 to +0.93% | 100% of 1 | no clear direction |
| weekly | PCR up · put and call writing · walls same · mid walls | 10 | 33% | +0.02% | -0.78 to +0.90% | 100% of 2 | too few (9/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 9 | 60% | +0.09% | -0.40 to +0.90% | 75% of 4 | too few (5/10) |
| weekly | PCR down · call writing · walls same · mid walls | 9 | 89% | +0.26% | -0.43 to +0.75% | 50% of 4 | too few (9/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 8 | 67% | +0.14% | -0.16 to +0.71% | 100% of 1 | too few (6/10) |
| monthly | PCR down · call writing · walls same · near call wall | 8 | 83% | +0.27% | -0.78 to +1.18% | 100% of 1 | too few (6/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% |  | too few (6/10) |
| weekly | PCR up · put writing · walls up · near put wall | 8 | 62% | +0.33% | -0.13 to +1.65% | 0% of 4 | too few (8/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| weekly | PCR down · call writing · walls down · mid walls | 8 | 88% | +0.28% | -0.07 to +0.54% | 67% of 3 | too few (8/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 7 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (7/10) |
| weekly | PCR up · put writing · walls same · mid walls | 7 | 43% | -0.06% | -0.57 to +0.89% | 67% of 3 | too few (7/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR up · put writing · walls same · mid walls | 6 | 100% | +0.65% | +0.24 to +0.85% | 100% of 1 | too few (6/10) |
| weekly | PCR up · put writing · walls up · mid walls | 6 | 83% | +0.48% | -0.16 to +1.40% | 33% of 3 | too few (6/10) |
| weekly | PCR down · call writing · walls down · near call wall | 6 | 83% | +0.53% | -0.06 to +1.68% | 67% of 3 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 6 | 67% | +0.27% | -1.22 to +1.24% | 50% of 2 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 5 | 80% | +0.12% | -0.05 to +0.28% |  | too few (5/10) |
| weekly | PCR down · call writing · walls same · near call wall | 5 | 80% | +0.53% | -0.02 to +0.91% | 33% of 3 | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 5 | 60% | +0.05% | -0.47 to +0.49% | 100% of 1 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 100% of 1 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 5 | 80% | +0.46% | -1.11 to +1.69% | 0% of 2 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 5 | 80% | +0.22% | -0.11 to +0.50% | 33% of 3 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 5 | 75% | +0.21% | -0.05 to +0.63% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 5 | 100% | +0.29% | +0.04 to +0.59% | 0% of 4 | too few (5/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 5 | 100% | +0.54% | +0.47 to +0.61% | 67% of 3 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 5 | 60% | +0.15% | -0.07 to +0.33% |  | too few (5/10) |
| weekly | PCR down · call writing · walls down · near put wall | 5 | 60% | +0.09% | -0.51 to +0.73% | 0% of 2 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 4 | 33% | +0.13% | -0.02 to +0.43% | 33% of 3 | too few (3/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 100% | +0.79% | +0.14 to +1.65% |  | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 4 | 50% | +0.06% | -0.63 to +0.58% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 4 | 75% | +0.84% | -0.07 to +1.82% | 33% of 3 | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 4 | 25% | -0.15% | -0.75 to +0.38% | 50% of 2 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 4 | 100% | +0.50% | +0.37 to +0.62% |  | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | +0.10% | -0.68 to +0.75% | 50% of 2 | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 4 | 100% | +0.24% | +0.10 to +0.28% |  | too few (4/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 4 | 75% | +0.10% | -0.02 to +0.28% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 4 | 75% | +0.22% | -0.22 to +0.68% | 75% of 4 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 4 |  |  |  | 100% of 4 | too few (0/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 3 | 33% | -0.01% | -0.37 to +0.53% | 50% of 2 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 3 | 100% | +0.19% | +0.16 to +0.25% | 50% of 2 | too few (3/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 3 | 67% | +0.06% | -0.13 to +0.17% |  | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 3 | 100% | +0.28% | +0.07 to +0.50% | 100% of 2 | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 3 | 100% | +0.12% | +0.05 to +0.16% | 100% of 2 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 2 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 2 | 100% | +0.20% | +0.20 to +0.20% | 100% of 2 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 2 | 100% | +0.30% | +0.29 to +0.31% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near put wall | 2 | 100% | +0.21% | +0.18 to +0.24% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 0% | -0.44% | -0.69 to -0.20% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 2 | 100% | +0.61% | +0.01 to +1.22% | 50% of 2 | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 2 | 100% | +0.15% | +0.10 to +0.21% |  | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% |  | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · near put wall | 1 | 0% | -0.09% | -0.09 to -0.09% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +1.86% | +1.86 to +1.86% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near call wall | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near put wall | 1 | 0% | -0.29% | -0.29 to -0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · mid walls | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 4 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | +0.73% | -0.39 to +2.40% |  | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 100% | +0.55% | +0.51 to +0.58% | 50% of 2 | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% |  | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 100% | +0.35% | +0.06 to +0.65% | 100% of 2 | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.17% | -0.61 to +0.27% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.58% | +0.58 to +0.58% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 100 | 70% | +0.16% | up |
| intraday | monthly | writers even · weak calls | 99 | 76% | +0.18% | up |
| intraday | weekly | writers even · few weak writers | 97 | 57% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · weak calls | 62 | 86% | +0.59% | up |
| intraday | weekly | put writers stronger · weak calls | 59 | 78% | +0.39% | up |
| intraday | weekly | call writers stronger · weak puts | 38 | 89% | +0.40% | up |
| intraday | weekly | call writers stronger · few weak writers | 31 | 79% | +0.25% | up |
| intraday | weekly | put writers stronger · few weak writers | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · weak calls | 24 | 90% | +0.51% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak on both sides | 7 | 100% | +0.39% | too few (7/10) |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| day | monthly | writers even · few weak writers | 10 | 56% | +0.34% | too few (9/10) |
| day | monthly | writers even · weak calls | 7 | 71% | +0.52% | too few (7/10) |
| day | weekly | writers even · few weak writers | 6 | 67% | +0.55% | too few (6/10) |
| day | weekly | put writers stronger · weak calls | 5 | 80% | +0.40% | too few (5/10) |
| day | monthly | put writers stronger · weak calls | 4 | 100% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | writers even · weak calls | 3 | 50% | +1.00% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 2 | 100% | +0.92% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 57 | 78% | +0.39% | up |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 49 | 85% | +0.68% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 45 | 93% | +0.31% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m up | 37 | 51% | +0.05% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 34 | 50% | -0.01% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 28 | 77% | +0.29% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m sideways | 17 | 88% | +0.14% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.73% | up |
| intraday | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 13 | 91% | +0.21% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 11 | 70% | +0.07% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 6 | 100% | +0.18% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 6 | 80% | +0.16% | too few (5/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 6 | 100% | +0.26% | too few (5/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 5 | 100% | +0.08% | too few (3/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 5 | 100% | +0.53% | too few (5/10) |
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
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 2 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 | 0% | -0.01% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 1 | 100% | +0.28% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m up | 1 | 100% | +0.91% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 100% | +0.55% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +1.32% | too few (2/10) |
| day | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.27% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m up | 2 | 50% | -0.22% | too few (2/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.17% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.58% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.18% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 1 | 100% | +0.58% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m up | 1 | 100% | +2.01% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
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
