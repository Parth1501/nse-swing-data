# Nifty option chain pattern log
Updated 2026-10-23 14:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 169 snapshots over 7 trading days
- 183 patterns logged; 97 different patterns so far

## Latest read (2026-10-23 14:44:59)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 4.0 | 22481 | 1.022 | 22700 | 22000 | 23000 | ±1.27% (22195-22766) | 15.54 |
| 2026-11-23 (monthly) | 31.0 | 22486 | 1.396 | 23000 | 22000 | 23000 | ±3.81% (21630-23341) | 15.95 |

- **Weekly, last 30 min**: `PCR up · unwinding · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 29 times before; Nifty was up after it 78% of the time, average +0.20%. History points to a bull call debit spread, ATM to about the call wall 23000.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.44%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR up · quiet OI · walls same · mid walls`. Seen 5 times before; Nifty was up after it 80% of the time, average +0.11%. Too few outcomes (5/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 13 times before; Nifty was up after it 54% of the time, average +0.06%. Too few outcomes (13/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22000; weakest call writers at -, weakest put writers at 22600. Covers 94% of near-money call OI and 91% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22150 | 606 | 489 | 490.8 | 22563 | 410.0 | 22641 | +160 | +80.8 | strong |
| Call | 22200 | 8430 | 3157 | 441.8 | 22552 | 360.0 | 22642 | +161 | +81.8 | strong |
| Call | 22250 | 2575 | 2102 | 353.6 | 22487 | 318.8 | 22604 | +123 | +34.9 | strong |
| Call | 22300 | 17058 | 12101 | 298.3 | 22473 | 280.9 | 22598 | +118 | +17.4 | strong |
| Call | 22350 | 9767 | 9468 | 257.2 | 22465 | 244.2 | 22607 | +127 | +12.9 | strong |
| Call | 22400 | 47789 | 44665 | 222.3 | 22462 | 210.1 | 22622 | +142 | +12.2 | strong |
| Call | 22450 | 37027 | 36817 | 192.7 | 22467 | 179.6 | 22643 | +162 | +13.1 | strong |
| Call | 22500 | 147555 | 139573 | 191.2 | 22511 | 151.4 | 22691 | +211 | +39.8 | strong |
| Call | 22550 | 60246 | 59928 | 171.3 | 22517 | 126.0 | 22721 | +241 | +45.3 | strong |
| Call | 22600 | 136546 | 133663 | 151.1 | 22525 | 104.5 | 22751 | +270 | +46.5 | strong |
| Call | 22650 | 65537 | 65322 | 131.0 | 22534 | 85.7 | 22781 | +300 | +45.4 | strong |
| Call | 22700 | 201938 | 194735 | 135.5 | 22595 | 69.5 | 22836 | +355 | +66.0 | strong |
| Call | 22750 | 78998 | 77324 | 139.8 | 22663 | 56.2 | 22890 | +409 | +83.6 | strong |
| Call | 22800 | 197639 | 189492 | 121.5 | 22655 | 45.2 | 22922 | +441 | +76.2 | strong |
| Put | 22150 | 38451 | 37659 | 24.1 | 22696 | 34.2 | 22126 | +355 | -10.1 | strong |
| Put | 22200 | 134716 | 121522 | 28.7 | 22742 | 42.1 | 22171 | +309 | -13.4 | strong |
| Put | 22250 | 52333 | 50534 | 39.7 | 22652 | 51.9 | 22210 | +270 | -12.2 | strong |
| Put | 22300 | 121824 | 99002 | 45.2 | 22701 | 63.5 | 22255 | +226 | -18.2 | strong |
| Put | 22350 | 68344 | 67100 | 67.7 | 22581 | 77.6 | 22282 | +198 | -9.9 | strong |
| Put | 22400 | 170109 | 159145 | 74.5 | 22624 | 93.8 | 22325 | +155 | -19.3 | strong |
| Put | 22450 | 83994 | 83606 | 92.1 | 22601 | 112.7 | 22358 | +123 | -20.6 | strong |
| Put | 22500 | 232425 | 206027 | 85.6 | 22681 | 134.4 | 22414 | +66 | -48.9 | medium |
| Put | 22550 | 53437 | 52995 | 106.0 | 22634 | 159.6 | 22444 | +37 | -53.6 | weak |
| Put | 22600 | 113733 | 105574 | 112.2 | 22716 | 186.9 | 22488 | -7 | -74.8 | weak |
| Put | 22650 | 31966 | 31519 | 126.5 | 22701 | 218.2 | 22524 | -43 | -91.8 | weak |
| Put | 22700 | 94891 | 89489 | 136.3 | 22728 | 251.9 | 22564 | -83 | -115.6 | weak |
| Put | 22750 | 28261 | 28146 | 156.3 | 22726 | 288.5 | 22594 | -113 | -132.2 | weak |
| Put | 22800 | 79794 | 73184 | 164.9 | 22774 | 326.5 | 22635 | -155 | -161.6 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at -, weakest put writers at 23000. Covers 58% of near-money call OI and 50% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22150 | 38 | 29 | 719.1 | 22497 | 707.7 | 22869 | +384 | +11.4 | strong |
| Call | 22200 | 2139 | 505 | 732.0 | 22587 | 668.3 | 22932 | +446 | +63.7 | strong |
| Call | 22250 | 139 | 51 | 696.7 | 22625 | 706.0 | 22947 | +461 | -9.2 | strong |
| Call | 22300 | 1431 | 655 | 675.7 | 22608 | 595.0 | 22976 | +490 | +80.7 | strong |
| Call | 22350 | 159 | 108 | 624.5 | 22582 | 593.2 | 22974 | +489 | +31.3 | strong |
| Call | 22400 | 2928 | 1681 | 529.9 | 22463 | 541.0 | 22930 | +444 | -11.1 | strong |
| Call | 22450 | 404 | 338 | 549.7 | 22563 | 505.3 | 23000 | +514 | +44.4 | strong |
| Call | 22500 | 25620 | 15258 | 541.5 | 22601 | 482.4 | 23042 | +556 | +59.1 | strong |
| Call | 22550 | 570 | 393 | 490.9 | 22566 | 448.0 | 23041 | +555 | +42.9 | strong |
| Call | 22600 | 27807 | 19236 | 478.5 | 22626 | 426.0 | 23078 | +593 | +52.5 | strong |
| Call | 22650 | 4344 | 4048 | 456.1 | 22603 | 391.9 | 23106 | +621 | +64.2 | strong |
| Call | 22700 | 28822 | 25132 | 450.6 | 22675 | 375.6 | 23151 | +665 | +74.9 | strong |
| Call | 22750 | 1298 | 628 | 408.9 | 22612 | 343.7 | 23159 | +673 | +65.2 | strong |
| Call | 22800 | 21341 | 16092 | 399.2 | 22678 | 323.6 | 23199 | +714 | +75.6 | strong |
| Put | 22150 | 792 | 328 | 187.8 | 22703 | 255.4 | 21962 | +523 | -67.6 | strong |
| Put | 22200 | 11437 | 3185 | 201.0 | 22705 | 267.8 | 21999 | +487 | -66.8 | strong |
| Put | 22250 | 1845 | 419 | 214.6 | 22722 | 285.6 | 22035 | +450 | -71.1 | strong |
| Put | 22300 | 17343 | 10330 | 232.8 | 22681 | 298.9 | 22067 | +418 | -66.0 | strong |
| Put | 22350 | 801 | 299 | 246.1 | 22689 | 317.9 | 22104 | +382 | -71.8 | strong |
| Put | 22400 | 17306 | 5148 | 267.6 | 22666 | 335.1 | 22132 | +353 | -67.5 | strong |
| Put | 22450 | 647 | 247 | 292.0 | 22635 | 352.6 | 22158 | +328 | -60.6 | strong |
| Put | 22500 | 50157 | 23122 | 281.6 | 22724 | 373.6 | 22218 | +267 | -91.9 | strong |
| Put | 22550 | 830 | 405 | 280.3 | 22769 | 395.0 | 22270 | +216 | -114.7 | strong |
| Put | 22600 | 27102 | 18036 | 349.7 | 22640 | 421.5 | 22250 | +235 | -71.8 | strong |
| Put | 22650 | 4675 | 4144 | 360.6 | 22630 | 440.1 | 22289 | +196 | -79.6 | strong |
| Put | 22700 | 28958 | 22326 | 353.9 | 22714 | 462.9 | 22346 | +139 | -109.1 | strong |
| Put | 22750 | 1150 | 722 | 343.4 | 22792 | 496.0 | 22407 | +79 | -152.6 | medium |
| Put | 22800 | 20425 | 11687 | 397.9 | 22713 | 516.9 | 22402 | +83 | -119.0 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 9 | 67% | +0.01% | -0.44 to +0.28% |  | too few (9/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 6 | 80% | +0.11% | -0.39 to +0.40% |  | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 5 | 80% | +0.10% | -0.37 to +0.38% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 5 | 60% | +0.02% | -0.21 to +0.17% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.12% | -0.95 to +0.62% |  | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| weekly | PCR up · put writing · walls same · near put wall | 4 | 25% | -0.28% | -0.47 to +0.06% | 0% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 4 | 50% | -0.32% | -0.95 to +0.37% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 75% | +0.02% | -0.24 to +0.15% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.20% | +0.04 to +0.36% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | +0.11% | -0.09 to +0.29% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 3 | 50% | -0.02% | -0.40 to +0.36% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 0% | -0.32% | -0.61 to -0.02% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 2 | 100% | +0.28% | +0.27 to +0.29% |  | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 50% | -0.15% | -0.30 to +0.01% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 2 | 50% | -0.03% | -0.07 to +0.01% |  | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.89% | -0.89 to -0.89% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.89% | -0.89 to -0.89% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | call writers stronger · weak puts | 30 | 78% | +0.20% | up |
| intraday | monthly | writers even · few weak writers | 29 | 59% | -0.08% | no clear direction |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | weekly | writers even · few weak writers | 15 | 21% | -0.53% | down |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | writers even · weak puts | 14 | 54% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts | 8 | 38% | -0.23% | too few (8/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.36% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| day | weekly | call writers stronger · weak puts | 3 | 0% | -0.44% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.72% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.89% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
