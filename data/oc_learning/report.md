# Nifty option chain pattern log
Updated 2026-11-26 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 697 snapshots over 29 trading days
- 774 patterns logged; 193 different patterns so far

## Latest read (2026-11-26 09:44:52)

Nifty trend: weekly **sideways**, 125-min **up**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-12-01 (weekly) | 5.2 | 25741 | 0.884 | 25800 | 25500 | 26000 | ±1.62% (25324-26158) | 17.39 |
| 2026-12-29 (monthly) | 33.2 | 25747 | 1.073 | 25500 | 25000 | 27000 | ±3.58% (24825-26669) | 14.96 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · mid walls`. Seen 10 times before; Nifty was up after it 40% of the time, average +0.03%. Too few outcomes (10/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 126 times before; Nifty was up after it 58% of the time, average +0.08%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 51 times before; Nifty was up after it 52% of the time, average -0.02%. No direction and the walls have not held reliably: no structure.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.55%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 8 times before; Nifty was up after it 62% of the time, average +0.53%. Too few outcomes (8/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Nifty was up after it 33% of the time, average -0.17%. Too few outcomes (3/20) to trade on.
- **Monthly, last 30 min**: `PCR up · put and call writing · walls same · mid walls`. Seen 11 times before; Nifty was up after it 73% of the time, average +0.15%. Too few outcomes (11/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 173 times before; Nifty was up after it 66% of the time, average +0.17%. History points to a bull call debit spread, ATM to about the call wall 27000.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 56 times before; Nifty was up after it 65% of the time, average +0.14%. History points to a bull call debit spread, ATM to about the call wall 27000.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. Seen 2 times before; Nifty was up after it 50% of the time, average +0.02%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 14 times before; Nifty was up after it 50% of the time, average +0.19%. Too few outcomes (14/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 5 times before; Nifty was up after it 40% of the time, average -0.23%. Too few outcomes (5/20) to trade on.

## Strong vs weak writers, weekly 2026-12-01

Strongest call writers at 25800, strongest put writers at 25800; weakest call writers at 25000, weakest put writers at 26000. Covers 56% of near-money call OI and 75% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25400 | 31059 | 663 | 411.4 | 25696 | 423.9 | 25811 | +70 | -12.4 | medium |
| Call | 25450 | 4118 | 115 | 409.4 | 25744 | 386.4 | 25859 | +118 | +22.9 | strong |
| Call | 25500 | 41005 | 1540 | 370.8 | 25762 | 352.1 | 25871 | +130 | +18.7 | strong |
| Call | 25550 | 5347 | 1607 | 304.6 | 25655 | 318.9 | 25855 | +114 | -14.3 | medium |
| Call | 25600 | 21439 | 4490 | 295.6 | 25701 | 288.2 | 25896 | +155 | +7.4 | strong |
| Call | 25650 | 9277 | 5799 | 267.5 | 25704 | 259.1 | 25918 | +176 | +8.4 | strong |
| Call | 25700 | 39793 | 25393 | 256.8 | 25716 | 231.4 | 25957 | +216 | +25.4 | strong |
| Call | 25750 | 30553 | 28078 | 232.8 | 25734 | 205.7 | 25983 | +242 | +27.1 | strong |
| Call | 25800 | 128549 | 96034 | 197.1 | 25736 | 181.7 | 25997 | +256 | +15.4 | strong |
| Call | 25850 | 56495 | 51000 | 182.0 | 25757 | 160.2 | 26032 | +291 | +21.8 | strong |
| Call | 25900 | 100175 | 74658 | 173.3 | 25770 | 140.1 | 26073 | +332 | +33.2 | strong |
| Call | 25950 | 39285 | 32811 | 176.8 | 25804 | 122.2 | 26127 | +386 | +54.5 | strong |
| Call | 26000 | 163341 | 74836 | 130.8 | 25749 | 106.1 | 26131 | +390 | +24.7 | strong |
| Call | 26050 | 24362 | 19909 | 133.2 | 25788 | 91.5 | 26183 | +442 | +41.7 | strong |
| Call | 26100 | 52236 | 29344 | 107.0 | 25768 | 78.7 | 26207 | +466 | +28.3 | strong |
| Put | 25400 | 76316 | 56091 | 84.2 | 25762 | 81.6 | 25316 | +425 | +2.6 | strong |
| Put | 25450 | 27107 | 23020 | 86.9 | 25809 | 95.1 | 25363 | +378 | -8.2 | strong |
| Put | 25500 | 111090 | 70984 | 104.5 | 25791 | 109.8 | 25395 | +346 | -5.3 | strong |
| Put | 25550 | 18418 | 15954 | 127.2 | 25758 | 126.6 | 25423 | +318 | +0.7 | strong |
| Put | 25600 | 61296 | 45849 | 134.2 | 25799 | 145.0 | 25466 | +275 | -10.8 | strong |
| Put | 25650 | 28208 | 26743 | 173.8 | 25739 | 164.9 | 25476 | +265 | +8.9 | strong |
| Put | 25700 | 80561 | 69996 | 184.5 | 25763 | 187.2 | 25515 | +226 | -2.6 | strong |
| Put | 25750 | 48385 | 47265 | 208.6 | 25752 | 211.6 | 25541 | +200 | -3.0 | strong |
| Put | 25800 | 111701 | 99281 | 225.5 | 25771 | 238.1 | 25575 | +167 | -12.6 | strong |
| Put | 25850 | 32016 | 31567 | 243.6 | 25786 | 265.8 | 25606 | +135 | -22.2 | strong |
| Put | 25900 | 55704 | 53062 | 263.5 | 25804 | 296.4 | 25636 | +105 | -32.9 | medium |
| Put | 25950 | 8732 | 8488 | 253.2 | 25872 | 328.4 | 25697 | +44 | -75.2 | weak |
| Put | 26000 | 45107 | 30127 | 300.4 | 25839 | 361.6 | 25700 | +41 | -61.2 | weak |
| Put | 26050 | 2545 | 2398 | 305.9 | 25874 | 397.4 | 25744 | -3 | -91.5 | weak |
| Put | 26100 | 5816 | 4621 | 350.4 | 25854 | 435.4 | 25750 | -9 | -85.0 | weak |

## Strong vs weak writers, monthly 2026-12-29

Strongest call writers at 26000, strongest put writers at 25500; weakest call writers at 25250, weakest put writers at -. Covers 54% of near-money call OI and 55% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 25400 | 7071 | 4818 | 521.6 | 25369 | 729.4 | 25922 | +175 | -207.8 | strong |
| Call | 25450 | 974 | 629 | 485.3 | 25354 | 685.0 | 25935 | +188 | -199.7 | strong |
| Call | 25500 | 60743 | 29895 | 513.6 | 25443 | 666.8 | 26014 | +267 | -153.2 | strong |
| Call | 25550 | 867 | 654 | 462.2 | 25400 | 665.0 | 26012 | +265 | -202.8 | strong |
| Call | 25600 | 15449 | 12690 | 493.9 | 25513 | 599.1 | 26094 | +347 | -105.2 | strong |
| Call | 25650 | 829 | 555 | 466.0 | 25502 | 561.2 | 26116 | +369 | -95.2 | strong |
| Call | 25700 | 15246 | 13001 | 488.2 | 25599 | 545.1 | 26188 | +441 | -56.9 | strong |
| Call | 25750 | 1659 | 1494 | 484.6 | 25636 | 509.2 | 26235 | +488 | -24.7 | strong |
| Call | 25800 | 25745 | 23266 | 402.7 | 25526 | 489.8 | 26203 | +456 | -87.1 | strong |
| Call | 25850 | 1199 | 1087 | 449.9 | 25676 | 463.6 | 26300 | +553 | -13.7 | strong |
| Call | 25900 | 11871 | 10689 | 442.0 | 25703 | 439.6 | 26342 | +595 | +2.4 | strong |
| Call | 25950 | 1695 | 1577 | 452.0 | 25764 | 413.2 | 26402 | +655 | +38.8 | strong |
| Call | 26000 | 93692 | 37599 | 324.5 | 25539 | 390.1 | 26324 | +578 | -65.7 | strong |
| Call | 26050 | 732 | 572 | 337.8 | 25621 | 369.2 | 26388 | +641 | -31.5 | strong |
| Call | 26100 | 8016 | 6165 | 291.9 | 25543 | 346.4 | 26392 | +645 | -54.5 | strong |
| Put | 25400 | 18054 | 10708 | 416.1 | 25351 | 282.0 | 24984 | +763 | +134.1 | strong |
| Put | 25450 | 1229 | 946 | 410.4 | 25426 | 301.4 | 25040 | +707 | +109.0 | strong |
| Put | 25500 | 96274 | 49223 | 413.3 | 25483 | 314.6 | 25087 | +660 | +98.7 | strong |
| Put | 25550 | 888 | 717 | 443.1 | 25467 | 335.0 | 25107 | +640 | +108.1 | strong |
| Put | 25600 | 20027 | 16964 | 436.8 | 25557 | 351.2 | 25163 | +584 | +85.5 | strong |
| Put | 25650 | 899 | 843 | 433.4 | 25603 | 375.7 | 25217 | +530 | +57.7 | strong |
| Put | 25700 | 15145 | 14532 | 433.4 | 25651 | 391.9 | 25267 | +480 | +41.5 | strong |
| Put | 25750 | 5353 | 5214 | 415.2 | 25739 | 412.8 | 25335 | +412 | +2.5 | strong |
| Put | 25800 | 18572 | 17879 | 469.2 | 25683 | 436.5 | 25331 | +416 | +32.7 | strong |
| Put | 25850 | 970 | 943 | 461.0 | 25731 | 459.0 | 25389 | +358 | +2.0 | strong |
| Put | 25900 | 9577 | 9310 | 471.6 | 25770 | 482.8 | 25428 | +318 | -11.2 | strong |
| Put | 25950 | 512 | 473 | 477.1 | 25798 | 512.2 | 25473 | +274 | -35.1 | strong |
| Put | 26000 | 72592 | 23619 | 548.0 | 25703 | 533.8 | 25452 | +295 | +14.2 | strong |
| Put | 26050 | 323 | 249 | 556.0 | 25745 | 574.0 | 25494 | +253 | -18.0 | strong |
| Put | 26100 | 4197 | 3843 | 647.2 | 25619 | 594.6 | 25453 | +294 | +52.6 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 43 | 68% | +0.25% | -0.44 to +0.97% | 50% of 2 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 22 | 86% | +0.39% | -0.50 to +1.68% | 0% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 22 | 82% | +0.25% | -0.36 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 20 | 79% | +0.33% | -0.49 to +1.02% | 50% of 2 | up |
| weekly | PCR down · call writing · walls same · near put wall | 20 | 60% | +0.13% | -1.00 to +0.85% | 60% of 5 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 18 | 56% | +0.06% | -0.61 to +0.80% | 60% of 5 | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near put wall | 16 | 79% | +0.12% | -0.28 to +0.90% | 0% of 1 | up |
| monthly | PCR flat · put and call writing · walls same · near call wall | 16 | 56% | +0.28% | -0.71 to +1.70% | 50% of 2 | no clear direction |
| monthly | PCR flat · put writing · walls same · near call wall | 13 | 73% | +0.36% | -0.50 to +1.56% | 0% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · mid walls | 13 | 62% | +0.16% | -0.57 to +0.89% | 75% of 4 | no clear direction |
| weekly | PCR down · unwinding · walls same · mid walls | 13 | 67% | +0.06% | -0.40 to +0.90% | 80% of 5 | too few (9/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 12 | 73% | +0.15% | -0.24 to +0.63% | 50% of 2 | no clear direction |
| weekly | PCR down · unwinding · walls same · near call wall | 12 | 73% | +0.37% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| monthly | PCR up · put writing · walls same · near call wall | 11 | 50% | +0.18% | -0.40 to +0.93% | 50% of 2 | no clear direction |
| monthly | PCR up · quiet OI · walls same · mid walls | 11 | 82% | +0.23% | -0.39 to +0.91% | 50% of 2 | up |
| weekly | PCR down · call writing · walls same · mid walls | 11 | 82% | +0.21% | -0.43 to +0.75% | 40% of 5 | up |
| weekly | PCR up · put and call writing · walls same · mid walls | 11 | 40% | +0.03% | -0.78 to +0.90% | 100% of 2 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · mid walls | 10 | 57% | +0.11% | -0.16 to +0.71% | 50% of 2 | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 10 | 80% | +0.28% | -0.21 to +1.13% | 50% of 2 | no clear direction |
| monthly | PCR flat · put writing · walls same · near put wall | 10 | 75% | +0.13% | -0.83 to +0.98% | 0% of 1 | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 10 | 60% | +0.01% | -1.01 to +1.12% | 100% of 1 | no clear direction |
| monthly | PCR down · quiet OI · walls same · mid walls | 10 | 88% | +0.31% | -0.07 to +0.70% | 0% of 1 | too few (8/10) |
| monthly | PCR down · call writing · walls same · mid walls | 9 | 44% | +0.02% | -0.47 to +0.49% | 50% of 2 | too few (9/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 9 | 78% | +0.31% | -1.22 to +1.24% | 67% of 3 | too few (9/10) |
| weekly | PCR down · call writing · walls down · mid walls | 9 | 78% | +0.24% | -0.07 to +0.54% | 67% of 3 | too few (9/10) |
| monthly | PCR up · put writing · walls same · mid walls | 8 | 75% | +0.42% | -0.29 to +0.85% | 50% of 2 | too few (8/10) |
| weekly | PCR up · put writing · walls up · mid walls | 8 | 62% | +0.31% | -0.26 to +1.40% | 33% of 3 | too few (8/10) |
| weekly | PCR up · put writing · walls up · near put wall | 8 | 62% | +0.33% | -0.13 to +1.65% | 0% of 4 | too few (8/10) |
| monthly | PCR down · call writing · walls same · near call wall | 8 | 83% | +0.27% | -0.78 to +1.18% | 50% of 2 | too few (6/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% | 0% of 1 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 7 | 86% | +0.50% | -0.37 to +1.25% | 50% of 2 | too few (7/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 7 | 43% | -0.05% | -0.89 to +0.90% | 67% of 3 | too few (7/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.02% | -0.74 to +0.62% | 50% of 2 | too few (7/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 7 | 86% | +0.29% | -0.11 to +0.62% | 50% of 4 | too few (7/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 7 | 71% | +0.53% | -1.02 to +1.82% | 50% of 4 | too few (7/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 7 | 83% | +0.23% | -0.05 to +0.63% | 67% of 3 | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 50% of 2 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near call wall | 6 | 83% | +0.50% | -0.02 to +0.91% | 33% of 3 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 6 | 67% | -0.08% | -1.07 to +0.28% | 100% of 1 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 6 | 20% | +0.00% | -0.29 to +0.43% | 33% of 3 | too few (5/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 6 | 100% | +0.54% | +0.47 to +0.61% | 67% of 3 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near call wall | 6 | 83% | +0.53% | -0.06 to +1.68% | 67% of 3 | too few (6/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 5 | 80% | +0.26% | -0.02 to +0.90% | 33% of 3 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 5 | 80% | +0.46% | -1.11 to +1.69% | 0% of 2 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 50% of 2 | too few (5/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 5 | 40% | +0.06% | -0.68 to +0.75% | 50% of 2 | too few (5/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 5 | 100% | +0.19% | +0.16 to +0.25% | 67% of 3 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 5 | 60% | +0.15% | -0.07 to +0.33% | 100% of 1 | too few (5/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 5 | 80% | +0.21% | -0.22 to +0.68% | 60% of 5 | too few (5/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 5 | 100% | +0.29% | +0.04 to +0.59% | 0% of 4 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near put wall | 5 | 60% | +0.09% | -0.51 to +0.73% | 0% of 2 | too few (5/10) |
| monthly | PCR flat · quiet OI · walls up · near put wall | 4 | 0% | -0.25% | -0.61 to -0.05% | 100% of 1 | too few (3/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 4 | 100% | +0.15% | +0.06 to +0.25% | 100% of 1 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 50% of 2 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 4 | 100% | +0.60% | +0.23 to +0.85% | 0% of 1 | too few (4/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 4 | 100% | +0.50% | +0.37 to +0.62% | 0% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 4 | 100% | +0.61% | +0.01 to +1.22% | 67% of 3 | too few (2/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 100% | +0.79% | +0.14 to +1.65% | 0% of 1 | too few (4/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 4 | 100% | +0.51% | +0.13 to +1.17% | 50% of 2 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 4 |  |  |  | 100% of 4 | too few (0/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 4 | 50% | +0.06% | -0.63 to +0.58% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 4 | 25% | -0.02% | -0.69 to +0.99% | 50% of 2 | too few (4/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 3 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 3 | 67% | +0.08% | -0.07 to +0.27% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 3 | 50% | -0.03% | -0.43 to +0.37% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near put wall | 3 | 67% | -0.09% | -1.22 to +0.65% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 3 | 67% | -0.03% | -0.44 to +0.19% | 0% of 1 | too few (3/10) |
| weekly | PCR up · call writing · walls down · mid walls | 3 | 67% | +0.18% | -0.61 to +0.64% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 3 | 67% | +0.38% | -0.18 to +0.91% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 3 | 33% | -0.01% | -0.37 to +0.53% | 50% of 2 | too few (3/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 3 | 50% | -0.15% | -0.33 to +0.03% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 3 | 100% | +0.28% | +0.07 to +0.50% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 3 | 100% | +0.12% | +0.05 to +0.16% | 100% of 2 | too few (3/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 3 | 67% | +0.08% | -0.04 to +0.18% | 50% of 2 | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls same · near put wall | 2 | 0% | -0.07% | -0.07 to -0.07% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 2 | 50% | +0.18% | -0.20 to +0.57% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 2 | 50% | -0.57% | -1.32 to +0.18% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 2 | 50% | -0.15% | -0.30 to +0.01% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 2 | 100% | +0.20% | +0.20 to +0.20% | 100% of 2 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 2 | 50% | -0.08% | -0.49 to +0.34% |  | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 50% of 2 | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% | 0% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · mid walls | 2 | 50% | +0.04% | -0.19 to +0.28% | 100% of 2 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 50% of 2 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near put wall | 2 | 100% | +0.21% | +0.18 to +0.24% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 2 | 50% | -0.10% | -0.29 to +0.09% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls same · mid walls | 2 | 100% | +0.30% | +0.29 to +0.31% | 100% of 2 | too few (2/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 100% | +0.90% | +0.90 to +0.90% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.20% | -0.20 to -0.20% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls up · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +1.14% | +1.14 to +1.14% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · near put wall | 1 | 0% | -0.44% | -0.44 to -0.44% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| monthly | PCR flat · put writing · walls down · mid walls | 1 | 0% | -0.35% | -0.35 to -0.35% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near call wall | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% | 0% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +1.86% | +1.86 to +1.86% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -1.33% | -1.33 to -1.33% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls same · mid walls | 1 | 100% | +0.49% | +0.49 to +0.49% | 100% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% | 0% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.40% | +0.40 to +0.40% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · near put wall | 1 | 100% | +1.02% | +1.02 to +1.02% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near put wall | 1 | 0% | -0.29% | -0.29 to -0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near put wall | 1 | 0% | -0.83% | -0.83 to -0.83% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · mid walls | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 50% of 2 | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 3 | 67% | +0.30% | -0.61 to +1.12% | 100% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 3 | 100% | +0.55% | +0.51 to +0.58% | 50% of 2 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 3 | 100% | +0.61% | +0.06 to +1.12% | 100% of 3 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | +0.73% | -0.39 to +2.40% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 50% | +0.02% | -0.63 to +0.68% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.53% | -0.63 to +1.68% | 0% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 2 | 0% | -1.15% | -1.75 to -0.54% | 100% of 2 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 50% | +0.18% | -0.28 to +0.65% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -1.75% | -1.75 to -1.75% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near put wall | 1 | 100% | +1.85% | +1.85 to +1.85% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.58% | +0.58 to +0.58% | 100% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +1.85% | +1.85 to +1.85% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.84% | +0.84 to +0.84% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.38% | +0.38 to +0.38% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +1.14% | +1.14 to +1.14% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 174 | 66% | +0.17% | up |
| intraday | weekly | writers even · few weak writers | 127 | 58% | +0.08% | no clear direction |
| intraday | monthly | writers even · weak calls | 103 | 73% | +0.14% | up |
| intraday | weekly | put writers stronger · weak calls | 79 | 76% | +0.32% | up |
| intraday | monthly | put writers stronger · weak calls | 63 | 85% | +0.57% | up |
| intraday | weekly | call writers stronger · weak puts | 43 | 80% | +0.33% | up |
| intraday | weekly | put writers stronger · few weak writers | 41 | 84% | +0.35% | up |
| intraday | weekly | call writers stronger · few weak writers | 36 | 74% | +0.17% | up |
| intraday | weekly | writers even · weak calls | 27 | 80% | +0.38% | up |
| intraday | monthly | writers even · weak puts | 21 | 80% | +0.42% | up |
| intraday | weekly | writers even · weak puts | 21 | 78% | +0.24% | up |
| intraday | monthly | call writers stronger · few weak writers | 15 | 62% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak on both sides | 11 | 73% | +0.20% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 7 | 29% | -0.51% | too few (7/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | weekly | put writers stronger · weak on both sides | 1 | 0% | -0.29% | too few (1/10) |
| day | monthly | writers even · few weak writers | 15 | 50% | +0.19% | no clear direction |
| day | weekly | writers even · few weak writers | 9 | 62% | +0.53% | too few (8/10) |
| day | monthly | writers even · weak calls | 7 | 71% | +0.52% | too few (7/10) |
| day | weekly | put writers stronger · weak calls | 7 | 71% | +0.20% | too few (7/10) |
| day | monthly | put writers stronger · weak calls | 4 | 100% | +0.88% | too few (4/10) |
| day | weekly | call writers stronger · weak puts | 3 | 33% | +0.32% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | writers even · weak puts | 3 | 33% | -0.06% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 2 | 100% | +0.92% | too few (2/10) |
| day | weekly | writers even · weak calls | 2 | 50% | +1.00% | too few (2/10) |
| day | monthly | writers even · weak puts | 1 | 100% | +1.85% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 57 | 65% | +0.14% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 57 | 78% | +0.39% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 52 | 52% | -0.02% | no clear direction |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 49 | 85% | +0.68% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 45 | 93% | +0.31% | up |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m up | 41 | 46% | -0.03% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 28 | 77% | +0.29% | up |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 23 | 55% | +0.22% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 23 | 67% | +0.27% | no clear direction |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 22 | 72% | +0.11% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m sideways | 17 | 88% | +0.14% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 14 | 83% | +0.16% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.73% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 9 | 50% | -0.12% | too few (8/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly sideways · 125m up | 9 | 78% | +0.56% | too few (9/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 9 | 67% | +0.03% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 8 | 100% | +0.19% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 6 | 20% | -0.14% | too few (5/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 5 | 100% | +0.53% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 5 | 40% | +0.00% | too few (5/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly sideways · 125m sideways | 4 | 50% | +0.01% | too few (4/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly sideways · 125m sideways | 2 | 0% | -0.07% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 2 | 0% | -0.89% | too few (1/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.02% | too few (1/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 1 | 0% | -1.33% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | put writers stronger · weak on both sides · weekly sideways · 125m up | 1 | 0% | -0.29% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m up | 1 | 100% | +0.91% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 6 | 40% | -0.23% | too few (5/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 4 | 75% | +0.07% | too few (4/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 4 | 33% | -0.17% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +1.32% | too few (2/10) |
| day | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m up | 2 | 50% | -0.22% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +0.86% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 | 100% | +1.14% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.58% | too few (1/10) |
| day | monthly | writers even · weak puts · weekly sideways · 125m sideways | 1 | 100% | +1.85% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.18% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 1 | 100% | +1.85% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m up | 1 | 100% | +2.01% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.22% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 0% | -0.63% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
