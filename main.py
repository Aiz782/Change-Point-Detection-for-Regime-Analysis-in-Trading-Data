from src.pipeline import run_pipeline

if __name__ == "__main__":
    df, breaks = run_pipeline()
    print("Validated Breakpoints:", breaks)
    print(df.tail())
