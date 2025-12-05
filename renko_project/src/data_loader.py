import pandas as pd
def load_data(path="data/sample_data.csv", tz=None):
    df = pd.read_csv(path)
    req = {"timestamp","open","high","low","close"}
    if not req.issubset(set(df.columns)):
        raise ValueError("Bad columns")
    df['timestamp']=pd.to_datetime(df['timestamp'])
    df=df.sort_values('timestamp').set_index('timestamp')
    return df
