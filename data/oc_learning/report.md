# Nifty option chain pattern log
Updated 2026-11-18 14:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 591 snapshots over 24 trading days
- 655 patterns logged; 178 different patterns so far

## Latest read (2026-11-18 14:45:18)

Nifty trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-23 (weekly) | 5.0 | 25238 | 0.875 | 25150 | 25000 | 26000 | ±1.32% (24906-25570) | 14.16 |
| 2026-12-29 (monthly) | 41.0 | 25240 | 1.301 | 25200 | 25000 | 27000 | ±3.7% (24305-26175) | 13.79 |

- **Weekly, last 30 min**: `PCR up · put writing · walls same · near put wall`. Seen 13 times before; Nifty was up after it 62% of the time, average +0.05%. Too few outcomes (13/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 105 times before; Nifty was up after it 55% of the time, average +0.05%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 15 times before; Nifty was up after it 57% of the time, average +0.06%. Too few outcomes (14/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 6 times before; Nifty was up after it 67% of the time, average +0.57%. Too few outcomes (6/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 1 times before; Nifty was up after it 100% of the time, average +0.58%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls up · near put wall`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.09%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 118 times before; Nifty was up after it 65% of the time, average +0.13%. History points to a bull call debit spread, ATM to about the call wall 27000.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 7 times before; Nifty was up after it 57% of the time, average +0.10%. Too few outcomes (7/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 10 times before; Nifty was up after it 50% of the time, average +0.25%. Too few outcomes (10/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-23

Strongest call writers at 25500, strongest put writers at 25000; weakest call writers at 25000, weakest put writers at 25400. Covers 99% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24900 | 15244 | 15206 | 312.3 | 24828 | 395.1 | 25212 | -26 | -82.8 | weak |
| Call | 24950 | 1884 | 1882 | 318.3 | 25044 | 363.5 | 25268 | +30 | -45.2 | weak |
| Call | 25000 | 52942 | 47031 | 185.0 | 24455 | 321.9 | 25185 | -53 | -136.9 | weak |
| Call | 25050 | 4589 | 4587 | 270.8 | 25181 | 286.9 | 25321 | +83 | -16.1 | medium |
| Call | 25100 | 27179 | 27148 | 243.7 | 25119 | 253.2 | 25344 | +105 | -9.5 | medium |
| Call | 25150 | 22172 | 22166 | 199.3 | 25186 | 221.4 | 25349 | +111 | -22.1 | medium |
| Call | 25200 | 99027 | 99005 | 195.5 | 25186 | 193.1 | 25396 | +157 | +2.4 | strong |
| Call | 25250 | 71984 | 71983 | 170.5 | 25230 | 166.8 | 25420 | +182 | +3.6 | strong |
| Call | 25300 | 144370 | 144363 | 168.5 | 25233 | 143.1 | 25468 | +230 | +25.4 | strong |
| Call | 25350 | 72230 | 72101 | 132.7 | 25233 | 121.8 | 25483 | +244 | +10.9 | strong |
| Call | 25400 | 150338 | 149825 | 138.2 | 25257 | 103.2 | 25538 | +300 | +35.0 | strong |
| Call | 25450 | 67180 | 67173 | 128.2 | 25292 | 86.0 | 25578 | +340 | +42.1 | strong |
| Call | 25500 | 212019 | 209286 | 99.3 | 25159 | 71.7 | 25599 | +361 | +27.6 | strong |
| Call | 25550 | 41347 | 41264 | 80.8 | 25246 | 59.9 | 25631 | +393 | +20.9 | strong |
| Call | 25600 | 87446 | 87411 | 86.2 | 25253 | 49.4 | 25686 | +448 | +36.9 | strong |
| Put | 24900 | 68753 | 68669 | 101.2 | 25228 | 49.0 | 24799 | +439 | +52.2 | strong |
| Put | 24950 | 26729 | 26570 | 80.8 | 25252 | 59.5 | 24869 | +369 | +21.3 | strong |
| Put | 25000 | 177395 | 170880 | 271.8 | 25074 | 71.7 | 24728 | +510 | +200.1 | strong |
| Put | 25050 | 27955 | 27953 | 93.8 | 25269 | 85.8 | 24956 | +282 | +8.0 | strong |
| Put | 25100 | 74143 | 73178 | 122.1 | 25289 | 102.3 | 24978 | +260 | +19.8 | strong |
| Put | 25150 | 42191 | 42190 | 136.8 | 25252 | 121.1 | 25013 | +225 | +15.7 | strong |
| Put | 25200 | 122819 | 122806 | 155.1 | 25287 | 142.2 | 25045 | +193 | +12.9 | strong |
| Put | 25250 | 61764 | 61761 | 171.9 | 25256 | 165.2 | 25078 | +160 | +6.8 | strong |
| Put | 25300 | 86488 | 86453 | 196.4 | 25285 | 191.8 | 25104 | +135 | +4.6 | strong |
| Put | 25350 | 24733 | 24732 | 225.0 | 25271 | 220.6 | 25125 | +113 | +4.4 | medium |
| Put | 25400 | 52770 | 51921 | 207.1 | 25364 | 251.8 | 25193 | +45 | -44.7 | weak |
| Put | 25450 | 32886 | 32883 | 205.8 | 25388 | 285.6 | 25244 | -6 | -79.8 | weak |
| Put | 25500 | 66248 | 60934 | 393.4 | 25238 | 320.8 | 25107 | +132 | +72.7 | strong |
| Put | 25550 | 3166 | 3164 | 289.6 | 25361 | 358.6 | 25260 | -22 | -69.1 | weak |
| Put | 25600 | 10807 | 10781 | 343.3 | 25361 | 401.4 | 25257 | -18 | -58.1 | weak |

## Strong vs weak writers, monthly 2026-12-29

Strongest call writers at 25500, strongest put writers at 25500; weakest call writers at -, weakest put writers at -. Covers 14% of near-money call OI and 11% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24900 | 1242 | 53 | 730.1 | 25198 | 765.0 | 25630 | +390 | -34.9 | strong |
| Call | 24950 | 375 | 12 | 683.6 | 25185 | 700.0 | 25634 | +394 | -16.4 | strong |
| Call | 25000 | 43543 | 1152 | 689.8 | 25242 | 695.0 | 25690 | +450 | -5.3 | strong |
| Call | 25050 | 209 | 19 | 654.4 | 25219 | 666.0 | 25704 | +465 | -11.6 | strong |
| Call | 25100 | 1851 | 64 | 623.6 | 25227 | 633.0 | 25724 | +484 | -9.4 | strong |
| Call | 25150 | 311 | 73 | 570.9 | 25193 | 610.0 | 25721 | +481 | -39.1 | strong |
| Call | 25200 | 7492 | 1203 | 557.3 | 25225 | 573.5 | 25757 | +517 | -16.2 | strong |
| Call | 25250 | 562 | 242 | 530.2 | 25228 | 548.0 | 25780 | +540 | -17.8 | strong |
| Call | 25300 | 6987 | 1683 | 502.9 | 25229 | 516.1 | 25803 | +563 | -13.3 | strong |
| Call | 25350 | 811 | 266 | 466.4 | 25213 | 483.0 | 25816 | +577 | -16.6 | strong |
| Call | 25400 | 5309 | 1413 | 445.9 | 25217 | 461.2 | 25846 | +606 | -15.3 | strong |
| Call | 25450 | 1318 | 512 | 420.1 | 25216 | 434.1 | 25870 | +630 | -14.0 | strong |
| Call | 25500 | 53982 | 10813 | 398.0 | 25221 | 413.0 | 25898 | +658 | -15.0 | strong |
| Call | 25550 | 1297 | 737 | 375.2 | 25232 | 397.4 | 25925 | +685 | -22.2 | strong |
| Call | 25600 | 5551 | 1333 | 354.8 | 25219 | 368.2 | 25955 | +715 | -13.4 | strong |
| Put | 24900 | 3020 | 89 | 266.1 | 25222 | 260.0 | 24634 | +606 | +6.1 | strong |
| Put | 24950 | 820 | 29 | 294.6 | 25197 | 275.2 | 24655 | +584 | +19.4 | strong |
| Put | 25000 | 65476 | 1958 | 296.1 | 25227 | 290.7 | 24704 | +536 | +5.4 | strong |
| Put | 25050 | 574 | 29 | 325.4 | 25196 | 307.8 | 24725 | +515 | +17.6 | strong |
| Put | 25100 | 2737 | 128 | 318.3 | 25257 | 326.5 | 24782 | +458 | -8.2 | strong |
| Put | 25150 | 399 | 86 | 366.9 | 25190 | 341.2 | 24783 | +457 | +25.7 | strong |
| Put | 25200 | 8738 | 2492 | 378.4 | 25213 | 365.9 | 24822 | +418 | +12.4 | strong |
| Put | 25250 | 725 | 187 | 380.4 | 25249 | 386.9 | 24870 | +370 | -6.5 | strong |
| Put | 25300 | 9440 | 1094 | 404.5 | 25255 | 407.4 | 24896 | +344 | -2.9 | strong |
| Put | 25350 | 723 | 192 | 448.1 | 25210 | 431.0 | 24902 | +338 | +17.1 | strong |
| Put | 25400 | 11214 | 2249 | 475.6 | 25199 | 454.6 | 24924 | +315 | +21.0 | strong |
| Put | 25450 | 836 | 349 | 492.4 | 25216 | 479.4 | 24958 | +282 | +13.1 | strong |
| Put | 25500 | 66746 | 10975 | 511.4 | 25225 | 503.4 | 24989 | +251 | +8.0 | strong |
| Put | 25550 | 1122 | 675 | 532.4 | 25234 | 525.0 | 25018 | +222 | +7.4 | strong |
| Put | 25600 | 4852 | 797 | 561.0 | 25231 | 555.2 | 25039 | +201 | +5.7 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 37 | 67% | +0.23% | -0.44 to +0.97% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 20 | 85% | +0.28% | -0.27 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 18 | 83% | +0.36% | -0.50 to +1.68% |  | up |
| monthly | PCR flat · put writing · walls same · mid walls | 18 | 88% | +0.35% | -0.42 to +1.02% | 100% of 1 | up |
| weekly | PCR down · call writing · walls same · near put wall | 18 | 67% | +0.25% | -0.37 to +0.85% | 50% of 4 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near call wall | 16 | 56% | +0.28% | -0.71 to +1.70% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 14 | 62% | +0.05% | -0.47 to +0.42% | 50% of 4 | no clear direction |
| monthly | PCR flat · put writing · walls same · near call wall | 12 | 70% | +0.38% | -0.50 to +1.56% |  | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near put wall | 12 | 80% | +0.08% | -0.18 to +0.20% |  | no clear direction |
| weekly | PCR down · unwinding · walls same · near call wall | 11 | 70% | +0.39% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| monthly | PCR up · put writing · walls same · near call wall | 11 | 50% | +0.18% | -0.40 to +0.93% | 100% of 1 | no clear direction |
| monthly | PCR up · put and call writing · walls same · mid walls | 11 | 73% | +0.16% | -0.24 to +0.63% | 100% of 1 | no clear direction |
| monthly | PCR up · quiet OI · walls same · mid walls | 10 | 80% | +0.25% | -0.39 to +0.91% | 100% of 1 | no clear direction |
| weekly | PCR down · call writing · walls same · mid walls | 10 | 80% | +0.21% | -0.43 to +0.75% | 50% of 4 | no clear direction |
| weekly | PCR down · unwinding · walls same · mid walls | 10 | 50% | +0.04% | -0.40 to +0.90% | 75% of 4 | too few (6/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 10 | 57% | +0.11% | -0.16 to +0.71% | 100% of 1 | too few (7/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 10 | 40% | +0.03% | -0.78 to +0.90% | 100% of 2 | no clear direction |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 9 | 78% | +0.19% | -0.21 to +0.90% | 100% of 1 | too few (9/10) |
| weekly | PCR down · call writing · walls down · mid walls | 9 | 78% | +0.24% | -0.07 to +0.54% | 67% of 3 | too few (9/10) |
| monthly | PCR down · call writing · walls same · mid walls | 8 | 38% | +0.01% | -0.47 to +0.49% | 100% of 1 | too few (8/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 8 | 75% | +0.22% | -1.22 to +1.24% | 50% of 2 | too few (8/10) |
| weekly | PCR up · put writing · walls up · near put wall | 8 | 62% | +0.33% | -0.13 to +1.65% | 0% of 4 | too few (8/10) |
| weekly | PCR up · put writing · walls up · mid walls | 8 | 62% | +0.31% | -0.26 to +1.40% | 33% of 3 | too few (8/10) |
| monthly | PCR up · put writing · walls same · mid walls | 8 | 75% | +0.42% | -0.29 to +0.85% | 100% of 1 | too few (8/10) |
| monthly | PCR down · call writing · walls same · near call wall | 8 | 83% | +0.27% | -0.78 to +1.18% | 100% of 1 | too few (6/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% |  | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (7/10) |
| weekly | PCR up · put writing · walls same · mid walls | 7 | 43% | -0.06% | -0.57 to +0.89% | 67% of 3 | too few (7/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 7 | 86% | +0.51% | -0.37 to +1.25% | 100% of 1 | too few (7/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| weekly | PCR down · call writing · walls down · near call wall | 6 | 83% | +0.53% | -0.06 to +1.68% | 67% of 3 | too few (6/10) |
| weekly | PCR down · call writing · walls down · near put wall | 5 | 60% | +0.09% | -0.51 to +0.73% | 0% of 2 | too few (5/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 5 | 80% | +0.12% | -0.05 to +0.28% |  | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 100% of 1 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 5 | 80% | +0.46% | -1.11 to +1.69% | 0% of 2 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 5 | 75% | +0.21% | -0.05 to +0.63% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 5 | 100% | +0.29% | +0.04 to +0.59% | 0% of 4 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 5 | 80% | +0.22% | -0.11 to +0.50% | 33% of 3 | too few (5/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 5 | 100% | +0.54% | +0.47 to +0.61% | 67% of 3 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 5 | 25% | +0.07% | -0.10 to +0.43% | 33% of 3 | too few (4/10) |
| weekly | PCR down · call writing · walls same · near call wall | 5 | 80% | +0.53% | -0.02 to +0.91% | 33% of 3 | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 5 | 60% | +0.15% | -0.07 to +0.33% |  | too few (5/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 5 | 40% | +0.06% | -0.68 to +0.75% | 50% of 2 | too few (5/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 4 | 50% | +0.06% | -0.63 to +0.58% | 50% of 2 | too few (4/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 4 | 100% | +0.50% | +0.37 to +0.62% |  | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 4 | 25% | -0.15% | -0.75 to +0.38% | 50% of 2 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 4 | 75% | +0.84% | -0.07 to +1.82% | 33% of 3 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 100% | +0.79% | +0.14 to +1.65% |  | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 4 | 100% | +0.24% | +0.10 to +0.28% |  | too few (4/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 4 | 75% | +0.10% | -0.02 to +0.28% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 4 | 75% | +0.22% | -0.22 to +0.68% | 75% of 4 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 4 |  |  |  | 100% of 4 | too few (0/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 3 | 33% | -0.01% | -0.37 to +0.53% | 50% of 2 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 3 | 100% | +0.28% | +0.07 to +0.50% | 100% of 2 | too few (2/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 3 | 50% | -0.03% | -0.43 to +0.37% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 3 | 100% | +0.19% | +0.16 to +0.25% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 3 | 67% | +0.10% | -0.00 to +0.22% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 3 | 100% | +0.12% | +0.05 to +0.16% | 100% of 2 | too few (3/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 3 | 67% | +0.06% | -0.13 to +0.17% |  | too few (3/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 3 | 100% | +0.61% | +0.01 to +1.22% | 50% of 2 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 3 | 0% | -0.34% | -0.69 to -0.14% | 0% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls same · mid walls | 2 | 100% | +0.30% | +0.29 to +0.31% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 2 | 100% | +0.20% | +0.20 to +0.20% | 100% of 2 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 2 | 100% | +0.15% | +0.10 to +0.21% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near put wall | 2 | 100% | +0.21% | +0.18 to +0.24% |  | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% |  | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · near put wall | 2 | 0% | -0.09% | -0.09 to -0.09% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 2 | 50% | +0.04% | -0.19 to +0.28% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near call wall | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +1.86% | +1.86 to +1.86% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.18% | +0.18 to +0.18% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.40% | +0.40 to +0.40% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near put wall | 1 | 0% | -0.29% | -0.29 to -0.29% | 100% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · quiet OI · walls same · mid walls | 1 | 100% | +0.17% | +0.17 to +0.17% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | +0.73% | -0.39 to +2.40% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 2 | 50% | -0.12% | -0.61 to +0.38% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 2 | 50% | +0.05% | -0.59 to +0.68% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 100% | +0.55% | +0.51 to +0.58% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.55% | -0.59 to +1.68% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 100% | +0.35% | +0.06 to +0.65% | 100% of 2 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls down · near call wall | 1 | 100% | +0.58% | +0.58 to +0.58% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.38% | +0.38 to +0.38% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 119 | 65% | +0.13% | up |
| intraday | weekly | writers even · few weak writers | 106 | 55% | +0.05% | no clear direction |
| intraday | monthly | writers even · weak calls | 101 | 74% | +0.17% | up |
| intraday | weekly | put writers stronger · weak calls | 64 | 73% | +0.34% | up |
| intraday | monthly | put writers stronger · weak calls | 63 | 85% | +0.57% | up |
| intraday | weekly | call writers stronger · weak puts | 38 | 89% | +0.40% | up |
| intraday | weekly | call writers stronger · few weak writers | 33 | 81% | +0.25% | up |
| intraday | weekly | put writers stronger · few weak writers | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · weak calls | 26 | 83% | +0.44% | up |
| intraday | weekly | writers even · weak puts | 20 | 82% | +0.31% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | monthly | call writers stronger · few weak writers | 15 | 62% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak on both sides | 11 | 73% | +0.20% | no clear direction |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| intraday | weekly | put writers stronger · weak on both sides | 1 | 0% | -0.29% | too few (1/10) |
| day | monthly | writers even · few weak writers | 11 | 50% | +0.25% | no clear direction |
| day | monthly | writers even · weak calls | 7 | 71% | +0.52% | too few (7/10) |
| day | weekly | writers even · few weak writers | 7 | 67% | +0.57% | too few (6/10) |
| day | weekly | put writers stronger · weak calls | 5 | 80% | +0.40% | too few (5/10) |
| day | monthly | put writers stronger · weak calls | 4 | 100% | +0.88% | too few (4/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | writers even · weak puts | 3 | 33% | -0.04% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · few weak writers | 2 | 100% | +0.92% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak calls | 2 | 50% | +1.00% | too few (2/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 57 | 78% | +0.39% | up |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 49 | 85% | +0.68% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 45 | 93% | +0.31% | up |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m up | 39 | 49% | +0.04% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 38 | 47% | -0.02% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 28 | 77% | +0.29% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 17 | 40% | -0.05% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m sideways | 17 | 88% | +0.14% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 16 | 57% | +0.06% | no clear direction |
| intraday | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 14 | 83% | +0.16% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.73% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 8 | 57% | +0.10% | too few (7/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 8 | 100% | +0.21% | too few (8/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 8 | 75% | +0.16% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 7 | 20% | -0.17% | too few (5/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 6 | 80% | +0.16% | too few (5/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 5 | 100% | +0.53% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 5 | 40% | +0.01% | too few (5/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.07% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m sideways | 1 | 100% | +0.28% | too few (1/10) |
| intraday | weekly | put writers stronger · weak on both sides · weekly sideways · 125m up | 1 | 0% | -0.29% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m up | 1 | 100% | +0.91% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +1.32% | too few (2/10) |
| day | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.10% | too few (2/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m up | 2 | 50% | -0.22% | too few (2/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 2 | 100% | +0.58% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.12% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m sideways | 1 | 100% | +0.58% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.18% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m up | 1 | 100% | +2.01% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.22% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 0% | -0.59% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
