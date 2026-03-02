import numpy as np

def detect_bayesian(series, threshold=0.8):
    prob = np.abs(series - np.mean(series)) / np.std(series)
    breakpoints = np.where(prob > threshold)[0].tolist()
    return breakpoints
