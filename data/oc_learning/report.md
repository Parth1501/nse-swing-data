# Nifty option chain pattern log
Updated 2026-10-28 10:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 231 snapshots over 10 trading days
- 250 patterns logged; 112 different patterns so far

## Latest read (2026-10-28 10:42:19)

Nifty trend: weekly **bearish**, 125-min **up**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-03 (weekly) | 6.2 | 22540 | 0.769 | 22600 | 20050 | 23000 | ±1.8% (22135-22946) | 17.5 |
| 2026-11-23 (monthly) | 26.2 | 22539 | 1.376 | 23000 | 22000 | 23500 | ±3.53% (21744-23334) | 16.48 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 13 times before; Nifty was up after it 42% of the time, average +0.00%. Too few outcomes (12/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 10 times before; Nifty was up after it 44% of the time, average +0.11%. Too few outcomes (9/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. Seen 1 times before; Nifty was up after it 100% of the time, average +1.66%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 1 times before; Nifty was up after it 100% of the time, average +1.66%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls same · mid walls`. Seen 5 times before; Nifty was up after it 67% of the time, average -0.01%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 18 times before; Nifty was up after it 78% of the time, average +0.39%. Too few outcomes (18/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m up`: Seen 4 times before; Nifty was up after it 0% of the time, average -0.17%. Too few outcomes (4/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.68%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly bearish · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-03

Strongest call writers at 22600, strongest put writers at 22500; weakest call writers at 21900, weakest put writers at 23000. Covers 62% of near-money call OI and 44% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22250 | 983 | 559 | 407.1 | 22585 | 378.9 | 22657 | +117 | +28.1 | strong |
| Call | 22300 | 8684 | 3401 | 361.4 | 22574 | 343.4 | 22661 | +121 | +18.0 | strong |
| Call | 22350 | 2706 | 2119 | 328.7 | 22577 | 310.0 | 22679 | +138 | +18.7 | strong |
| Call | 22400 | 19751 | 10262 | 295.8 | 22576 | 278.7 | 22696 | +155 | +17.1 | strong |
| Call | 22450 | 10494 | 8898 | 265.2 | 22575 | 248.4 | 22715 | +175 | +16.8 | strong |
| Call | 22500 | 80425 | 61335 | 238.1 | 22578 | 220.1 | 22738 | +198 | +18.0 | strong |
| Call | 22550 | 64307 | 61872 | 218.4 | 22593 | 194.3 | 22768 | +228 | +24.1 | strong |
| Call | 22600 | 151636 | 136790 | 201.1 | 22610 | 170.2 | 22801 | +261 | +30.9 | strong |
| Call | 22650 | 54993 | 48996 | 176.8 | 22614 | 148.7 | 22827 | +286 | +28.1 | strong |
| Call | 22700 | 151102 | 95809 | 146.1 | 22593 | 128.8 | 22846 | +306 | +17.3 | strong |
| Call | 22750 | 48873 | 29488 | 124.8 | 22591 | 110.8 | 22875 | +334 | +14.0 | strong |
| Call | 22800 | 121237 | 49789 | 109.5 | 22597 | 94.4 | 22909 | +369 | +15.1 | strong |
| Call | 22850 | 38617 | 24826 | 96.1 | 22606 | 79.9 | 22946 | +406 | +16.2 | strong |
| Put | 22250 | 21637 | 11267 | 80.5 | 22604 | 95.8 | 22169 | +371 | -15.3 | strong |
| Put | 22300 | 61825 | 12087 | 90.9 | 22615 | 110.0 | 22209 | +331 | -19.1 | strong |
| Put | 22350 | 23182 | 4529 | 110.1 | 22596 | 127.0 | 22240 | +301 | -16.9 | strong |
| Put | 22400 | 55141 | 22907 | 125.1 | 22604 | 144.7 | 22275 | +266 | -19.6 | strong |
| Put | 22450 | 25653 | 18096 | 147.7 | 22591 | 164.7 | 22302 | +238 | -17.0 | strong |
| Put | 22500 | 106838 | 62186 | 168.8 | 22588 | 187.0 | 22331 | +209 | -18.2 | strong |
| Put | 22550 | 45607 | 37527 | 180.3 | 22614 | 210.8 | 22370 | +171 | -30.5 | strong |
| Put | 22600 | 89787 | 59641 | 203.0 | 22616 | 237.2 | 22397 | +143 | -34.2 | strong |
| Put | 22650 | 16210 | 7973 | 239.4 | 22600 | 264.6 | 22411 | +130 | -25.2 | strong |
| Put | 22700 | 58570 | 6981 | 255.3 | 22615 | 295.4 | 22445 | +96 | -40.1 | medium |
| Put | 22850 | 4066 | 317 | 397.7 | 22544 | 396.4 | 22452 | +88 | +1.3 | medium |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at -, weakest put writers at 23000. Covers 72% of near-money call OI and 66% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22250 | 175 | 94 | 711.4 | 22645 | 611.4 | 22961 | +423 | +100.0 | strong |
| Call | 22300 | 1790 | 1123 | 651.7 | 22582 | 576.5 | 22952 | +413 | +75.2 | strong |
| Call | 22350 | 293 | 251 | 652.5 | 22632 | 547.0 | 23003 | +464 | +105.5 | strong |
| Call | 22400 | 3894 | 2930 | 553.3 | 22524 | 510.3 | 22953 | +415 | +43.0 | strong |
| Call | 22450 | 727 | 673 | 569.1 | 22596 | 484.4 | 23019 | +480 | +84.8 | strong |
| Call | 22500 | 38135 | 29473 | 524.7 | 22603 | 450.7 | 23025 | +486 | +74.0 | strong |
| Call | 22550 | 1491 | 1410 | 489.4 | 22596 | 425.0 | 23039 | +501 | +64.4 | strong |
| Call | 22600 | 36312 | 30967 | 454.4 | 22616 | 397.6 | 23054 | +516 | +56.9 | strong |
| Call | 22650 | 4485 | 4284 | 457.3 | 22611 | 370.5 | 23107 | +569 | +86.8 | strong |
| Call | 22700 | 48161 | 45371 | 451.4 | 22690 | 348.3 | 23151 | +613 | +103.1 | strong |
| Call | 22750 | 2281 | 1751 | 417.7 | 22667 | 325.0 | 23168 | +629 | +92.7 | strong |
| Call | 22800 | 29398 | 25385 | 403.6 | 22692 | 299.4 | 23204 | +665 | +104.2 | strong |
| Call | 22850 | 1732 | 1339 | 364.2 | 22684 | 277.5 | 23214 | +675 | +86.7 | strong |
| Put | 22250 | 2166 | 827 | 215.4 | 22691 | 253.9 | 22035 | +504 | -38.5 | strong |
| Put | 22300 | 19622 | 12683 | 235.4 | 22669 | 270.9 | 22065 | +474 | -35.5 | strong |
| Put | 22350 | 1249 | 761 | 244.4 | 22678 | 288.4 | 22106 | +433 | -44.0 | strong |
| Put | 22400 | 19046 | 8134 | 265.1 | 22662 | 305.6 | 22135 | +404 | -40.4 | strong |
| Put | 22450 | 1245 | 928 | 293.4 | 22621 | 323.8 | 22157 | +382 | -30.3 | strong |
| Put | 22500 | 68806 | 43346 | 293.7 | 22676 | 348.6 | 22206 | +332 | -54.9 | strong |
| Put | 22550 | 1998 | 1699 | 319.8 | 22645 | 370.0 | 22230 | +309 | -50.2 | strong |
| Put | 22600 | 36271 | 30098 | 348.1 | 22634 | 391.5 | 22252 | +287 | -43.5 | strong |
| Put | 22650 | 5078 | 4635 | 355.4 | 22642 | 412.2 | 22295 | +244 | -56.9 | strong |
| Put | 22700 | 54629 | 48787 | 355.7 | 22706 | 443.8 | 22344 | +194 | -88.1 | strong |
| Put | 22750 | 4301 | 3981 | 341.6 | 22755 | 467.9 | 22408 | +130 | -126.3 | strong |
| Put | 22800 | 30782 | 22862 | 398.0 | 22702 | 495.0 | 22402 | +137 | -97.0 | strong |
| Put | 22850 | 2236 | 886 | 395.6 | 22748 | 523.7 | 22454 | +84 | -128.1 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 16 | 62% | +0.09% | -0.44 to +0.76% | 100% of 1 | no clear direction |
| monthly | PCR down · put and call writing · walls same · mid walls | 7 | 71% | +0.04% | -0.37 to +0.46% | 100% of 1 | too few (7/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 50% of 2 | too few (7/10) |
| weekly | PCR up · put writing · walls same · near put wall | 7 | 57% | -0.03% | -0.47 to +0.41% | 50% of 2 | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 7 | 86% | +0.32% | -0.39 to +0.91% | 100% of 1 | too few (7/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 67% | +0.16% | -0.24 to +0.56% | 100% of 1 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 6 | 67% | -0.01% | -0.12 to +0.08% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 6 | 100% | +0.46% | +0.27 to +0.70% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 5 | 100% | +0.44% | +0.09 to +1.02% | 100% of 1 | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 5 | 40% | +0.04% | -0.78 to +0.90% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near put wall | 5 | 80% | +0.35% | -0.37 to +0.85% | 50% of 2 | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% | 100% of 1 | too few (4/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 4 | 67% | +0.06% | -0.05 to +0.15% | 50% of 2 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 3 | 0% | -0.35% | -0.68 to -0.02% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · mid walls | 3 | 67% | +0.23% | -0.07 to +0.54% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 3 | 67% | +0.16% | -0.02 to +0.37% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 50% of 2 | too few (3/10) |
| monthly | PCR down · put writing · walls same · mid walls | 3 | 67% | +0.06% | -0.05 to +0.21% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 100% | +0.57% | +0.24 to +0.85% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.45% | +0.15 to +0.76% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 1 | 100% | +0.72% | +0.72 to +0.72% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.36% | +0.36 to +0.36% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put and call writing · walls same · mid walls | 2 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 0% | -0.63% | -0.92 to -0.34% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.92% | -0.92 to -0.92% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 58 | 64% | +0.08% | up |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | weekly | writers even · few weak writers | 23 | 32% | -0.27% | no clear direction |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · weak puts | 19 | 78% | +0.39% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 14 | 42% | +0.00% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | weekly | writers even · weak on both sides | 5 | 100% | +0.25% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak calls | 4 | 33% | -0.06% | too few (3/10) |
| day | monthly | writers even · few weak writers | 5 | 20% | -0.24% | too few (5/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 2 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | -0.12% | too few (2/10) |
| day | monthly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.02% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 29 | 71% | +0.17% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 11 | 44% | +0.11% | too few (9/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 11 | 36% | -0.21% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 10 | 33% | -0.20% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 7 | 14% | -0.40% | too few (7/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 0% | -0.17% | too few (4/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.66% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 1 | 0% | -0.92% | too few (1/10) |
| day | monthly | writers even · weak puts · weekly bearish · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.92% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
