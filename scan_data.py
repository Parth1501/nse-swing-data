"""
Daily NSE swing-scan data builder (runs on GitHub Actions).

Downloads ~2 years of daily prices for the NSE F&O stock universe plus
Nifty 50 and India VIX, calculates every indicator used by the swing-trade
rules, applies the mechanical checks, and writes:
  data/latest.csv  - one row per stock with indicators, levels and pass/fail reasons
  data/meta.json   - data date, market filter numbers, F&O ban list, run stats
"""
import io
import json
import math
import os
import time
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd
import requests
import yfinance as yf

IST = timezone(timedelta(hours=5, minutes=30))
OUT_DIR = "data"
NSE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "*/*",
    "Referer": "https://www.nseindia.com/",
}