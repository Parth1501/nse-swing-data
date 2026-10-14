# Nifty option chain pattern log
Updated 2026-10-14 13:56 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 12 snapshots over 1 trading days
- 12 patterns logged; 11 different patterns so far

## Latest read (2026-10-14 13:45:23)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 5.1 | 22613 | 0.741 | 22600 | 22500 | 22700 | ±1.29% (22322-22904) | 13.87 |
| 2026-10-27 (monthly) | 13.1 | 22616 | 0.987 | 23000 | 22000 | 23000 | ±2.06% (22151-23081) | 13.56 |

- **Weekly, last 30 min**: `PCR down · call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
- **Monthly, last 30 min**: `PCR down · call writing · walls down · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.48% | -0.52 to -0.43% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.50% | -0.50 to -0.50% |  | too few (1/10) |
| monthly | PCR down · call writing · walls down · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 1 | 0% | -0.40% | -0.40 to -0.40% |  | too few (1/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.47% | -0.47 to -0.47% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.42% | -0.42 to -0.42% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 | 100% | +0.25% | +0.25 to +0.25% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 | 100% | +0.21% | +0.21 to +0.21% |  | too few (1/10) |
| weekly | PCR down · call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.41% | -0.41 to -0.41% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.45% | -0.45 to -0.45% |  | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
