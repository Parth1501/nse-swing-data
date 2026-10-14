# Nifty option chain pattern log
Updated 2026-10-14 14:36 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 14 snapshots over 1 trading days
- 14 patterns logged; 13 different patterns so far

## Latest read (2026-10-14 14:14:01)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 5.0 | 22625 | 0.805 | 22650 | 22500 | 23000 | ±1.29% (22333-22917) | 13.41 |
| 2026-10-27 (monthly) | 13.1 | 22619 | 1.008 | 23000 | 22000 | 23500 | ±2.07% (22151-23087) | 13.4 |

- **Weekly, last 30 min**: `PCR up · put writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 4 times before; Nifty was up after it 50% of the time, average -0.11%. Too few outcomes (4/20) to trade on.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · unwinding · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · few weak writers`. Seen 6 times before; Nifty was up after it 33% of the time, average -0.25%. Too few outcomes (6/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `call writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 22700, strongest put writers at 22600; weakest call writers at 22300, weakest put writers at 22750. Covers 26% of near-money call OI and 18% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 13903 | 6261 | 366.6 | 22619 | 356.8 | 22667 | +42 | +9.9 | weak |
| Call | 22350 | 3462 | 307 | 303.4 | 22592 | 316.4 | 22653 | +29 | -13.0 | weak |
| Call | 22400 | 17278 | 2666 | 268.7 | 22597 | 277.7 | 22669 | +44 | -9.0 | weak |
| Call | 22450 | 7231 | 2948 | 232.2 | 22594 | 242.4 | 22682 | +58 | -10.3 | medium |
| Call | 22500 | 59876 | 18859 | 195.5 | 22585 | 207.8 | 22695 | +71 | -12.3 | medium |
| Call | 22550 | 25046 | 17272 | 167.9 | 22590 | 176.3 | 22718 | +93 | -8.4 | medium |
| Call | 22600 | 72780 | 43392 | 140.7 | 22587 | 148.2 | 22741 | +116 | -7.5 | strong |
| Call | 22650 | 62556 | 36669 | 126.7 | 22607 | 123.2 | 22777 | +152 | +3.5 | strong |
| Call | 22700 | 178405 | 54974 | 110.8 | 22620 | 101.1 | 22811 | +186 | +9.7 | strong |
| Call | 22750 | 78918 | 12467 | 110.5 | 22671 | 81.8 | 22861 | +236 | +28.8 | strong |
| Call | 22800 | 130291 | 32265 | 77.2 | 22631 | 65.7 | 22877 | +253 | +11.6 | strong |
| Call | 22850 | 55164 | 11742 | 73.1 | 22684 | 52.1 | 22923 | +298 | +21.0 | strong |
| Call | 22900 | 100800 | 30665 | 46.6 | 22618 | 41.0 | 22947 | +322 | +5.6 | strong |
| Call | 22950 | 74606 | 8342 | 39.5 | 22661 | 32.0 | 22989 | +365 | +7.4 | strong |
| Put | 22300 | 85445 | 13622 | 44.0 | 22661 | 51.3 | 22256 | +369 | -7.3 | strong |
| Put | 22350 | 36081 | 11768 | 47.0 | 22681 | 61.0 | 22303 | +322 | -14.0 | strong |
| Put | 22400 | 76962 | 14154 | 57.4 | 22678 | 72.8 | 22343 | +282 | -15.4 | strong |
| Put | 22450 | 43371 | 4757 | 78.5 | 22651 | 86.2 | 22371 | +253 | -7.7 | strong |
| Put | 22500 | 143150 | 17552 | 81.0 | 22683 | 102.8 | 22419 | +206 | -21.8 | strong |
| Put | 22550 | 64584 | 15188 | 112.4 | 22637 | 121.8 | 22438 | +187 | -9.5 | strong |
| Put | 22600 | 115430 | 23577 | 123.3 | 22666 | 143.7 | 22477 | +148 | -20.4 | strong |
| Put | 22650 | 61519 | 17624 | 153.4 | 22652 | 168.3 | 22497 | +128 | -14.9 | strong |
| Put | 22700 | 95003 | 12630 | 135.5 | 22722 | 195.3 | 22565 | +60 | -59.8 | medium |
| Put | 22750 | 19996 | 5763 | 164.9 | 22712 | 226.6 | 22585 | +40 | -61.7 | weak |
| Put | 22800 | 30691 | 4114 | 192.8 | 22712 | 259.6 | 22607 | +17 | -66.9 | weak |
| Put | 22850 | 7375 | 855 | 208.9 | 22730 | 295.7 | 22641 | -16 | -86.8 | weak |
| Put | 22900 | 9295 | 548 | 241.0 | 22729 | 334.6 | 22659 | -34 | -93.6 | weak |
| Put | 22950 | 2775 | 219 | 327.9 | 22675 | 375.8 | 22622 | +3 | -47.8 | weak |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at -, weakest put writers at 22900. Covers 11% of near-money call OI and 5% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 17188 | 20 | 455.1 | 22616 | 455.1 | 22755 | +136 | -0.1 | strong |
| Call | 22350 | 1312 | 9 | 382.5 | 22560 | 415.6 | 22732 | +114 | -33.1 | strong |
| Call | 22400 | 20923 | 66 | 355.4 | 22576 | 384.1 | 22755 | +137 | -28.7 | strong |
| Call | 22450 | 2096 | 378 | 339.7 | 22604 | 347.1 | 22790 | +171 | -7.5 | strong |
| Call | 22500 | 51651 | 2856 | 297.6 | 22586 | 314.8 | 22798 | +179 | -17.2 | strong |
| Call | 22550 | 4697 | 1150 | 275.7 | 22600 | 283.3 | 22826 | +207 | -7.6 | strong |
| Call | 22600 | 42708 | 8053 | 243.1 | 22591 | 254.2 | 22843 | +224 | -11.2 | strong |
| Call | 22650 | 6530 | 1619 | 221.6 | 22595 | 228.0 | 22872 | +253 | -6.5 | strong |
| Call | 22700 | 63936 | 11365 | 203.5 | 22613 | 201.9 | 22903 | +285 | +1.6 | strong |
| Call | 22750 | 10947 | 1687 | 189.1 | 22634 | 178.9 | 22939 | +320 | +10.2 | strong |
| Call | 22800 | 67543 | 9466 | 167.7 | 22636 | 157.0 | 22968 | +349 | +10.7 | strong |
| Call | 22850 | 6630 | 455 | 173.3 | 22712 | 138.4 | 23023 | +405 | +34.9 | strong |
| Call | 22900 | 29155 | 3664 | 134.8 | 22658 | 120.3 | 23035 | +416 | +14.5 | strong |
| Call | 22950 | 4777 | 722 | 129.7 | 22701 | 104.2 | 23080 | +461 | +25.5 | strong |
| Put | 22300 | 61505 | 364 | 111.3 | 22628 | 114.2 | 22189 | +430 | -2.9 | strong |
| Put | 22350 | 6227 | 451 | 109.2 | 22673 | 126.7 | 22241 | +378 | -17.4 | strong |
| Put | 22400 | 31841 | 1254 | 123.7 | 22671 | 140.6 | 22276 | +342 | -16.9 | strong |
| Put | 22450 | 4604 | 693 | 147.9 | 22638 | 156.2 | 22302 | +317 | -8.2 | strong |
| Put | 22500 | 75797 | 2130 | 146.1 | 22685 | 173.3 | 22354 | +265 | -27.2 | strong |
| Put | 22550 | 6025 | 1100 | 182.1 | 22641 | 191.4 | 22368 | +251 | -9.3 | strong |
| Put | 22600 | 40280 | 5474 | 212.8 | 22619 | 213.9 | 22387 | +232 | -1.1 | strong |
| Put | 22650 | 5771 | 821 | 215.8 | 22657 | 234.9 | 22434 | +184 | -19.2 | strong |
| Put | 22700 | 53212 | 6713 | 250.7 | 22635 | 261.1 | 22449 | +169 | -10.3 | strong |
| Put | 22750 | 5862 | 561 | 228.7 | 22714 | 285.4 | 22521 | +97 | -56.6 | medium |
| Put | 22800 | 39257 | 2763 | 287.1 | 22662 | 314.2 | 22513 | +106 | -27.1 | strong |
| Put | 22850 | 2947 | 256 | 343.9 | 22621 | 349.3 | 22506 | +113 | -5.4 | strong |
| Put | 22900 | 11522 | 1049 | 326.4 | 22688 | 376.4 | 22574 | +45 | -50.0 | weak |
| Put | 22950 | 1241 | 220 | 363.3 | 22684 | 409.3 | 22587 | +32 | -46.0 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.42% | -0.46 to -0.38% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.49% | -0.49 to -0.49% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.46% | -0.46 to -0.46% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.41% | -0.41 to -0.41% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.36% | -0.36 to -0.36% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | call writers stronger · few weak writers | 7 | 33% | -0.25% | too few (6/10) |
| intraday | weekly | call writers stronger · few weak writers | 5 | 50% | -0.11% | too few (4/10) |
| intraday | weekly | writers even · few weak writers | 2 | 0% | -0.42% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
