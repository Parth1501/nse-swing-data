# Sensex option chain pattern log
Updated 2026-11-20 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 12 snapshots over 2 trading days
- 21 patterns logged; 18 different patterns so far

## Latest read (2026-11-20 13:45:00)

Sensex trend: weekly **sideways**, 125-min **up**, 25-min (timing) **up**. Each is up when the close is above its fast average and the fast average above the slow one, down when both are the other way, sideways otherwise (weekly 20/50 weeks; 125-min and 25-min 6/15 candles).

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 (weekly) | 6.1 | 83780 | 0.983 | 83000 | 82500 | 88000 | ±1.58% (82456-85104) | 15.29 |
| 2026-12-31 (monthly) | 41.1 | 83780 | 1.061 | 83000 | 83000 | 87900 | ±3.8% (80598-86962) | 14.04 |

- **Weekly, last 30 min**: `PCR flat · call writing · walls same · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. Seen 3 times before; Sensex was up after it 100% of the time, average +0.15%. Too few outcomes (3/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 3 times before; Sensex was up after it 100% of the time, average +0.15%. Too few outcomes (3/20) to trade on.
- **Weekly, today vs previous day**: `PCR up · put and call writing · walls up · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
  - Writers: `writers even · weak calls`. New pattern, never seen before. Logged; nothing to go on yet.
  - Same, only when the trend was `weekly sideways · 125m up`: New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, last 30 min**: `PCR up · put writing · walls same · near put wall`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.06%. Too few outcomes (1/20) to trade on.
  - Writers: `writers even · few weak writers`. Seen 7 times before; Sensex was up after it 100% of the time, average +0.50%. Too few outcomes (6/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 7 times before; Sensex was up after it 100% of the time, average +0.50%. Too few outcomes (6/20) to trade on.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
  - Writers: `writers even · few weak writers`. Seen 1 times before; Sensex was up after it 100% of the time, average +0.91%. Too few outcomes (1/20) to trade on.
  - Same, only when the trend was `weekly sideways · 125m up`: Seen 1 times before; Sensex was up after it 100% of the time, average +0.91%. Too few outcomes (1/20) to trade on.

## Strong vs weak writers, weekly 2026-11-26

Strongest call writers at 85500, strongest put writers at 83000; weakest call writers at 83000, weakest put writers at -. Covers 75% of near-money call OI and 74% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82600 | 55880 | 42138 | 848.4 | 83024 | 1465.5 | 83448 | -332 | -617.1 | weak |
| Call | 82700 | 81500 | 63443 | 791.0 | 83023 | 1389.0 | 83491 | -289 | -598.0 | weak |
| Call | 82800 | 166600 | 120865 | 733.3 | 83023 | 1309.8 | 83533 | -247 | -576.4 | weak |
| Call | 82900 | 117300 | 82748 | 688.0 | 83022 | 1240.0 | 83588 | -192 | -552.0 | weak |
| Call | 83000 | 283660 | 167109 | 662.5 | 83020 | 1171.7 | 83662 | -118 | -509.2 | weak |
| Call | 83100 | 137780 | 121729 | 633.5 | 83044 | 1087.5 | 83734 | -46 | -453.9 | weak |
| Call | 83200 | 93680 | 85234 | 598.5 | 83094 | 1034.3 | 83799 | +19 | -435.8 | weak |
| Call | 83300 | 124980 | 113387 | 544.6 | 83072 | 969.0 | 83845 | +65 | -424.4 | weak |
| Call | 83400 | 111500 | 95193 | 574.0 | 83204 | 903.6 | 83974 | +194 | -329.6 | medium |
| Call | 83500 | 200080 | 137218 | 512.5 | 83177 | 846.6 | 84012 | +233 | -334.2 | medium |
| Call | 83600 | 129740 | 116031 | 518.2 | 83264 | 789.4 | 84118 | +338 | -271.1 | medium |
| Call | 83700 | 279880 | 259488 | 597.5 | 83502 | 732.7 | 84298 | +518 | -135.2 | strong |
| Call | 83800 | 239360 | 217898 | 562.8 | 83523 | 677.3 | 84363 | +583 | -114.5 | strong |
| Call | 83900 | 136220 | 124853 | 454.0 | 83366 | 630.1 | 84354 | +574 | -176.2 | strong |
| Call | 84000 | 391140 | 266543 | 362.0 | 83230 | 582.1 | 84362 | +582 | -220.1 | strong |
| Call | 84100 | 101640 | 90225 | 369.5 | 83335 | 536.1 | 84470 | +690 | -166.6 | strong |
| Call | 84200 | 108200 | 98476 | 380.6 | 83448 | 493.1 | 84581 | +801 | -112.4 | strong |
| Call | 84300 | 81100 | 70671 | 242.2 | 83152 | 454.1 | 84542 | +762 | -211.9 | strong |
| Call | 84400 | 87860 | 71810 | 261.6 | 83262 | 416.4 | 84662 | +882 | -154.9 | strong |
| Call | 84500 | 202740 | 117861 | 190.4 | 83095 | 379.9 | 84690 | +910 | -189.5 | strong |
| Call | 84600 | 81940 | 74496 | 254.9 | 83400 | 348.2 | 84855 | +1075 | -93.4 | strong |
| Call | 84700 | 84380 | 72389 | 236.0 | 83431 | 318.1 | 84936 | +1156 | -82.1 | strong |
| Call | 84800 | 111920 | 96418 | 188.7 | 83306 | 289.0 | 84989 | +1209 | -100.3 | strong |
| Call | 84900 | 71520 | 50031 | 123.1 | 83069 | 263.7 | 85023 | +1243 | -140.6 | strong |
| Call | 85000 | 326940 | 189724 | 114.3 | 83064 | 239.8 | 85114 | +1334 | -125.5 | strong |
| Put | 82600 | 177460 | 139687 | 503.0 | 83059 | 243.5 | 82097 | +1683 | +259.5 | strong |
| Put | 82700 | 304960 | 264373 | 466.8 | 83250 | 265.0 | 82233 | +1547 | +201.8 | strong |
| Put | 82800 | 353540 | 261454 | 593.2 | 83034 | 289.0 | 82207 | +1573 | +304.2 | strong |
| Put | 82900 | 209240 | 167441 | 628.5 | 83049 | 313.4 | 82272 | +1508 | +315.1 | strong |
| Put | 83000 | 527500 | 339800 | 627.5 | 83098 | 341.0 | 82372 | +1407 | +286.5 | strong |
| Put | 83100 | 189420 | 177760 | 655.2 | 83111 | 371.6 | 82445 | +1335 | +283.5 | strong |
| Put | 83200 | 178720 | 170646 | 672.5 | 83192 | 404.1 | 82527 | +1252 | +268.5 | strong |
| Put | 83300 | 123160 | 117145 | 660.4 | 83329 | 437.4 | 82640 | +1140 | +223.0 | strong |
| Put | 83400 | 117800 | 113560 | 675.8 | 83412 | 476.4 | 82724 | +1056 | +199.4 | strong |
| Put | 83500 | 248700 | 233841 | 675.4 | 83499 | 513.2 | 82825 | +955 | +162.2 | strong |
| Put | 83600 | 132640 | 129260 | 641.3 | 83649 | 556.0 | 82959 | +821 | +85.2 | strong |
| Put | 83700 | 190240 | 186500 | 661.7 | 83687 | 598.6 | 83038 | +742 | +63.0 | strong |
| Put | 83800 | 129420 | 125860 | 719.1 | 83675 | 646.6 | 83081 | +699 | +72.5 | strong |
| Put | 83900 | 62180 | 58820 | 768.8 | 83676 | 700.1 | 83131 | +649 | +68.7 | strong |
| Put | 84000 | 89540 | 75960 | 884.6 | 83588 | 748.5 | 83115 | +665 | +136.1 | strong |
| Put | 84100 | 15960 | 15440 | 973.0 | 83573 | 807.7 | 83127 | +653 | +165.3 | strong |
| Put | 84200 | 16260 | 16140 | 988.5 | 83639 | 865.0 | 83212 | +568 | +123.5 | strong |
| Put | 84300 | 9520 | 8151 | 1006.0 | 83682 | 921.0 | 83294 | +486 | +85.0 | strong |
| Put | 84400 | 6840 | 6821 | 1130.2 | 83629 | 988.5 | 83270 | +510 | +141.6 | strong |
| Put | 84500 | 15400 | 14980 | 1185.0 | 83635 | 1053.8 | 83315 | +465 | +131.3 | strong |
| Put | 84600 | 3560 | 3560 | 1284.2 | 83627 | 1121.8 | 83316 | +464 | +162.4 | strong |
| Put | 84700 | 1600 | 1600 | 1431.5 | 83559 | 1190.2 | 83268 | +512 | +241.4 | strong |
| Put | 84800 | 400 | 400 | 1998.4 | 83164 | 1242.0 | 82802 | +978 | +756.4 | strong |
| Put | 84900 | 1420 | 1420 | 1875.8 | 83224 | 1323.8 | 83024 | +756 | +552.0 | strong |
| Put | 85000 | 14360 | 12176 | 1764.0 | 83311 | 1411.1 | 83236 | +544 | +352.9 | strong |

## Strong vs weak writers, monthly 2026-12-31

Strongest call writers at 83000, strongest put writers at 83000; weakest call writers at -, weakest put writers at -. Covers 78% of near-money call OI and 80% of put OI (the rest was open before it was watched, so its selling price is unknown).

| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |
|---|---|---|---|---|---|---|---|---|---|---|
| Call | 82800 | 320 | 100 | 1766.7 | 83023 | 1766.7 | 84567 | +787 | +0.0 | strong |
| Call | 83000 | 7600 | 6576 | 2115.3 | 83516 | 2214.9 | 85115 | +1335 | -99.6 | strong |
| Call | 83100 | 80 | 40 | 1607.8 | 83023 | 1786.2 | 84708 | +928 | -178.4 | strong |
| Call | 83200 | 120 | 15 | 2180.4 | 83732 | 2129.1 | 85380 | +1600 | +51.4 | strong |
| Call | 83300 | 40 | 40 | 1653.3 | 83117 | 1653.3 | 84953 | +1173 | +0.0 | strong |
| Call | 83400 | 120 | 109 | 1484.0 | 83023 | 2050.1 | 84884 | +1104 | -566.1 | strong |
| Call | 83500 | 700 | 354 | 1621.6 | 83190 | 2012.5 | 85122 | +1342 | -390.9 | strong |
| Call | 83600 | 260 | 260 | 1610.9 | 83438 | 1627.2 | 85211 | +1431 | -16.3 | strong |
| Call | 83700 | 420 | 420 | 1620.8 | 83414 | 1885.0 | 85321 | +1541 | -264.2 | strong |
| Call | 83800 | 160 | 160 | 1589.6 | 83424 | 1788.5 | 85390 | +1610 | -198.8 | strong |
| Call | 83900 | 660 | 620 | 1438.5 | 83244 | 1764.6 | 85339 | +1559 | -326.1 | strong |
| Call | 84000 | 1240 | 1240 | 1428.8 | 83304 | 1681.8 | 85429 | +1649 | -252.9 | strong |
| Call | 84100 | 60 | 60 | 1412.8 | 83406 | 1600.0 | 85513 | +1733 | -187.2 | strong |
| Call | 84200 | 720 | 703 | 1320.8 | 83321 | 1569.8 | 85521 | +1741 | -249.0 | strong |
| Call | 84300 | 40 | 40 | 1278.3 | 83117 | 1351.5 | 85578 | +1798 | -73.2 | strong |
| Call | 84500 | 20 | 20 | 1285.3 | 83519 | 1449.2 | 85785 | +2005 | -163.9 | strong |
| Call | 84600 | 40 | 40 | 1052.9 | 83137 | 1153.7 | 85653 | +1873 | -100.8 | strong |
| Call | 84700 | 120 | 120 | 1037.1 | 83172 | 1187.1 | 85737 | +1957 | -150.0 | strong |
| Call | 84800 | 100 | 100 | 1009.5 | 83203 | 1129.5 | 85810 | +2030 | -120.0 | strong |
| Call | 84900 | 120 | 120 | 969.8 | 83203 | 1099.4 | 85870 | +2090 | -129.7 | strong |
| Call | 85000 | 540 | 540 | 1075.6 | 83478 | 1190.0 | 86076 | +2296 | -114.4 | strong |
| Put | 82700 | 100 | 100 | 1182.2 | 83322 | 1018.2 | 81518 | +2262 | +164.0 | strong |
| Put | 82800 | 260 | 260 | 1262.6 | 83210 | 1227.2 | 81537 | +2243 | +35.3 | strong |
| Put | 82900 | 180 | 180 | 1342.9 | 83166 | 1263.3 | 81557 | +2223 | +79.5 | strong |
| Put | 83000 | 9020 | 8136 | 1272.6 | 83327 | 1089.0 | 81727 | +2053 | +183.6 | strong |
| Put | 83100 | 260 | 260 | 1417.8 | 83121 | 1219.2 | 81682 | +2098 | +198.6 | strong |
| Put | 83200 | 480 | 480 | 1428.8 | 83156 | 1266.2 | 81771 | +2009 | +162.6 | strong |
| Put | 83300 | 440 | 440 | 1514.9 | 83101 | 1379.7 | 81785 | +1995 | +135.3 | strong |
| Put | 83400 | 600 | 600 | 1508.2 | 83205 | 1251.2 | 81892 | +1888 | +257.0 | strong |
| Put | 83500 | 1860 | 1391 | 1534.8 | 83252 | 1300.0 | 81965 | +1815 | +234.8 | strong |
| Put | 83600 | 740 | 740 | 1561.4 | 83257 | 1331.0 | 82039 | +1741 | +230.5 | strong |
| Put | 83700 | 660 | 660 | 1559.8 | 83353 | 1378.9 | 82140 | +1640 | +180.9 | strong |
| Put | 83800 | 220 | 220 | 1461.5 | 83614 | 1393.3 | 82339 | +1441 | +68.2 | strong |
| Put | 83900 | 320 | 300 | 1444.5 | 83722 | 1436.2 | 82455 | +1324 | +8.3 | strong |
| Put | 84000 | 700 | 700 | 1559.8 | 83604 | 1455.0 | 82440 | +1340 | +104.8 | strong |
| Put | 84100 | 480 | 480 | 1545.7 | 83745 | 1544.1 | 82554 | +1226 | +1.6 | strong |
| Put | 84200 | 580 | 580 | 1551.9 | 83760 | 1543.2 | 82648 | +1132 | +8.7 | strong |
| Put | 84300 | 680 | 680 | 1638.1 | 83733 | 1589.8 | 82662 | +1118 | +48.3 | strong |
| Put | 84400 | 440 | 440 | 1717.9 | 83718 | 1652.1 | 82682 | +1098 | +65.8 | strong |
| Put | 84500 | 320 | 320 | 1770.3 | 83667 | 1682.8 | 82730 | +1050 | +87.5 | strong |
| Put | 84600 | 260 | 260 | 1910.0 | 83558 | 1797.5 | 82690 | +1090 | +112.6 | strong |
| Put | 84700 | 220 | 220 | 1959.9 | 83572 | 1820.5 | 82740 | +1040 | +139.4 | strong |
| Put | 84800 | 100 | 100 | 2170.5 | 83203 | 2170.5 | 82630 | +1150 | +0.0 | strong |
| Put | 84900 | 140 | 140 | 2229.6 | 83379 | 1947.0 | 82670 | +1110 | +282.5 | strong |
| Put | 85000 | 2520 | 2520 | 1991.6 | 83702 | 1995.7 | 83008 | +772 | -4.1 | strong |

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| monthly | PCR up · put writing · walls same · near put wall | 2 | 100% | +0.06% | +0.06 to +0.06% |  | too few (1/10) |
| weekly | PCR flat · put and call writing · walls same · near put wall | 2 | 100% | +0.75% | +0.69 to +0.80% |  | too few (2/10) |
| monthly | PCR up · put and call writing · walls up · near put wall | 2 | 100% | +0.76% | +0.72 to +0.80% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · near put wall | 1 | 100% | +0.08% | +0.08 to +0.08% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR up · put and call writing · walls same · near call wall | 1 | 100% | +0.92% | +0.92 to +0.92% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.69% | +0.69 to +0.69% |  | too few (1/10) |
| monthly | PCR up · put and call writing · walls up · near call wall | 1 | 100% | +0.91% | +0.91 to +0.91% |  | too few (1/10) |
| monthly | PCR down · put and call writing · walls same · near put wall | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR down · put and call writing · walls up · near put wall | 1 | 100% | +0.91% | +0.91 to +0.91% |  | too few (1/10) |
| weekly | PCR down · unwinding · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR flat · put writing · walls up · near put wall | 1 | 100% | +0.31% | +0.31 to +0.31% |  | too few (1/10) |
| weekly | PCR flat · unwinding · walls same · near put wall | 1 | 100% | +0.08% | +0.08 to +0.08% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls same · near put wall | 1 | 100% | +0.73% | +0.73 to +0.73% |  | too few (1/10) |
| weekly | PCR up · put and call writing · walls up · near put wall | 1 | 100% | +0.92% | +0.92 to +0.92% |  | too few (1/10) |
| weekly | PCR up · put writing · walls same · near put wall | 1 | 100% | +0.06% | +0.06 to +0.06% |  | too few (1/10) |

## Day patterns (Nifty move next day)

| Expiry | Pattern | Seen | Up after | Avg move next day | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put and call writing · walls up · near put wall | 1 |  |  |  |  | too few (0/10) |

## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)

| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers | 8 | 100% | +0.50% | too few (6/10) |
| intraday | weekly | writers even · few weak writers | 5 | 100% | +0.81% | too few (5/10) |
| intraday | weekly | writers even · weak calls | 4 | 100% | +0.15% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers | 2 | 100% | +0.75% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts | 1 | 100% | +1.49% | too few (1/10) |
| intraday | weekly | writers even · weak puts | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers | 2 | 100% | +0.91% | too few (1/10) |
| day | weekly | writers even · weak calls | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts | 1 | 100% | +0.91% | too few (1/10) |

## Writer patterns by market trend

| Layer | Expiry | Writers · trend | Seen | Up after | Avg move | Lean |
|---|---|---|---|---|---|---|
| intraday | monthly | writers even · few weak writers · weekly sideways · 125m up | 8 | 100% | +0.50% | too few (6/10) |
| intraday | weekly | writers even · few weak writers · weekly sideways · 125m up | 5 | 100% | +0.81% | too few (5/10) |
| intraday | weekly | writers even · weak calls · weekly sideways · 125m up | 4 | 100% | +0.15% | too few (3/10) |
| intraday | monthly | put writers stronger · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.75% | too few (2/10) |
| intraday | weekly | call writers stronger · weak puts · weekly sideways · 125m up | 1 | 100% | +1.49% | too few (1/10) |
| intraday | weekly | writers even · weak puts · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | monthly | writers even · few weak writers · weekly sideways · 125m up | 2 | 100% | +0.91% | too few (1/10) |
| day | weekly | writers even · weak calls · weekly sideways · 125m up | 1 |  |  | too few (0/10) |
| day | weekly | writers even · weak puts · weekly sideways · 125m up | 1 | 100% | +0.91% | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Every reading is also tagged with the Nifty trend at the time on the weekly chart (10 years of candles) and the 125-min chart, and each pattern is learned again within each trend pair, so a lean that only held in a bearish market shows up as such. The 25-min trend is shown for timing entries but does not split the learning.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
