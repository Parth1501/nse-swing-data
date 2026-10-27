# Nifty option chain pattern log
Updated 2026-10-27 09:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 201 snapshots over 9 trading days
- 219 patterns logged; 107 different patterns so far

## Latest read (2026-10-27 09:45:52)

Nifty trend: weekly **bearish**, 125-min **sideways**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 0.2 | 22754 | 0.868 | 22700 | 22500 | 23000 | ±0.71% (22593-22915) | 17.25 |
| 2026-11-23 (monthly) | 27.2 | 22741 | 1.18 | 23050 | 22000 | 23500 | ±3.61% (21919-23563) | 16.5 |

- **Weekly, last 30 min**: `PCR down · put and call writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.68%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 17 times before; Nifty was up after it 31% of the time, average -0.36%. Too few outcomes (16/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 5 times before; Nifty was up after it 40% of the time, average -0.42%. Too few outcomes (5/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.39%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · put and call writing · walls same · mid walls`. Seen 5 times before; Nifty was up after it 80% of the time, average +0.13%. Too few outcomes (5/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 43 times before; Nifty was up after it 72% of the time, average +0.13%. History points to a bull call debit spread, ATM to about the call wall 23500.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 17 times before; Nifty was up after it 88% of the time, average +0.27%. Too few outcomes (16/20) to trade on.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.34%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 4 times before; Nifty was up after it 25% of the time, average -0.08%. Too few outcomes (4/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 1 times before; Nifty was up after it 0% of the time, average -0.05%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at 22600, weakest put writers at 22900. Covers 97% of near-money call OI and 97% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22450 | 11799 | 11782 | 180.2 | 22479 | 319.4 | 22630 | -124 | -139.2 | weak |
| Call | 22500 | 64820 | 63348 | 165.7 | 22495 | 272.2 | 22666 | -88 | -106.5 | weak |
| Call | 22550 | 21079 | 21057 | 152.4 | 22542 | 228.0 | 22702 | -51 | -75.6 | weak |
| Call | 22600 | 84655 | 84139 | 128.4 | 22536 | 185.8 | 22728 | -25 | -57.4 | weak |
| Call | 22650 | 80415 | 80378 | 132.1 | 22656 | 148.6 | 22782 | +28 | -16.4 | weak |
| Call | 22700 | 278016 | 275619 | 111.5 | 22672 | 113.0 | 22812 | +58 | -1.5 | medium |
| Call | 22750 | 217168 | 216707 | 87.8 | 22711 | 84.9 | 22838 | +84 | +3.0 | medium |
| Call | 22800 | 296349 | 293066 | 75.3 | 22681 | 63.1 | 22875 | +122 | +12.1 | strong |
| Call | 22850 | 148775 | 148435 | 51.9 | 22687 | 44.0 | 22902 | +148 | +8.0 | strong |
| Call | 22900 | 229315 | 226388 | 56.2 | 22692 | 29.8 | 22956 | +202 | +26.4 | strong |
| Call | 22950 | 108406 | 108022 | 44.4 | 22702 | 19.8 | 22994 | +241 | +24.6 | strong |
| Call | 23000 | 422255 | 400391 | 44.5 | 22698 | 13.5 | 23044 | +291 | +31.0 | strong |
| Call | 23050 | 145566 | 144965 | 34.3 | 22726 | 8.3 | 23084 | +331 | +26.0 | strong |
| Put | 22450 | 133160 | 133023 | 65.0 | 22597 | 8.0 | 22385 | +369 | +57.0 | strong |
| Put | 22500 | 360611 | 345863 | 63.2 | 22658 | 11.8 | 22437 | +317 | +51.4 | strong |
| Put | 22550 | 135684 | 135489 | 61.6 | 22666 | 17.5 | 22488 | +265 | +44.1 | strong |
| Put | 22600 | 293418 | 289164 | 72.8 | 22681 | 26.0 | 22527 | +227 | +46.8 | strong |
| Put | 22650 | 199017 | 198881 | 61.1 | 22710 | 37.3 | 22589 | +165 | +23.8 | strong |
| Put | 22700 | 339530 | 337222 | 78.9 | 22720 | 54.6 | 22621 | +133 | +24.2 | strong |
| Put | 22750 | 138430 | 138386 | 96.9 | 22720 | 76.0 | 22653 | +101 | +20.8 | medium |
| Put | 22800 | 115247 | 112004 | 135.6 | 22731 | 101.1 | 22664 | +89 | +34.5 | medium |
| Put | 22850 | 21355 | 21259 | 163.9 | 22725 | 133.8 | 22686 | +68 | +30.1 | medium |
| Put | 22900 | 43331 | 41342 | 174.2 | 22870 | 169.8 | 22726 | +28 | +4.3 | weak |
| Put | 22950 | 10407 | 10363 | 199.8 | 22848 | 210.4 | 22750 | +4 | -10.6 | weak |
| Put | 23000 | 44872 | 39540 | 239.1 | 22870 | 253.2 | 22761 | -7 | -14.1 | weak |
| Put | 23050 | 6809 | 6786 | 183.0 | 23017 | 298.6 | 22867 | -113 | -115.5 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23150. Covers 62% of near-money call OI and 60% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22450 | 593 | 538 | 583.6 | 22594 | 657.0 | 23034 | +292 | -73.4 | strong |
| Call | 22500 | 28519 | 19339 | 551.8 | 22603 | 626.1 | 23052 | +310 | -74.3 | strong |
| Call | 22550 | 639 | 558 | 501.5 | 22549 | 593.1 | 23052 | +310 | -91.6 | strong |
| Call | 22600 | 20848 | 15299 | 485.9 | 22628 | 560.7 | 23086 | +345 | -74.8 | strong |
| Call | 22650 | 4161 | 3935 | 469.7 | 22611 | 529.0 | 23120 | +378 | -59.3 | strong |
| Call | 22700 | 31306 | 28465 | 464.4 | 22692 | 496.7 | 23164 | +423 | -32.3 | strong |
| Call | 22750 | 1499 | 937 | 424.6 | 22632 | 470.7 | 23175 | +433 | -46.1 | strong |
| Call | 22800 | 21061 | 17056 | 404.9 | 22679 | 437.4 | 23205 | +463 | -32.5 | strong |
| Call | 22850 | 1140 | 748 | 381.2 | 22700 | 410.5 | 23231 | +490 | -29.3 | strong |
| Call | 22900 | 11863 | 9306 | 366.5 | 22700 | 383.5 | 23267 | +525 | -17.0 | strong |
| Call | 22950 | 1346 | 614 | 343.2 | 22703 | 356.6 | 23293 | +552 | -13.4 | strong |
| Call | 23000 | 90980 | 46656 | 307.2 | 22660 | 333.2 | 23307 | +566 | -26.0 | strong |
| Call | 23050 | 1331 | 244 | 283.6 | 22660 | 311.1 | 23334 | +592 | -27.5 | strong |
| Put | 22450 | 1036 | 699 | 295.2 | 22616 | 243.8 | 22155 | +587 | +51.5 | strong |
| Put | 22500 | 59490 | 33586 | 289.0 | 22692 | 262.9 | 22211 | +530 | +26.0 | strong |
| Put | 22550 | 1087 | 787 | 322.6 | 22644 | 274.0 | 22227 | +514 | +48.5 | strong |
| Put | 22600 | 21758 | 15514 | 342.3 | 22651 | 295.0 | 22258 | +484 | +47.3 | strong |
| Put | 22650 | 4097 | 3653 | 359.1 | 22633 | 309.2 | 22291 | +450 | +49.9 | strong |
| Put | 22700 | 36588 | 30721 | 349.7 | 22715 | 332.0 | 22350 | +391 | +17.7 | strong |
| Put | 22750 | 1472 | 1109 | 359.1 | 22742 | 351.3 | 22391 | +350 | +7.8 | strong |
| Put | 22800 | 25583 | 17502 | 401.7 | 22695 | 371.9 | 22398 | +343 | +29.8 | strong |
| Put | 22850 | 1786 | 365 | 400.6 | 22727 | 387.2 | 22449 | +292 | +13.4 | strong |
| Put | 22900 | 11309 | 8038 | 451.8 | 22681 | 415.6 | 22448 | +293 | +36.2 | strong |
| Put | 22950 | 612 | 270 | 437.2 | 22745 | 426.8 | 22513 | +229 | +10.4 | strong |
| Put | 23000 | 76949 | 40118 | 488.9 | 22725 | 463.9 | 22511 | +230 | +25.0 | strong |
| Put | 23050 | 546 | 220 | 462.7 | 22791 | 486.7 | 22587 | +154 | -24.0 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 11 | 82% | +0.16% | -0.44 to +0.76% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 50% of 2 | too few (7/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 6 | 100% | +0.46% | +0.27 to +0.70% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 6 | 80% | +0.13% | -0.21 to +0.46% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 6 | 83% | +0.35% | -0.39 to +0.91% | 100% of 1 | too few (6/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 5 | 50% | +0.25% | -0.40 to +0.90% | 100% of 2 | too few (2/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 5 | 100% | +0.44% | +0.09 to +1.02% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put writing · walls same · near put wall | 5 | 60% | -0.04% | -0.47 to +0.41% | 50% of 2 | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% | 100% of 1 | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 75% | +0.15% | -0.24 to +0.56% | 100% of 1 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls same · near put wall | 4 | 75% | +0.44% | -0.37 to +0.85% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 4 | 50% | +0.08% | -0.78 to +0.90% | 100% of 1 | too few (4/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put writing · walls same · mid walls | 3 | 100% | +0.57% | +0.24 to +0.85% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 50% of 2 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.11% | +0.01 to +0.21% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 50% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 2 | 0% | -0.68% | -0.68 to -0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 2 | 50% | +0.24% | -0.07 to +0.54% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.45% | +0.15 to +0.76% | 100% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 1 | 100% | +0.16% | +0.16 to +0.16% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · near call wall | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 1 | 100% | +0.72% | +0.72 to +0.72% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.12% | +0.12 to +0.12% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.36% | +0.36 to +0.36% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% | 100% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 0% | -0.34% | -0.34 to -0.34% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 44 | 72% | +0.13% | up |
| intraday | weekly | call writers stronger · weak puts | 31 | 86% | +0.38% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | weekly | writers even · few weak writers | 18 | 31% | -0.36% | no clear direction |
| intraday | monthly | writers even · weak puts | 17 | 82% | +0.42% | up |
| intraday | weekly | writers even · weak puts | 17 | 81% | +0.32% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides | 3 | 100% | +0.30% | too few (3/10) |
| intraday | weekly | writers even · weak calls | 2 | 100% | +0.16% | too few (1/10) |
| day | monthly | writers even · few weak writers | 5 | 25% | -0.08% | too few (4/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · few weak writers | 2 | 0% | -0.39% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.05% | too few (1/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +0.68% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 18 | 88% | +0.27% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 11 | 90% | +0.32% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 8 | 57% | +0.20% | too few (7/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 7 | 43% | -0.11% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 7 | 14% | -0.40% | too few (7/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 7 | 86% | +0.33% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 6 | 40% | -0.42% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 3 | 0% | -0.20% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 2 | 100% | +0.16% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 2 | 100% | +0.27% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.27% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.05% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.05% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
