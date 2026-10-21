# Nifty option chain pattern log
Updated 2026-10-21 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 119 snapshots over 5 trading days
- 127 patterns logged; 83 different patterns so far

## Latest read (2026-10-21 14:45:04)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 6.0 | 22671 | 0.891 | 22900 | 22000 | 23000 | ±1.48% (22336-23006) | 14.33 |
| 2026-11-23 (monthly) | 33.0 | 22671 | 1.416 | 23000 | 22000 | 23000 | ±3.68% (21838-23505) | 15.04 |

- **Weekly, last 30 min**: `PCR up · call writing · walls same · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 11 times before; Nifty was up after it 20% of the time, average -0.18%. Too few outcomes (10/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls down · near call wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.95%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR up · put and call writing · walls same · near call wall`. Seen 3 times before; Nifty was up after it 0% of the time, average -0.49%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 4 times before; Nifty was up after it 0% of the time, average -0.16%. Too few outcomes (4/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at -, weakest put writers at 23000. Covers 82% of near-money call OI and 75% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22350 | 1556 | 899 | 462.0 | 22753 | 391.5 | 22812 | +141 | +70.5 | strong |
| Call | 22400 | 10401 | 2673 | 521.7 | 22856 | 348.9 | 22922 | +250 | +172.8 | strong |
| Call | 22450 | 1855 | 981 | 384.9 | 22732 | 311.5 | 22835 | +163 | +73.4 | strong |
| Call | 22500 | 37790 | 16873 | 392.1 | 22791 | 275.6 | 22892 | +221 | +116.5 | strong |
| Call | 22550 | 6481 | 5093 | 369.1 | 22823 | 243.1 | 22919 | +248 | +126.0 | strong |
| Call | 22600 | 40006 | 26868 | 249.4 | 22700 | 212.6 | 22849 | +178 | +36.8 | strong |
| Call | 22650 | 22553 | 20422 | 214.7 | 22709 | 184.4 | 22865 | +193 | +30.2 | strong |
| Call | 22700 | 105075 | 87039 | 193.2 | 22716 | 158.7 | 22893 | +222 | +34.5 | strong |
| Call | 22750 | 51974 | 47503 | 177.6 | 22737 | 135.9 | 22928 | +256 | +41.7 | strong |
| Call | 22800 | 128524 | 112342 | 177.4 | 22778 | 115.5 | 22977 | +306 | +61.9 | strong |
| Call | 22850 | 46986 | 44670 | 168.1 | 22815 | 97.7 | 23018 | +347 | +70.5 | strong |
| Call | 22900 | 135832 | 123385 | 159.6 | 22842 | 82.2 | 23060 | +388 | +77.4 | strong |
| Call | 22950 | 78089 | 76175 | 144.3 | 22859 | 69.1 | 23094 | +423 | +75.2 | strong |
| Call | 23000 | 273466 | 214051 | 137.2 | 22882 | 58.5 | 23137 | +466 | +78.7 | strong |
| Put | 22350 | 25539 | 22095 | 29.8 | 22969 | 55.5 | 22320 | +351 | -25.8 | strong |
| Put | 22400 | 76363 | 54505 | 45.3 | 22916 | 66.0 | 22355 | +317 | -20.6 | strong |
| Put | 22450 | 26762 | 25598 | 36.5 | 22973 | 78.5 | 22414 | +258 | -42.0 | strong |
| Put | 22500 | 152130 | 93928 | 53.8 | 22960 | 92.7 | 22446 | +225 | -38.9 | strong |
| Put | 22550 | 32129 | 29653 | 50.1 | 22977 | 109.3 | 22500 | +172 | -59.3 | strong |
| Put | 22600 | 100601 | 74570 | 72.0 | 22977 | 128.6 | 22528 | +143 | -56.6 | strong |
| Put | 22650 | 47611 | 44062 | 98.2 | 22882 | 150.5 | 22552 | +120 | -52.3 | strong |
| Put | 22700 | 118379 | 89826 | 104.6 | 22943 | 174.8 | 22595 | +76 | -70.2 | medium |
| Put | 22750 | 40084 | 38832 | 117.7 | 22922 | 201.6 | 22632 | +39 | -83.9 | weak |
| Put | 22800 | 82944 | 62869 | 117.4 | 22964 | 231.9 | 22683 | -11 | -114.5 | weak |
| Put | 22850 | 17574 | 16729 | 125.4 | 22979 | 264.0 | 22725 | -53 | -138.6 | weak |
| Put | 22900 | 65938 | 60751 | 132.1 | 23011 | 297.6 | 22768 | -96 | -165.5 | weak |
| Put | 22950 | 18940 | 18770 | 143.4 | 23012 | 334.6 | 22807 | -135 | -191.2 | weak |
| Put | 23000 | 100539 | 80381 | 156.2 | 23054 | 374.3 | 22844 | -172 | -218.1 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at -, weakest put writers at 23000. Covers 25% of near-money call OI and 21% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22350 | 88 | 19 | 853.5 | 22918 | 673.5 | 23204 | +532 | +180.1 | strong |
| Call | 22400 | 1481 | 56 | 668.3 | 22717 | 636.5 | 23068 | +397 | +31.9 | strong |
| Call | 22450 | 113 | 34 | 717.0 | 22836 | 603.8 | 23167 | +496 | +113.2 | strong |
| Call | 22500 | 14490 | 3086 | 634.7 | 22765 | 574.5 | 23135 | +463 | +60.1 | strong |
| Call | 22550 | 378 | 129 | 567.7 | 22709 | 540.9 | 23118 | +446 | +26.8 | strong |
| Call | 22600 | 9125 | 181 | 530.8 | 22701 | 510.4 | 23131 | +459 | +20.4 | strong |
| Call | 22650 | 435 | 107 | 490.9 | 22691 | 478.9 | 23141 | +469 | +12.1 | strong |
| Call | 22700 | 5207 | 1150 | 473.5 | 22709 | 452.4 | 23173 | +502 | +21.1 | strong |
| Call | 22750 | 1232 | 389 | 447.6 | 22711 | 422.1 | 23198 | +526 | +25.6 | strong |
| Call | 22800 | 10455 | 4547 | 418.7 | 22712 | 394.4 | 23219 | +547 | +24.2 | strong |
| Call | 22850 | 890 | 355 | 401.5 | 22732 | 370.6 | 23252 | +580 | +31.0 | strong |
| Call | 22900 | 8712 | 5374 | 377.7 | 22739 | 344.6 | 23278 | +606 | +33.0 | strong |
| Call | 22950 | 1256 | 282 | 381.9 | 22791 | 320.0 | 23332 | +660 | +61.9 | strong |
| Call | 23000 | 69957 | 17677 | 369.5 | 22832 | 299.8 | 23369 | +698 | +69.7 | strong |
| Put | 22350 | 763 | 152 | 208.2 | 22817 | 247.6 | 22142 | +530 | -39.4 | strong |
| Put | 22400 | 13867 | 1304 | 244.2 | 22753 | 264.1 | 22156 | +516 | -20.0 | strong |
| Put | 22450 | 600 | 110 | 261.3 | 22730 | 279.1 | 22189 | +483 | -17.9 | strong |
| Put | 22500 | 40037 | 11184 | 235.5 | 22861 | 297.1 | 22264 | +407 | -61.5 | strong |
| Put | 22550 | 741 | 239 | 210.7 | 22971 | 313.5 | 22339 | +332 | -102.8 | strong |
| Put | 22600 | 10277 | 805 | 299.6 | 22765 | 334.1 | 22300 | +371 | -34.4 | strong |
| Put | 22650 | 930 | 317 | 221.0 | 23020 | 354.4 | 22429 | +242 | -133.4 | strong |
| Put | 22700 | 8474 | 1283 | 297.4 | 22861 | 373.6 | 22403 | +269 | -76.2 | strong |
| Put | 22750 | 1017 | 437 | 282.0 | 22942 | 395.2 | 22468 | +203 | -113.2 | strong |
| Put | 22800 | 13587 | 3586 | 376.0 | 22761 | 417.9 | 22424 | +247 | -41.8 | strong |
| Put | 22850 | 2850 | 28 | 327.3 | 22915 | 441.9 | 22523 | +149 | -114.6 | strong |
| Put | 22900 | 6027 | 2026 | 385.2 | 22838 | 466.0 | 22515 | +157 | -80.8 | strong |
| Put | 22950 | 687 | 100 | 334.8 | 22956 | 491.0 | 22615 | +56 | -156.2 | medium |
| Put | 23000 | 54147 | 12298 | 361.9 | 22964 | 520.5 | 22638 | +33 | -158.5 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 86% | +0.14% | -0.19 to +0.37% | 0% of 1 | too few (7/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 4 | 0% | -0.49% | -0.74 to -0.06% |  | too few (3/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -1.06% | -1.28 to -0.71% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 3 | 67% | +0.02% | -0.21 to +0.17% |  | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 0% | -0.09% | -0.11 to -0.06% |  | too few (2/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.14% | +0.07 to +0.22% |  | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 2 | 100% | +0.19% | +0.14 to +0.25% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.43% | -0.47 to -0.39% | 0% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 0% | -0.42% | -0.51 to -0.33% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 0% | -0.30% | -0.30 to -0.30% |  | too few (1/10) |
| monthly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.83% | -1.83 to -1.83% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 0% | -0.11% | -0.11 to -0.11% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.31% | -0.31 to -0.31% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 | 100% | +0.04% | +0.04 to +0.04% | 0% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -1.29% | -1.29 to -1.29% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 1 | 100% | +0.11% | +0.11 to +0.11% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 0% | -0.32% | -0.32 to -0.32% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.83% | -1.83 to -1.83% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -1.18% | -1.18 to -1.18% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.95% | -0.95 to -0.95% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.95% | -0.95 to -0.95% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 42% | -0.04% | no clear direction |
| intraday | monthly | writers even · few weak writers | 13 | 54% | -0.18% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 12 | 20% | -0.18% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 10 | 44% | -0.02% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | writers even · few weak writers | 10 | 10% | -0.74% | down |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.77% | too few (5/10) |
| intraday | monthly | writers even · weak puts | 5 | 0% | -0.16% | too few (4/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | weekly | writers even · weak puts | 4 | 50% | -0.35% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 0% | -0.22% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.35% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.95% | too few (1/10) |
| day | monthly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
