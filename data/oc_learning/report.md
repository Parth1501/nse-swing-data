# Nifty option chain pattern log
Updated 2026-10-14 14:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 16 snapshots over 1 trading days
- 16 patterns logged; 15 different patterns so far

## Latest read (2026-10-14 14:45:21)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 5.0 | 22617 | 0.803 | 22650 | 22500 | 23000 | ±1.25% (22333-22900) | 13.2 |
| 2026-10-27 (monthly) | 13.0 | 22619 | 1.007 | 23000 | 22000 | 23500 | ±2.03% (22160-23078) | 13.25 |

- **Weekly, last 30 min**: `PCR flat · unwinding · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 5 times before; Nifty was up after it 40% of the time, average -0.12%. Too few outcomes (5/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 7 times before; Nifty was up after it 43% of the time, average -0.21%. Too few outcomes (7/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 22700, strongest put writers at 22600; weakest call writers at 22000, weakest put writers at 22750. Covers 29% of near-money call OI and 18% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 13772 | 6202 | 366.6 | 22619 | 357.1 | 22667 | +50 | +9.5 | medium |
| Call | 22350 | 3544 | 389 | 306.0 | 22597 | 315.6 | 22656 | +39 | -9.6 | weak |
| Call | 22400 | 17493 | 2881 | 269.4 | 22599 | 277.4 | 22669 | +53 | -8.0 | medium |
| Call | 22450 | 7420 | 3137 | 232.6 | 22595 | 239.8 | 22683 | +66 | -7.2 | medium |
| Call | 22500 | 60744 | 19727 | 195.9 | 22587 | 205.5 | 22696 | +79 | -9.6 | medium |
| Call | 22550 | 26632 | 18858 | 168.4 | 22592 | 174.3 | 22718 | +102 | -5.9 | strong |
| Call | 22600 | 82471 | 53083 | 141.6 | 22592 | 145.6 | 22742 | +125 | -4.0 | strong |
| Call | 22650 | 69070 | 43183 | 125.8 | 22608 | 121.0 | 22776 | +159 | +4.8 | strong |
| Call | 22700 | 180896 | 57465 | 110.2 | 22620 | 98.5 | 22810 | +194 | +11.7 | strong |
| Call | 22750 | 83631 | 17180 | 102.1 | 22656 | 79.8 | 22852 | +236 | +22.3 | strong |
| Call | 22800 | 133040 | 35014 | 76.1 | 22630 | 63.5 | 22876 | +260 | +12.7 | strong |
| Call | 22850 | 57334 | 13912 | 69.5 | 22674 | 50.2 | 22920 | +303 | +19.3 | strong |
| Call | 22900 | 101700 | 31565 | 46.4 | 22618 | 39.4 | 22946 | +330 | +7.0 | strong |
| Call | 22950 | 73436 | 8211 | 39.5 | 22661 | 30.8 | 22989 | +373 | +8.7 | strong |
| Put | 22300 | 80523 | 12837 | 44.0 | 22661 | 47.1 | 22256 | +361 | -3.2 | strong |
| Put | 22350 | 34713 | 11322 | 47.0 | 22681 | 56.9 | 22303 | +314 | -9.9 | strong |
| Put | 22400 | 74789 | 13755 | 57.4 | 22678 | 68.2 | 22343 | +274 | -10.8 | strong |
| Put | 22450 | 41850 | 4590 | 78.5 | 22651 | 81.6 | 22371 | +245 | -3.0 | strong |
| Put | 22500 | 137792 | 16896 | 81.0 | 22683 | 97.3 | 22419 | +198 | -16.3 | strong |
| Put | 22550 | 61295 | 14414 | 112.4 | 22637 | 116.3 | 22438 | +179 | -3.9 | strong |
| Put | 22600 | 110795 | 22631 | 123.3 | 22666 | 137.8 | 22477 | +140 | -14.6 | strong |
| Put | 22650 | 56890 | 16298 | 153.4 | 22652 | 161.8 | 22497 | +120 | -8.3 | strong |
| Put | 22700 | 89442 | 11891 | 135.5 | 22722 | 189.6 | 22565 | +52 | -54.1 | medium |
| Put | 22750 | 18088 | 5214 | 164.9 | 22712 | 220.6 | 22585 | +31 | -55.6 | weak |
| Put | 22800 | 29866 | 4003 | 192.8 | 22712 | 254.9 | 22607 | +9 | -62.1 | weak |
| Put | 22850 | 7425 | 905 | 213.5 | 22724 | 290.9 | 22637 | -20 | -77.5 | weak |
| Put | 22900 | 9420 | 673 | 257.4 | 22708 | 329.2 | 22643 | -26 | -71.9 | weak |
| Put | 22950 | 2823 | 267 | 335.7 | 22665 | 370.9 | 22614 | +2 | -35.2 | weak |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at -, weakest put writers at 22900. Covers 14% of near-money call OI and 7% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 17152 | 20 | 455.1 | 22616 | 452.2 | 22755 | +136 | +2.9 | strong |
| Call | 22350 | 1312 | 9 | 382.5 | 22560 | 418.0 | 22732 | +113 | -35.5 | strong |
| Call | 22400 | 20707 | 66 | 355.4 | 22576 | 379.2 | 22755 | +136 | -23.8 | strong |
| Call | 22450 | 1689 | 304 | 339.7 | 22604 | 343.2 | 22790 | +170 | -3.6 | strong |
| Call | 22500 | 52040 | 3245 | 299.1 | 22590 | 310.4 | 22799 | +180 | -11.3 | strong |
| Call | 22550 | 4846 | 1299 | 276.2 | 22602 | 279.5 | 22826 | +207 | -3.3 | strong |
| Call | 22600 | 43724 | 9069 | 243.9 | 22595 | 250.6 | 22844 | +225 | -6.7 | strong |
| Call | 22650 | 6512 | 1615 | 221.6 | 22595 | 223.7 | 22872 | +252 | -2.1 | strong |
| Call | 22700 | 63833 | 11347 | 203.5 | 22613 | 198.2 | 22903 | +284 | +5.3 | strong |
| Call | 22750 | 10951 | 1691 | 189.1 | 22634 | 173.0 | 22939 | +320 | +16.1 | strong |
| Call | 22800 | 66596 | 9333 | 167.7 | 22636 | 153.9 | 22968 | +348 | +13.7 | strong |
| Call | 22850 | 6533 | 448 | 173.3 | 22712 | 134.3 | 23023 | +404 | +38.9 | strong |
| Call | 22900 | 35913 | 10422 | 122.8 | 22633 | 116.3 | 23023 | +404 | +6.5 | strong |
| Call | 22950 | 4684 | 708 | 129.7 | 22701 | 102.7 | 23080 | +460 | +27.0 | strong |
| Put | 22300 | 61539 | 398 | 111.2 | 22628 | 109.7 | 22189 | +430 | +1.5 | strong |
| Put | 22350 | 5966 | 432 | 109.2 | 22673 | 121.8 | 22241 | +378 | -12.6 | strong |
| Put | 22400 | 35330 | 4743 | 132.7 | 22633 | 135.9 | 22267 | +352 | -3.2 | strong |
| Put | 22450 | 4346 | 654 | 147.9 | 22638 | 151.5 | 22302 | +317 | -3.6 | strong |
| Put | 22500 | 76446 | 2779 | 151.3 | 22670 | 168.1 | 22349 | +270 | -16.8 | strong |
| Put | 22550 | 6048 | 1123 | 182.2 | 22640 | 187.4 | 22368 | +251 | -5.2 | strong |
| Put | 22600 | 41067 | 6261 | 212.3 | 22619 | 208.6 | 22388 | +232 | +3.8 | strong |
| Put | 22650 | 5707 | 812 | 215.8 | 22657 | 230.2 | 22434 | +185 | -14.4 | strong |
| Put | 22700 | 53465 | 6966 | 250.9 | 22634 | 255.4 | 22449 | +170 | -4.5 | strong |
| Put | 22750 | 5796 | 555 | 228.7 | 22714 | 282.3 | 22521 | +98 | -53.6 | medium |
| Put | 22800 | 39008 | 2745 | 287.1 | 22662 | 309.6 | 22513 | +106 | -22.4 | strong |
| Put | 22850 | 2955 | 264 | 343.8 | 22621 | 341.0 | 22506 | +113 | +2.8 | strong |
| Put | 22900 | 11465 | 1044 | 326.4 | 22688 | 373.7 | 22574 | +46 | -47.3 | weak |
| Put | 22950 | 1228 | 217 | 363.3 | 22684 | 405.9 | 22587 | +32 | -42.5 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.46% | -0.50 to -0.42% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.48% | -0.48 to -0.48% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.46% | -0.46 to -0.46% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.41% | -0.41 to -0.41% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.00% | +0.00 to +0.00% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.43% | -0.43 to -0.43% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.04% | -0.04 to -0.04% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | call writers stronger · few weak writers | 8 | 43% | -0.21% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers | 6 | 40% | -0.12% | too few (5/10) |
| intraday | weekly | writers even · few weak writers | 2 | 0% | -0.46% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
