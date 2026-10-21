# Nifty option chain pattern log
Updated 2026-10-21 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 103 snapshots over 5 trading days
- 111 patterns logged; 74 different patterns so far

## Latest read (2026-10-21 10:45:09)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 6.2 | 22967 | 0.85 | 23000 | 22500 | 23500 | ±1.48% (22628-23307) | 14.3 |
| 2026-11-23 (monthly) | 33.2 | 22966 | 0.943 | 23000 | 22000 | 23000 | ±3.46% (22172-23760) | 14.08 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 9 times before; Nifty was up after it 11% of the time, average -0.40%. Too few outcomes (9/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls same · near call wall`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.71%. Too few outcomes (1/20) to trade on.
  - Writers: `put writers stronger · few weak writers`. Seen 4 times before; Nifty was up after it 75% of the time, average -0.01%. Too few outcomes (4/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `put writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at 22700, weakest put writers at 23100. Covers 73% of near-money call OI and 71% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 3684 | 1505 | 309.5 | 22786 | 397.9 | 22959 | -8 | -88.5 | weak |
| Call | 22700 | 27046 | 8855 | 263.4 | 22764 | 356.6 | 22963 | -4 | -93.2 | weak |
| Call | 22750 | 7013 | 2542 | 259.6 | 22836 | 319.2 | 23010 | +42 | -59.7 | weak |
| Call | 22800 | 35642 | 19285 | 254.0 | 22888 | 283.4 | 23054 | +87 | -29.4 | medium |
| Call | 22850 | 11943 | 9591 | 219.0 | 22909 | 249.1 | 23069 | +102 | -30.0 | medium |
| Call | 22900 | 80523 | 67975 | 186.6 | 22894 | 217.3 | 23087 | +119 | -30.7 | strong |
| Call | 22950 | 44017 | 42103 | 180.3 | 22946 | 189.3 | 23130 | +163 | -9.1 | strong |
| Call | 23000 | 211937 | 151060 | 161.9 | 22944 | 162.9 | 23162 | +194 | -1.1 | strong |
| Call | 23050 | 71411 | 69026 | 169.8 | 23026 | 138.2 | 23220 | +252 | +31.6 | strong |
| Call | 23100 | 156566 | 134955 | 153.2 | 23037 | 117.3 | 23253 | +286 | +35.8 | strong |
| Call | 23150 | 67994 | 65403 | 130.6 | 23038 | 98.1 | 23281 | +313 | +32.5 | strong |
| Call | 23200 | 156291 | 109533 | 99.6 | 22970 | 81.2 | 23300 | +332 | +18.4 | strong |
| Call | 23250 | 55032 | 51635 | 81.2 | 22995 | 67.0 | 23331 | +364 | +14.2 | strong |
| Call | 23300 | 124569 | 80786 | 74.1 | 23015 | 55.1 | 23374 | +407 | +19.0 | strong |
| Put | 22650 | 24661 | 21112 | 58.4 | 23039 | 57.2 | 22592 | +376 | +1.1 | strong |
| Put | 22700 | 117565 | 81554 | 81.5 | 23028 | 68.0 | 22618 | +349 | +13.5 | strong |
| Put | 22750 | 38988 | 37041 | 79.3 | 23035 | 80.2 | 22671 | +297 | -0.8 | strong |
| Put | 22800 | 97251 | 70437 | 106.1 | 22996 | 94.3 | 22694 | +274 | +11.8 | strong |
| Put | 22850 | 34756 | 32588 | 115.9 | 23008 | 111.0 | 22734 | +233 | +4.9 | strong |
| Put | 22900 | 108457 | 99481 | 130.5 | 23016 | 129.7 | 22770 | +198 | +0.8 | strong |
| Put | 22950 | 60274 | 59650 | 140.1 | 23022 | 150.4 | 22810 | +158 | -10.3 | strong |
| Put | 23000 | 166917 | 133163 | 155.9 | 23055 | 173.1 | 22844 | +123 | -17.2 | strong |
| Put | 23050 | 40545 | 40375 | 144.7 | 23092 | 200.5 | 22905 | +62 | -55.8 | medium |
| Put | 23100 | 67733 | 60748 | 173.1 | 23094 | 228.1 | 22927 | +41 | -55.0 | weak |
| Put | 23150 | 12246 | 11991 | 205.0 | 23083 | 258.5 | 22945 | +22 | -53.5 | weak |
| Put | 23200 | 44725 | 25831 | 231.7 | 23094 | 293.0 | 22968 | -1 | -61.3 | weak |
| Put | 23250 | 3847 | 3522 | 264.9 | 23079 | 328.1 | 22985 | -18 | -63.2 | weak |
| Put | 23300 | 33756 | 8773 | 307.4 | 23086 | 364.7 | 22993 | -25 | -57.3 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23500. Covers 6% of near-money call OI and 11% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22700 | 4070 | 8 | 616.6 | 22966 | 616.6 | 23317 | +350 | +0.0 | strong |
| Call | 22800 | 5998 | 90 | 539.3 | 22951 | 552.5 | 23339 | +373 | -13.2 | strong |
| Call | 22850 | 545 | 10 | 499.8 | 22951 | 539.8 | 23350 | +384 | -40.0 | strong |
| Call | 22900 | 3644 | 286 | 486.4 | 22964 | 488.2 | 23386 | +420 | -1.8 | strong |
| Call | 22950 | 1042 | 68 | 466.5 | 22964 | 470.0 | 23416 | +450 | -3.5 | strong |
| Call | 23000 | 57201 | 4921 | 422.8 | 22957 | 427.9 | 23423 | +457 | -5.1 | strong |
| Call | 23050 | 1665 | 32 | 389.9 | 22951 | 408.4 | 23440 | +474 | -18.5 | strong |
| Call | 23100 | 12171 | 1727 | 364.3 | 22951 | 373.8 | 23464 | +498 | -9.5 | strong |
| Call | 23150 | 1181 | 16 | 352.6 | 22966 | 352.6 | 23503 | +536 | +0.0 | strong |
| Call | 23200 | 14916 | 1387 | 338.6 | 23005 | 321.9 | 23539 | +573 | +16.7 | strong |
| Call | 23250 | 1433 | 39 | 311.2 | 22989 | 303.9 | 23561 | +595 | +7.3 | strong |
| Call | 23300 | 6636 | 47 | 275.0 | 22966 | 275.0 | 23575 | +609 | +0.0 | strong |
| Put | 22650 | 912 | 272 | 193.2 | 23093 | 229.4 | 22457 | +509 | -36.3 | strong |
| Put | 22700 | 7709 | 452 | 209.7 | 23079 | 241.2 | 22490 | +476 | -31.5 | strong |
| Put | 22750 | 865 | 267 | 220.5 | 23088 | 255.0 | 22529 | +437 | -34.5 | strong |
| Put | 22800 | 10582 | 507 | 246.1 | 23061 | 276.4 | 22554 | +412 | -30.2 | strong |
| Put | 22850 | 3090 | 18 | 243.0 | 23094 | 280.9 | 22607 | +359 | -37.9 | strong |
| Put | 22900 | 4884 | 800 | 283.7 | 23040 | 309.5 | 22616 | +350 | -25.8 | strong |
| Put | 22950 | 903 | 119 | 325.8 | 22974 | 323.9 | 22624 | +342 | +1.9 | strong |
| Put | 23000 | 50149 | 8296 | 319.0 | 23046 | 350.1 | 22681 | +285 | -31.1 | strong |
| Put | 23050 | 694 | 122 | 318.2 | 23094 | 363.6 | 22732 | +234 | -45.4 | strong |
| Put | 23100 | 8059 | 1864 | 367.9 | 23023 | 392.8 | 22732 | +234 | -24.9 | strong |
| Put | 23150 | 1525 | 155 | 355.0 | 23094 | 410.8 | 22795 | +171 | -55.8 | strong |
| Put | 23200 | 9751 | 1701 | 410.7 | 23030 | 440.3 | 22789 | +177 | -29.6 | strong |
| Put | 23250 | 465 | 44 | 401.4 | 23087 | 469.9 | 22849 | +118 | -68.5 | strong |
| Put | 23300 | 2414 | 142 | 427.1 | 23091 | 492.0 | 22873 | +93 | -64.9 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% | 0% of 1 | too few (6/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 3 | 67% | +0.02% | -0.21 to +0.17% |  | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 2 | 0% | -0.71% | -0.71 to -0.71% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 1 | 0% | -0.51% | -0.51 to -0.51% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.74% | -0.74 to -0.74% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -0.55% | -0.55 to -0.55% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -0.55% | -0.55 to -0.55% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 12 | 50% | +0.00% | no clear direction |
| intraday | monthly | writers even · few weak writers | 11 | 64% | -0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · few weak writers | 10 | 11% | -0.40% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 75% | -0.01% | too few (4/10) |
| intraday | weekly | call writers stronger · weak puts | 5 | 50% | -0.03% | too few (4/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak puts | 4 | 75% | -0.03% | too few (4/10) |
| intraday | monthly | writers even · weak puts | 3 | 0% | -0.20% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 100% | +1.00% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | put writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts | 1 | 100% | +0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
