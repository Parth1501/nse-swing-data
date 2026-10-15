# Nifty option chain pattern log
Updated 2026-10-15 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 35 snapshots over 2 trading days
- 36 patterns logged; 27 different patterns so far

## Latest read (2026-10-15 12:45:29)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 4.1 | 22990 | 1.184 | 22900 | 22700 | 23000 | ±1.14% (22728-23252) | 13.65 |
| 2026-10-27 (monthly) | 12.1 | 22995 | 0.764 | 23000 | 22000 | 23500 | ±1.96% (22546-23445) | 13.63 |

- **Weekly, last 30 min**: `PCR up · put writing · walls same · near call wall`. Seen 3 times before; Nifty was up after it 100% of the time, average +0.29%. Too few outcomes (3/20) to trade on.
  - Writers: `put writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `PCR up · put writing · walls up · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `put writers stronger · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR down · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 5 times before; Nifty was up after it 100% of the time, average +0.24%. Too few outcomes (5/20) to trade on.
- **Monthly, today vs previous day**: `PCR down · put writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23300, strongest put writers at 22700; weakest call writers at 22900, weakest put writers at -. Covers 38% of near-money call OI and 74% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 19355 | 12101 | 125.8 | 22608 | 380.6 | 22776 | -214 | -254.8 | weak |
| Call | 22700 | 51805 | 16457 | 110.2 | 22620 | 337.9 | 22810 | -180 | -227.7 | weak |
| Call | 22750 | 31466 | 12713 | 117.3 | 22721 | 296.0 | 22867 | -123 | -178.7 | weak |
| Call | 22800 | 58684 | 23047 | 87.6 | 22689 | 255.7 | 22888 | -103 | -168.1 | weak |
| Call | 22850 | 30196 | 11435 | 74.2 | 22715 | 219.1 | 22924 | -66 | -144.9 | weak |
| Call | 22900 | 89335 | 38008 | 66.2 | 22702 | 185.7 | 22966 | -24 | -119.5 | weak |
| Call | 22950 | 53785 | 24802 | 105.4 | 22887 | 152.8 | 23055 | +65 | -47.4 | medium |
| Call | 23000 | 143672 | 49807 | 54.8 | 22734 | 124.2 | 23055 | +65 | -69.4 | medium |
| Call | 23050 | 45088 | 26585 | 49.6 | 22794 | 100.2 | 23100 | +109 | -50.6 | strong |
| Call | 23100 | 91723 | 22318 | 38.1 | 22819 | 78.0 | 23138 | +148 | -39.9 | strong |
| Call | 23150 | 43884 | 16237 | 35.8 | 22839 | 59.9 | 23186 | +196 | -24.0 | strong |
| Call | 23200 | 103895 | 19711 | 13.6 | 22658 | 45.5 | 23214 | +223 | -31.9 | strong |
| Call | 23250 | 49354 | 26187 | 20.2 | 22851 | 34.5 | 23270 | +280 | -14.3 | strong |
| Call | 23300 | 91556 | 40277 | 8.9 | 22763 | 25.6 | 23309 | +319 | -16.8 | strong |
| Put | 22650 | 78800 | 59883 | 88.2 | 22790 | 42.4 | 22562 | +428 | +45.8 | strong |
| Put | 22700 | 208190 | 153599 | 98.2 | 22808 | 49.9 | 22602 | +388 | +48.4 | strong |
| Put | 22750 | 106103 | 97783 | 105.1 | 22836 | 58.8 | 22645 | +345 | +46.4 | strong |
| Put | 22800 | 165591 | 145785 | 112.6 | 22866 | 69.5 | 22687 | +303 | +43.2 | strong |
| Put | 22850 | 85346 | 80642 | 110.5 | 22913 | 82.0 | 22739 | +251 | +28.6 | strong |
| Put | 22900 | 151818 | 144761 | 125.9 | 22923 | 97.2 | 22774 | +216 | +28.6 | strong |
| Put | 22950 | 71652 | 69271 | 139.6 | 22942 | 116.1 | 22810 | +180 | +23.5 | strong |
| Put | 23000 | 107180 | 95215 | 165.4 | 22942 | 137.8 | 22835 | +156 | +27.6 | strong |
| Put | 23050 | 16756 | 15611 | 189.1 | 22949 | 161.3 | 22861 | +129 | +27.8 | strong |
| Put | 23100 | 22746 | 19333 | 219.1 | 22950 | 190.2 | 22881 | +109 | +28.8 | strong |
| Put | 23150 | 3901 | 3567 | 254.2 | 22952 | 222.2 | 22896 | +94 | +32.0 | medium |
| Put | 23200 | 9482 | 8059 | 308.1 | 22931 | 259.0 | 22892 | +98 | +49.0 | medium |
| Put | 23250 | 1464 | 1079 | 350.6 | 22931 | 296.0 | 22899 | +91 | +54.6 | medium |
| Put | 23300 | 4196 | 2147 | 386.2 | 22939 | 338.0 | 22914 | +76 | +48.2 | medium |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23200, strongest put writers at 22700; weakest call writers at 22700, weakest put writers at 23600. Covers 17% of near-money call OI and 18% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22700 | 53580 | 10964 | 208.3 | 22626 | 439.8 | 22908 | -87 | -231.5 | weak |
| Call | 22750 | 7341 | 1147 | 189.3 | 22635 | 402.1 | 22939 | -56 | -212.8 | weak |
| Call | 22800 | 54021 | 9163 | 175.6 | 22659 | 366.1 | 22976 | -20 | -190.5 | weak |
| Call | 22850 | 5882 | 532 | 163.9 | 22689 | 330.8 | 23014 | +19 | -166.8 | weak |
| Call | 22900 | 30460 | 9393 | 125.1 | 22640 | 298.9 | 23025 | +30 | -173.8 | weak |
| Call | 22950 | 5928 | 2319 | 197.1 | 22866 | 267.1 | 23147 | +152 | -70.0 | strong |
| Call | 23000 | 112686 | 17137 | 103.2 | 22659 | 237.0 | 23103 | +108 | -133.8 | strong |
| Call | 23050 | 5636 | 2179 | 109.4 | 22720 | 210.0 | 23159 | +164 | -100.6 | strong |
| Call | 23100 | 31533 | 4224 | 90.7 | 22712 | 184.7 | 23191 | +195 | -94.0 | strong |
| Call | 23150 | 4500 | 1233 | 100.0 | 22798 | 160.1 | 23250 | +255 | -60.1 | strong |
| Call | 23200 | 71255 | 18897 | 58.7 | 22664 | 139.5 | 23259 | +263 | -80.8 | strong |
| Call | 23250 | 5582 | 1835 | 62.7 | 22734 | 119.7 | 23313 | +317 | -56.9 | strong |
| Call | 23300 | 50872 | 3904 | 45.3 | 22722 | 102.7 | 23345 | +350 | -57.4 | strong |
| Put | 22700 | 62033 | 17839 | 192.1 | 22775 | 112.4 | 22508 | +487 | +79.7 | strong |
| Put | 22750 | 9859 | 4914 | 192.2 | 22812 | 126.0 | 22558 | +438 | +66.2 | strong |
| Put | 22800 | 39451 | 8758 | 215.2 | 22812 | 139.8 | 22585 | +411 | +75.4 | strong |
| Put | 22850 | 7138 | 4447 | 226.4 | 22843 | 155.8 | 22624 | +372 | +70.7 | strong |
| Put | 22900 | 19306 | 9231 | 220.6 | 22892 | 172.6 | 22679 | +316 | +48.0 | strong |
| Put | 22950 | 6512 | 5515 | 217.2 | 22944 | 191.3 | 22733 | +263 | +25.9 | strong |
| Put | 23000 | 68285 | 16673 | 317.4 | 22823 | 212.8 | 22683 | +313 | +104.6 | strong |
| Put | 23050 | 1151 | 452 | 274.5 | 22924 | 232.8 | 22776 | +220 | +41.7 | strong |
| Put | 23100 | 21308 | 519 | 329.5 | 22890 | 257.4 | 22771 | +225 | +72.1 | strong |
| Put | 23150 | 782 | 335 | 319.9 | 22944 | 282.2 | 22830 | +165 | +37.6 | strong |
| Put | 23200 | 27962 | 1038 | 381.5 | 22905 | 312.7 | 22818 | +177 | +68.8 | strong |
| Put | 23250 | 866 | 111 | 397.5 | 22926 | 342.0 | 22852 | +143 | +55.5 | strong |
| Put | 23300 | 35648 | 507 | 431.6 | 22927 | 373.6 | 22868 | +127 | +57.9 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put writing · walls same · near call wall | 4 | 100% | +0.29% | +0.25 to +0.34% |  | too few (3/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 3 | 67% | -0.01% | -0.44 to +0.27% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.64% | +0.28 to +1.01% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.10% | +0.10 to +0.10% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.00% | +1.00 to +1.00% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.12% | too few (8/10) |
| intraday | monthly | writers even · weak calls | 6 | 100% | +0.24% | too few (5/10) |
| intraday | weekly | put writers stronger · weak calls | 6 | 100% | +0.35% | too few (6/10) |
| intraday | weekly | writers even · few weak writers | 2 | 0% | -0.43% | too few (2/10) |
| intraday | monthly | writers even · few weak writers | 1 | 100% | +1.01% | too few (1/10) |
| intraday | weekly | put writers stronger · few weak writers | 1 |  |  | too few (0/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.62% | too few (1/10) |
| day | monthly | writers even · weak calls | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.62% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
