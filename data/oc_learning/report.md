# Nifty option chain pattern log
Updated 2026-11-02 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 306 snapshots over 13 trading days
- 334 patterns logged; 133 different patterns so far

## Latest read (2026-11-02 10:44:44)

Nifty trend: weekly **bearish**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-03 (weekly) | 1.2 | 23351 | 0.979 | 23300 | 23300 | 23500 | ±0.77% (23172-23530) | 18.33 |
| 2026-11-23 (monthly) | 21.2 | 23348 | 0.786 | 23200 | 23000 | 23500 | ±2.75% (22706-23990) | 14.32 |

- **Weekly, last 30 min**: `PCR flat · put and call writing · walls same · near put wall`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.45%. Too few outcomes (2/20) to trade on.
  - Writers: `put writers stronger · weak calls`. Seen 26 times before; Nifty was up after it 68% of the time, average +0.11%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 26 times before; Nifty was up after it 68% of the time, average +0.11%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. Seen 1 times before; Nifty was up after it 0% of the time, average -1.11%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 1 times before; Nifty was up after it 0% of the time, average -1.11%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls same · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.26%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 23 times before; Nifty was up after it 86% of the time, average +0.04%. History points to a bull call debit spread, ATM to about the call wall 23500.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 23 times before; Nifty was up after it 86% of the time, average +0.04%. History points to a bull call debit spread, ATM to about the call wall 23500.
- **Monthly, today vs previous day**: `PCR down · put writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 2 times before; Nifty was up after it 50% of the time, average -0.23%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 2 times before; Nifty was up after it 50% of the time, average -0.23%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-11-03

Strongest call writers at 23600, strongest put writers at 23300; weakest call writers at 23300, weakest put writers at 23650. Covers 88% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 23050 | 22551 | 21423 | 94.5 | 22964 | 303.5 | 23144 | -206 | -209.0 | weak |
| Call | 23100 | 48702 | 42772 | 75.8 | 22954 | 259.4 | 23176 | -175 | -183.6 | weak |
| Call | 23150 | 38430 | 35725 | 58.7 | 22948 | 217.4 | 23209 | -142 | -158.8 | weak |
| Call | 23200 | 115475 | 93094 | 48.2 | 22926 | 177.8 | 23248 | -103 | -129.6 | weak |
| Call | 23250 | 114074 | 110169 | 97.8 | 23165 | 141.4 | 23348 | -3 | -43.6 | weak |
| Call | 23300 | 282978 | 260672 | 80.3 | 23195 | 109.3 | 23380 | +29 | -29.0 | weak |
| Call | 23350 | 194401 | 190595 | 62.6 | 23214 | 82.0 | 23413 | +62 | -19.4 | medium |
| Call | 23400 | 243006 | 209977 | 32.5 | 23088 | 58.8 | 23433 | +82 | -26.2 | medium |
| Call | 23450 | 119112 | 114220 | 24.4 | 23117 | 40.5 | 23474 | +123 | -16.1 | strong |
| Call | 23500 | 263862 | 183467 | 14.1 | 23038 | 27.0 | 23514 | +163 | -12.9 | strong |
| Call | 23550 | 107179 | 102488 | 11.7 | 23160 | 17.2 | 23562 | +211 | -5.5 | strong |
| Call | 23600 | 214937 | 198047 | 9.1 | 23193 | 10.7 | 23609 | +258 | -1.6 | strong |
| Call | 23650 | 98879 | 94641 | 6.3 | 23200 | 7.0 | 23656 | +305 | -0.6 | strong |
| Call | 23700 | 132601 | 116100 | 4.2 | 23031 | 4.8 | 23704 | +353 | -0.6 | strong |
| Put | 23050 | 109539 | 109334 | 85.5 | 23172 | 19.8 | 22965 | +386 | +65.7 | strong |
| Put | 23100 | 176769 | 175732 | 63.8 | 23251 | 25.5 | 23036 | +315 | +38.3 | strong |
| Put | 23150 | 98797 | 98664 | 54.1 | 23290 | 33.1 | 23096 | +255 | +20.9 | strong |
| Put | 23200 | 290266 | 289198 | 61.9 | 23299 | 43.6 | 23138 | +213 | +18.3 | strong |
| Put | 23250 | 238260 | 237955 | 72.1 | 23306 | 57.2 | 23178 | +173 | +14.8 | strong |
| Put | 23300 | 348375 | 347518 | 90.5 | 23311 | 74.9 | 23209 | +142 | +15.6 | strong |
| Put | 23350 | 99456 | 99399 | 112.6 | 23316 | 97.4 | 23237 | +114 | +15.2 | strong |
| Put | 23400 | 73359 | 72329 | 148.7 | 23307 | 124.3 | 23251 | +100 | +24.3 | medium |
| Put | 23450 | 15669 | 15641 | 208.4 | 23276 | 156.3 | 23242 | +109 | +52.1 | strong |
| Put | 23500 | 29519 | 24186 | 246.3 | 23278 | 193.3 | 23254 | +97 | +52.9 | medium |
| Put | 23550 | 3942 | 3930 | 268.3 | 23299 | 233.4 | 23282 | +69 | +34.8 | medium |
| Put | 23600 | 6446 | 5505 | 318.8 | 23290 | 276.8 | 23281 | +70 | +42.0 | medium |
| Put | 23650 | 859 | 799 | 350.1 | 23309 | 325.1 | 23300 | +51 | +25.0 | weak |
| Put | 23700 | 1749 | 1418 | 475.5 | 23231 | 370.1 | 23225 | +126 | +105.4 | strong |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 23000, weakest put writers at -. Covers 69% of near-money call OI and 77% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 23000 | 84621 | 53200 | 293.6 | 22669 | 583.8 | 23294 | -54 | -290.2 | weak |
| Call | 23050 | 2566 | 1761 | 317.1 | 22889 | 543.5 | 23367 | +20 | -226.5 | weak |
| Call | 23100 | 16522 | 10536 | 302.6 | 22863 | 509.2 | 23403 | +55 | -206.6 | medium |
| Call | 23150 | 2068 | 1490 | 272.4 | 22893 | 475.4 | 23422 | +75 | -203.1 | medium |
| Call | 23200 | 21223 | 11435 | 237.4 | 22761 | 443.9 | 23437 | +90 | -206.5 | medium |
| Call | 23250 | 2572 | 1670 | 239.0 | 22891 | 407.0 | 23489 | +141 | -168.0 | strong |
| Call | 23300 | 25052 | 19932 | 211.1 | 22756 | 379.5 | 23511 | +164 | -168.4 | strong |
| Call | 23350 | 3066 | 2521 | 215.5 | 22962 | 349.0 | 23565 | +218 | -133.5 | strong |
| Call | 23400 | 15929 | 10803 | 183.8 | 22828 | 321.4 | 23584 | +236 | -137.6 | strong |
| Call | 23450 | 1798 | 1368 | 171.9 | 22837 | 293.2 | 23622 | +274 | -121.3 | strong |
| Call | 23500 | 100345 | 69073 | 120.7 | 22643 | 267.6 | 23621 | +273 | -146.9 | strong |
| Call | 23550 | 1843 | 924 | 131.4 | 22825 | 241.0 | 23681 | +334 | -109.6 | strong |
| Call | 23600 | 14106 | 8372 | 120.5 | 22796 | 219.2 | 23720 | +373 | -98.8 | strong |
| Call | 23650 | 1288 | 1072 | 108.1 | 22848 | 193.2 | 23758 | +411 | -85.1 | strong |
| Put | 23000 | 99220 | 66511 | 439.3 | 22805 | 177.7 | 22561 | +787 | +261.6 | strong |
| Put | 23050 | 1827 | 1542 | 363.9 | 22951 | 195.0 | 22686 | +661 | +168.9 | strong |
| Put | 23100 | 16297 | 11695 | 365.2 | 23016 | 204.0 | 22735 | +613 | +161.2 | strong |
| Put | 23150 | 1876 | 1055 | 379.3 | 23017 | 219.3 | 22771 | +577 | +159.9 | strong |
| Put | 23200 | 21863 | 15775 | 439.2 | 22979 | 236.0 | 22761 | +587 | +203.2 | strong |
| Put | 23250 | 1552 | 1307 | 367.1 | 23129 | 253.5 | 22883 | +465 | +113.6 | strong |
| Put | 23300 | 19633 | 17663 | 540.5 | 22901 | 271.7 | 22759 | +588 | +268.8 | strong |
| Put | 23350 | 1006 | 934 | 429.4 | 23103 | 293.1 | 22921 | +427 | +136.4 | strong |
| Put | 23400 | 7719 | 6152 | 510.3 | 23025 | 312.9 | 22890 | +458 | +197.4 | strong |
| Put | 23450 | 546 | 492 | 567.1 | 22951 | 339.1 | 22883 | +465 | +228.0 | strong |
| Put | 23500 | 65794 | 53103 | 835.6 | 22662 | 360.0 | 22664 | +683 | +475.6 | strong |
| Put | 23550 | 298 | 220 | 717.6 | 22846 | 385.2 | 22832 | +515 | +332.4 | strong |
| Put | 23600 | 2689 | 1867 | 776.0 | 22834 | 411.4 | 22824 | +524 | +364.5 | strong |
| Put | 23650 | 382 | 312 | 874.2 | 22752 | 439.2 | 22776 | +572 | +435.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 30 | 69% | +0.19% | -0.44 to +0.76% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 10 | 100% | +0.31% | +0.03 to +0.62% | 50% of 2 | up |
| weekly | PCR up · put writing · walls same · near put wall | 10 | 60% | +0.02% | -0.47 to +0.41% | 50% of 2 | no clear direction |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| weekly | PCR down · call writing · walls same · near put wall | 7 | 86% | +0.33% | -0.37 to +0.85% | 50% of 2 | too few (7/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 7 | 80% | +0.21% | -0.12 to +0.71% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 7 | 100% | +0.41% | +0.09 to +1.02% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · quiet OI · walls same · near put wall | 6 | 80% | +0.04% | -0.18 to +0.19% |  | too few (5/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| weekly | PCR up · put writing · walls up · near put wall | 5 | 60% | +0.15% | -0.13 to +0.35% | 0% of 1 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 5 | 40% | +0.04% | -0.78 to +0.90% | 100% of 1 | too few (5/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 5 | 60% | +0.12% | -0.07 to +0.32% | 50% of 2 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 4 | 67% | +0.06% | -0.05 to +0.15% | 50% of 2 | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% | 100% of 1 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.07% | -0.05 to +0.21% | 100% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls same · mid walls | 4 | 100% | +0.39% | +0.04 to +0.73% | 50% of 2 | too few (4/10) |
| weekly | PCR down · call writing · walls down · mid walls | 4 | 75% | +0.28% | -0.07 to +0.54% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 100% | +0.57% | +0.24 to +0.85% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · near call wall | 3 | 67% | +0.35% | -0.02 to +0.55% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 3 | 33% | -0.12% | -0.68 to +0.34% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 3 | 67% | +0.16% | -0.02 to +0.37% | 100% of 1 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 3 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 3 | 67% | +0.16% | -0.11 to +0.50% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 2 | 0% | -0.01% | -0.02 to -0.01% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 2 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 2 | 100% | +0.26% | +0.17 to +0.35% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 2 | 100% | +0.19% | +0.13 to +0.26% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% |  | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 50% | +0.10% | -0.16 to +0.36% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 0% | -0.44% | -0.69 to -0.20% |  | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 2 | 100% | +0.78% | +0.70 to +0.85% |  | too few (2/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 100% | +0.19% | +0.19 to +0.19% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% | 100% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.29% | +1.29 to +1.29% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +1.29% | +1.29 to +1.29% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 94 | 70% | +0.17% | up |
| intraday | weekly | writers even · few weak writers | 40 | 47% | -0.04% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | weekly | put writers stronger · weak calls | 27 | 68% | +0.11% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 25 | 91% | +0.15% | up |
| intraday | monthly | writers even · weak calls | 24 | 86% | +0.04% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | weekly | call writers stronger · few weak writers | 15 | 64% | +0.18% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 5 | 40% | +0.01% | too few (5/10) |
| intraday | weekly | writers even · weak on both sides | 5 | 100% | +0.25% | too few (5/10) |
| intraday | weekly | writers even · weak calls | 4 | 33% | -0.06% | too few (3/10) |
| day | monthly | writers even · few weak writers | 8 | 50% | +0.29% | too few (8/10) |
| day | monthly | writers even · weak calls | 3 | 50% | -0.23% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.82% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | put writers stronger · weak calls | 2 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 2 | 50% | +0.33% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.02% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 27 | 68% | +0.11% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 25 | 91% | +0.15% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 24 | 86% | +0.04% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 16 | 60% | +0.09% | no clear direction |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 12 | 73% | +0.32% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 5 | 40% | +0.01% | too few (5/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
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
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.66% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 3 | 50% | -0.23% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.82% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 0% | -1.11% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.05% | too few (1/10) |
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
