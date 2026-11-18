# Nifty option chain pattern log
Updated 2026-11-18 15:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 594 snapshots over 24 trading days
- 659 patterns logged; 179 different patterns so far

## Latest read (2026-11-18 15:40:00)

Nifty trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **sideways**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-23 (weekly) | 5.0 | 25228 | 0.878 | 25050 | 24000 | 26000 | ±1.29% (24902-25554) | 13.84 |
| 2026-12-29 (monthly) | 41.0 | 25228 | 1.3 | 25200 | 24000 | 26000 | ±3.65% (24307-26148) | 13.56 |

- **Weekly, last 30 min**: `PCR flat · unwinding · walls same · mid walls`. Seen 3 times before; Nifty was up after it 100% of the time, average +0.19%. Too few outcomes (3/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 107 times before; Nifty was up after it 54% of the time, average +0.05%. No direction and the walls have not held reliably: no structure.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 17 times before; Nifty was up after it 56% of the time, average +0.04%. Too few outcomes (16/20) to trade on.
- **Weekly, today vs previous day**: `PCR flat · put and call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 6 times before; Nifty was up after it 67% of the time, average +0.57%. Too few outcomes (6/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 1 times before; Nifty was up after it 100% of the time, average +0.58%. Too few outcomes (1/20) to trade on.
- **Monthly, last 30 min**: `PCR flat · quiet OI · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · few weak writers`. Seen 120 times before; Nifty was up after it 64% of the time, average +0.13%. History points to a bull call debit spread, ATM to about the call wall 26000.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 9 times before; Nifty was up after it 44% of the time, average +0.04%. Too few outcomes (9/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 10 times before; Nifty was up after it 50% of the time, average +0.25%. Too few outcomes (10/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-23

Strongest call writers at 25500, strongest put writers at 25000; weakest call writers at 25000, weakest put writers at 25400. Covers 99% of near-money call OI and 98% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24850 | 2294 | 2290 | 343.6 | 24833 | 415.0 | 25194 | -34 | -71.4 | weak |
| Call | 24900 | 14849 | 14812 | 312.3 | 24828 | 374.2 | 25212 | -16 | -61.9 | weak |
| Call | 24950 | 1618 | 1616 | 318.3 | 25044 | 334.6 | 25268 | +40 | -16.2 | weak |
| Call | 25000 | 52760 | 46890 | 185.5 | 24458 | 297.2 | 25186 | -42 | -111.7 | weak |
| Call | 25050 | 3620 | 3618 | 270.8 | 25181 | 263.0 | 25321 | +93 | +7.8 | medium |
| Call | 25100 | 24723 | 24694 | 243.7 | 25119 | 230.0 | 25344 | +116 | +13.7 | strong |
| Call | 25150 | 15118 | 15114 | 199.3 | 25186 | 202.5 | 25349 | +121 | -3.2 | strong |
| Call | 25200 | 88724 | 88705 | 195.4 | 25186 | 174.4 | 25395 | +167 | +21.0 | strong |
| Call | 25250 | 55661 | 55660 | 170.5 | 25230 | 150.1 | 25420 | +193 | +20.4 | strong |
| Call | 25300 | 108607 | 108602 | 168.5 | 25233 | 128.7 | 25468 | +241 | +39.8 | strong |
| Call | 25350 | 53123 | 53028 | 132.7 | 25233 | 109.1 | 25483 | +255 | +23.6 | strong |
| Call | 25400 | 122777 | 122358 | 138.2 | 25257 | 91.0 | 25538 | +310 | +47.2 | strong |
| Call | 25450 | 49168 | 49163 | 128.2 | 25292 | 76.0 | 25578 | +350 | +52.1 | strong |
| Call | 25500 | 199346 | 196776 | 99.3 | 25159 | 63.5 | 25599 | +371 | +35.8 | strong |
| Call | 25550 | 35208 | 35137 | 80.8 | 25246 | 52.4 | 25631 | +403 | +28.4 | strong |
| Call | 25600 | 83519 | 83485 | 86.2 | 25253 | 43.0 | 25686 | +458 | +43.2 | strong |
| Put | 24850 | 20430 | 20429 | 52.9 | 25288 | 40.9 | 24797 | +431 | +12.0 | strong |
| Put | 24900 | 64234 | 64156 | 101.2 | 25228 | 50.3 | 24799 | +429 | +50.9 | strong |
| Put | 24950 | 20611 | 20488 | 80.8 | 25252 | 61.9 | 24869 | +359 | +19.0 | strong |
| Put | 25000 | 163932 | 157911 | 271.8 | 25074 | 74.5 | 24728 | +500 | +197.2 | strong |
| Put | 25050 | 19790 | 19789 | 93.8 | 25269 | 90.1 | 24956 | +272 | +3.7 | strong |
| Put | 25100 | 58780 | 58015 | 122.1 | 25289 | 108.2 | 24978 | +250 | +13.8 | strong |
| Put | 25150 | 27040 | 27040 | 136.8 | 25252 | 128.0 | 25013 | +215 | +8.8 | strong |
| Put | 25200 | 97165 | 97154 | 155.1 | 25287 | 150.5 | 25045 | +183 | +4.6 | strong |
| Put | 25250 | 40168 | 40166 | 171.9 | 25256 | 175.8 | 25078 | +150 | -3.9 | strong |
| Put | 25300 | 65970 | 65943 | 196.4 | 25285 | 203.7 | 25104 | +124 | -7.3 | strong |
| Put | 25350 | 17267 | 17266 | 225.0 | 25271 | 233.1 | 25125 | +103 | -8.1 | medium |
| Put | 25400 | 46643 | 45892 | 207.1 | 25364 | 266.1 | 25193 | +35 | -58.9 | weak |
| Put | 25450 | 22129 | 22127 | 205.8 | 25388 | 301.4 | 25244 | -16 | -95.6 | weak |
| Put | 25500 | 62577 | 57557 | 393.4 | 25238 | 338.5 | 25107 | +121 | +55.0 | strong |
| Put | 25550 | 2769 | 2767 | 289.6 | 25361 | 376.9 | 25260 | -32 | -87.3 | weak |
| Put | 25600 | 10081 | 10056 | 343.3 | 25361 | 418.8 | 25257 | -29 | -75.4 | weak |

## Strong vs weak writers, monthly 2026-12-29

Strongest call writers at 25500, strongest put writers at 25500; weakest call writers at -, weakest put writers at -. Covers 14% of near-money call OI and 12% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24850 | 169 | 10 | 734.9 | 25174 | 799.2 | 25585 | +357 | -64.3 | strong |
| Call | 24900 | 1239 | 55 | 731.3 | 25200 | 743.2 | 25631 | +403 | -11.9 | strong |
| Call | 24950 | 375 | 12 | 683.6 | 25185 | 729.9 | 25634 | +406 | -46.2 | strong |
| Call | 25000 | 43246 | 1144 | 689.8 | 25242 | 675.0 | 25690 | +462 | +14.8 | strong |
| Call | 25050 | 211 | 21 | 654.3 | 25220 | 647.1 | 25704 | +476 | +7.2 | strong |
| Call | 25100 | 1876 | 89 | 621.8 | 25227 | 613.0 | 25722 | +494 | +8.8 | strong |
| Call | 25150 | 312 | 75 | 571.3 | 25194 | 585.5 | 25721 | +493 | -14.2 | strong |
| Call | 25200 | 7602 | 1313 | 557.7 | 25225 | 555.9 | 25758 | +530 | +1.8 | strong |
| Call | 25250 | 580 | 260 | 530.5 | 25228 | 527.9 | 25780 | +553 | +2.6 | strong |
| Call | 25300 | 7017 | 1713 | 502.9 | 25228 | 495.0 | 25803 | +575 | +7.9 | strong |
| Call | 25350 | 816 | 271 | 466.4 | 25213 | 468.9 | 25816 | +588 | -2.4 | strong |
| Call | 25400 | 5433 | 1537 | 446.5 | 25217 | 443.4 | 25846 | +619 | +3.1 | strong |
| Call | 25450 | 1326 | 520 | 420.1 | 25217 | 418.8 | 25870 | +642 | +1.3 | strong |
| Call | 25500 | 54629 | 11460 | 397.9 | 25221 | 395.1 | 25898 | +670 | +2.9 | strong |
| Call | 25550 | 1270 | 722 | 375.2 | 25232 | 370.9 | 25925 | +697 | +4.3 | strong |
| Call | 25600 | 5605 | 1407 | 355.1 | 25219 | 350.1 | 25955 | +727 | +5.1 | strong |
| Put | 24850 | 478 | 31 | 250.7 | 25221 | 247.2 | 24599 | +629 | +3.5 | strong |
| Put | 24900 | 3070 | 149 | 262.8 | 25221 | 263.9 | 24637 | +591 | -1.0 | strong |
| Put | 24950 | 817 | 31 | 293.7 | 25198 | 279.1 | 24656 | +572 | +14.7 | strong |
| Put | 25000 | 65291 | 2155 | 295.6 | 25227 | 296.0 | 24704 | +524 | -0.3 | strong |
| Put | 25050 | 575 | 30 | 325.0 | 25196 | 313.2 | 24725 | +503 | +11.8 | strong |
| Put | 25100 | 2619 | 123 | 318.3 | 25257 | 331.1 | 24782 | +446 | -12.8 | strong |
| Put | 25150 | 388 | 84 | 366.7 | 25191 | 350.9 | 24783 | +445 | +15.8 | strong |
| Put | 25200 | 8997 | 2751 | 377.6 | 25214 | 371.1 | 24822 | +406 | +6.5 | strong |
| Put | 25250 | 729 | 199 | 380.8 | 25246 | 392.6 | 24869 | +359 | -11.8 | strong |
| Put | 25300 | 9280 | 1075 | 404.5 | 25255 | 412.1 | 24896 | +332 | -7.6 | strong |
| Put | 25350 | 703 | 187 | 448.1 | 25210 | 435.6 | 24902 | +326 | +12.5 | strong |
| Put | 25400 | 11354 | 2415 | 474.2 | 25200 | 461.8 | 24926 | +302 | +12.4 | strong |
| Put | 25450 | 818 | 343 | 492.4 | 25216 | 485.0 | 24958 | +270 | +7.4 | strong |
| Put | 25500 | 67484 | 11713 | 511.3 | 25225 | 511.9 | 24989 | +239 | -0.6 | strong |
| Put | 25550 | 1120 | 674 | 532.4 | 25234 | 535.1 | 25018 | +210 | -2.8 | strong |
| Put | 25600 | 4867 | 821 | 560.9 | 25231 | 563.8 | 25039 | +189 | -2.9 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 37 | 67% | +0.23% | -0.44 to +0.97% | 100% of 1 | up |
| weekly | PCR up · put writing · walls same · near call wall | 20 | 85% | +0.28% | -0.27 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · put writing · walls same · mid walls | 18 | 82% | +0.35% | -0.42 to +1.02% | 100% of 1 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 18 | 83% | +0.36% | -0.50 to +1.68% |  | up |
| weekly | PCR down · call writing · walls same · near put wall | 18 | 67% | +0.24% | -0.37 to +0.85% | 50% of 4 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · near call wall | 16 | 56% | +0.28% | -0.71 to +1.70% | 100% of 1 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 14 | 57% | +0.04% | -0.47 to +0.42% | 50% of 4 | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near put wall | 13 | 82% | +0.08% | -0.18 to +0.20% |  | up |
| monthly | PCR flat · put writing · walls same · near call wall | 12 | 70% | +0.38% | -0.50 to +1.56% |  | no clear direction |
| monthly | PCR up · put and call writing · walls same · mid walls | 11 | 73% | +0.15% | -0.24 to +0.63% | 100% of 1 | no clear direction |
| weekly | PCR down · unwinding · walls same · near call wall | 11 | 70% | +0.39% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| monthly | PCR up · put writing · walls same · near call wall | 11 | 50% | +0.18% | -0.40 to +0.93% | 100% of 1 | no clear direction |
| monthly | PCR flat · put and call writing · walls same · mid walls | 10 | 57% | +0.11% | -0.16 to +0.71% | 100% of 1 | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 10 | 80% | +0.24% | -0.39 to +0.91% | 100% of 1 | no clear direction |
| weekly | PCR down · call writing · walls same · mid walls | 10 | 80% | +0.21% | -0.43 to +0.75% | 50% of 4 | no clear direction |
| weekly | PCR down · unwinding · walls same · mid walls | 10 | 50% | +0.04% | -0.40 to +0.90% | 75% of 4 | too few (6/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 10 | 40% | +0.03% | -0.78 to +0.90% | 100% of 2 | no clear direction |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| weekly | PCR down · call writing · walls down · mid walls | 9 | 78% | +0.24% | -0.07 to +0.54% | 67% of 3 | too few (9/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 9 | 78% | +0.19% | -0.21 to +0.90% | 100% of 1 | too few (9/10) |
| monthly | PCR down · call writing · walls same · mid walls | 8 | 38% | +0.01% | -0.47 to +0.49% | 100% of 1 | too few (8/10) |
| monthly | PCR down · call writing · walls same · near call wall | 8 | 83% | +0.27% | -0.78 to +1.18% | 100% of 1 | too few (6/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 8 | 75% | +0.21% | -1.22 to +1.24% | 50% of 2 | too few (8/10) |
| weekly | PCR up · put writing · walls up · near put wall | 8 | 62% | +0.33% | -0.13 to +1.65% | 0% of 4 | too few (8/10) |
| weekly | PCR up · put writing · walls up · mid walls | 8 | 62% | +0.31% | -0.26 to +1.40% | 33% of 3 | too few (8/10) |
| monthly | PCR up · put writing · walls same · mid walls | 8 | 75% | +0.42% | -0.29 to +0.85% | 100% of 1 | too few (8/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% |  | too few (6/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 7 | 86% | +0.50% | -0.37 to +1.25% | 100% of 1 | too few (7/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (7/10) |
| weekly | PCR up · put writing · walls same · mid walls | 7 | 43% | -0.06% | -0.57 to +0.89% | 67% of 3 | too few (7/10) |
| weekly | PCR down · call writing · walls down · near call wall | 6 | 83% | +0.53% | -0.06 to +1.68% | 67% of 3 | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 5 | 80% | +0.12% | -0.05 to +0.28% |  | too few (5/10) |
| weekly | PCR down · call writing · walls down · near put wall | 5 | 60% | +0.09% | -0.51 to +0.73% | 0% of 2 | too few (5/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 5 | 40% | +0.06% | -0.68 to +0.75% | 50% of 2 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 100% of 1 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 5 | 80% | +0.46% | -1.11 to +1.69% | 0% of 2 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 5 | 75% | +0.21% | -0.05 to +0.63% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 5 | 100% | +0.29% | +0.04 to +0.59% | 0% of 4 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 5 | 80% | +0.22% | -0.11 to +0.50% | 33% of 3 | too few (5/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 5 | 100% | +0.54% | +0.47 to +0.61% | 67% of 3 | too few (3/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 5 | 25% | +0.07% | -0.10 to +0.43% | 33% of 3 | too few (4/10) |
| weekly | PCR down · call writing · walls same · near call wall | 5 | 80% | +0.53% | -0.02 to +0.91% | 33% of 3 | too few (5/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 5 | 60% | +0.15% | -0.07 to +0.33% |  | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 4 | 25% | -0.15% | -0.75 to +0.38% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 4 | 50% | +0.06% | -0.63 to +0.58% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 4 | 75% | +0.84% | -0.07 to +1.82% | 33% of 3 | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 4 |  |  |  | 100% of 4 | too few (0/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 4 | 75% | +0.22% | -0.22 to +0.68% | 75% of 4 | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 4 | 100% | +0.50% | +0.37 to +0.62% |  | too few (4/10) |
| monthly | PCR flat · put and call writing · walls same · near put wall | 4 | 100% | +0.24% | +0.10 to +0.28% |  | too few (4/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 100% | +0.79% | +0.14 to +1.65% |  | too few (4/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 4 | 75% | +0.10% | -0.02 to +0.28% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 4 | 100% | +0.19% | +0.16 to +0.25% | 50% of 2 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 3 | 100% | +0.28% | +0.07 to +0.50% | 100% of 2 | too few (2/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 3 | 50% | -0.03% | -0.43 to +0.37% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 3 | 33% | -0.01% | -0.37 to +0.53% | 50% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 3 | 67% | +0.06% | -0.13 to +0.17% |  | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 3 | 67% | +0.08% | -0.04 to +0.18% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 3 | 100% | +0.12% | +0.05 to +0.16% | 100% of 2 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 3 | 0% | -0.36% | -0.69 to -0.18% | 0% of 1 | too few (3/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 3 | 100% | +0.61% | +0.01 to +1.22% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% | 0% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls same · mid walls | 2 | 100% | +0.30% | +0.29 to +0.31% | 100% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 2 | 100% | +0.20% | +0.20 to +0.20% | 100% of 2 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near put wall | 2 | 100% | +0.21% | +0.18 to +0.24% |  | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · near put wall | 2 | 0% | -0.07% | -0.09 to -0.05% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% |  | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% |  | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 2 | 100% | +0.15% | +0.10 to +0.21% |  | too few (2/10) |
| monthly | PCR up · call writing · walls same · mid walls | 2 | 50% | +0.04% | -0.19 to +0.28% | 100% of 1 | too few (2/10) |
| monthly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.04% | +0.04 to +0.04% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · near call wall | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
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
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
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
| monthly | PCR up · put and call writing · walls same · mid walls | 2 | 50% | +0.02% | -0.63 to +0.68% |  | too few (2/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 100% | +0.55% | +0.51 to +0.58% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 2 | 50% | +0.53% | -0.63 to +1.68% | 0% of 1 | too few (2/10) |
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
| weekly | PCR flat · put and call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.61% | -0.61 to -0.61% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 121 | 64% | +0.13% | up |
| intraday | weekly | writers even · few weak writers | 108 | 54% | +0.05% | no clear direction |
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
| day | weekly | writers even · weak puts | 3 | 33% | -0.06% | too few (3/10) |
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
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 18 | 56% | +0.04% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 17 | 40% | -0.06% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m sideways | 17 | 88% | +0.14% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 14 | 83% | +0.16% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.73% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m sideways | 10 | 44% | +0.04% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 8 | 100% | +0.19% | too few (8/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 8 | 75% | +0.16% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 7 | 20% | -0.17% | too few (5/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 6 | 80% | +0.16% | too few (5/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 5 | 100% | +0.53% | too few (5/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 5 | 40% | +0.00% | too few (5/10) |
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
| intraday | monthly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.02% | too few (1/10) |
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
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 50% | -0.12% | too few (2/10) |
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
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 0% | -0.63% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
