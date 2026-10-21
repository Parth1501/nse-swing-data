# Nifty option chain pattern log
Updated 2026-10-21 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 122 snapshots over 5 trading days
- 131 patterns logged; 84 different patterns so far

## Latest read (2026-10-21 15:40:00)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 6.0 | 22811 | 0.726 | 22900 | 22000 | 23000 | ±1.47% (22475-23148) | 14.32 |
| 2026-11-23 (monthly) | 33.0 | 22811 | 1.135 | 23000 | 22000 | 23000 | ±3.53% (22006-23616) | 14.41 |

- **Weekly, last 30 min**: `PCR flat · unwinding · walls same · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.07%. Too few outcomes (1/20) to trade on.
  - Writers: `call writers stronger · weak puts`. Seen 13 times before; Nifty was up after it 75% of the time, average +0.24%. Too few outcomes (12/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.34%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR down · quiet OI · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 14 times before; Nifty was up after it 57% of the time, average -0.05%. Too few outcomes (14/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at 22600, weakest put writers at 23000. Covers 82% of near-money call OI and 76% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22500 | 37283 | 16646 | 392.1 | 22791 | 308.0 | 22892 | +81 | +84.1 | medium |
| Call | 22550 | 5372 | 4222 | 369.1 | 22823 | 274.6 | 22919 | +108 | +94.5 | strong |
| Call | 22600 | 33860 | 22740 | 249.4 | 22700 | 241.0 | 22849 | +38 | +8.4 | weak |
| Call | 22650 | 15155 | 13723 | 214.7 | 22709 | 210.1 | 22865 | +53 | +4.5 | medium |
| Call | 22700 | 89278 | 73953 | 193.2 | 22716 | 184.2 | 22893 | +82 | +9.0 | medium |
| Call | 22750 | 41256 | 37707 | 177.6 | 22737 | 158.7 | 22928 | +116 | +18.9 | strong |
| Call | 22800 | 120687 | 105492 | 177.4 | 22778 | 135.9 | 22977 | +166 | +41.4 | strong |
| Call | 22850 | 37447 | 35601 | 168.1 | 22815 | 116.9 | 23018 | +207 | +51.2 | strong |
| Call | 22900 | 115904 | 105284 | 159.6 | 22842 | 98.4 | 23060 | +248 | +61.2 | strong |
| Call | 22950 | 61375 | 59870 | 144.3 | 22859 | 83.0 | 23094 | +283 | +61.3 | strong |
| Call | 23000 | 251027 | 196487 | 137.2 | 22882 | 71.5 | 23137 | +326 | +65.7 | strong |
| Call | 23050 | 65375 | 63498 | 156.4 | 22989 | 60.3 | 23206 | +395 | +96.1 | strong |
| Call | 23100 | 156979 | 138713 | 136.9 | 22988 | 50.4 | 23237 | +426 | +86.5 | strong |
| Call | 23150 | 56217 | 54231 | 124.4 | 23017 | 43.0 | 23274 | +463 | +81.4 | strong |
| Put | 22500 | 132347 | 81713 | 53.8 | 22960 | 76.4 | 22446 | +365 | -22.6 | strong |
| Put | 22550 | 24518 | 22629 | 50.1 | 22977 | 90.2 | 22500 | +311 | -40.2 | strong |
| Put | 22600 | 88049 | 65266 | 72.0 | 22977 | 107.0 | 22528 | +283 | -35.0 | strong |
| Put | 22650 | 31742 | 29376 | 98.2 | 22882 | 127.5 | 22552 | +260 | -29.3 | strong |
| Put | 22700 | 110593 | 84849 | 106.3 | 22933 | 148.8 | 22594 | +218 | -42.5 | strong |
| Put | 22750 | 41706 | 40496 | 121.6 | 22914 | 171.2 | 22628 | +183 | -49.5 | strong |
| Put | 22800 | 81336 | 61650 | 117.4 | 22964 | 200.3 | 22683 | +129 | -83.0 | strong |
| Put | 22850 | 13690 | 13032 | 125.4 | 22979 | 230.7 | 22725 | +87 | -105.3 | medium |
| Put | 22900 | 60278 | 55536 | 132.1 | 23011 | 260.9 | 22768 | +43 | -128.8 | weak |
| Put | 22950 | 14047 | 13921 | 143.4 | 23012 | 299.9 | 22807 | +5 | -156.5 | weak |
| Put | 23000 | 93359 | 74641 | 156.2 | 23054 | 335.4 | 22844 | -32 | -179.1 | weak |
| Put | 23050 | 13430 | 13374 | 145.0 | 23091 | 374.3 | 22905 | -94 | -229.3 | weak |
| Put | 23100 | 35058 | 31443 | 173.1 | 23094 | 415.0 | 22927 | -116 | -241.9 | weak |
| Put | 23150 | 6455 | 6320 | 205.0 | 23083 | 455.9 | 22945 | -134 | -250.9 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23400. Covers 31% of near-money call OI and 28% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22500 | 14084 | 3000 | 634.7 | 22765 | 600.8 | 23135 | +323 | +33.9 | strong |
| Call | 22550 | 394 | 145 | 567.4 | 22717 | 571.8 | 23117 | +306 | -4.4 | strong |
| Call | 22600 | 9106 | 207 | 532.6 | 22706 | 536.0 | 23133 | +321 | -3.4 | strong |
| Call | 22650 | 451 | 124 | 493.9 | 22698 | 505.0 | 23144 | +333 | -11.1 | strong |
| Call | 22700 | 15836 | 11819 | 479.8 | 22736 | 472.3 | 23180 | +368 | +7.5 | strong |
| Call | 22750 | 1206 | 381 | 447.6 | 22711 | 445.2 | 23198 | +386 | +2.4 | strong |
| Call | 22800 | 13667 | 7759 | 419.4 | 22726 | 417.5 | 23219 | +408 | +1.9 | strong |
| Call | 22850 | 940 | 408 | 400.1 | 22743 | 391.1 | 23250 | +439 | +8.9 | strong |
| Call | 22900 | 9600 | 6262 | 376.4 | 22740 | 365.0 | 23276 | +465 | +11.3 | strong |
| Call | 22950 | 1238 | 278 | 381.9 | 22791 | 340.8 | 23332 | +520 | +41.1 | strong |
| Call | 23000 | 71453 | 19173 | 365.5 | 22830 | 317.5 | 23365 | +554 | +48.0 | strong |
| Call | 23050 | 1602 | 56 | 346.7 | 22838 | 293.1 | 23397 | +585 | +53.5 | strong |
| Call | 23100 | 13900 | 3464 | 339.4 | 22887 | 271.4 | 23439 | +628 | +67.9 | strong |
| Call | 23150 | 1101 | 51 | 284.4 | 22812 | 251.2 | 23434 | +623 | +33.2 | strong |
| Put | 22500 | 40872 | 12264 | 239.2 | 22856 | 274.5 | 22261 | +551 | -35.3 | strong |
| Put | 22550 | 752 | 250 | 214.0 | 22962 | 289.1 | 22336 | +475 | -75.1 | strong |
| Put | 22600 | 10257 | 830 | 299.7 | 22764 | 307.4 | 22300 | +511 | -7.6 | strong |
| Put | 22650 | 918 | 313 | 221.0 | 23020 | 326.4 | 22429 | +382 | -105.4 | strong |
| Put | 22700 | 19562 | 12394 | 334.5 | 22751 | 345.0 | 22366 | +446 | -10.5 | strong |
| Put | 22750 | 1024 | 444 | 283.3 | 22940 | 365.6 | 22467 | +345 | -82.2 | strong |
| Put | 22800 | 16358 | 6357 | 378.9 | 22752 | 387.4 | 22421 | +390 | -8.5 | strong |
| Put | 22850 | 2855 | 60 | 370.2 | 22860 | 407.8 | 22480 | +332 | -37.6 | strong |
| Put | 22900 | 6680 | 2679 | 395.8 | 22816 | 434.4 | 22504 | +307 | -38.6 | strong |
| Put | 22950 | 658 | 95 | 334.8 | 22956 | 459.4 | 22615 | +196 | -124.6 | strong |
| Put | 23000 | 55096 | 13321 | 371.0 | 22946 | 487.0 | 22629 | +182 | -116.0 | strong |
| Put | 23050 | 559 | 118 | 339.1 | 23051 | 510.2 | 22711 | +100 | -171.1 | medium |
| Put | 23100 | 9362 | 3208 | 417.9 | 22936 | 538.4 | 22682 | +129 | -120.5 | strong |
| Put | 23150 | 1463 | 149 | 355.0 | 23094 | 566.2 | 22795 | +16 | -211.2 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 4 | 50% | +0.09% | -0.74 to +0.62% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 3 | 67% | +0.02% | -0.21 to +0.17% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 2 | 100% | +0.32% | +0.31 to +0.32% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · few weak writers | 15 | 57% | -0.05% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 14 | 75% | +0.24% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 10 | 44% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · few weak writers | 10 | 10% | -0.56% | down |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | writers even · weak puts | 5 | 40% | +0.12% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak puts | 4 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 100% | +0.39% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.34% | too few (1/10) |
| day | monthly | writers even · few weak writers | 1 |  |  | too few (0/10) |
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
