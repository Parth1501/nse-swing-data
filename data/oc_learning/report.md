# Nifty option chain pattern log
Updated 2026-11-13 12:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 510 snapshots over 21 trading days
- 564 patterns logged; 170 different patterns so far

## Latest read (2026-11-13 12:44:59)

Nifty trend: weekly **sideways**, 125-min **sideways**, 25-min (timing) **down**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-17 (weekly) | 4.1 | 25108 | 0.833 | 25150 | 25000 | 25200 | ±1.16% (24816-25401) | 13.95 |
| 2026-11-23 (monthly) | 10.1 | 25104 | 1.054 | 24500 | 25000 | 26000 | ±1.94% (24616-25592) | 14.66 |

- **Weekly, last 30 min**: `PCR down · call writing · walls same · mid walls`. Seen 7 times before; Nifty was up after it 86% of the time, average +0.30%. Too few outcomes (7/20) to trade on.
  - Writers: `call writers stronger · few weak writers`. Seen 24 times before; Nifty was up after it 73% of the time, average +0.26%. History points to a bull call debit spread, ATM to about the call wall 25200.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls same · mid walls`. Seen 1 times before; Nifty was up after it 100% of the time, average +0.51%. Too few outcomes (1/20) to trade on.
  - Writers: `call writers stronger · few weak writers`. Seen 2 times before; Nifty was up after it 100% of the time, average +0.92%. Too few outcomes (2/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR flat · call writing · walls same · near put wall`. Seen 1 times before; Nifty was up after it 0% of the time, average -0.21%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · weak calls`. Seen 82 times before; Nifty was up after it 72% of the time, average +0.17%. History points to a bull call debit spread, ATM to about the call wall 26000.
  - Same, only when the trend was `weekly sideways · 125m sideways`: Seen 6 times before; Nifty was up after it 83% of the time, average +0.08%. Too few outcomes (6/20) to trade on.
- **Monthly, today vs previous day**: `PCR up · put and call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 6 times before; Nifty was up after it 67% of the time, average +0.49%. Too few outcomes (6/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m sideways`: New pattern, never seen before. Logged; nothing to go on yet.

## Strong vs weak writers, weekly 2026-11-17

Strongest call writers at 25200, strongest put writers at 25100; weakest call writers at -, weakest put writers at 25300. Covers 85% of near-money call OI and 84% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24750 | 2948 | 180 | 513.2 | 25201 | 407.7 | 25263 | +155 | +105.5 | strong |
| Call | 24800 | 11767 | 1783 | 433.1 | 25197 | 363.1 | 25233 | +125 | +70.0 | strong |
| Call | 24850 | 3016 | 779 | 417.9 | 25201 | 325.2 | 25268 | +159 | +92.7 | strong |
| Call | 24900 | 13893 | 3840 | 314.3 | 25149 | 285.5 | 25214 | +106 | +28.8 | medium |
| Call | 24950 | 6276 | 3910 | 283.8 | 25150 | 249.6 | 25234 | +125 | +34.2 | strong |
| Call | 25000 | 56166 | 21489 | 248.0 | 25137 | 217.1 | 25248 | +139 | +30.9 | strong |
| Call | 25050 | 28999 | 25894 | 212.8 | 25142 | 187.3 | 25263 | +154 | +25.5 | strong |
| Call | 25100 | 127224 | 122972 | 182.9 | 25141 | 159.6 | 25283 | +174 | +23.3 | strong |
| Call | 25150 | 122380 | 121224 | 161.1 | 25149 | 134.6 | 25311 | +203 | +26.5 | strong |
| Call | 25200 | 230281 | 221198 | 165.7 | 25189 | 113.4 | 25366 | +257 | +52.3 | strong |
| Call | 25250 | 135984 | 133733 | 155.7 | 25201 | 94.2 | 25406 | +297 | +61.5 | strong |
| Call | 25300 | 192741 | 181666 | 171.0 | 25244 | 78.2 | 25471 | +362 | +92.7 | strong |
| Call | 25350 | 111483 | 107994 | 184.0 | 25292 | 64.5 | 25534 | +426 | +119.5 | strong |
| Call | 25400 | 185865 | 166096 | 151.9 | 25274 | 52.6 | 25552 | +443 | +99.2 | strong |
| Call | 25450 | 73888 | 70946 | 121.6 | 25256 | 43.1 | 25572 | +463 | +78.5 | strong |
| Put | 24750 | 41121 | 37745 | 34.1 | 25238 | 29.4 | 24716 | +393 | +4.7 | strong |
| Put | 24800 | 132012 | 102907 | 43.6 | 25265 | 37.4 | 24756 | +352 | +6.2 | strong |
| Put | 24850 | 52883 | 47232 | 54.4 | 25256 | 47.1 | 24796 | +313 | +7.3 | strong |
| Put | 24900 | 101113 | 80764 | 57.0 | 25262 | 59.3 | 24843 | +265 | -2.3 | strong |
| Put | 24950 | 57761 | 53916 | 68.6 | 25261 | 73.6 | 24881 | +227 | -5.0 | strong |
| Put | 25000 | 196277 | 156566 | 81.8 | 25260 | 90.2 | 24918 | +190 | -8.5 | strong |
| Put | 25050 | 69234 | 68028 | 99.5 | 25227 | 110.0 | 24951 | +158 | -10.5 | strong |
| Put | 25100 | 176506 | 170283 | 119.4 | 25235 | 132.6 | 24981 | +128 | -13.2 | strong |
| Put | 25150 | 93590 | 93159 | 141.6 | 25214 | 158.2 | 25008 | +100 | -16.6 | medium |
| Put | 25200 | 118128 | 117394 | 157.5 | 25234 | 186.6 | 25043 | +66 | -29.1 | medium |
| Put | 25250 | 30869 | 30759 | 171.1 | 25276 | 218.1 | 25079 | +30 | -47.0 | weak |
| Put | 25300 | 52166 | 51862 | 182.7 | 25332 | 251.3 | 25117 | -9 | -68.6 | weak |
| Put | 25350 | 22242 | 22212 | 199.7 | 25352 | 288.0 | 25150 | -42 | -88.3 | weak |
| Put | 25400 | 25914 | 25824 | 235.0 | 25334 | 325.6 | 25165 | -56 | -90.5 | weak |
| Put | 25450 | 4147 | 4120 | 260.9 | 25333 | 365.4 | 25189 | -81 | -104.5 | weak |

## Strong vs weak writers, monthly 2026-11-23

Strongest call writers at 25500, strongest put writers at 25000; weakest call writers at 25000, weakest put writers at 25400. Covers 96% of near-money call OI and 95% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 24750 | 1091 | 1080 | 255.4 | 24510 | 497.2 | 25005 | -99 | -241.8 | weak |
| Call | 24800 | 7808 | 7543 | 223.0 | 24361 | 454.8 | 25023 | -81 | -231.8 | weak |
| Call | 24850 | 1504 | 1504 | 261.8 | 24556 | 418.8 | 25112 | +8 | -157.0 | weak |
| Call | 24900 | 11891 | 11852 | 259.9 | 24638 | 384.8 | 25160 | +56 | -124.9 | medium |
| Call | 24950 | 1060 | 1056 | 281.4 | 24780 | 352.1 | 25231 | +127 | -70.7 | strong |
| Call | 25000 | 57997 | 49083 | 126.1 | 24115 | 321.1 | 25126 | +22 | -195.0 | weak |
| Call | 25050 | 1538 | 1537 | 304.8 | 25025 | 294.2 | 25355 | +251 | +10.6 | strong |
| Call | 25100 | 16253 | 16189 | 255.4 | 24949 | 266.0 | 25355 | +251 | -10.6 | strong |
| Call | 25150 | 5544 | 5543 | 260.9 | 25099 | 240.3 | 25411 | +307 | +20.5 | strong |
| Call | 25200 | 39484 | 39419 | 261.1 | 25050 | 216.0 | 25461 | +357 | +45.1 | strong |
| Call | 25250 | 5925 | 5922 | 250.2 | 25124 | 195.6 | 25500 | +396 | +54.7 | strong |
| Call | 25300 | 33102 | 33086 | 284.5 | 25177 | 174.1 | 25585 | +480 | +110.4 | strong |
| Call | 25350 | 4762 | 4762 | 259.1 | 25208 | 156.2 | 25609 | +505 | +102.9 | strong |
| Call | 25400 | 21881 | 21834 | 238.0 | 25199 | 138.3 | 25638 | +534 | +99.7 | strong |
| Call | 25450 | 5334 | 5322 | 198.9 | 25188 | 123.8 | 25649 | +545 | +75.1 | strong |
| Put | 24750 | 2912 | 2905 | 178.4 | 25084 | 98.0 | 24572 | +533 | +80.4 | strong |
| Put | 24800 | 23956 | 23864 | 214.4 | 25057 | 110.8 | 24586 | +519 | +103.7 | strong |
| Put | 24850 | 3545 | 3543 | 203.1 | 25079 | 124.3 | 24647 | +457 | +78.8 | strong |
| Put | 24900 | 20946 | 20932 | 271.8 | 24994 | 141.3 | 24628 | +476 | +130.5 | strong |
| Put | 24950 | 3062 | 3062 | 230.8 | 25098 | 157.8 | 24719 | +385 | +73.0 | strong |
| Put | 25000 | 108490 | 99342 | 548.4 | 24765 | 177.8 | 24452 | +653 | +370.6 | strong |
| Put | 25050 | 2462 | 2457 | 236.6 | 25143 | 198.7 | 24813 | +291 | +37.9 | strong |
| Put | 25100 | 18409 | 18401 | 280.3 | 25132 | 221.8 | 24820 | +284 | +58.5 | strong |
| Put | 25150 | 5093 | 5091 | 242.7 | 25197 | 245.8 | 24907 | +197 | -3.1 | strong |
| Put | 25200 | 28732 | 28708 | 267.7 | 25254 | 272.0 | 24932 | +172 | -4.3 | strong |
| Put | 25250 | 3707 | 3699 | 274.9 | 25259 | 298.9 | 24975 | +129 | -24.0 | strong |
| Put | 25300 | 25128 | 25122 | 264.3 | 25339 | 330.0 | 25036 | +68 | -65.7 | medium |
| Put | 25350 | 1637 | 1633 | 291.8 | 25332 | 360.2 | 25058 | +46 | -68.4 | weak |
| Put | 25400 | 12229 | 12218 | 308.3 | 25344 | 393.3 | 25092 | +12 | -85.0 | weak |
| Put | 25450 | 700 | 696 | 347.4 | 25329 | 422.4 | 25103 | +2 | -75.0 | weak |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · quiet OI · walls same · mid walls | 35 | 71% | +0.25% | -0.44 to +0.97% | 100% of 1 | up |
| monthly | PCR flat · quiet OI · walls same · near call wall | 18 | 83% | +0.36% | -0.50 to +1.68% |  | up |
| weekly | PCR up · put writing · walls same · near call wall | 17 | 94% | +0.34% | -0.02 to +0.92% | 25% of 4 | up |
| monthly | PCR flat · put and call writing · walls same · near call wall | 16 | 56% | +0.27% | -0.71 to +1.70% | 100% of 1 | no clear direction |
| monthly | PCR flat · put writing · walls same · mid walls | 14 | 100% | +0.49% | +0.09 to +1.02% | 100% of 1 | up |
| weekly | PCR down · call writing · walls same · near put wall | 13 | 69% | +0.27% | -0.37 to +0.85% | 33% of 3 | no clear direction |
| weekly | PCR up · put writing · walls same · near put wall | 12 | 67% | +0.06% | -0.47 to +0.42% | 33% of 3 | no clear direction |
| monthly | PCR flat · put writing · walls same · near call wall | 12 | 70% | +0.36% | -0.53 to +1.56% |  | no clear direction |
| monthly | PCR flat · quiet OI · walls same · near put wall | 11 | 78% | +0.07% | -0.18 to +0.20% |  | too few (9/10) |
| weekly | PCR down · unwinding · walls same · near call wall | 11 | 70% | +0.39% | -0.07 to +1.52% | 25% of 4 | no clear direction |
| monthly | PCR up · put writing · walls same · near call wall | 10 | 50% | +0.18% | -0.40 to +0.93% | 100% of 1 | no clear direction |
| weekly | PCR up · put and call writing · walls same · mid walls | 9 | 33% | +0.02% | -0.78 to +0.90% | 100% of 1 | too few (9/10) |
| monthly | PCR down · quiet OI · walls same · mid walls | 9 | 86% | +0.32% | -0.07 to +0.70% |  | too few (7/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 8 | 75% | +0.27% | -0.39 to +0.91% | 100% of 1 | too few (8/10) |
| monthly | PCR down · call writing · walls same · near call wall | 8 | 83% | +0.27% | -0.78 to +1.18% | 100% of 1 | too few (6/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 8 | 67% | +0.24% | -0.14 to +0.91% |  | too few (6/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 8 | 88% | +0.24% | -0.21 to +0.90% | 100% of 1 | too few (8/10) |
| monthly | PCR flat · put and call writing · walls same · mid walls | 8 | 67% | +0.14% | -0.16 to +0.71% | 100% of 1 | too few (6/10) |
| weekly | PCR down · call writing · walls same · mid walls | 8 | 86% | +0.30% | -0.43 to +0.75% | 33% of 3 | too few (7/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 8 | 50% | +0.07% | -0.40 to +0.90% | 67% of 3 | too few (4/10) |
| weekly | PCR down · call writing · walls down · mid walls | 7 | 86% | +0.24% | -0.07 to +0.54% | 50% of 2 | too few (7/10) |
| weekly | PCR up · put writing · walls up · near put wall | 7 | 57% | +0.34% | -0.13 to +1.65% | 0% of 3 | too few (7/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 7 | 43% | -0.02% | -0.74 to +0.62% | 100% of 1 | too few (7/10) |
| weekly | PCR up · put writing · walls up · mid walls | 6 | 83% | +0.48% | -0.16 to +1.40% | 33% of 3 | too few (6/10) |
| weekly | PCR down · call writing · walls down · near call wall | 6 | 83% | +0.53% | -0.06 to +1.68% | 50% of 2 | too few (6/10) |
| monthly | PCR up · put writing · walls same · mid walls | 6 | 100% | +0.65% | +0.24 to +0.85% | 100% of 1 | too few (6/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 6 | 83% | +0.28% | -0.24 to +0.63% | 100% of 1 | too few (6/10) |
| monthly | PCR flat · unwinding · walls same · mid walls | 6 | 40% | +0.15% | -0.15 to +0.76% | 100% of 1 | too few (5/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 6 | 83% | +0.55% | -0.37 to +1.25% | 100% of 1 | too few (6/10) |
| monthly | PCR down · call writing · walls same · mid walls | 5 | 60% | +0.05% | -0.47 to +0.49% | 100% of 1 | too few (5/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 5 | 80% | +0.46% | -1.11 to +1.69% | 0% of 2 | too few (5/10) |
| weekly | PCR down · call writing · walls same · near call wall | 5 | 80% | +0.53% | -0.02 to +0.91% | 33% of 3 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · mid walls | 5 | 100% | +0.17% | +0.07 to +0.30% | 100% of 1 | too few (5/10) |
| weekly | PCR up · unwinding · walls same · mid walls | 5 | 75% | +0.21% | -0.05 to +0.63% | 50% of 2 | too few (4/10) |
| weekly | PCR up · put writing · walls same · mid walls | 5 | 20% | -0.17% | -0.57 to +0.89% | 50% of 2 | too few (5/10) |
| monthly | PCR up · unwinding · walls same · near call wall | 4 | 100% | +0.79% | +0.14 to +1.65% |  | too few (4/10) |
| monthly | PCR down · put writing · walls same · mid walls | 4 | 75% | +0.17% | -0.05 to +0.50% | 100% of 1 | too few (4/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 4 | 100% | +0.35% | +0.13 to +0.59% | 0% of 3 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · mid walls | 4 |  |  |  | 100% of 3 | too few (0/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 4 | 25% | -0.18% | -0.75 to +0.38% | 0% of 1 | too few (4/10) |
| weekly | PCR flat · put and call writing · walls same · mid walls | 4 | 75% | +0.24% | -0.11 to +0.50% | 50% of 2 | too few (4/10) |
| weekly | PCR down · unwinding · walls up · near put wall | 4 | 75% | +0.20% | -0.02 to +0.37% | 100% of 1 | too few (4/10) |
| weekly | PCR flat · quiet OI · walls same · mid walls | 4 | 75% | +0.22% | -0.22 to +0.68% | 67% of 3 | too few (4/10) |
| monthly | PCR up · quiet OI · walls same · near call wall | 4 | 100% | +0.50% | +0.37 to +0.62% |  | too few (4/10) |
| weekly | PCR down · call writing · walls down · near put wall | 4 | 50% | +0.05% | -0.51 to +0.73% | 0% of 1 | too few (4/10) |
| weekly | PCR up · put writing · walls down · near call wall | 4 | 100% | +0.76% | +0.15 to +1.56% | 33% of 3 | too few (4/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 4 | 50% | +0.06% | -0.63 to +0.58% | 0% of 1 | too few (4/10) |
| weekly | PCR up · unwinding · walls down · mid walls | 4 | 100% | +0.54% | +0.47 to +0.61% | 50% of 2 | too few (3/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 4 | 75% | +0.34% | -1.22 to +1.24% | 0% of 1 | too few (4/10) |
| weekly | PCR down · put and call writing · walls same · mid walls | 4 | 50% | +0.10% | -0.68 to +0.75% | 50% of 2 | too few (4/10) |
| weekly | PCR flat · put and call writing · walls up · near put wall | 3 | 33% | -0.10% | -0.51 to +0.53% | 0% of 1 | too few (3/10) |
| monthly | PCR down · quiet OI · walls same · near call wall | 3 | 100% | +0.26% | +0.26 to +0.26% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near call wall | 3 | 100% | +0.43% | +0.17 to +0.78% | 0% of 3 | too few (3/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 3 | 100% | +0.28% | +0.13 to +0.44% | 100% of 1 | too few (3/10) |
| weekly | PCR down · put and call writing · walls same · near call wall | 3 | 100% | +0.72% | +0.60 to +0.85% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · unwinding · walls same · near call wall | 3 | 100% | +0.28% | +0.07 to +0.50% | 100% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls same · near put wall | 3 | 33% | +0.13% | -0.02 to +0.43% | 0% of 2 | too few (3/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 3 | 100% | +1.15% | +0.59 to +1.82% | 0% of 2 | too few (3/10) |
| weekly | PCR up · unwinding · walls down · near call wall | 3 | 100% | +0.10% | +0.02 to +0.21% | 0% of 1 | too few (3/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 3 | 67% | +0.05% | -0.02 to +0.13% | 0% of 1 | too few (3/10) |
| monthly | PCR down · call writing · walls down · mid walls | 2 | 100% | +0.03% | +0.03 to +0.03% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near call wall | 2 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · mid walls | 2 | 100% | +0.26% | +0.20 to +0.32% | 0% of 1 | too few (2/10) |
| weekly | PCR up · call writing · walls down · mid walls | 2 | 50% | -0.05% | -0.61 to +0.51% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put writing · walls down · mid walls | 2 | 100% | +0.30% | +0.12 to +0.48% | 100% of 1 | too few (2/10) |
| weekly | PCR up · put and call writing · walls down · near call wall | 2 | 100% | +0.38% | +0.14 to +0.63% | 0% of 2 | too few (2/10) |
| monthly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.02% | -0.13 to +0.17% |  | too few (2/10) |
| weekly | PCR down · call writing · walls up · mid walls | 2 | 100% | +0.73% | +0.62 to +0.85% | 0% of 2 | too few (2/10) |
| monthly | PCR up · call writing · walls same · near call wall | 2 | 50% | -0.11% | -0.51 to +0.29% | 100% of 1 | too few (2/10) |
| weekly | PCR down · put and call writing · walls same · near put wall | 2 | 0% | -0.44% | -0.69 to -0.20% | 0% of 1 | too few (2/10) |
| weekly | PCR down · call writing · walls up · near put wall | 2 | 100% | +0.39% | +0.27 to +0.52% | 100% of 1 | too few (2/10) |
| monthly | PCR flat · quiet OI · walls up · mid walls | 2 | 100% | +0.34% | +0.16 to +0.52% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls same · near put wall | 2 | 0% | -0.21% | -0.21 to -0.21% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · near call wall | 2 | 100% | +0.31% | +0.21 to +0.40% |  | too few (2/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 2 | 100% | +0.36% | +0.35 to +0.38% | 100% of 1 | too few (2/10) |
| monthly | PCR down · unwinding · walls same · near put wall | 2 | 100% | +0.15% | +0.10 to +0.21% |  | too few (2/10) |
| monthly | PCR flat · call writing · walls down · near call wall | 2 | 100% | +0.30% | +0.22 to +0.38% |  | too few (2/10) |
| weekly | PCR up · call writing · walls same · mid walls | 2 | 100% | +0.30% | +0.29 to +0.31% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · put writing · walls same · mid walls | 2 | 100% | +0.09% | +0.08 to +0.11% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · quiet OI · walls same · near put wall | 2 | 100% | +0.54% | +0.36 to +0.72% | 50% of 2 | too few (2/10) |
| weekly | PCR flat · unwinding · walls down · near put wall | 2 | 100% | +0.06% | +0.01 to +0.12% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 2 | 100% | +0.21% | +0.16 to +0.25% | 100% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · near put wall | 2 | 100% | +0.15% | +0.14 to +0.16% | 100% of 1 | too few (2/10) |
| weekly | PCR up · unwinding · walls down · near put wall | 2 | 100% | +0.17% | +0.15 to +0.19% | 0% of 1 | too few (2/10) |
| weekly | PCR flat · unwinding · walls up · mid walls | 2 | 100% | +0.20% | +0.20 to +0.20% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near put wall | 2 | 50% | +0.12% | -0.18 to +0.42% | 0% of 1 | too few (2/10) |
| weekly | PCR down · unwinding · walls down · near call wall | 2 | 100% | +0.61% | +0.01 to +1.22% | 50% of 2 | too few (2/10) |
| monthly | PCR down · put writing · walls same · near call wall | 1 | 100% | +0.35% | +0.35 to +0.35% |  | too few (1/10) |
| monthly | PCR down · call writing · walls up · mid walls | 1 |  |  |  | 100% of 1 | too few (0/10) |
| monthly | PCR down · call writing · walls down · near call wall | 1 | 0% | -0.36% | -0.36 to -0.36% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · mid walls | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -1.13% | -1.13 to -1.13% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.30% | +0.30 to +0.30% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls up · near put wall | 1 | 0% | -0.25% | -0.25 to -0.25% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.23% | -0.23 to -0.23% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls up · mid walls | 1 | 0% | -0.14% | -0.14 to -0.14% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · put and call writing · walls down · mid walls | 1 | 100% | +0.05% | +0.05 to +0.05% | 100% of 1 | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% |  | too few (1/10) |
| monthly | PCR down · quiet OI · walls same · near put wall | 1 | 0% | -0.20% | -0.20 to -0.20% |  | too few (1/10) |
| monthly | PCR down · unwinding · walls same · near call wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.28% | +0.28 to +0.28% | 100% of 1 | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| monthly | PCR flat · unwinding · walls same · near call wall | 1 | 100% | +1.86% | +1.86 to +1.86% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% |  | too few (1/10) |
| monthly | PCR up · call writing · walls down · near call wall | 1 | 0% | -0.61% | -0.61 to -0.61% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · near put wall | 1 | 100% | +0.02% | +0.02 to +0.02% |  | too few (1/10) |
| monthly | PCR up · call writing · walls up · mid walls | 1 | 100% | +0.78% | +0.78 to +0.78% | 100% of 1 | too few (1/10) |
| weekly | PCR down · quiet OI · walls up · mid walls | 1 | 100% | +0.18% | +0.18 to +0.18% |  | too few (1/10) |
| weekly | PCR down · put writing · walls up · near put wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% | 0% of 1 | too few (1/10) |
| weekly | PCR down · put writing · walls same · mid walls | 1 | 0% | -0.08% | -0.08 to -0.08% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near call wall | 1 | 100% | +0.11% | +0.11 to +0.11% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near put wall | 1 | 0% | -0.19% | -0.19 to -0.19% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 100% | +0.34% | +0.34 to +0.34% |  | too few (1/10) |
| monthly | PCR up · unwinding · walls up · mid walls | 1 | 100% | +0.02% | +0.02 to +0.02% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.59% | +0.59 to +0.59% |  | too few (1/10) |
| monthly | PCR up · put writing · walls same · near put wall | 1 | 0% | -1.22% | -1.22 to -1.22% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls up · mid walls | 1 | 100% | +0.14% | +0.14 to +0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls down · near call wall | 1 | 100% | +0.24% | +0.24 to +0.24% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.40% | -0.40 to -0.40% | 0% of 1 | too few (1/10) |
| weekly | PCR down · unwinding · walls up · near call wall | 1 |  |  |  | 100% of 1 | too few (0/10) |
| weekly | PCR flat · call writing · walls down · mid walls | 1 | 100% | +0.31% | +0.31 to +0.31% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls down · near call wall | 1 | 100% | +0.72% | +0.72 to +0.72% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · unwinding · walls down · near call wall | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR flat · put writing · walls up · mid walls | 1 | 0% | -0.05% | -0.05 to -0.05% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · quiet OI · walls down · near call wall | 1 | 0% | -0.14% | -0.14 to -0.14% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls down · near call wall | 1 | 100% | +0.21% | +0.21 to +0.21% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls up · near call wall | 1 | 100% | +0.18% | +0.18 to +0.18% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · call writing · walls same · mid walls | 1 | 100% | +0.56% | +0.56 to +0.56% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · near put wall | 1 | 0% | -0.43% | -0.43 to -0.43% |  | too few (1/10) |
| weekly | PCR up · call writing · walls same · near call wall | 1 | 100% | +0.62% | +0.62 to +0.62% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · unwinding · walls up · near call wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.23% | +0.23 to +0.23% |  | too few (1/10) |
| weekly | PCR up · quiet OI · walls down · mid walls | 1 |  |  |  | 0% of 1 | too few (0/10) |
| weekly | PCR up · quiet OI · walls same · near call wall | 1 | 100% | +0.37% | +0.37 to +0.37% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near call wall | 1 | 100% | +0.01% | +0.01 to +0.01% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls same · near put wall | 1 | 100% | +0.09% | +0.09 to +0.09% | 0% of 1 | too few (1/10) |
| weekly | PCR up · unwinding · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR flat · put and call writing · walls same · mid walls | 3 | 33% | +0.16% | -0.34 to +1.05% | 100% of 1 | too few (3/10) |
| monthly | PCR flat · put and call writing · walls same · near call wall | 3 | 67% | +0.73% | -0.39 to +2.40% |  | too few (3/10) |
| monthly | PCR down · put and call writing · walls up · near call wall | 2 | 100% | +0.34% | +0.06 to +0.63% |  | too few (2/10) |
| weekly | PCR up · put and call writing · walls same · mid walls | 2 | 100% | +0.51% | +0.51 to +0.51% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls up · mid walls | 2 | 100% | +0.35% | +0.06 to +0.65% | 100% of 2 | too few (2/10) |
| monthly | PCR down · put writing · walls up · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% |  | too few (1/10) |
| monthly | PCR down · put writing · walls same · mid walls | 1 | 100% | +0.65% | +0.65 to +0.65% | 100% of 1 | too few (1/10) |
| monthly | PCR down · unwinding · walls same · mid walls | 1 | 100% | +0.51% | +0.51 to +0.51% |  | too few (1/10) |
| monthly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +1.68% | +1.68 to +1.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR down · put and call writing · walls same · near call wall | 1 | 100% | +1.58% | +1.58 to +1.58% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 0% | -0.77% | -0.77 to -0.77% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| monthly | PCR up · put writing · walls up · near call wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · mid walls | 1 | 100% | +0.68% | +0.68 to +0.68% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · near call wall | 1 | 0% | -0.54% | -0.54 to -0.54% | 100% of 1 | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · mid walls | 1 | 100% | +1.58% | +1.58 to +1.58% | 100% of 1 | too few (1/10) |
| weekly | PCR down · call writing · walls same · near call wall | 1 | 0% | -0.34% | -0.34 to -0.34% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls down · mid walls | 1 | 0% | -1.11% | -1.11 to -1.11% | 100% of 1 | too few (1/10) |
| weekly | PCR flat · put writing · walls same · near call wall | 1 | 100% | +2.01% | +2.01 to +2.01% | 0% of 1 | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near call wall | 1 | 100% | +1.68% | +1.68 to +1.68% | 0% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls down · mid walls | 1 | 0% | -0.77% | -0.77 to -0.77% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · mid walls | 1 | 0% | -0.22% | -0.22 to -0.22% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · mid walls | 1 | 0% | -0.39% | -0.39 to -0.39% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.84% | +0.84 to +0.84% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · mid walls | 1 | 0% | -0.02% | -0.02 to -0.02% | 100% of 1 | too few (1/10) |
| weekly | PCR up · put writing · walls same · near call wall | 1 | 100% | +0.63% | +0.63 to +0.63% |  | too few (1/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 94 | 70% | +0.17% | up |
| intraday | weekly | writers even · few weak writers | 84 | 54% | +0.04% | no clear direction |
| intraday | monthly | writers even · weak calls | 83 | 72% | +0.17% | up |
| intraday | monthly | put writers stronger · weak calls | 62 | 86% | +0.59% | up |
| intraday | weekly | put writers stronger · weak calls | 59 | 78% | +0.39% | up |
| intraday | weekly | call writers stronger · weak puts | 36 | 88% | +0.40% | up |
| intraday | weekly | put writers stronger · few weak writers | 28 | 92% | +0.34% | up |
| intraday | weekly | call writers stronger · few weak writers | 25 | 73% | +0.26% | up |
| intraday | weekly | writers even · weak calls | 23 | 90% | +0.51% | up |
| intraday | monthly | writers even · weak puts | 19 | 84% | +0.45% | up |
| intraday | weekly | writers even · weak puts | 19 | 82% | +0.31% | up |
| intraday | monthly | call writers stronger · few weak writers | 14 | 58% | +0.06% | no clear direction |
| intraday | weekly | writers even · weak on both sides | 7 | 100% | +0.39% | too few (7/10) |
| intraday | monthly | put writers stronger · few weak writers | 6 | 33% | -0.37% | too few (6/10) |
| intraday | monthly | call writers stronger · weak puts | 5 | 100% | +0.66% | too few (5/10) |
| day | monthly | writers even · few weak writers | 8 | 50% | +0.34% | too few (8/10) |
| day | monthly | writers even · weak calls | 7 | 67% | +0.49% | too few (6/10) |
| day | weekly | put writers stronger · weak calls | 5 | 80% | +0.40% | too few (5/10) |
| day | monthly | put writers stronger · weak calls | 4 | 100% | +0.88% | too few (4/10) |
| day | weekly | writers even · few weak writers | 4 | 50% | +0.57% | too few (4/10) |
| day | weekly | call writers stronger · few weak writers | 3 | 100% | +0.92% | too few (2/10) |
| day | weekly | put writers stronger · few weak writers | 3 | 100% | +0.95% | too few (3/10) |
| day | monthly | call writers stronger · few weak writers | 2 | 50% | +0.66% | too few (2/10) |
| day | weekly | call writers stronger · weak puts | 2 | 0% | -0.44% | too few (2/10) |
| day | weekly | writers even · weak calls | 2 | 50% | +1.00% | too few (2/10) |
| day | weekly | writers even · weak puts | 2 | 50% | +0.23% | too few (2/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 57 | 78% | +0.39% | up |
| intraday | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 49 | 85% | +0.68% | up |
| intraday | monthly | writers even · weak calls · weekly bearish · 125m up | 45 | 93% | +0.31% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m up | 38 | 79% | +0.23% | up |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 37 | 61% | +0.14% | no clear direction |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m up | 31 | 41% | -0.01% | no clear direction |
| intraday | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 28 | 92% | +0.34% | up |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m up | 28 | 77% | +0.29% | up |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 26 | 36% | -0.09% | no clear direction |
| intraday | monthly | writers even · few weak writers · weekly bearish · 125m down | 19 | 69% | +0.09% | no clear direction |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m sideways | 19 | 37% | -0.11% | no clear direction |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 18 | 94% | +0.48% | up |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 16 | 80% | +0.42% | up |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m up | 14 | 100% | +0.73% | up |
| intraday | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 13 | 91% | +0.19% | up |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m down | 12 | 100% | +0.55% | up |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 12 | 91% | +0.33% | up |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 10 | 56% | +0.05% | too few (9/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m down | 9 | 88% | +0.37% | too few (8/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m sideways | 8 | 88% | +0.31% | too few (8/10) |
| intraday | monthly | writers even · weak calls · weekly sideways · 125m sideways | 7 | 83% | +0.08% | too few (6/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m sideways | 6 | 83% | +0.08% | too few (6/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m up | 5 | 40% | +0.15% | too few (5/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 5 | 75% | +0.10% | too few (4/10) |
| intraday | weekly | writers even · few weak writers · weekly bearish · 125m down | 5 | 50% | -0.20% | too few (4/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 5 | 100% | +0.26% | too few (5/10) |
| intraday | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 4 | 67% | +0.09% | too few (3/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 4 | 100% | +0.59% | too few (4/10) |
| intraday | weekly | writers even · weak calls · weekly bearish · 125m sideways | 4 | 33% | -0.06% | too few (3/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m sideways | 4 | 100% | +0.22% | too few (4/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m down | 3 | 100% | +0.84% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m sideways | 3 | 0% | -0.83% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 67% | +0.09% | too few (3/10) |
| intraday | monthly | call writers stronger · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.39% | too few (2/10) |
| intraday | monthly | writers even · weak puts · weekly bearish · 125m sideways | 2 | 100% | +0.59% | too few (2/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 2 | 0% | -0.49% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly bearish · 125m up | 2 | 0% | -0.16% | too few (2/10) |
| intraday | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 2 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak puts · weekly bearish · 125m up | 2 | 0% | -0.27% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly bearish · 125m down | 1 | 100% | +0.01% | too few (1/10) |
| intraday | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m down | 1 | 100% | +0.36% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly bearish · 125m up | 1 | 100% | +0.91% | too few (1/10) |
| intraday | weekly | writers even · weak on both sides · weekly sideways · 125m up | 1 | 100% | +0.55% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m up | 4 | 75% | +0.75% | too few (4/10) |
| day | monthly | writers even · weak calls · weekly bearish · 125m up | 4 | 75% | +0.88% | too few (4/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m down | 3 | 33% | -0.08% | too few (3/10) |
| day | weekly | put writers stronger · few weak writers · weekly bearish · 125m up | 3 | 100% | +0.95% | too few (3/10) |
| day | weekly | put writers stronger · weak calls · weekly bearish · 125m up | 3 | 67% | +0.37% | too few (3/10) |
| day | monthly | put writers stronger · weak calls · weekly bearish · 125m up | 2 | 100% | +1.32% | too few (2/10) |
| day | monthly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m up | 2 | 50% | -0.30% | too few (2/10) |
| day | weekly | put writers stronger · weak calls · weekly sideways · 125m up | 2 | 100% | +0.45% | too few (2/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m up | 2 | 100% | +1.73% | too few (2/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | monthly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | monthly | writers even · few weak writers · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | monthly | writers even · weak calls · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly bearish · 125m up | 1 | 100% | +1.66% | too few (1/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m sideways | 1 |  |  | too few (0/10) |
| day | weekly | call writers stronger · few weak writers · weekly sideways · 125m up | 1 | 100% | +0.18% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m down | 1 | 0% | -0.54% | too few (1/10) |
| day | weekly | call writers stronger · weak puts · weekly bearish · 125m sideways | 1 | 0% | -0.34% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly bearish · 125m down | 1 | 0% | -0.39% | too few (1/10) |
| day | weekly | writers even · few weak writers · weekly sideways · 125m up | 1 | 0% | -0.77% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m sideways | 1 | 0% | -0.02% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly bearish · 125m up | 1 | 100% | +2.01% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m down | 1 | 100% | +0.68% | too few (1/10) |
| day | weekly | writers even · weak puts · weekly bearish · 125m up | 1 | 0% | -0.22% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
