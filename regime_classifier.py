from hmmlearn.hmm import GaussianHMM
import numpy as np

def classify_regimes(features, n_states=3):
    model = GaussianHMM(n_components=n_states, covariance_type="full")
    model.fit(features)
    regimes = model.predict(features)
    return regimes
