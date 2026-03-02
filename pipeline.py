from data_loader import load_data
from feature_engineering import engineer_features
from pelt_detector import detect_pelt
from cusum_detector import detect_cusum
from bayesian_detector import detect_bayesian
from validator import validate_break
from regime_classifier import classify_regimes
import numpy as np

def run_pipeline():
    df = load_data()
    df = engineer_features(df)

    series = df['rolling_vol']

    pelt_breaks = detect_pelt(series)
    cusum_breaks = detect_cusum(series)
    bayes_breaks = detect_bayesian(series)

    combined = list(set(pelt_breaks + cusum_breaks + bayes_breaks))

    validated = [idx for idx in combined if validate_break(series, idx)]

    features = df[['log_return', 'rolling_vol', 'volume_zscore', 'amihud']].values
    regimes = classify_regimes(features)

    df['regime'] = regimes

    return df, validated
