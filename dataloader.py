import yfinance as yf
import pandas as pd

def load_data(ticker="^NSEI", start="2020-01-01", end="2024-01-01"):
    df = yf.download(ticker, start=start, end=end)
    df = df[['Close', 'Volume']]
    df.dropna(inplace=True)
    return df*
