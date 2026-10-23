# Nifty option chain pattern log
Updated 2026-10-23 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 151 snapshots over 7 trading days
- 163 patterns logged; 94 different patterns so far

## Latest read (2026-10-23 09:45:07)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 4.2 | 22696 | 0.994 | 22800 | 22000 | 24000 | ±1.38% (22382-23010) | 16.78 |
| 2026-11-23 (monthly) | 31.2 | 22701 | 1.192 | 23000 | 22000 | 23000 | ±3.69% (21862-23539) | 15.6 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.78%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 14 times before; Nifty was up after it 23% of the time, average -0.43%. Too few outcomes (13/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.06%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR up · put and call writing · walls same · near call wall`. Seen 4 times before; Nifty was up after it 50% of the time, average +0.09%. Too few outcomes (4/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 28 times before; Nifty was up after it 62% of the time, average -0.01%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR flat · put and call writing · walls same · near call wall`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.06%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 2 times before; Nifty was up after it 50% of the time, average -0.24%. Too few outcomes (2/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at 22300, weakest put writers at 23000. Covers 90% of near-money call OI and 89% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 11529 | 5444 | 410.1 | 22732 | 390.0 | 22810 | +114 | +20.1 | strong |
| Call | 22450 | 3990 | 3506 | 311.0 | 22658 | 351.9 | 22761 | +65 | -40.9 | medium |
| Call | 22500 | 46464 | 32976 | 300.8 | 22688 | 309.4 | 22801 | +104 | -8.5 | strong |
| Call | 22550 | 13028 | 12563 | 250.8 | 22673 | 274.7 | 22801 | +104 | -23.9 | strong |
| Call | 22600 | 60696 | 56774 | 201.7 | 22645 | 240.3 | 22802 | +105 | -38.6 | strong |
| Call | 22650 | 33694 | 33370 | 168.9 | 22639 | 206.0 | 22819 | +123 | -37.1 | strong |
| Call | 22700 | 141807 | 132766 | 170.3 | 22682 | 178.0 | 22870 | +174 | -7.7 | strong |
| Call | 22750 | 94502 | 92130 | 154.2 | 22702 | 149.6 | 22904 | +208 | +4.6 | strong |
| Call | 22800 | 199843 | 188626 | 144.3 | 22723 | 126.5 | 22944 | +248 | +17.8 | strong |
| Call | 22850 | 62442 | 61134 | 127.8 | 22739 | 103.2 | 22978 | +281 | +24.6 | strong |
| Call | 22900 | 146913 | 139592 | 123.6 | 22773 | 83.9 | 23024 | +327 | +39.7 | strong |
| Call | 22950 | 71778 | 70844 | 106.1 | 22772 | 68.4 | 23056 | +360 | +37.7 | strong |
| Call | 23000 | 299522 | 256152 | 103.5 | 22799 | 54.4 | 23104 | +407 | +49.2 | strong |
| Put | 22400 | 119105 | 105112 | 52.2 | 22760 | 49.0 | 22348 | +349 | +3.2 | strong |
| Put | 22450 | 48132 | 47605 | 61.2 | 22750 | 58.2 | 22389 | +308 | +3.0 | strong |
| Put | 22500 | 214529 | 176415 | 70.0 | 22780 | 70.7 | 22430 | +266 | -0.7 | strong |
| Put | 22550 | 70905 | 69599 | 90.2 | 22741 | 84.2 | 22460 | +237 | +6.0 | strong |
| Put | 22600 | 181169 | 164862 | 105.1 | 22761 | 98.8 | 22495 | +201 | +6.3 | strong |
| Put | 22650 | 108614 | 106861 | 123.0 | 22722 | 117.6 | 22527 | +169 | +5.5 | strong |
| Put | 22700 | 226651 | 212246 | 131.6 | 22749 | 136.1 | 22568 | +128 | -4.5 | strong |
| Put | 22750 | 88167 | 87803 | 155.6 | 22728 | 159.8 | 22594 | +102 | -4.2 | medium |
| Put | 22800 | 134185 | 123070 | 164.9 | 22774 | 182.8 | 22635 | +61 | -17.9 | medium |
| Put | 22850 | 24570 | 24118 | 182.1 | 22800 | 213.0 | 22668 | +28 | -30.9 | weak |
| Put | 22900 | 61612 | 58264 | 169.9 | 22907 | 244.0 | 22730 | -34 | -74.1 | weak |
| Put | 22950 | 14917 | 14825 | 186.3 | 22912 | 276.5 | 22764 | -67 | -90.2 | weak |
| Put | 23000 | 75985 | 63171 | 187.5 | 22986 | 314.4 | 22813 | -116 | -126.9 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 23000; weakest call writers at -, weakest put writers at 23200. Covers 49% of near-money call OI and 47% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22400 | 1619 | 252 | 628.9 | 22684 | 690.0 | 23029 | +328 | -61.1 | strong |
| Call | 22450 | 250 | 172 | 609.8 | 22701 | 636.6 | 23060 | +359 | -26.9 | strong |
| Call | 22500 | 19658 | 9017 | 589.2 | 22702 | 597.8 | 23089 | +388 | -8.6 | strong |
| Call | 22550 | 410 | 217 | 541.2 | 22685 | 571.4 | 23091 | +390 | -30.2 | strong |
| Call | 22600 | 24103 | 15500 | 491.3 | 22664 | 539.5 | 23091 | +390 | -48.2 | strong |
| Call | 22650 | 2042 | 1743 | 462.7 | 22671 | 510.0 | 23113 | +412 | -47.3 | strong |
| Call | 22700 | 27530 | 23538 | 462.4 | 22707 | 476.2 | 23162 | +462 | -13.8 | strong |
| Call | 22750 | 1056 | 375 | 442.4 | 22702 | 446.0 | 23192 | +492 | -3.6 | strong |
| Call | 22800 | 20657 | 15128 | 407.6 | 22703 | 422.5 | 23208 | +507 | -14.9 | strong |
| Call | 22850 | 1177 | 702 | 378.8 | 22710 | 393.8 | 23229 | +528 | -15.0 | strong |
| Call | 22900 | 10431 | 7301 | 369.3 | 22729 | 369.6 | 23269 | +568 | -0.4 | strong |
| Call | 22950 | 1304 | 401 | 357.4 | 22750 | 343.4 | 23307 | +607 | +14.0 | strong |
| Call | 23000 | 80643 | 29295 | 340.9 | 22772 | 320.9 | 23341 | +640 | +20.0 | strong |
| Put | 22400 | 15672 | 3494 | 239.1 | 22757 | 257.0 | 22161 | +540 | -17.9 | strong |
| Put | 22450 | 599 | 165 | 261.1 | 22723 | 257.6 | 22189 | +512 | +3.5 | strong |
| Put | 22500 | 44730 | 17695 | 255.1 | 22800 | 287.1 | 22245 | +456 | -32.1 | strong |
| Put | 22550 | 803 | 314 | 234.4 | 22901 | 299.2 | 22316 | +385 | -64.8 | strong |
| Put | 22600 | 24357 | 15216 | 338.4 | 22670 | 323.4 | 22262 | +439 | +14.9 | strong |
| Put | 22650 | 2500 | 1938 | 333.5 | 22727 | 334.2 | 22316 | +384 | -0.7 | strong |
| Put | 22700 | 29758 | 22778 | 350.4 | 22722 | 362.4 | 22350 | +351 | -11.9 | strong |
| Put | 22750 | 1243 | 750 | 326.6 | 22830 | 383.6 | 22423 | +277 | -56.9 | strong |
| Put | 22800 | 21922 | 12370 | 394.6 | 22721 | 404.1 | 22405 | +295 | -9.6 | strong |
| Put | 22850 | 2184 | 146 | 399.6 | 22763 | 428.1 | 22450 | +250 | -28.6 | strong |
| Put | 22900 | 7325 | 3391 | 409.5 | 22787 | 449.8 | 22490 | +210 | -40.3 | strong |
| Put | 22950 | 638 | 180 | 407.5 | 22819 | 470.0 | 22542 | +158 | -62.5 | strong |
| Put | 23000 | 72762 | 31325 | 453.7 | 22795 | 502.6 | 22546 | +154 | -48.9 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 50% | +0.09% | -0.74 to +0.62% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 4 | 75% | +0.04% | -0.21 to +0.17% |  | too few (4/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 3 | 67% | +0.01% | -0.39 to +0.34% |  | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| weekly | PCR up · put writing · walls same · near put wall | 3 | 33% | -0.27% | -0.47 to +0.06% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 2 | 100% | +0.28% | +0.27 to +0.29% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · mid walls | 2 | 100% | +0.20% | +0.04 to +0.36% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.40% | -0.40 to -0.40% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 2 | 100% | +0.21% | +0.13 to +0.29% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · near call wall | 2 | 100% | +0.06% | +0.06 to +0.06% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 100% | +0.06% | +0.06 to +0.06% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 29 | 62% | -0.01% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 22 | 80% | +0.23% | up |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | weekly | writers even · few weak writers | 15 | 23% | -0.43% | no clear direction |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | writers even · weak puts | 7 | 57% | +0.19% | too few (7/10) |
| intraday | weekly | writers even · weak puts | 6 | 50% | -0.18% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 100% | +0.39% | too few (2/10) |
| day | monthly | writers even · few weak writers | 3 | 50% | -0.24% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · few weak writers | 2 | 100% | +0.06% | too few (1/10) |
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
