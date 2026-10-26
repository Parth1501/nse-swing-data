# Nifty option chain pattern log
Updated 2026-10-26 09:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 176 snapshots over 8 trading days
- 191 patterns logged; 100 different patterns so far

## Latest read (2026-10-26 09:45:18)

Nifty trend: weekly **bearish**, 125-min **down**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (weekly) | 1.2 | 22474 | 1.098 | 22600 | 22400 | 23000 | ±1.19% (22206-22742) | 28.98 |
| 2026-11-23 (monthly) | 28.2 | 22473 | 1.422 | 23000 | 22000 | 23000 | ±3.92% (21591-23354) | 17.87 |

- **Weekly, last 30 min**: `PCR up · put and call writing · walls same · near put wall`. Seen 1 times before; Nifty was up after it 0% of the time, average -1.22%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 10 times before; Nifty was up after it 67% of the time, average -0.04%. Too few outcomes (9/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m down`: Seen 6 times before; Nifty was up after it 80% of the time, average +0.08%. Too few outcomes (5/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.56%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m down`: Seen 1 times before; Nifty was up after it 0% of the time, average -0.56%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · call writing · walls same · mid walls`. Seen 5 times before; Nifty was up after it 80% of the time, average +0.41%. Too few outcomes (5/20) to trade on.
  - Writers: `writers even · weak puts`. Seen 16 times before; Nifty was up after it 75% of the time, average +0.29%. Too few outcomes (16/20) to trade on.
  - Same, only when the trend was `weekly bearish · 125m down`: Seen 11 times before; Nifty was up after it 91% of the time, average +0.37%. Too few outcomes (11/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak puts`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly bearish · 125m down`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-10-27

Strongest call writers at 23000, strongest put writers at 22400; weakest call writers at -, weakest put writers at 22600. Covers 96% of near-money call OI and 94% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22150 | 930 | 814 | 455.7 | 22527 | 404.4 | 22606 | +132 | +51.3 | strong |
| Call | 22200 | 10736 | 5803 | 401.6 | 22514 | 360.1 | 22602 | +127 | +41.5 | strong |
| Call | 22250 | 4638 | 4209 | 335.6 | 22480 | 320.6 | 22586 | +111 | +15.0 | strong |
| Call | 22300 | 24323 | 19670 | 291.1 | 22473 | 281.0 | 22591 | +117 | +10.1 | strong |
| Call | 22350 | 15154 | 14915 | 249.2 | 22470 | 240.9 | 22599 | +125 | +8.3 | strong |
| Call | 22400 | 85800 | 83312 | 212.2 | 22469 | 204.8 | 22612 | +138 | +7.5 | strong |
| Call | 22450 | 88647 | 88511 | 177.2 | 22472 | 171.4 | 22627 | +153 | +5.8 | strong |
| Call | 22500 | 277898 | 271275 | 164.8 | 22491 | 143.0 | 22665 | +191 | +21.8 | strong |
| Call | 22550 | 95118 | 94915 | 140.5 | 22493 | 116.3 | 22690 | +216 | +24.1 | strong |
| Call | 22600 | 180777 | 178843 | 123.0 | 22500 | 94.8 | 22723 | +249 | +28.2 | strong |
| Call | 22650 | 78959 | 78803 | 109.3 | 22510 | 76.8 | 22759 | +285 | +32.5 | strong |
| Call | 22700 | 202625 | 197084 | 117.4 | 22566 | 59.5 | 22817 | +343 | +57.8 | strong |
| Call | 22750 | 88572 | 87430 | 102.7 | 22588 | 46.0 | 22853 | +378 | +56.7 | strong |
| Call | 22800 | 208856 | 202397 | 99.3 | 22608 | 35.5 | 22899 | +425 | +63.8 | strong |
| Put | 22150 | 43727 | 43157 | 25.1 | 22614 | 26.9 | 22125 | +349 | -1.8 | strong |
| Put | 22200 | 147231 | 137592 | 30.4 | 22647 | 33.5 | 22170 | +305 | -3.1 | strong |
| Put | 22250 | 73260 | 71988 | 40.8 | 22562 | 41.8 | 22209 | +265 | -1.0 | strong |
| Put | 22300 | 165883 | 148078 | 48.1 | 22592 | 51.3 | 22252 | +222 | -3.2 | strong |
| Put | 22350 | 105504 | 104783 | 65.5 | 22514 | 64.2 | 22284 | +190 | +1.4 | strong |
| Put | 22400 | 280006 | 272176 | 77.3 | 22537 | 79.3 | 22323 | +152 | -2.0 | strong |
| Put | 22450 | 147727 | 147469 | 94.8 | 22522 | 96.5 | 22355 | +119 | -1.6 | strong |
| Put | 22500 | 276866 | 255389 | 96.0 | 22610 | 116.1 | 22404 | +70 | -20.1 | medium |
| Put | 22550 | 52901 | 52577 | 114.7 | 22593 | 139.7 | 22435 | +39 | -25.0 | weak |
| Put | 22600 | 114378 | 107388 | 120.8 | 22678 | 167.2 | 22479 | -5 | -46.4 | weak |
| Put | 22650 | 24687 | 24356 | 129.3 | 22692 | 196.8 | 22521 | -46 | -67.4 | weak |
| Put | 22700 | 81828 | 77299 | 139.1 | 22721 | 231.3 | 22561 | -87 | -92.2 | weak |
| Put | 22750 | 21170 | 21086 | 158.9 | 22720 | 267.8 | 22591 | -117 | -108.9 | weak |
| Put | 22800 | 68261 | 62723 | 168.1 | 22768 | 307.0 | 22632 | -158 | -138.9 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 23000, strongest put writers at 22500; weakest call writers at -, weakest put writers at 23000. Covers 60% of near-money call OI and 51% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 22150 | 39 | 30 | 718.5 | 22498 | 683.0 | 22868 | +396 | +35.5 | strong |
| Call | 22200 | 2284 | 652 | 723.1 | 22562 | 691.5 | 22923 | +451 | +31.6 | strong |
| Call | 22250 | 140 | 53 | 693.9 | 22619 | 622.9 | 22944 | +471 | +71.0 | strong |
| Call | 22300 | 1609 | 842 | 662.8 | 22577 | 620.0 | 22963 | +490 | +42.8 | strong |
| Call | 22350 | 194 | 144 | 614.1 | 22557 | 580.1 | 22964 | +492 | +34.0 | strong |
| Call | 22400 | 3512 | 2289 | 538.4 | 22466 | 559.8 | 22938 | +466 | -21.4 | strong |
| Call | 22450 | 480 | 415 | 545.9 | 22546 | 530.0 | 22996 | +523 | +16.0 | strong |
| Call | 22500 | 26877 | 16636 | 537.7 | 22590 | 497.8 | 23038 | +565 | +39.9 | strong |
| Call | 22550 | 919 | 752 | 477.8 | 22519 | 465.1 | 23028 | +555 | +12.8 | strong |
| Call | 22600 | 29184 | 20568 | 476.1 | 22616 | 442.5 | 23076 | +604 | +33.6 | strong |
| Call | 22650 | 4375 | 4079 | 455.8 | 22602 | 416.2 | 23106 | +633 | +39.6 | strong |
| Call | 22700 | 28677 | 25029 | 450.1 | 22674 | 387.6 | 23150 | +678 | +62.5 | strong |
| Call | 22750 | 1290 | 635 | 407.4 | 22607 | 365.9 | 23157 | +685 | +41.5 | strong |
| Call | 22800 | 21437 | 16329 | 396.8 | 22670 | 339.4 | 23197 | +724 | +57.4 | strong |
| Put | 22150 | 836 | 372 | 196.0 | 22678 | 264.9 | 21954 | +519 | -69.0 | strong |
| Put | 22200 | 13867 | 6056 | 229.4 | 22610 | 266.6 | 21971 | +502 | -37.2 | strong |
| Put | 22250 | 1878 | 453 | 220.1 | 22703 | 292.2 | 22030 | +443 | -72.1 | strong |
| Put | 22300 | 17635 | 10693 | 235.6 | 22673 | 299.1 | 22064 | +408 | -63.5 | strong |
| Put | 22350 | 846 | 344 | 253.6 | 22667 | 313.4 | 22096 | +376 | -59.8 | strong |
| Put | 22400 | 17536 | 5491 | 272.3 | 22652 | 334.6 | 22128 | +345 | -62.2 | strong |
| Put | 22450 | 747 | 370 | 313.8 | 22577 | 352.0 | 22136 | +336 | -38.2 | strong |
| Put | 22500 | 51841 | 25167 | 290.1 | 22701 | 373.2 | 22210 | +263 | -83.1 | strong |
| Put | 22550 | 1142 | 732 | 331.9 | 22631 | 391.2 | 22218 | +254 | -59.3 | strong |
| Put | 22600 | 27064 | 18074 | 350.1 | 22640 | 412.1 | 22250 | +223 | -62.0 | strong |
| Put | 22650 | 4673 | 4140 | 360.6 | 22630 | 434.8 | 22289 | +183 | -74.1 | strong |
| Put | 22700 | 29103 | 22517 | 355.1 | 22712 | 460.4 | 22345 | +128 | -105.3 | strong |
| Put | 22750 | 967 | 608 | 343.9 | 22791 | 503.9 | 22406 | +66 | -159.9 | medium |
| Put | 22800 | 20585 | 11972 | 401.2 | 22708 | 507.9 | 22399 | +74 | -106.7 | medium |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 9 | 78% | +0.07% | -0.44 to +0.28% |  | too few (9/10) |
| weekly | PCR up · put writing · walls same · near call wall | 7 | 100% | +0.23% | +0.03 to +0.42% | 0% of 1 | too few (7/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 80% | +0.41% | -0.37 to +0.89% |  | too few (5/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 6 | 83% | +0.35% | -0.39 to +0.91% |  | too few (6/10) |
| monthly | PCR flat · put writing · walls same · mid walls | 5 | 100% | +0.44% | +0.09 to +1.02% |  | too few (4/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 5 | 80% | +0.13% | -0.21 to +0.46% |  | too few (5/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 5 | 60% | +0.11% | -0.14 to +0.32% |  | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 5 | 40% | -0.02% | -0.74 to +0.62% |  | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 4 | 100% | +0.18% | +0.07 to +0.30% |  | too few (4/10) |
| weekly | PCR up · put writing · walls same · near put wall | 4 | 50% | -0.15% | -0.47 to +0.19% | 0% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 4 | 50% | +0.25% | -0.40 to +0.90% | 100% of 1 | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 4 | 75% | +0.15% | -0.24 to +0.56% |  | too few (4/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 4 | 50% | +0.08% | -0.78 to +0.90% |  | too few (4/10) |
| monthly | PCR down · call writing · walls same · mid walls | 4 | 50% | -0.06% | -0.47 to +0.14% |  | too few (4/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 3 | 100% | +0.24% | +0.14 to +0.32% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 100% | +0.05% | +0.02 to +0.08% |  | too few (2/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 0% | -0.65% | -0.71 to -0.57% |  | too few (3/10) |
| weekly | PCR down · call writing · walls down · near put wall | 3 | 33% | -0.17% | -0.51 to +0.25% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR down · call writing · walls same · mid walls | 3 | 100% | +0.38% | +0.04 to +0.73% | 0% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% |  | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 3 | 100% | +0.28% | +0.27 to +0.29% |  | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | -0.17% | -1.11 to +0.78% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 0% | -0.45% | -0.75 to -0.14% |  | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 2 | 50% | -0.01% | -0.11 to +0.09% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 2 | 100% | +0.12% | +0.09 to +0.15% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 2 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 2 | 100% | +0.07% | +0.07 to +0.07% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 2 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR down · call writing · walls down · mid walls | 2 | 50% | +0.24% | -0.07 to +0.54% |  | too few (2/10) |
| monthly | PCR down · put writing · walls same · mid walls | 2 | 100% | +0.11% | +0.01 to +0.21% |  | too few (2/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 2 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls same · near call wall | 2 | 50% | -0.38% | -0.78 to +0.02% |  | too few (2/10) |
| weekly | PCR down · call writing · walls same · near call wall | 2 | 100% | +0.53% | +0.51 to +0.55% |  | too few (2/10) |
| monthly | PCR up · put writing · walls same · near call wall | 2 | 0% | -0.23% | -0.40 to -0.07% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 1 | 100% | +0.15% | +0.15 to +0.15% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.38% | +0.38 to +0.38% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.50% | +0.50 to +0.50% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near call wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · mid walls | 1 | 100% | +0.24% | +0.24 to +0.24% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 1 | 0% | -0.69% | -0.69 to -0.69% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% |  | too few (1/10) |
| weekly | PCR down · call writing · walls up · near put wall | 1 | 100% | +0.27% | +0.27 to +0.27% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.37% | -0.37 to -0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 1 | 0% | -0.68% | -0.68 to -0.68% |  | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +0.13% | +0.13 to +0.13% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.29% | +0.29 to +0.29% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · mid walls | 1 | 100% | +0.12% | +0.12 to +0.12% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +1.03% | +1.03 to +1.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% |  | too few (1/10) |
| weekly | PCR up · put writing · walls down · near call wall | 1 | 100% | +0.15% | +0.15 to +0.15% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.57% | -0.57 to -0.57% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 1 | 100% | +0.53% | +0.53 to +0.53% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · near put wall | 1 | 0% | -0.01% | -0.01 to -0.01% | 0% of 1 | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 0% | -0.56% | -0.56 to -0.56% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 0% | -0.56% | -0.56 to -0.56% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% |  | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | call writers stronger · weak puts | 31 | 83% | +0.33% | up |
| intraday | monthly | writers even · few weak writers | 30 | 59% | -0.04% | no clear direction |
| intraday | monthly | writers even · weak calls | 20 | 89% | +0.05% | up |
| intraday | weekly | put writers stronger · weak calls | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · weak puts | 17 | 75% | +0.29% | up |
| intraday | weekly | writers even · few weak writers | 15 | 21% | -0.46% | down |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | call writers stronger · few weak writers | 11 | 50% | +0.04% | no clear direction |
| intraday | weekly | writers even · weak puts | 11 | 67% | -0.04% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers | 10 | 89% | -0.02% | too few (9/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | monthly | put writers stronger · few weak writers | 5 | 40% | -0.41% | too few (5/10) |
| intraday | monthly | put writers stronger · weak calls | 4 | 25% | -0.08% | too few (4/10) |
| day | monthly | writers even · few weak writers | 3 | 0% | -0.50% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | monthly | writers even · weak calls | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 0% | -0.56% | too few (1/10) |
| day | monthly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers | 1 | 0% | -0.39% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 20 | 89% | +0.05% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 88% | +0.40% | up |
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 18 | 76% | +0.13% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 16 | 62% | -0.03% | no clear direction |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 91% | +0.37% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 11 | 90% | +0.32% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 10 | 89% | -0.02% | too few (9/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 8 | 57% | +0.20% | too few (7/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 7 | 71% | +0.00% | too few (7/10) |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 7 | 43% | -0.11% | too few (7/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 7 | 14% | -0.40% | too few (7/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 7 | 80% | +0.08% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 4 | 25% | -0.08% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 3 | 0% | -0.20% | too few (3/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.92% | too few (3/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 3 | 67% | -0.18% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 2 | 100% | +0.23% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.27% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 0% | -0.50% | too few (3/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 2 | 50% | -0.23% | too few (2/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 2 | 0% | -0.56% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · weak puts · weekly bearish · 125m down | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +0.65% | too few (1/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 1 | 0% | -1.11% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
