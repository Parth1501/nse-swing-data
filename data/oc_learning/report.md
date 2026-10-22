# Nifty option chain pattern log
Updated 2026-10-22 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 137 snapshots over 6 trading days
- 147 patterns logged; 91 different patterns so far

## Latest read (2026-10-22 12:44:54)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 5.1 | 22626 | 0.953 | 22800 | 22600 | 23000 | ±1.36% (22318-22934) | 14.59 |
| 2026-11-23 (monthly) | 32.1 | 22628 | 1.349 | 23000 | 22000 | 23000 | ±3.62% (21808-23447) | 15.05 |

- **Weekly, last 30 min**: `PCR down · call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 19 times before; Nifty was up after it 65% of the time, average +0.14%. Too few outcomes (17/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.58%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR down · quiet OI · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 20 times before; Nifty was up after it 42% of the time, average -0.12%. Too few outcomes (19/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.81%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22600; weakest call writers at -, weakest put writers at 22700. Covers 85% of near-money call OI and 81% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 13654 | 3585 | 429.1 | 22659 | 391.6 | 22729 | +103 | +37.5 | strong |
| Call | 22350 | 2802 | 2212 | 407.8 | 22692 | 349.6 | 22758 | +132 | +58.2 | strong |
| Call | 22400 | 11708 | 5208 | 415.6 | 22741 | 313.8 | 22816 | +190 | +101.9 | strong |
| Call | 22450 | 4622 | 3929 | 311.6 | 22663 | 275.9 | 22762 | +136 | +35.7 | strong |
| Call | 22500 | 50830 | 33926 | 310.1 | 22701 | 240.9 | 22810 | +184 | +69.1 | strong |
| Call | 22550 | 18714 | 17883 | 255.1 | 22682 | 208.8 | 22805 | +179 | +46.3 | strong |
| Call | 22600 | 87730 | 80317 | 203.2 | 22651 | 179.0 | 22803 | +177 | +24.2 | strong |
| Call | 22650 | 54737 | 53945 | 168.9 | 22644 | 153.1 | 22819 | +193 | +15.9 | strong |
| Call | 22700 | 126720 | 113281 | 169.2 | 22680 | 128.8 | 22869 | +243 | +40.4 | strong |
| Call | 22750 | 56554 | 53500 | 162.4 | 22716 | 108.3 | 22912 | +286 | +54.1 | strong |
| Call | 22800 | 143166 | 128894 | 160.6 | 22748 | 90.5 | 22961 | +335 | +70.2 | strong |
| Call | 22850 | 44519 | 42779 | 151.5 | 22781 | 74.8 | 23001 | +375 | +76.6 | strong |
| Call | 22900 | 111143 | 101890 | 152.9 | 22830 | 62.0 | 23053 | +427 | +90.9 | strong |
| Call | 22950 | 67125 | 65745 | 129.2 | 22820 | 51.0 | 23079 | +453 | +78.2 | strong |
| Put | 22300 | 92535 | 58541 | 28.6 | 22915 | 45.0 | 22271 | +355 | -16.4 | strong |
| Put | 22350 | 39626 | 37559 | 44.8 | 22762 | 54.1 | 22305 | +321 | -9.3 | strong |
| Put | 22400 | 79055 | 63468 | 52.8 | 22829 | 65.2 | 22347 | +279 | -12.4 | strong |
| Put | 22450 | 38082 | 37314 | 63.0 | 22801 | 78.3 | 22387 | +239 | -15.3 | strong |
| Put | 22500 | 166265 | 119642 | 68.9 | 22850 | 93.5 | 22431 | +195 | -24.6 | strong |
| Put | 22550 | 58855 | 57129 | 93.4 | 22773 | 111.0 | 22457 | +169 | -17.6 | strong |
| Put | 22600 | 173276 | 151242 | 107.3 | 22794 | 131.2 | 22493 | +133 | -23.9 | strong |
| Put | 22650 | 58083 | 55872 | 125.8 | 22770 | 154.8 | 22524 | +102 | -29.1 | medium |
| Put | 22700 | 121530 | 102368 | 121.4 | 22846 | 180.6 | 22579 | +47 | -59.2 | weak |
| Put | 22750 | 35270 | 34745 | 140.0 | 22820 | 210.2 | 22610 | +16 | -70.2 | weak |
| Put | 22800 | 70969 | 57170 | 133.5 | 22907 | 240.8 | 22666 | -40 | -107.3 | weak |
| Put | 22850 | 13919 | 13384 | 147.3 | 22920 | 276.6 | 22703 | -77 | -129.3 | weak |
| Put | 22900 | 53021 | 49042 | 138.4 | 22995 | 313.1 | 22762 | -136 | -174.6 | weak |
| Put | 22950 | 11555 | 11454 | 147.1 | 23004 | 352.4 | 22803 | -177 | -205.3 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at -, weakest put writers at 23200. Covers 44% of near-money call OI and 38% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 1199 | 390 | 726.4 | 22703 | 661.1 | 23026 | +399 | +65.2 | strong |
| Call | 22350 | 102 | 32 | 780.2 | 22833 | 636.5 | 23130 | +503 | +143.8 | strong |
| Call | 22400 | 1645 | 244 | 626.9 | 22684 | 607.5 | 23027 | +399 | +19.3 | strong |
| Call | 22450 | 230 | 152 | 607.8 | 22703 | 567.0 | 23058 | +430 | +40.8 | strong |
| Call | 22500 | 18049 | 6991 | 588.1 | 22706 | 533.7 | 23088 | +460 | +54.4 | strong |
| Call | 22550 | 479 | 253 | 541.4 | 22686 | 502.0 | 23091 | +464 | +39.4 | strong |
| Call | 22600 | 23688 | 14966 | 490.2 | 22664 | 475.5 | 23090 | +463 | +14.7 | strong |
| Call | 22650 | 2055 | 1735 | 461.3 | 22671 | 448.0 | 23111 | +484 | +13.3 | strong |
| Call | 22700 | 24009 | 20002 | 461.0 | 22709 | 416.9 | 23161 | +533 | +44.1 | strong |
| Call | 22750 | 1090 | 364 | 443.2 | 22704 | 390.3 | 23193 | +566 | +52.9 | strong |
| Call | 22800 | 17060 | 11425 | 407.3 | 22708 | 367.1 | 23207 | +580 | +40.2 | strong |
| Call | 22850 | 1285 | 757 | 378.7 | 22710 | 336.0 | 23229 | +601 | +42.7 | strong |
| Call | 22900 | 11004 | 7668 | 369.4 | 22730 | 316.9 | 23269 | +642 | +52.5 | strong |
| Call | 22950 | 1354 | 407 | 358.7 | 22752 | 294.1 | 23309 | +681 | +64.6 | strong |
| Put | 22300 | 13272 | 5959 | 224.0 | 22720 | 250.7 | 22076 | +552 | -26.7 | strong |
| Put | 22350 | 779 | 188 | 212.0 | 22803 | 265.9 | 22138 | +490 | -53.9 | strong |
| Put | 22400 | 15596 | 3254 | 237.8 | 22763 | 281.4 | 22162 | +465 | -43.6 | strong |
| Put | 22450 | 596 | 126 | 262.5 | 22732 | 300.6 | 22187 | +440 | -38.1 | strong |
| Put | 22500 | 41546 | 14157 | 246.3 | 22831 | 314.5 | 22254 | +374 | -68.2 | strong |
| Put | 22550 | 765 | 269 | 222.3 | 22938 | 331.9 | 22328 | +300 | -109.6 | strong |
| Put | 22600 | 24191 | 14893 | 338.8 | 22670 | 354.0 | 22261 | +366 | -15.2 | strong |
| Put | 22650 | 2374 | 1795 | 333.6 | 22731 | 371.6 | 22316 | +311 | -38.0 | strong |
| Put | 22700 | 25777 | 18741 | 347.9 | 22727 | 395.6 | 22352 | +275 | -47.7 | strong |
| Put | 22750 | 1079 | 577 | 309.6 | 22873 | 419.3 | 22440 | +187 | -109.7 | strong |
| Put | 22800 | 19646 | 9759 | 391.6 | 22728 | 439.9 | 22408 | +219 | -48.3 | strong |
| Put | 22850 | 2262 | 128 | 394.8 | 22776 | 459.8 | 22455 | +172 | -65.0 | strong |
| Put | 22900 | 7193 | 3205 | 405.8 | 22796 | 493.1 | 22494 | +133 | -87.4 | strong |
| Put | 22950 | 623 | 137 | 382.7 | 22867 | 519.6 | 22567 | +60 | -136.9 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 4 | 50% | +0.01% | -0.41 to +0.32% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | -0.03% | -0.21 to +0.17% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 4 | 50% | +0.09% | -0.74 to +0.62% |  | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 3 | 67% | +0.05% | -0.15 to +0.22% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · mid walls | 2 | 100% | +0.06% | +0.04 to +0.08% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 50% | -0.04% | -0.19 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.37% | -0.67 to -0.07% |  | too few (2/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 2 | 50% | -0.16% | -0.39 to +0.08% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.67% | -0.67 to -0.67% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.81% | -0.81 to -0.81% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 21 | 42% | -0.12% | no clear direction |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | call writers stronger · weak puts | 20 | 65% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 10 | 44% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · few weak writers | 10 | 10% | -0.56% | down |
| intraday | monthly | writers even · weak puts | 7 | 57% | +0.11% | too few (7/10) |
| intraday | weekly | writers even · weak puts | 6 | 33% | -0.27% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 100% | +0.39% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 3 | 0% | -0.58% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.81% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
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
