# Nifty option chain pattern log
Updated 2026-10-14 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 19 snapshots over 1 trading days
- 20 patterns logged; 17 different patterns so far

## Latest read (2026-10-14 15:40:00)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 5.0 | 22623 | 0.722 | 22600 | 22000 | 23000 | ±1.23% (22343-22902) | 13.07 |
| 2026-10-27 (monthly) | 13.0 | 22623 | 0.974 | 23000 | 22000 | 23500 | ±2.01% (22168-23077) | 13.15 |

- **Weekly, last 30 min**: `PCR flat · unwinding · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 7 times before; Nifty was up after it 43% of the time, average -0.07%. Too few outcomes (7/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put and call writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.02%. Too few outcomes (1/20) to trade on.
  - Writers: `call writers stronger · few weak writers`. Seen 9 times before; Nifty was up after it 44% of the time, average -0.15%. Too few outcomes (9/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 22600, strongest put writers at 22600; weakest call writers at 22300, weakest put writers at 22750. Covers 28% of near-money call OI and 18% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 14057 | 6725 | 364.8 | 22620 | 357.0 | 22665 | +42 | +7.8 | weak |
| Call | 22350 | 3314 | 364 | 306.0 | 22597 | 314.6 | 22656 | +33 | -8.6 | weak |
| Call | 22400 | 16262 | 2868 | 269.4 | 22601 | 275.9 | 22669 | +47 | -6.5 | weak |
| Call | 22450 | 6072 | 2567 | 232.6 | 22595 | 235.2 | 22683 | +60 | -2.6 | medium |
| Call | 22500 | 49845 | 16187 | 195.9 | 22587 | 202.8 | 22696 | +73 | -6.9 | medium |
| Call | 22550 | 21033 | 15135 | 168.4 | 22594 | 173.2 | 22718 | +96 | -4.8 | medium |
| Call | 22600 | 68958 | 45707 | 141.5 | 22595 | 145.8 | 22741 | +119 | -4.4 | strong |
| Call | 22650 | 47000 | 29384 | 125.8 | 22608 | 119.8 | 22776 | +153 | +6.0 | strong |
| Call | 22700 | 141122 | 44830 | 110.2 | 22620 | 98.0 | 22810 | +188 | +12.2 | strong |
| Call | 22750 | 64651 | 13281 | 102.1 | 22656 | 79.0 | 22852 | +229 | +23.2 | strong |
| Call | 22800 | 110657 | 29123 | 76.1 | 22630 | 62.8 | 22876 | +253 | +13.4 | strong |
| Call | 22850 | 48423 | 11750 | 69.5 | 22674 | 49.9 | 22920 | +297 | +19.7 | strong |
| Call | 22900 | 92839 | 28814 | 46.4 | 22618 | 38.9 | 22946 | +324 | +7.5 | strong |
| Call | 22950 | 48638 | 5439 | 39.5 | 22661 | 30.7 | 22989 | +367 | +8.8 | strong |
| Put | 22300 | 71355 | 11376 | 44.0 | 22661 | 42.1 | 22256 | +367 | +1.8 | strong |
| Put | 22350 | 26440 | 8624 | 47.0 | 22681 | 53.0 | 22303 | +320 | -6.0 | strong |
| Put | 22400 | 60457 | 11119 | 57.4 | 22678 | 62.8 | 22343 | +280 | -5.4 | strong |
| Put | 22450 | 33517 | 3676 | 78.5 | 22651 | 76.9 | 22371 | +251 | +1.6 | strong |
| Put | 22500 | 108044 | 13248 | 81.0 | 22683 | 93.0 | 22419 | +204 | -11.9 | strong |
| Put | 22550 | 40483 | 9520 | 112.4 | 22637 | 111.8 | 22438 | +185 | +0.5 | strong |
| Put | 22600 | 84158 | 17190 | 123.3 | 22666 | 133.4 | 22477 | +146 | -10.1 | strong |
| Put | 22650 | 31070 | 8901 | 153.4 | 22652 | 158.0 | 22497 | +126 | -4.6 | strong |
| Put | 22700 | 66171 | 8797 | 135.5 | 22722 | 186.2 | 22565 | +58 | -50.8 | medium |
| Put | 22750 | 12518 | 3608 | 164.9 | 22712 | 217.4 | 22585 | +38 | -52.5 | weak |
| Put | 22800 | 23571 | 3159 | 192.8 | 22712 | 251.3 | 22607 | +15 | -58.6 | weak |
| Put | 22850 | 5357 | 653 | 213.5 | 22724 | 285.2 | 22637 | -14 | -71.8 | weak |
| Put | 22900 | 7603 | 543 | 257.4 | 22708 | 322.6 | 22643 | -20 | -65.2 | weak |
| Put | 22950 | 2634 | 249 | 335.7 | 22665 | 367.6 | 22614 | +8 | -31.9 | weak |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22600; weakest call writers at -, weakest put writers at 22900. Covers 15% of near-money call OI and 8% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 17070 | 20 | 455.1 | 22616 | 451.5 | 22755 | +132 | +3.6 | strong |
| Call | 22350 | 1297 | 11 | 388.7 | 22572 | 415.2 | 22739 | +116 | -26.6 | strong |
| Call | 22400 | 20833 | 268 | 372.6 | 22613 | 380.8 | 22773 | +150 | -8.2 | strong |
| Call | 22450 | 1752 | 373 | 340.1 | 22608 | 343.9 | 22790 | +167 | -3.8 | strong |
| Call | 22500 | 54429 | 5634 | 303.8 | 22604 | 309.5 | 22804 | +181 | -5.7 | strong |
| Call | 22550 | 4683 | 1256 | 276.2 | 22602 | 281.4 | 22826 | +203 | -5.2 | strong |
| Call | 22600 | 47100 | 12445 | 245.7 | 22602 | 250.2 | 22846 | +223 | -4.5 | strong |
| Call | 22650 | 6454 | 1600 | 221.6 | 22595 | 225.0 | 22872 | +249 | -3.5 | strong |
| Call | 22700 | 64957 | 12471 | 203.2 | 22614 | 201.0 | 22903 | +281 | +2.2 | strong |
| Call | 22750 | 10612 | 1638 | 189.1 | 22634 | 175.1 | 22939 | +316 | +14.0 | strong |
| Call | 22800 | 66152 | 9488 | 167.4 | 22636 | 155.2 | 22967 | +345 | +12.2 | strong |
| Call | 22850 | 6690 | 605 | 163.9 | 22689 | 137.6 | 23014 | +391 | +26.3 | strong |
| Call | 22900 | 36123 | 10692 | 122.7 | 22633 | 119.5 | 23023 | +400 | +3.2 | strong |
| Call | 22950 | 4634 | 725 | 128.7 | 22698 | 104.8 | 23079 | +456 | +23.9 | strong |
| Put | 22300 | 60896 | 394 | 111.2 | 22628 | 106.3 | 22189 | +434 | +4.8 | strong |
| Put | 22350 | 5956 | 522 | 110.8 | 22664 | 117.8 | 22239 | +383 | -7.0 | strong |
| Put | 22400 | 36884 | 6297 | 132.8 | 22631 | 134.2 | 22267 | +356 | -1.3 | strong |
| Put | 22450 | 4231 | 637 | 147.9 | 22638 | 146.8 | 22302 | +321 | +1.2 | strong |
| Put | 22500 | 77777 | 4228 | 156.0 | 22654 | 165.1 | 22344 | +279 | -9.1 | strong |
| Put | 22550 | 5861 | 1088 | 182.2 | 22640 | 184.2 | 22368 | +255 | -1.9 | strong |
| Put | 22600 | 43423 | 8794 | 210.0 | 22620 | 204.3 | 22390 | +233 | +5.7 | strong |
| Put | 22650 | 5899 | 1014 | 218.1 | 22650 | 227.0 | 22432 | +191 | -8.9 | strong |
| Put | 22700 | 52826 | 6883 | 250.9 | 22634 | 254.6 | 22449 | +174 | -3.6 | strong |
| Put | 22750 | 5488 | 525 | 228.7 | 22714 | 278.4 | 22521 | +101 | -49.7 | medium |
| Put | 22800 | 38589 | 2786 | 287.6 | 22661 | 307.0 | 22512 | +110 | -19.4 | strong |
| Put | 22850 | 3821 | 1130 | 341.9 | 22623 | 343.3 | 22508 | +115 | -1.4 | strong |
| Put | 22900 | 11309 | 1030 | 326.4 | 22688 | 371.8 | 22574 | +49 | -45.4 | weak |
| Put | 22950 | 1211 | 214 | 363.3 | 22684 | 405.2 | 22587 | +36 | -42.0 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.44% | -0.44 to -0.44% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | call writers stronger · few weak writers | 10 | 44% | -0.15% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers | 8 | 43% | -0.07% | too few (7/10) |
| intraday | weekly | writers even · few weak writers | 2 | 0% | -0.43% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
