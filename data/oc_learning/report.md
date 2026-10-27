# Nifty option chain pattern log
Updated 2026-10-27 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 221 snapshots over 9 trading days
- 239 patterns logged; 110 different patterns so far

## Latest read (2026-10-27 14:39:12)

Nifty trend: weekly **bearish**, 125-min **sideways**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 0.0 | 22720 | 0.949 | 22700 | 22700 | 22800 | ±0.3% (22652-22788) | 6.66 |
| 2026-11-23 (monthly) | 27.0 | 22717 | 1.244 | 23000 | 22000 | 23500 | ±3.47% (21928-23506) | 15.92 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls up · near put wall`. Seen 2 times before; Nifty was up after it 50% of the time, average +0.11%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · weak on both sides`. Seen 4 times before; Nifty was up after it 100% of the time, average +0.21%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 3 times before; Nifty was up after it 100% of the time, average +0.16%. Too few outcomes (3/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak on both sides`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly bearish · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · quiet OI · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 53 times before; Nifty was up after it 63% of the time, average +0.08%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 27 times before; Nifty was up after it 65% of the time, average +0.12%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.34%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Nifty was up after it 25% of the time, average -0.10%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 1 times before; Nifty was up after it 0% of the time, average -0.16%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 22800, strongest put writers at 22600; weakest call writers at 22700, weakest put writers at 22750. Covers 98% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 15280 | 14860 | 217.3 | 22482 | 340.1 | 22617 | -103 | -122.8 | weak |
| Call | 22450 | 7872 | 7861 | 182.6 | 22484 | 290.4 | 22633 | -88 | -107.8 | weak |
| Call | 22500 | 45862 | 44912 | 169.2 | 22512 | 240.7 | 22669 | -51 | -71.5 | weak |
| Call | 22550 | 20642 | 20626 | 153.2 | 22582 | 190.8 | 22703 | -17 | -37.6 | weak |
| Call | 22600 | 75367 | 75143 | 121.1 | 22616 | 141.9 | 22721 | +1 | -20.8 | weak |
| Call | 22650 | 93735 | 93726 | 82.3 | 22676 | 94.7 | 22732 | +12 | -12.3 | weak |
| Call | 22700 | 328330 | 327504 | 63.6 | 22687 | 53.8 | 22764 | +43 | +9.8 | weak |
| Call | 22750 | 308308 | 308086 | 51.2 | 22713 | 24.8 | 22801 | +81 | +26.4 | medium |
| Call | 22800 | 413942 | 411753 | 50.1 | 22708 | 9.6 | 22850 | +130 | +40.5 | strong |
| Call | 22850 | 216782 | 216514 | 37.5 | 22714 | 3.6 | 22888 | +167 | +33.9 | strong |
| Call | 22900 | 219874 | 217805 | 45.8 | 22710 | 1.7 | 22946 | +226 | +44.1 | strong |
| Call | 22950 | 111249 | 111002 | 32.4 | 22731 | 1.0 | 22982 | +262 | +31.4 | strong |
| Call | 23000 | 305695 | 291584 | 40.4 | 22706 | 0.8 | 23040 | +320 | +39.6 | strong |
| Call | 23050 | 109316 | 108953 | 28.6 | 22735 | 0.6 | 23079 | +358 | +28.1 | strong |
| Put | 22400 | 206580 | 202674 | 54.4 | 22602 | 0.6 | 22346 | +375 | +53.8 | strong |
| Put | 22450 | 115612 | 115526 | 48.1 | 22634 | 0.6 | 22402 | +318 | +47.5 | strong |
| Put | 22500 | 277773 | 267698 | 56.6 | 22671 | 0.8 | 22443 | +277 | +55.8 | strong |
| Put | 22550 | 153287 | 153174 | 35.3 | 22686 | 1.2 | 22515 | +206 | +34.1 | strong |
| Put | 22600 | 344344 | 341520 | 47.0 | 22694 | 2.3 | 22553 | +167 | +44.7 | strong |
| Put | 22650 | 323676 | 323584 | 39.1 | 22712 | 5.2 | 22611 | +109 | +33.9 | strong |
| Put | 22700 | 456516 | 454656 | 59.9 | 22731 | 14.1 | 22640 | +80 | +45.8 | medium |
| Put | 22750 | 183494 | 183477 | 61.6 | 22744 | 35.0 | 22688 | +32 | +26.6 | weak |
| Put | 22800 | 113794 | 112936 | 82.5 | 22765 | 70.2 | 22718 | +3 | +12.3 | weak |
| Put | 22850 | 23234 | 23216 | 100.6 | 22776 | 114.5 | 22749 | -29 | -13.8 | weak |
| Put | 22900 | 34420 | 33609 | 157.1 | 22821 | 162.1 | 22743 | -23 | -5.0 | weak |
| Put | 22950 | 9215 | 9195 | 181.4 | 22821 | 212.3 | 22769 | -48 | -30.9 | weak |
| Put | 23000 | 34135 | 30936 | 237.4 | 22843 | 261.1 | 22763 | -42 | -23.7 | weak |
| Put | 23050 | 5583 | 5567 | 194.9 | 22980 | 311.2 | 22855 | -135 | -116.3 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23150. Covers 67% of near-money call OI and 65% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 3138 | 2171 | 555.9 | 22495 | 651.3 | 22956 | +239 | -95.4 | strong |
| Call | 22450 | 601 | 547 | 585.2 | 22598 | 598.3 | 23035 | +318 | -13.1 | strong |
| Call | 22500 | 27628 | 18941 | 552.6 | 22606 | 589.6 | 23053 | +336 | -37.1 | strong |
| Call | 22550 | 930 | 849 | 519.9 | 22600 | 553.3 | 23070 | +353 | -33.4 | strong |
| Call | 22600 | 21757 | 16303 | 487.8 | 22632 | 521.7 | 23088 | +371 | -33.9 | strong |
| Call | 22650 | 3812 | 3609 | 470.3 | 22613 | 491.9 | 23120 | +403 | -21.7 | strong |
| Call | 22700 | 39259 | 36443 | 469.5 | 22705 | 459.4 | 23169 | +453 | +10.1 | strong |
| Call | 22750 | 1817 | 1271 | 431.8 | 22661 | 429.9 | 23182 | +465 | +1.9 | strong |
| Call | 22800 | 26182 | 22276 | 410.8 | 22697 | 401.8 | 23211 | +494 | +9.0 | strong |
| Call | 22850 | 1351 | 963 | 387.3 | 22712 | 374.9 | 23237 | +520 | +12.4 | strong |
| Call | 22900 | 13495 | 10981 | 368.6 | 22709 | 349.5 | 23269 | +552 | +19.1 | strong |
| Call | 22950 | 1622 | 918 | 349.6 | 22726 | 326.2 | 23300 | +583 | +23.4 | strong |
| Call | 23000 | 96934 | 53471 | 308.1 | 22669 | 302.5 | 23308 | +591 | +5.6 | strong |
| Call | 23050 | 1534 | 455 | 295.3 | 22707 | 277.8 | 23345 | +628 | +17.6 | strong |
| Put | 22400 | 19574 | 8157 | 264.9 | 22663 | 225.9 | 22135 | +582 | +39.0 | strong |
| Put | 22450 | 1103 | 768 | 291.0 | 22626 | 239.9 | 22159 | +558 | +51.1 | strong |
| Put | 22500 | 60662 | 35160 | 287.8 | 22693 | 258.2 | 22212 | +505 | +29.5 | strong |
| Put | 22550 | 1486 | 1190 | 308.7 | 22668 | 273.6 | 22241 | +476 | +35.1 | strong |
| Put | 22600 | 23698 | 17454 | 337.3 | 22658 | 292.2 | 22263 | +454 | +45.0 | strong |
| Put | 22650 | 4636 | 4192 | 353.7 | 22643 | 308.9 | 22296 | +421 | +44.7 | strong |
| Put | 22700 | 44930 | 39063 | 345.6 | 22724 | 329.9 | 22354 | +362 | +15.6 | strong |
| Put | 22750 | 1948 | 1596 | 354.3 | 22745 | 351.6 | 22396 | +321 | +2.7 | strong |
| Put | 22800 | 29471 | 21442 | 394.8 | 22706 | 372.1 | 22405 | +312 | +22.6 | strong |
| Put | 22850 | 2084 | 689 | 390.3 | 22748 | 392.9 | 22460 | +257 | -2.6 | strong |
| Put | 22900 | 16189 | 12919 | 436.0 | 22709 | 418.6 | 22464 | +253 | +17.4 | strong |
| Put | 22950 | 775 | 459 | 430.1 | 22755 | 441.1 | 22520 | +197 | -11.0 | strong |
| Put | 23000 | 88618 | 51815 | 483.5 | 22730 | 472.5 | 22517 | +200 | +11.0 | strong |
| Put | 23050 | 666 | 341 | 469.6 | 22781 | 525.0 | 22580 | +136 | -55.5 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 16 | 56% | +0.05% | -0.44 to +0.76% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 7 | 43% | -0.06% | -0.47 to +0.41% | 50% of 2 | too few (7/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 50% of 2 | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 7 | 86% | +0.30% | -0.39 to +0.91% | 100% of 1 | too few (7/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | +0.02% | -0.42 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 6 | 67% | +0.09% | -0.21 to +0.46% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 6 | 100% | +0.46% | +0.27 to +0.70% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 5 | 80% | +0.18% | -0.24 to +0.56% | 100% of 1 | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 5 | 40% | +0.01% | -0.78 to +0.90% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near put wall | 5 | 60% | +0.33% | -0.37 to +0.85% | 50% of 2 | too few (5/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 5 | 100% | +0.44% | +0.09 to +1.02% | 100% of 1 | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% | 100% of 1 | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 4 | 67% | -0.06% | -0.27 to +0.08% | 100% of 1 | too few (3/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 50% of 2 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 50% of 2 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 3 | 50% | +0.11% | -0.15 to +0.37% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls down · mid walls | 3 | 67% | +0.19% | -0.07 to +0.54% | 100% of 1 | too few (3/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 100% | +0.57% | +0.24 to +0.85% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% | 100% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.11% | +0.01 to +0.21% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 50% of 2 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.23% | +0.12 to +0.35% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 2 | 0% | -0.41% | -0.68 to -0.15% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.45% | +0.15 to +0.76% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 1 | 100% | +0.72% | +0.72 to +0.72% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.36% | +0.36 to +0.36% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 0% | -0.34% | -0.34 to -0.34% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.16% | -0.16 to -0.16% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.16% | -0.16 to -0.16% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 54 | 63% | +0.08% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | weekly | writers even · few weak writers | 23 | 23% | -0.30% | down |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | weekly | writers even · weak puts | 18 | 82% | +0.30% | up |
| intraday | monthly | writers even · weak puts | 17 | 82% | +0.42% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | weekly | writers even · weak on both sides | 5 | 100% | +0.21% | too few (4/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak calls | 3 | 50% | -0.13% | too few (2/10) |
| day | monthly | writers even · few weak writers | 5 | 25% | -0.10% | too few (4/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.16% | too few (1/10) |
| day | weekly | writers even · weak on both sides | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +0.68% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 28 | 65% | +0.12% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.32% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 11 | 18% | -0.28% | down |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 8 | 57% | +0.20% | too few (7/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.29% | too few (8/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 7 | 43% | -0.11% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 7 | 14% | -0.40% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.16% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 3 | 0% | -0.20% | too few (3/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 3 | 50% | -0.13% | too few (2/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.27% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.16% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.16% | too few (1/10) |
| day | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
