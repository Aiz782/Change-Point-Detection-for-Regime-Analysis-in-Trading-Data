from scipy.stats import ks_2samp, ttest_ind
import numpy as np
from config import Config

def validate_break(series, idx):
    pre = series[:idx]
    post = series[idx:]

    if len(pre) < 30 or len(post) < 30:
        return False

    ks_p = ks_2samp(pre, post).pvalue
    t_p = ttest_ind(pre, post, equal_var=False).pvalue

    return ks_p < Config.SIGNIFICANCE_LEVEL and t_p < Config.SIGNIFICANCE_LEVEL
