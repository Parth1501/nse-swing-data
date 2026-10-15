# Nifty option chain pattern log
Updated 2026-10-15 09:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 23 snapshots over 2 trading days
- 24 patterns logged; 21 different patterns so far

## Latest read (2026-10-15 09:45:29)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 4.2 | 22762 | 0.895 | 22700 | 22700 | 23000 | ±1.14% (22503-23021) | 13.66 |
| 2026-10-27 (monthly) | 12.2 | 22765 | 0.873 | 23000 | 22000 | 23500 | ±1.98% (22313-23216) | 13.62 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, today vs previous day**: `PCR down · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 22800, strongest put writers at 22700; weakest call writers at 22700, weakest put writers at 23200. Covers 32% of near-money call OI and 50% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22450 | 5606 | 2370 | 232.6 | 22595 | 331.4 | 22683 | -79 | -98.8 | weak |
| Call | 22500 | 43724 | 14199 | 195.9 | 22587 | 291.0 | 22696 | -66 | -95.1 | weak |
| Call | 22550 | 15108 | 10871 | 168.4 | 22594 | 252.8 | 22718 | -43 | -84.3 | weak |
| Call | 22600 | 56990 | 37775 | 141.5 | 22595 | 218.0 | 22741 | -20 | -76.5 | weak |
| Call | 22650 | 40452 | 25291 | 125.8 | 22608 | 185.2 | 22776 | +14 | -59.4 | weak |
| Call | 22700 | 135498 | 43043 | 110.2 | 22620 | 152.2 | 22810 | +48 | -42.0 | weak |
| Call | 22750 | 85669 | 34613 | 117.3 | 22721 | 126.6 | 22867 | +105 | -9.3 | strong |
| Call | 22800 | 132533 | 52049 | 87.6 | 22689 | 101.8 | 22888 | +126 | -14.2 | strong |
| Call | 22850 | 59024 | 22351 | 74.2 | 22715 | 79.5 | 22924 | +162 | -5.3 | strong |
| Call | 22900 | 103313 | 39404 | 50.4 | 22657 | 61.4 | 22950 | +189 | -10.9 | strong |
| Call | 22950 | 50449 | 7419 | 41.7 | 22688 | 47.8 | 22992 | +230 | -6.0 | strong |
| Call | 23000 | 161766 | 41958 | 29.1 | 22621 | 36.0 | 23029 | +267 | -6.9 | strong |
| Call | 23050 | 40784 | 18046 | 24.6 | 22669 | 26.4 | 23075 | +313 | -1.9 | strong |
| Call | 23100 | 88442 | 13328 | 18.9 | 22715 | 19.9 | 23119 | +357 | -1.0 | strong |
| Put | 22450 | 49824 | 20186 | 47.6 | 22742 | 40.8 | 22402 | +360 | +6.8 | strong |
| Put | 22500 | 155931 | 63233 | 57.0 | 22746 | 50.8 | 22443 | +319 | +6.2 | strong |
| Put | 22550 | 55514 | 24769 | 81.5 | 22714 | 62.5 | 22468 | +293 | +19.1 | strong |
| Put | 22600 | 120557 | 54070 | 90.5 | 22732 | 75.4 | 22509 | +252 | +15.1 | strong |
| Put | 22650 | 72439 | 50367 | 102.3 | 22742 | 91.3 | 22548 | +214 | +10.9 | strong |
| Put | 22700 | 163731 | 108635 | 114.0 | 22759 | 112.2 | 22586 | +176 | +1.8 | strong |
| Put | 22750 | 63302 | 54418 | 134.7 | 22759 | 132.6 | 22615 | +147 | +2.1 | strong |
| Put | 22800 | 70554 | 50267 | 160.9 | 22759 | 158.8 | 22639 | +123 | +2.1 | strong |
| Put | 22850 | 12522 | 7818 | 190.9 | 22759 | 188.8 | 22659 | +103 | +2.1 | strong |
| Put | 22900 | 14580 | 7523 | 223.8 | 22758 | 221.2 | 22676 | +86 | +2.6 | medium |
| Put | 22950 | 3657 | 1276 | 270.2 | 22743 | 254.3 | 22680 | +82 | +15.8 | medium |
| Put | 23000 | 16835 | 4870 | 302.0 | 22747 | 292.2 | 22698 | +64 | +9.8 | medium |
| Put | 23050 | 1688 | 543 | 362.7 | 22729 | 335.6 | 22687 | +75 | +27.1 | medium |
| Put | 23100 | 3679 | 266 | 443.9 | 22686 | 378.2 | 22656 | +106 | +65.7 | strong |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at 22500, weakest put writers at 23350. Covers 17% of near-money call OI and 12% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22450 | 1666 | 355 | 340.1 | 22608 | 434.0 | 22790 | +26 | -93.8 | weak |
| Call | 22500 | 51436 | 5324 | 303.8 | 22604 | 401.2 | 22804 | +39 | -97.4 | weak |
| Call | 22550 | 3674 | 985 | 276.2 | 22602 | 365.4 | 22826 | +62 | -89.2 | medium |
| Call | 22600 | 42257 | 11166 | 245.7 | 22602 | 331.4 | 22846 | +81 | -85.7 | medium |
| Call | 22650 | 5342 | 1332 | 221.8 | 22596 | 299.5 | 22872 | +107 | -77.7 | strong |
| Call | 22700 | 65941 | 13493 | 208.3 | 22626 | 269.3 | 22908 | +144 | -61.0 | strong |
| Call | 22750 | 10339 | 1615 | 189.3 | 22635 | 240.7 | 22939 | +175 | -51.4 | strong |
| Call | 22800 | 66176 | 11225 | 175.6 | 22659 | 212.9 | 22976 | +211 | -37.3 | strong |
| Call | 22850 | 6449 | 583 | 163.9 | 22689 | 188.0 | 23014 | +249 | -24.1 | strong |
| Call | 22900 | 36665 | 11306 | 125.1 | 22640 | 165.0 | 23025 | +260 | -39.9 | strong |
| Call | 22950 | 4385 | 696 | 128.5 | 22698 | 143.9 | 23079 | +314 | -15.4 | strong |
| Call | 23000 | 126241 | 19199 | 103.2 | 22659 | 126.2 | 23103 | +339 | -22.9 | strong |
| Call | 23050 | 5591 | 1783 | 83.0 | 22641 | 108.3 | 23133 | +368 | -25.3 | strong |
| Call | 23100 | 32605 | 3572 | 73.4 | 22651 | 92.8 | 23173 | +409 | -19.4 | strong |
| Put | 22450 | 4354 | 762 | 141.5 | 22659 | 109.2 | 22308 | +456 | +32.3 | strong |
| Put | 22500 | 77935 | 5945 | 145.7 | 22687 | 122.1 | 22354 | +410 | +23.6 | strong |
| Put | 22550 | 5947 | 1192 | 178.1 | 22652 | 136.8 | 22372 | +393 | +41.3 | strong |
| Put | 22600 | 43230 | 8755 | 210.0 | 22620 | 152.0 | 22390 | +375 | +58.0 | strong |
| Put | 22650 | 6312 | 1427 | 204.8 | 22680 | 169.2 | 22445 | +319 | +35.6 | strong |
| Put | 22700 | 58500 | 12844 | 222.0 | 22695 | 189.2 | 22478 | +287 | +32.9 | strong |
| Put | 22750 | 8257 | 3294 | 213.6 | 22756 | 210.5 | 22536 | +228 | +3.1 | strong |
| Put | 22800 | 38721 | 4835 | 262.7 | 22708 | 232.8 | 22537 | +227 | +29.9 | strong |
| Put | 22850 | 4106 | 1415 | 326.0 | 22650 | 258.6 | 22524 | +241 | +67.4 | strong |
| Put | 22900 | 12105 | 1856 | 308.2 | 22722 | 285.6 | 22592 | +173 | +22.5 | strong |
| Put | 22950 | 1240 | 243 | 358.5 | 22692 | 315.0 | 22592 | +173 | +43.5 | strong |
| Put | 23000 | 60715 | 7982 | 421.7 | 22656 | 347.9 | 22578 | +186 | +73.8 | strong |
| Put | 23050 | 743 | 29 | 390.6 | 22749 | 381.6 | 22659 | +105 | +9.0 | strong |
| Put | 23100 | 22510 | 151 | 460.6 | 22697 | 421.0 | 22639 | +125 | +39.5 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.44% | -0.44 to -0.44% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | -0.10% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | -0.00% | too few (8/10) |
| intraday | weekly | writers even · few weak writers | 2 | 0% | -0.43% | too few (2/10) |
| intraday | monthly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| intraday | weekly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +0.63% | too few (1/10) |
| day | monthly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +0.63% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
