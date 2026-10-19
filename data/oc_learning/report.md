# Nifty option chain pattern log
Updated 2026-10-19 11:57 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 80 snapshots over 4 trading days
- 88 patterns logged; 61 different patterns so far

## Latest read (2026-10-19 11:45:38)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 0.2 | 23007 | 0.914 | 23000 | 23000 | 23100 | ±0.5% (22892-23121) | 12.07 |
| 2026-10-27 (monthly) | 8.2 | 23005 | 0.927 | 23100 | 22000 | 23500 | ±1.55% (22648-23362) | 13.0 |

- **Weekly, last 30 min**: `PCR down · call writing · walls down · near put wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.25%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 6 times before; Nifty was up after it 17% of the time, average -0.13%. Too few outcomes (6/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 6 times before; Nifty was up after it 50% of the time, average +0.21%. Too few outcomes (6/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23100, strongest put writers at 22900; weakest call writers at 22950, weakest put writers at 23100. Covers 90% of near-money call OI and 93% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22700 | 21110 | 6706 | 110.2 | 22620 | 293.2 | 22810 | -196 | -183.0 | weak |
| Call | 22750 | 8094 | 3270 | 117.3 | 22721 | 243.4 | 22867 | -139 | -126.2 | weak |
| Call | 22800 | 26686 | 18010 | 176.3 | 22909 | 197.9 | 22976 | -30 | -21.6 | weak |
| Call | 22850 | 16807 | 13815 | 163.1 | 22969 | 153.9 | 23013 | +7 | +9.2 | weak |
| Call | 22900 | 58025 | 47292 | 121.8 | 22949 | 113.4 | 23022 | +15 | +8.4 | weak |
| Call | 22950 | 66929 | 65178 | 106.5 | 23018 | 78.7 | 23057 | +50 | +27.8 | weak |
| Call | 23000 | 306845 | 283345 | 74.8 | 23004 | 51.4 | 23075 | +68 | +23.4 | medium |
| Call | 23050 | 302087 | 298932 | 60.8 | 23035 | 31.6 | 23111 | +104 | +29.1 | strong |
| Call | 23100 | 457389 | 436269 | 58.1 | 23059 | 19.0 | 23158 | +151 | +39.1 | strong |
| Call | 23150 | 345564 | 337039 | 54.4 | 23096 | 11.3 | 23204 | +198 | +43.1 | strong |
| Call | 23200 | 442552 | 404262 | 36.5 | 23085 | 6.8 | 23236 | +230 | +29.8 | strong |
| Call | 23250 | 206798 | 196819 | 28.1 | 23092 | 4.0 | 23278 | +272 | +24.1 | strong |
| Call | 23300 | 255636 | 225801 | 16.7 | 23062 | 2.8 | 23317 | +310 | +13.9 | strong |
| Call | 23350 | 148918 | 140066 | 11.7 | 23072 | 1.8 | 23362 | +355 | +9.9 | strong |
| Put | 22700 | 271445 | 239048 | 46.0 | 22979 | 3.5 | 22654 | +353 | +42.5 | strong |
| Put | 22750 | 157932 | 154244 | 40.4 | 23012 | 5.5 | 22710 | +297 | +34.9 | strong |
| Put | 22800 | 300280 | 290672 | 45.0 | 23026 | 9.1 | 22755 | +252 | +35.9 | strong |
| Put | 22850 | 229614 | 227539 | 39.5 | 23026 | 15.1 | 22810 | +196 | +24.4 | strong |
| Put | 22900 | 332660 | 329932 | 55.9 | 23045 | 25.4 | 22844 | +162 | +30.4 | strong |
| Put | 22950 | 226759 | 225980 | 58.1 | 23061 | 41.0 | 22892 | +115 | +17.1 | strong |
| Put | 23000 | 346581 | 343732 | 62.4 | 23088 | 63.0 | 22938 | +69 | -0.6 | medium |
| Put | 23050 | 161770 | 161671 | 62.0 | 23095 | 93.3 | 22988 | +19 | -31.3 | weak |
| Put | 23100 | 167388 | 166891 | 91.2 | 23111 | 130.2 | 23009 | -2 | -39.0 | weak |
| Put | 23150 | 79228 | 79201 | 103.5 | 23132 | 172.4 | 23047 | -40 | -68.9 | weak |
| Put | 23200 | 39352 | 39214 | 144.9 | 23118 | 218.2 | 23055 | -48 | -73.3 | weak |
| Put | 23250 | 10988 | 10920 | 173.9 | 23123 | 266.0 | 23076 | -70 | -92.1 | weak |
| Put | 23300 | 7722 | 7485 | 223.4 | 23114 | 315.0 | 23077 | -70 | -91.6 | weak |
| Put | 23350 | 2569 | 2522 | 285.4 | 23098 | 361.4 | 23065 | -58 | -76.0 | weak |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23500, strongest put writers at 23000; weakest call writers at 22500, weakest put writers at 23300. Covers 46% of near-money call OI and 49% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22700 | 24961 | 5588 | 227.9 | 22664 | 374.0 | 22928 | -77 | -146.1 | weak |
| Call | 22750 | 5748 | 1174 | 246.1 | 22754 | 335.5 | 22996 | -9 | -89.4 | weak |
| Call | 22800 | 27110 | 9178 | 275.1 | 22876 | 306.2 | 23075 | +70 | -31.1 | medium |
| Call | 22850 | 5103 | 1547 | 286.2 | 22965 | 270.9 | 23136 | +131 | +15.3 | strong |
| Call | 22900 | 27541 | 12935 | 194.9 | 22824 | 238.8 | 23095 | +90 | -43.9 | medium |
| Call | 22950 | 6558 | 4126 | 214.2 | 22951 | 209.9 | 23164 | +159 | +4.3 | strong |
| Call | 23000 | 107213 | 43575 | 185.6 | 22944 | 182.2 | 23186 | +180 | +3.4 | strong |
| Call | 23050 | 13401 | 11013 | 177.3 | 23010 | 158.1 | 23227 | +222 | +19.3 | strong |
| Call | 23100 | 60400 | 37835 | 169.3 | 23046 | 135.5 | 23269 | +264 | +33.8 | strong |
| Call | 23150 | 16509 | 13590 | 160.3 | 23080 | 115.7 | 23310 | +305 | +44.7 | strong |
| Call | 23200 | 91995 | 45124 | 106.4 | 22929 | 97.5 | 23306 | +301 | +8.9 | strong |
| Call | 23250 | 14237 | 10771 | 102.9 | 23018 | 81.5 | 23353 | +348 | +21.4 | strong |
| Call | 23300 | 72233 | 28207 | 90.2 | 23037 | 67.7 | 23390 | +385 | +22.5 | strong |
| Call | 23350 | 15379 | 13428 | 79.5 | 23044 | 55.8 | 23430 | +424 | +23.8 | strong |
| Put | 22700 | 80230 | 41168 | 119.9 | 22967 | 71.2 | 22580 | +425 | +48.8 | strong |
| Put | 22750 | 15285 | 13211 | 89.4 | 23076 | 84.2 | 22661 | +345 | +5.2 | strong |
| Put | 22800 | 50147 | 23333 | 135.4 | 22985 | 97.9 | 22665 | +341 | +37.5 | strong |
| Put | 22850 | 12227 | 9811 | 154.6 | 22979 | 114.0 | 22695 | +310 | +40.5 | strong |
| Put | 22900 | 40827 | 31851 | 145.3 | 23042 | 132.0 | 22755 | +251 | +13.3 | strong |
| Put | 22950 | 11855 | 11054 | 174.2 | 23023 | 153.3 | 22776 | +229 | +20.9 | strong |
| Put | 23000 | 106069 | 60935 | 203.3 | 23013 | 174.9 | 22797 | +209 | +28.3 | strong |
| Put | 23050 | 9310 | 8859 | 179.3 | 23077 | 200.0 | 22871 | +135 | -20.7 | strong |
| Put | 23100 | 39992 | 26856 | 188.3 | 23117 | 227.4 | 22912 | +94 | -39.1 | medium |
| Put | 23150 | 6955 | 6331 | 214.2 | 23117 | 257.8 | 22936 | +69 | -43.6 | medium |
| Put | 23200 | 38818 | 14406 | 246.6 | 23103 | 290.0 | 22953 | +52 | -43.4 | medium |
| Put | 23250 | 1646 | 1208 | 279.1 | 23095 | 324.9 | 22971 | +34 | -45.7 | weak |
| Put | 23300 | 33249 | 5239 | 302.2 | 23120 | 362.5 | 22998 | +7 | -60.3 | weak |
| Put | 23350 | 697 | 441 | 360.4 | 23077 | 398.8 | 22990 | +16 | -38.4 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 6 | 100% | +0.20% | +0.03 to +0.37% | 0% of 1 | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR down · call writing · walls same · mid walls | 3 | 33% | -0.11% | -0.47 to +0.14% |  | too few (3/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.09% | -0.61 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 2 | 100% | +0.14% | +0.07 to +0.21% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 2 | 100% | +0.14% | +0.11 to +0.17% |  | too few (2/10) |
| weekly | PCR down · call writing · walls down · near put wall | 2 | 100% | +0.25% | +0.25 to +0.25% | 0% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.63% | -0.63 to -0.63% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.27% | -0.27 to -0.27% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.21% | -0.21 to -0.21% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 0% | -0.24% | -0.24 to -0.24% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.18% | -0.18 to -0.18% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 1 | 0% | -0.24% | -0.24 to -0.24% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.27% | -0.27 to -0.27% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.10% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.15% | up |
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | +0.04% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | monthly | writers even · few weak writers | 7 | 50% | +0.21% | too few (6/10) |
| intraday | weekly | writers even · few weak writers | 7 | 17% | -0.13% | too few (6/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.23% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | +0.02% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -0.61% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
