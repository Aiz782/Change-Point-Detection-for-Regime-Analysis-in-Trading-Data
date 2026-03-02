from fastapi import FastAPI
from src.pipeline import run_pipeline

app = FastAPI()

@app.get("/detect")
def detect():
    df, breaks = run_pipeline()
    return {
        "breakpoints": breaks,
        "latest_regime": int(df['regime'].iloc[-1])
    }
