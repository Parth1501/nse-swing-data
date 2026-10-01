"""One-off chart for a stock that is not on today's eligible list (e.g. for an on-demand teardown).
Usage: CHART_SYMBOLS="POLICYBZR" python tools/chart_one.py  -> data/charts/<data date>/<SYMBOL>.png
Uses the stock's latest.csv row for levels; same drawing code as the daily list."""
import os
import sys

import pandas as pd
import yfinance as yf

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import charts          # noqa: E402
import scan_data       # noqa: E402

table = pd.read_csv("data/latest.csv")
for sym in os.environ.get("CHART_SYMBOLS", "").split():
    df = yf.download(sym + ".NS", period="2y", interval="1d", auto_adjust=False, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df.dropna(subset=["Open", "High", "Low", "Close"])
    rows = table[table["symbol"] == sym]
    row = rows.iloc[0].to_dict() if len(rows) else {"symbol": sym}
    row["history_sessions"] = len(df)
    peaks, troughs = scan_data.swing_points(df["High"].to_numpy(dtype=float), df["Low"].to_numpy(dtype=float))
    path = os.path.join("data", "charts", df.index[-1].strftime("%Y-%m-%d"), f"{sym}.png")
    charts.draw(sym, df, row, peaks, troughs, path)
    print("chart", path, "last close", float(df["Close"].iloc[-1]))
