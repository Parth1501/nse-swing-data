# Nifty option chain pattern log
Updated 2026-10-22 09:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 126 snapshots over 6 trading days
- 135 patterns logged; 87 different patterns so far

## Latest read (2026-10-22 09:45:43)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 5.2 | 22658 | 0.944 | 22800 | 22500 | 23000 | ±1.49% (22321-22995) | 15.88 |
| 2026-11-23 (monthly) | 32.2 | 22664 | 1.331 | 23000 | 22000 | 23000 | ±3.63% (21842-23486) | 15.24 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 15 times before; Nifty was up after it 77% of the time, average +0.23%. Too few outcomes (13/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.49%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · mid walls`. Seen 3 times before; Nifty was up after it 67% of the time, average +0.02%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 15 times before; Nifty was up after it 57% of the time, average -0.05%. Too few outcomes (14/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.64%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22600; weakest call writers at -, weakest put writers at 23000. Covers 83% of near-money call OI and 79% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22350 | 2213 | 1566 | 424.1 | 22712 | 374.6 | 22774 | +116 | +49.5 | strong |
| Call | 22400 | 12473 | 4953 | 434.7 | 22762 | 338.4 | 22835 | +177 | +96.2 | strong |
| Call | 22450 | 4723 | 3861 | 322.2 | 22677 | 301.4 | 22772 | +114 | +20.8 | strong |
| Call | 22500 | 51477 | 30840 | 334.0 | 22730 | 265.8 | 22834 | +176 | +68.2 | strong |
| Call | 22550 | 18840 | 17690 | 266.3 | 22697 | 234.7 | 22816 | +158 | +31.6 | strong |
| Call | 22600 | 89037 | 77917 | 216.8 | 22670 | 203.7 | 22817 | +159 | +13.1 | strong |
| Call | 22650 | 48589 | 47157 | 186.8 | 22673 | 175.7 | 22837 | +179 | +11.1 | strong |
| Call | 22700 | 112076 | 96751 | 182.8 | 22702 | 150.8 | 22883 | +225 | +32.0 | strong |
| Call | 22750 | 49648 | 46200 | 167.5 | 22721 | 128.8 | 22918 | +259 | +38.7 | strong |
| Call | 22800 | 138081 | 122956 | 167.3 | 22761 | 108.6 | 22967 | +309 | +58.7 | strong |
| Call | 22850 | 41480 | 39689 | 158.3 | 22795 | 92.3 | 23008 | +350 | +66.0 | strong |
| Call | 22900 | 116496 | 106043 | 157.7 | 22838 | 77.0 | 23058 | +400 | +80.7 | strong |
| Call | 22950 | 58092 | 56668 | 144.3 | 22859 | 64.5 | 23094 | +436 | +79.8 | strong |
| Put | 22350 | 28684 | 25669 | 38.0 | 22892 | 63.2 | 22312 | +346 | -25.2 | strong |
| Put | 22400 | 89608 | 69953 | 54.0 | 22839 | 74.3 | 22346 | +312 | -20.4 | strong |
| Put | 22450 | 39986 | 39066 | 61.0 | 22821 | 87.2 | 22389 | +269 | -26.2 | strong |
| Put | 22500 | 158552 | 108466 | 66.1 | 22883 | 102.2 | 22434 | +224 | -36.1 | strong |
| Put | 22550 | 59542 | 57653 | 92.4 | 22783 | 119.5 | 22458 | +201 | -27.1 | strong |
| Put | 22600 | 144854 | 122637 | 104.5 | 22823 | 139.6 | 22495 | +163 | -35.1 | strong |
| Put | 22650 | 43920 | 41675 | 119.2 | 22808 | 161.4 | 22531 | +127 | -42.2 | strong |
| Put | 22700 | 102825 | 78890 | 106.3 | 22933 | 187.2 | 22594 | +64 | -80.9 | medium |
| Put | 22750 | 30301 | 29422 | 121.6 | 22914 | 213.8 | 22628 | +30 | -92.2 | weak |
| Put | 22800 | 71196 | 53964 | 117.4 | 22964 | 244.3 | 22683 | -25 | -127.0 | weak |
| Put | 22850 | 13059 | 12432 | 125.5 | 22978 | 277.4 | 22724 | -66 | -151.9 | weak |
| Put | 22900 | 54966 | 50642 | 132.1 | 23011 | 312.5 | 22768 | -110 | -180.4 | weak |
| Put | 22950 | 12935 | 12819 | 143.8 | 23011 | 349.4 | 22806 | -148 | -205.6 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at -, weakest put writers at 23100. Covers 40% of near-money call OI and 32% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22350 | 94 | 24 | 818.9 | 22884 | 642.4 | 23169 | +505 | +176.6 | strong |
| Call | 22400 | 1623 | 198 | 635.0 | 22699 | 609.0 | 23035 | +371 | +26.0 | strong |
| Call | 22450 | 208 | 129 | 612.6 | 22712 | 574.0 | 23063 | +398 | +38.6 | strong |
| Call | 22500 | 15168 | 4097 | 611.9 | 22738 | 550.0 | 23112 | +448 | +62.0 | strong |
| Call | 22550 | 497 | 249 | 545.9 | 22695 | 516.0 | 23096 | +432 | +29.9 | strong |
| Call | 22600 | 22901 | 14002 | 490.5 | 22665 | 489.9 | 23090 | +426 | +0.6 | strong |
| Call | 22650 | 524 | 198 | 480.2 | 22685 | 457.1 | 23130 | +466 | +23.1 | strong |
| Call | 22700 | 20537 | 16520 | 465.0 | 22715 | 429.9 | 23165 | +501 | +35.2 | strong |
| Call | 22750 | 1183 | 374 | 447.6 | 22711 | 404.0 | 23198 | +533 | +43.6 | strong |
| Call | 22800 | 15223 | 9576 | 409.7 | 22712 | 376.4 | 23210 | +545 | +33.3 | strong |
| Call | 22850 | 1087 | 555 | 386.3 | 22722 | 348.2 | 23236 | +572 | +38.0 | strong |
| Call | 22900 | 10312 | 6974 | 371.3 | 22732 | 327.4 | 23271 | +607 | +43.8 | strong |
| Call | 22950 | 1264 | 307 | 374.2 | 22779 | 303.7 | 23324 | +660 | +70.5 | strong |
| Call | 23000 | 73081 | 20801 | 358.9 | 22816 | 284.2 | 23359 | +695 | +74.7 | strong |
| Put | 22350 | 760 | 160 | 210.7 | 22811 | 260.0 | 22139 | +525 | -49.3 | strong |
| Put | 22400 | 13623 | 1281 | 244.2 | 22753 | 272.8 | 22156 | +508 | -28.6 | strong |
| Put | 22450 | 587 | 109 | 261.9 | 22729 | 290.4 | 22188 | +476 | -28.5 | strong |
| Put | 22500 | 39650 | 11897 | 239.2 | 22856 | 304.1 | 22261 | +404 | -64.9 | strong |
| Put | 22550 | 758 | 256 | 216.7 | 22955 | 327.2 | 22333 | +331 | -110.5 | strong |
| Put | 22600 | 22263 | 12902 | 339.3 | 22671 | 342.0 | 22261 | +404 | -2.7 | strong |
| Put | 22650 | 902 | 313 | 226.1 | 23010 | 364.9 | 22424 | +240 | -138.9 | strong |
| Put | 22700 | 23110 | 15942 | 346.0 | 22731 | 383.6 | 22354 | +310 | -37.7 | strong |
| Put | 22750 | 963 | 418 | 283.3 | 22940 | 413.4 | 22467 | +198 | -130.1 | strong |
| Put | 22800 | 17865 | 7896 | 389.0 | 22735 | 430.0 | 22411 | +253 | -41.0 | strong |
| Put | 22850 | 2696 | 57 | 370.2 | 22860 | 453.8 | 22480 | +185 | -83.6 | strong |
| Put | 22900 | 6807 | 2807 | 399.6 | 22809 | 480.0 | 22500 | +164 | -80.4 | strong |
| Put | 22950 | 593 | 86 | 334.8 | 22956 | 505.8 | 22615 | +49 | -171.0 | weak |
| Put | 23000 | 59702 | 18000 | 413.8 | 22873 | 534.8 | 22586 | +78 | -121.0 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 4 | 50% | +0.09% | -0.74 to +0.62% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 4 | 67% | +0.02% | -0.21 to +0.17% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 2 | 100% | +0.32% | +0.31 to +0.32% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
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
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.64% | -0.64 to -0.64% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · few weak writers | 16 | 57% | -0.05% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 16 | 77% | +0.23% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 10 | 44% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · few weak writers | 10 | 10% | -0.56% | down |
| intraday | monthly | writers even · weak puts | 6 | 50% | +0.14% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak puts | 4 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 100% | +0.39% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 3 | 0% | -0.49% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.64% | too few (1/10) |
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
