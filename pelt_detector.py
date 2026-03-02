import ruptures as rpt
from config import Config

def detect_pelt(series):
    algo = rpt.Pelt(model="rbf").fit(series.values)
    breakpoints = algo.predict(pen=Config.PELT_PENALTY)
    return breakpoints
