# Nifty option chain pattern log
Updated 2026-10-22 13:55 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 141 snapshots over 6 trading days
- 151 patterns logged; 92 different patterns so far

## Latest read (2026-10-22 13:45:04)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 5.1 | 22617 | 1.048 | 22800 | 22000 | 23000 | ±1.39% (22302-22933) | 14.85 |
| 2026-11-23 (monthly) | 32.1 | 22620 | 1.367 | 23000 | 22000 | 23000 | ±3.65% (21794-23446) | 15.11 |

- **Weekly, last 30 min**: `PCR flat · call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 20 times before; Nifty was up after it 61% of the time, average +0.12%. Too few outcomes (18/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `call writers stronger · weak puts`. Seen 2 times before; Nifty was up after it 0% of the time, average -0.59%. Too few outcomes (2/20) to trade on.
- **Monthly, last 30 min**: `PCR up · unwinding · walls same · mid walls`. Seen 3 times before; Nifty was up after it 67% of the time, average +0.04%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 22 times before; Nifty was up after it 38% of the time, average -0.13%. No direction and the walls have not held reliably: no structure.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.85%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22600; weakest call writers at -, weakest put writers at 22700. Covers 87% of near-money call OI and 83% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 11037 | 2898 | 429.1 | 22659 | 410.8 | 22729 | +112 | +18.4 | strong |
| Call | 22350 | 2705 | 2143 | 407.1 | 22691 | 367.2 | 22757 | +140 | +39.8 | strong |
| Call | 22400 | 11750 | 5383 | 411.1 | 22734 | 328.5 | 22811 | +194 | +82.6 | strong |
| Call | 22450 | 4543 | 3945 | 308.9 | 22656 | 292.0 | 22759 | +142 | +16.9 | strong |
| Call | 22500 | 53253 | 37609 | 300.7 | 22687 | 253.4 | 22801 | +183 | +47.3 | strong |
| Call | 22550 | 18646 | 17943 | 249.7 | 22672 | 220.7 | 22800 | +182 | +29.0 | strong |
| Call | 22600 | 83088 | 77531 | 200.2 | 22643 | 190.0 | 22800 | +183 | +10.2 | strong |
| Call | 22650 | 48304 | 47795 | 167.1 | 22636 | 162.3 | 22817 | +200 | +4.8 | strong |
| Call | 22700 | 124350 | 112282 | 166.2 | 22674 | 137.3 | 22866 | +249 | +28.9 | strong |
| Call | 22750 | 57274 | 54250 | 161.3 | 22713 | 115.3 | 22911 | +294 | +46.0 | strong |
| Call | 22800 | 141023 | 127405 | 158.4 | 22744 | 96.8 | 22958 | +341 | +61.6 | strong |
| Call | 22850 | 42328 | 40710 | 149.9 | 22777 | 80.2 | 23000 | +383 | +69.7 | strong |
| Call | 22900 | 102310 | 93792 | 152.9 | 22830 | 66.2 | 23053 | +436 | +86.7 | strong |
| Call | 22950 | 59899 | 58671 | 129.0 | 22819 | 54.5 | 23079 | +462 | +74.5 | strong |
| Put | 22300 | 90674 | 58322 | 28.9 | 22904 | 43.0 | 22271 | +346 | -14.1 | strong |
| Put | 22350 | 32953 | 31234 | 44.8 | 22762 | 51.8 | 22305 | +312 | -6.9 | strong |
| Put | 22400 | 83032 | 67877 | 52.7 | 22815 | 62.2 | 22347 | +270 | -9.6 | strong |
| Put | 22450 | 41498 | 40791 | 62.9 | 22781 | 74.0 | 22387 | +230 | -11.2 | strong |
| Put | 22500 | 159434 | 115882 | 69.1 | 22844 | 89.3 | 22431 | +186 | -20.2 | strong |
| Put | 22550 | 57285 | 55624 | 93.4 | 22772 | 105.7 | 22457 | +161 | -12.3 | strong |
| Put | 22600 | 166008 | 144898 | 107.3 | 22794 | 125.4 | 22493 | +125 | -18.1 | strong |
| Put | 22650 | 67564 | 65353 | 127.4 | 22752 | 147.9 | 22523 | +95 | -20.5 | medium |
| Put | 22700 | 130015 | 112979 | 126.6 | 22813 | 173.2 | 22573 | +44 | -46.7 | weak |
| Put | 22750 | 39319 | 38877 | 148.5 | 22784 | 201.2 | 22601 | +16 | -52.7 | weak |
| Put | 22800 | 70548 | 57438 | 137.3 | 22894 | 231.0 | 22663 | -45 | -93.7 | weak |
| Put | 22850 | 13428 | 12933 | 151.0 | 22910 | 265.1 | 22699 | -82 | -114.1 | weak |
| Put | 22900 | 51274 | 47518 | 141.8 | 22987 | 300.9 | 22758 | -141 | -159.1 | weak |
| Put | 22950 | 11667 | 11570 | 154.5 | 22989 | 336.4 | 22795 | -178 | -181.9 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22700; weakest call writers at -, weakest put writers at 23200. Covers 46% of near-money call OI and 40% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22300 | 1213 | 404 | 724.8 | 22701 | 670.4 | 23025 | +405 | +54.4 | strong |
| Call | 22350 | 131 | 62 | 703.7 | 22730 | 622.0 | 23054 | +434 | +81.7 | strong |
| Call | 22400 | 1626 | 241 | 626.9 | 22684 | 606.4 | 23027 | +407 | +20.5 | strong |
| Call | 22450 | 234 | 156 | 608.4 | 22702 | 563.0 | 23058 | +438 | +45.3 | strong |
| Call | 22500 | 17944 | 7016 | 587.3 | 22704 | 538.0 | 23087 | +467 | +49.3 | strong |
| Call | 22550 | 449 | 238 | 541.3 | 22686 | 507.7 | 23091 | +471 | +33.6 | strong |
| Call | 22600 | 23623 | 14999 | 490.0 | 22663 | 478.9 | 23090 | +470 | +11.1 | strong |
| Call | 22650 | 2012 | 1698 | 461.3 | 22671 | 453.1 | 23111 | +491 | +8.2 | strong |
| Call | 22700 | 24539 | 20532 | 460.5 | 22708 | 421.6 | 23160 | +540 | +38.9 | strong |
| Call | 22750 | 1073 | 358 | 443.2 | 22704 | 396.9 | 23193 | +573 | +46.3 | strong |
| Call | 22800 | 17525 | 11890 | 406.3 | 22706 | 368.9 | 23206 | +586 | +37.3 | strong |
| Call | 22850 | 1279 | 755 | 378.6 | 22710 | 345.6 | 23229 | +608 | +33.0 | strong |
| Call | 22900 | 11000 | 7680 | 369.1 | 22729 | 321.1 | 23269 | +649 | +48.0 | strong |
| Call | 22950 | 1350 | 406 | 358.7 | 22752 | 292.0 | 23309 | +689 | +66.7 | strong |
| Put | 22300 | 14027 | 6714 | 224.9 | 22713 | 242.9 | 22075 | +545 | -18.0 | strong |
| Put | 22350 | 774 | 190 | 213.0 | 22798 | 250.9 | 22137 | +483 | -37.9 | strong |
| Put | 22400 | 15473 | 3228 | 237.8 | 22763 | 274.1 | 22162 | +458 | -36.3 | strong |
| Put | 22450 | 584 | 124 | 262.5 | 22732 | 286.1 | 22187 | +433 | -23.5 | strong |
| Put | 22500 | 42222 | 14833 | 248.3 | 22824 | 305.5 | 22252 | +368 | -57.1 | strong |
| Put | 22550 | 765 | 271 | 223.5 | 22935 | 330.6 | 22327 | +294 | -107.1 | strong |
| Put | 22600 | 24520 | 15222 | 338.6 | 22670 | 346.9 | 22261 | +359 | -8.3 | strong |
| Put | 22650 | 2366 | 1792 | 333.9 | 22730 | 372.0 | 22316 | +304 | -38.1 | strong |
| Put | 22700 | 26440 | 19409 | 348.3 | 22726 | 387.6 | 22352 | +268 | -39.3 | strong |
| Put | 22750 | 1074 | 577 | 310.1 | 22872 | 408.9 | 22440 | +180 | -98.8 | strong |
| Put | 22800 | 19907 | 10040 | 392.0 | 22727 | 436.0 | 22408 | +212 | -44.0 | strong |
| Put | 22850 | 2262 | 135 | 396.0 | 22770 | 461.0 | 22454 | +166 | -65.0 | strong |
| Put | 22900 | 7352 | 3364 | 408.0 | 22790 | 484.8 | 22492 | +128 | -76.7 | strong |
| Put | 22950 | 615 | 136 | 382.7 | 22867 | 523.8 | 22567 | +53 | -141.1 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 8 | 75% | +0.05% | -0.44 to +0.28% |  | too few (8/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 4 | 100% | +0.46% | +0.09 to +1.02% |  | too few (3/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 67% | +0.04% | -0.18 to +0.22% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | -0.03% | -0.21 to +0.17% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 4 | 50% | -0.01% | -0.44 to +0.32% |  | too few (4/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 4 | 50% | +0.09% | -0.74 to +0.62% |  | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 3 | 67% | +0.01% | -0.24 to +0.15% |  | too few (3/10) |
| weekly | PCR up · put writing · walls same · near put wall | 3 | 0% | -0.37% | -0.47 to -0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 0% | -0.53% | -0.78 to -0.27% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 2 | 50% | -0.06% | -0.37 to +0.25% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · mid walls | 2 | 100% | +0.05% | +0.04 to +0.05% | 0% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 50% | -0.06% | -0.23 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.38% | -0.70 to -0.07% |  | too few (2/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 2 | 50% | -0.17% | -0.39 to +0.04% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 2 | 0% | -0.71% | -0.71 to -0.71% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 1 | 0% | -0.03% | -0.03 to -0.03% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 0% | -0.04% | -0.04 to -0.04% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.07% | -0.07 to -0.07% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 0% | -0.18% | -0.18 to -0.18% |  | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.78% | -0.78 to -0.78% |  | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.85% | -0.85 to -0.85% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 23 | 38% | -0.13% | no clear direction |
| intraday | weekly | call writers stronger · weak puts | 21 | 61% | +0.12% | no clear direction |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | writers even · few weak writers | 11 | 9% | -0.53% | down |
| intraday | weekly | call writers stronger · few weak writers | 10 | 44% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | writers even · weak puts | 7 | 57% | +0.10% | too few (7/10) |
| intraday | weekly | writers even · weak puts | 6 | 33% | -0.28% | too few (6/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts | 2 | 100% | +0.39% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 3 | 0% | -0.59% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · few weak writers | 2 | 0% | -0.85% | too few (1/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
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
