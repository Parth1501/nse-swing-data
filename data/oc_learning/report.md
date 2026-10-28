# Nifty option chain pattern log
Updated 2026-10-28 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 239 snapshots over 10 trading days
- 258 patterns logged; 112 different patterns so far

## Latest read (2026-10-28 12:42:45)

Nifty trend: weekly **bearish**, 125-min **sideways**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-03 (weekly) | 6.1 | 22715 | 0.844 | 22650 | 20050 | 23000 | ±1.62% (22347-23083) | 15.93 |
| 2026-11-23 (monthly) | 26.1 | 22716 | 1.185 | 23000 | 22000 | 23500 | ±3.35% (21955-23476) | 15.74 |

- **Weekly, last 30 min**: `PCR down · unwinding · walls same · near call wall`. Seen 3 times before; Nifty was up after it 100% of the time, average +0.24%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 25 times before; Nifty was up after it 38% of the time, average -0.21%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 13 times before; Nifty was up after it 46% of the time, average -0.11%. Too few outcomes (13/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.39%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · quiet OI · walls same · mid walls`. Seen 7 times before; Nifty was up after it 100% of the time, average +0.43%. Too few outcomes (5/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 61 times before; Nifty was up after it 70% of the time, average +0.13%. History points to a bull call debit spread, ATM to about the call wall 23500.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 31 times before; Nifty was up after it 73% of the time, average +0.19%. History points to a bull call debit spread, ATM to about the call wall 23500.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · mid walls`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.24%. Too few outcomes (2/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 5 times before; Nifty was up after it 20% of the time, average -0.08%. Too few outcomes (5/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m sideways`: Seen 1 times before; Nifty was up after it 0% of the time, average -0.02%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-11-03

Strongest call writers at 23000, strongest put writers at 22600; weakest call writers at 22500, weakest put writers at -. Covers 59% of near-money call OI and 53% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 13744 | 7141 | 295.8 | 22576 | 367.1 | 22696 | -20 | -71.3 | weak |
| Call | 22450 | 6035 | 5117 | 265.2 | 22575 | 331.1 | 22715 | -0 | -65.9 | weak |
| Call | 22500 | 44927 | 34263 | 238.1 | 22578 | 296.0 | 22738 | +23 | -57.9 | weak |
| Call | 22550 | 29016 | 27917 | 218.4 | 22593 | 262.6 | 22768 | +53 | -44.1 | medium |
| Call | 22600 | 92011 | 83003 | 201.1 | 22610 | 231.6 | 22801 | +86 | -30.5 | medium |
| Call | 22650 | 51205 | 46277 | 175.7 | 22614 | 203.3 | 22826 | +110 | -27.6 | strong |
| Call | 22700 | 114999 | 72917 | 146.1 | 22593 | 175.9 | 22846 | +131 | -29.8 | strong |
| Call | 22750 | 38492 | 23225 | 124.8 | 22591 | 151.2 | 22875 | +159 | -26.4 | strong |
| Call | 22800 | 95172 | 39085 | 109.5 | 22597 | 128.8 | 22909 | +194 | -19.3 | strong |
| Call | 22850 | 32596 | 21275 | 95.8 | 22606 | 108.7 | 22946 | +231 | -12.8 | strong |
| Call | 22900 | 68181 | 37766 | 80.0 | 22602 | 90.7 | 22980 | +265 | -10.6 | strong |
| Call | 22950 | 47324 | 39482 | 70.8 | 22620 | 74.7 | 23021 | +306 | -3.8 | strong |
| Call | 23000 | 153970 | 77592 | 55.5 | 22598 | 61.5 | 23056 | +340 | -6.0 | strong |
| Call | 23050 | 27475 | 12555 | 46.6 | 22616 | 49.8 | 23097 | +381 | -3.2 | strong |
| Put | 22400 | 70463 | 38229 | 115.9 | 22616 | 83.0 | 22284 | +431 | +32.9 | strong |
| Put | 22450 | 29169 | 21628 | 143.6 | 22598 | 96.7 | 22306 | +409 | +47.0 | strong |
| Put | 22500 | 122107 | 77455 | 161.9 | 22599 | 111.6 | 22338 | +377 | +50.4 | strong |
| Put | 22550 | 57253 | 49387 | 178.6 | 22611 | 128.7 | 22371 | +344 | +49.9 | strong |
| Put | 22600 | 121500 | 91354 | 198.9 | 22613 | 148.0 | 22401 | +314 | +50.9 | strong |
| Put | 22650 | 47100 | 38863 | 202.7 | 22640 | 169.1 | 22447 | +268 | +33.5 | strong |
| Put | 22700 | 71543 | 19954 | 241.3 | 22622 | 192.2 | 22459 | +257 | +49.0 | strong |
| Put | 22750 | 15628 | 4481 | 230.8 | 22681 | 217.2 | 22519 | +196 | +13.6 | strong |
| Put | 22800 | 42180 | 833 | 298.0 | 22610 | 244.4 | 22502 | +213 | +53.5 | strong |
| Put | 22850 | 4478 | 735 | 343.5 | 22600 | 275.6 | 22507 | +209 | +67.8 | strong |
| Put | 22900 | 13074 | 2240 | 343.2 | 22648 | 306.0 | 22557 | +158 | +37.2 | strong |
| Put | 22950 | 2089 | 564 | 444.8 | 22579 | 340.2 | 22505 | +210 | +104.6 | strong |
| Put | 23000 | 30297 | 12164 | 494.8 | 22572 | 376.8 | 22505 | +210 | +118.1 | strong |
| Put | 23050 | 1714 | 605 | 492.5 | 22617 | 415.4 | 22557 | +158 | +77.1 | strong |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23150. Covers 72% of near-money call OI and 69% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 3786 | 2859 | 553.0 | 22525 | 594.0 | 22953 | +237 | -41.0 | strong |
| Call | 22450 | 709 | 656 | 569.1 | 22596 | 561.3 | 23019 | +304 | +7.8 | strong |
| Call | 22500 | 36819 | 28456 | 524.7 | 22603 | 530.0 | 23025 | +309 | -5.3 | strong |
| Call | 22550 | 1573 | 1501 | 490.3 | 22615 | 494.4 | 23040 | +325 | -4.1 | strong |
| Call | 22600 | 35658 | 30410 | 454.4 | 22616 | 467.2 | 23054 | +339 | -12.8 | strong |
| Call | 22650 | 4522 | 4321 | 457.0 | 22611 | 437.0 | 23107 | +391 | +20.0 | strong |
| Call | 22700 | 48676 | 45906 | 450.4 | 22690 | 408.7 | 23150 | +435 | +41.7 | strong |
| Call | 22750 | 2873 | 2353 | 403.9 | 22662 | 381.6 | 23154 | +438 | +22.3 | strong |
| Call | 22800 | 29014 | 25069 | 403.3 | 22692 | 352.8 | 23203 | +488 | +50.5 | strong |
| Call | 22850 | 1677 | 1300 | 363.5 | 22683 | 330.0 | 23213 | +498 | +33.5 | strong |
| Call | 22900 | 15032 | 12526 | 358.8 | 22701 | 306.7 | 23259 | +543 | +52.1 | strong |
| Call | 22950 | 1737 | 1041 | 339.0 | 22712 | 280.1 | 23289 | +573 | +58.9 | strong |
| Call | 23000 | 103943 | 62521 | 294.2 | 22656 | 261.0 | 23294 | +579 | +33.2 | strong |
| Call | 23050 | 1638 | 618 | 271.9 | 22678 | 237.9 | 23322 | +606 | +34.0 | strong |
| Put | 22400 | 19503 | 8658 | 264.5 | 22661 | 240.2 | 22136 | +580 | +24.2 | strong |
| Put | 22450 | 1258 | 945 | 293.6 | 22621 | 259.1 | 22156 | +559 | +34.6 | strong |
| Put | 22500 | 69771 | 44311 | 294.0 | 22675 | 273.1 | 22206 | +510 | +20.9 | strong |
| Put | 22550 | 1914 | 1630 | 320.0 | 22644 | 290.2 | 22230 | +486 | +29.8 | strong |
| Put | 22600 | 36998 | 30908 | 348.0 | 22633 | 309.9 | 22252 | +464 | +38.1 | strong |
| Put | 22650 | 5413 | 4970 | 354.6 | 22644 | 330.0 | 22295 | +420 | +24.6 | strong |
| Put | 22700 | 55896 | 50054 | 356.1 | 22705 | 351.8 | 22344 | +372 | +4.4 | strong |
| Put | 22750 | 4235 | 3920 | 341.7 | 22755 | 375.2 | 22408 | +307 | -33.5 | strong |
| Put | 22800 | 30646 | 22804 | 398.0 | 22702 | 398.3 | 22402 | +314 | -0.3 | strong |
| Put | 22850 | 2183 | 865 | 395.6 | 22748 | 422.2 | 22454 | +261 | -26.6 | strong |
| Put | 22900 | 17061 | 13822 | 436.6 | 22711 | 447.5 | 22463 | +252 | -10.9 | strong |
| Put | 22950 | 698 | 419 | 434.0 | 22750 | 475.3 | 22516 | +200 | -41.3 | strong |
| Put | 23000 | 88298 | 52057 | 485.0 | 22728 | 500.0 | 22515 | +201 | -15.0 | strong |
| Put | 23050 | 655 | 341 | 472.9 | 22776 | 530.4 | 22577 | +138 | -57.5 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 18 | 67% | +0.14% | -0.44 to +0.76% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · near call wall | 9 | 100% | +0.29% | +0.03 to +0.51% | 50% of 2 | too few (9/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 8 | 100% | +0.43% | +0.27 to +0.70% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 7 | 86% | +0.15% | -0.21 to +0.46% | 100% of 1 | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 7 | 86% | +0.32% | -0.39 to +0.91% | 100% of 1 | too few (7/10) |
| weekly | PCR up · put writing · walls same · near put wall | 7 | 57% | -0.03% | -0.47 to +0.41% | 50% of 2 | too few (7/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 6 | 33% | +0.07% | -0.40 to +0.90% | 100% of 2 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 6 | 75% | +0.19% | -0.12 to +0.78% | 100% of 1 | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.29% | -0.24 to +0.70% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 5 | 100% | +0.44% | +0.09 to +1.02% | 100% of 1 | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (5/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 5 | 40% | +0.04% | -0.78 to +0.90% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near put wall | 5 | 80% | +0.35% | -0.37 to +0.85% | 50% of 2 | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 4 | 100% | +0.24% | +0.14 to +0.32% | 50% of 2 | too few (3/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% | 100% of 1 | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% | 100% of 1 | too few (4/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 4 | 67% | +0.06% | -0.05 to +0.15% | 50% of 2 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · mid walls | 3 | 67% | +0.23% | -0.07 to +0.54% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 3 | 33% | -0.10% | -0.68 to +0.41% | 100% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 3 | 67% | +0.16% | -0.02 to +0.37% | 100% of 1 | too few (3/10) |
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
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 2 | 50% | +0.02% | -0.22 to +0.26% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 2 | 100% | +0.23% | +0.13 to +0.33% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 2 | too few (0/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% | 100% of 1 | too few (2/10) |
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
| monthly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.22% | +0.22 to +0.22% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
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
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 1 | 100% | +0.72% | +0.72 to +0.72% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.70% | +0.70 to +0.70% |  | too few (1/10) |
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
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 0% | -0.24% | -0.34 to -0.15% | 100% of 1 | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.15% | -0.15 to -0.15% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 62 | 70% | +0.13% | up |
| intraday | weekly | call writers stronger · weak puts | 32 | 87% | +0.38% | up |
| intraday | weekly | writers even · few weak writers | 26 | 38% | -0.21% | no clear direction |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.46% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | weekly | call writers stronger · few weak writers | 15 | 64% | +0.20% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | weekly | writers even · weak on both sides | 5 | 100% | +0.25% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak calls | 4 | 33% | -0.06% | too few (3/10) |
| day | monthly | writers even · few weak writers | 6 | 20% | -0.08% | too few (5/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · few weak writers | 2 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.26% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 | 0% | -0.02% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 32 | 73% | +0.19% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 18 | 76% | +0.13% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 14 | 46% | -0.11% | no clear direction |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 12 | 73% | +0.35% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 11 | 60% | +0.04% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 7 | 14% | -0.40% | too few (7/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.18% | too few (5/10) |
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
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 1 | 0% | -0.15% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.15% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
