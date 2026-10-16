# Nifty option chain pattern log
Updated 2026-10-16 09:57 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 48 snapshots over 3 trading days
- 52 patterns logged; 40 different patterns so far

## Latest read (2026-10-16 09:44:49)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 3.2 | 22968 | 0.979 | 22950 | 22900 | 23000 | ±1.01% (22736-23199) | 13.91 |
| 2026-10-27 (monthly) | 11.2 | 22968 | 0.95 | 23100 | 22500 | 23500 | ±1.8% (22554-23381) | 12.88 |

- **Weekly, last 30 min**: `PCR flat · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.43%. Too few outcomes (2/20) to trade on.
- **Weekly, today vs previous day**: `PCR down · put and call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 100% of the time, average +1.02%. Too few outcomes (1/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · call writing · walls up · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-19

Strongest call writers at 23000, strongest put writers at 22900; weakest call writers at 22900, weakest put writers at 23300. Covers 69% of near-money call OI and 82% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 12571 | 7859 | 125.8 | 22608 | 321.0 | 22776 | -192 | -195.2 | weak |
| Call | 22700 | 41059 | 13043 | 110.2 | 22620 | 279.5 | 22810 | -157 | -169.3 | weak |
| Call | 22750 | 18947 | 7655 | 117.3 | 22721 | 240.8 | 22867 | -100 | -123.5 | weak |
| Call | 22800 | 45465 | 23558 | 139.4 | 22804 | 204.2 | 22939 | -28 | -64.9 | weak |
| Call | 22850 | 33669 | 22371 | 140.8 | 22890 | 168.3 | 22991 | +23 | -27.5 | weak |
| Call | 22900 | 125870 | 87352 | 115.0 | 22881 | 137.6 | 23015 | +47 | -22.6 | weak |
| Call | 22950 | 161968 | 143475 | 111.1 | 22958 | 111.8 | 23061 | +94 | -0.7 | medium |
| Call | 23000 | 317716 | 241701 | 83.7 | 22929 | 88.5 | 23084 | +116 | -4.8 | strong |
| Call | 23050 | 147376 | 134162 | 72.3 | 22952 | 68.8 | 23122 | +155 | +3.6 | strong |
| Call | 23100 | 226497 | 166363 | 55.3 | 22956 | 53.5 | 23155 | +188 | +1.8 | strong |
| Call | 23150 | 84446 | 64231 | 41.2 | 22947 | 40.4 | 23191 | +224 | +0.9 | strong |
| Call | 23200 | 177357 | 104068 | 30.2 | 22924 | 29.8 | 23230 | +263 | +0.5 | strong |
| Call | 23250 | 80168 | 62542 | 23.7 | 22941 | 21.9 | 23274 | +306 | +1.9 | strong |
| Call | 23300 | 146554 | 95906 | 13.2 | 22884 | 16.2 | 23313 | +346 | -3.0 | strong |
| Put | 22650 | 83397 | 68350 | 70.8 | 22844 | 30.7 | 22579 | +388 | +40.1 | strong |
| Put | 22700 | 213054 | 168790 | 82.6 | 22850 | 38.8 | 22617 | +350 | +43.9 | strong |
| Put | 22750 | 110931 | 104975 | 86.3 | 22880 | 48.8 | 22664 | +304 | +37.5 | strong |
| Put | 22800 | 206916 | 192689 | 89.1 | 22917 | 61.9 | 22711 | +257 | +27.2 | strong |
| Put | 22850 | 142402 | 138558 | 93.2 | 22944 | 77.9 | 22757 | +211 | +15.3 | strong |
| Put | 22900 | 261717 | 256505 | 108.9 | 22951 | 97.2 | 22791 | +176 | +11.6 | strong |
| Put | 22950 | 152926 | 151368 | 124.8 | 22962 | 119.5 | 22825 | +142 | +5.3 | strong |
| Put | 23000 | 155838 | 149497 | 147.6 | 22971 | 146.9 | 22852 | +115 | +0.7 | strong |
| Put | 23050 | 40288 | 39858 | 169.2 | 22981 | 177.9 | 22881 | +87 | -8.7 | medium |
| Put | 23100 | 34197 | 32446 | 203.8 | 22975 | 210.6 | 22896 | +71 | -6.8 | medium |
| Put | 23150 | 7975 | 7833 | 240.0 | 22975 | 247.9 | 22910 | +58 | -7.9 | medium |
| Put | 23200 | 11131 | 10502 | 286.6 | 22964 | 289.6 | 22913 | +54 | -3.0 | medium |
| Put | 23250 | 2790 | 2469 | 321.3 | 22970 | 330.1 | 22929 | +39 | -8.8 | weak |
| Put | 23300 | 3975 | 2838 | 365.2 | 22968 | 373.9 | 22935 | +33 | -8.6 | weak |

## Strong vs weak writers, monthly 2026-10-27

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at 22700, weakest put writers at 23600. Covers 24% of near-money call OI and 27% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22650 | 3725 | 929 | 221.8 | 22596 | 415.9 | 22872 | -96 | -194.1 | weak |
| Call | 22700 | 31348 | 6910 | 223.6 | 22655 | 376.6 | 22924 | -44 | -153.0 | weak |
| Call | 22750 | 6313 | 986 | 189.3 | 22635 | 339.5 | 22939 | -28 | -150.2 | weak |
| Call | 22800 | 35341 | 9846 | 237.4 | 22802 | 308.4 | 23037 | +70 | -71.0 | medium |
| Call | 22850 | 5291 | 876 | 218.5 | 22816 | 277.4 | 23069 | +101 | -58.8 | medium |
| Call | 22900 | 28403 | 11690 | 170.1 | 22758 | 245.8 | 23070 | +102 | -75.7 | medium |
| Call | 22950 | 6526 | 3436 | 205.6 | 22904 | 218.9 | 23156 | +188 | -13.3 | strong |
| Call | 23000 | 100608 | 23283 | 139.0 | 22784 | 191.7 | 23139 | +171 | -52.7 | strong |
| Call | 23050 | 6461 | 3254 | 141.7 | 22823 | 168.2 | 23192 | +224 | -26.6 | strong |
| Call | 23100 | 31443 | 7493 | 119.0 | 22842 | 146.7 | 23219 | +251 | -27.6 | strong |
| Call | 23150 | 3711 | 1312 | 108.3 | 22851 | 124.3 | 23258 | +291 | -16.0 | strong |
| Call | 23200 | 69265 | 20427 | 65.6 | 22706 | 109.1 | 23266 | +298 | -43.5 | strong |
| Call | 23250 | 6328 | 2813 | 81.3 | 22836 | 92.8 | 23331 | +364 | -11.5 | strong |
| Call | 23300 | 52834 | 6296 | 61.8 | 22826 | 78.9 | 23362 | +394 | -17.1 | strong |
| Put | 22650 | 6559 | 2162 | 164.9 | 22791 | 91.2 | 22485 | +482 | +73.7 | strong |
| Put | 22700 | 66202 | 25129 | 162.0 | 22856 | 104.0 | 22538 | +430 | +57.9 | strong |
| Put | 22750 | 10342 | 5545 | 181.2 | 22837 | 118.8 | 22569 | +399 | +62.4 | strong |
| Put | 22800 | 37580 | 10432 | 193.7 | 22857 | 134.1 | 22606 | +361 | +59.6 | strong |
| Put | 22850 | 8089 | 5536 | 207.0 | 22881 | 153.4 | 22643 | +325 | +53.6 | strong |
| Put | 22900 | 23939 | 14207 | 199.3 | 22930 | 172.9 | 22701 | +267 | +26.4 | strong |
| Put | 22950 | 8668 | 7707 | 208.4 | 22956 | 194.8 | 22742 | +226 | +13.7 | strong |
| Put | 23000 | 80024 | 31538 | 262.2 | 22911 | 220.6 | 22738 | +230 | +41.6 | strong |
| Put | 23050 | 2474 | 1897 | 234.5 | 22992 | 245.6 | 22815 | +152 | -11.0 | strong |
| Put | 23100 | 15922 | 1252 | 279.2 | 22956 | 272.5 | 22821 | +147 | +6.7 | strong |
| Put | 23150 | 790 | 423 | 311.3 | 22954 | 300.8 | 22839 | +129 | +10.6 | strong |
| Put | 23200 | 27851 | 1581 | 351.9 | 22944 | 333.1 | 22848 | +120 | +18.9 | strong |
| Put | 23250 | 780 | 140 | 381.7 | 22947 | 367.2 | 22868 | +99 | +14.5 | medium |
| Put | 23300 | 29452 | 419 | 431.6 | 22927 | 400.0 | 22868 | +99 | +31.6 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put writing · walls same · near call wall | 4 | 100% | +0.25% | +0.03 to +0.37% |  | too few (4/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 4 | 50% | -0.03% | -0.44 to +0.28% |  | too few (4/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · mid walls | 2 | 0% | -0.24% | -0.47 to -0.01% |  | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 2 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.65% | +0.28 to +1.02% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.11% | -0.11 to -0.11% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 0% | -0.13% | -0.13 to -0.13% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | call writers stronger · few weak writers | 11 | 50% | +0.00% | no clear direction |
| intraday | weekly | put writers stronger · weak calls | 11 | 64% | +0.16% | no clear direction |
| intraday | monthly | writers even · weak calls | 9 | 88% | +0.16% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers | 9 | 50% | +0.13% | too few (8/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | put writers stronger · few weak writers | 3 | 100% | +0.05% | too few (2/10) |
| intraday | weekly | writers even · few weak writers | 3 | 0% | -0.43% | too few (2/10) |
| intraday | monthly | writers even · few weak writers | 2 | 100% | +1.02% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers | 1 |  |  | too few (0/10) |
| day | monthly | writers even · weak calls | 1 | 0% | -0.13% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 0% | -0.13% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 |  |  | too few (0/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
