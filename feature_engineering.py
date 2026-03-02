import numpy as np
import pandas as pd
from config import Config

def engineer_features(df):
    df['log_return'] = np.log(df['Close'] / df['Close'].shift(1))
    df['rolling_vol'] = df['log_return'].rolling(Config.WINDOW_VOL).std()
    df['volume_zscore'] = (
        (df['Volume'] - df['Volume'].rolling(20).mean()) /
        df['Volume'].rolling(20).std()
    )
    df['amihud'] = abs(df['log_return']) / df['Volume']
    df.dropna(inplace=True)
    return df
