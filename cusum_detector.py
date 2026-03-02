import numpy as np
from config import Config

def detect_cusum(series):
    mean = np.mean(series)
    cusum_pos, cusum_neg = 0, 0
    breakpoints = []

    for i, x in enumerate(series):
        cusum_pos = max(0, cusum_pos + x - mean)
        cusum_neg = min(0, cusum_neg + x - mean)

        if cusum_pos > Config.CUSUM_THRESHOLD or cusum_neg < -Config.CUSUM_THRESHOLD:
            breakpoints.append(i)
            cusum_pos, cusum_neg = 0, 0

    return breakpoints
