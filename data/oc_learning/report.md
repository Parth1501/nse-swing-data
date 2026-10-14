# Nifty option chain pattern log
Updated 2026-10-14 13:45 IST. Learns only from live snapshots since 14 Oct 2026. Analysis only, not trading advice.

## Data
- 10 snapshots over 1 trading days
- 10 patterns logged; 9 different patterns so far

## Latest read (2026-10-14 13:14:33)

| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |
|---|---|---|---|---|---|---|---|---|
| 2026-10-19 (weekly) | 5.1 | 22566 | 0.859 | 22650 | 22500 | 22700 | ±1.36% (22259-22872) | 13.86 |
| 2026-10-27 (monthly) | 13.1 | 22560 | 1.045 | 23000 | 22000 | 23500 | ±2.09% (22088-23031) | 13.62 |

- **Weekly, last 30 min**: `PCR down · call writing · walls down · near put wall`. New pattern, never seen before. Logged; nothing to go on yet.
- **Weekly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).
- **Monthly, last 30 min**: `PCR up · call writing · walls same · mid walls`. New pattern, never seen before. Logged; nothing to go on yet.
- **Monthly, today vs previous day**: `-`. No pattern yet (needs an earlier snapshot to compare with).

## 30-minute patterns (Nifty move to that day's close)

| Expiry | Pattern | Seen | Up after | Avg move to close | Range | Walls held to expiry | Lean |
|---|---|---|---|---|---|---|---|
| weekly | PCR up · put writing · walls same · near put wall | 2 | 0% | -0.68% | -0.72 to -0.64% |  | too few (2/10) |
| monthly | PCR down · call writing · walls same · mid walls | 1 | 0% | -0.74% | -0.74 to -0.74% |  | too few (1/10) |
| monthly | PCR flat · call writing · walls same · mid walls | 1 | 0% | -0.65% | -0.65 to -0.65% |  | too few (1/10) |
| monthly | PCR up · call writing · walls same · mid walls | 1 |  |  |  |  | too few (0/10) |
| monthly | PCR flat · quiet OI · walls same · mid walls | 1 | 0% | -0.72% | -0.72 to -0.72% |  | too few (1/10) |
| monthly | PCR up · quiet OI · walls same · mid walls | 1 | 0% | -0.67% | -0.67 to -0.67% |  | too few (1/10) |
| weekly | PCR down · call writing · walls down · near put wall | 1 |  |  |  |  | too few (0/10) |
| weekly | PCR down · call writing · walls same · near put wall | 1 | 0% | -0.62% | -0.62 to -0.62% |  | too few (1/10) |
| weekly | PCR flat · call writing · walls same · near put wall | 1 | 0% | -0.65% | -0.65 to -0.65% |  | too few (1/10) |

## How to read this
- A pattern is: near-money PCR change · where new OI near the money went · how the put and call walls (biggest OI strikes) moved · where spot sits between the walls.
- A pattern shows a lean only after 10 outcomes, and only when the 95% range of 'up after' sits fully above or below 50%. It points to a structure only after 20 outcomes.
- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.
- 30-minute patterns from one day move together, so trust a lean more once it has held across several weeks, not one busy day.
- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.
- Walls held means every daily close stayed between the walls; an intraday breach that closed back inside counts as held.
