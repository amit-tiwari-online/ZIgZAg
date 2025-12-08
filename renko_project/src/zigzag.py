import numpy as np
import pandas as pd

def compute_zigzag(df, pct=5):
    closes = df["Close"].values
    length = len(closes)

    zigzag = np.zeros(length)
    last_pivot = closes[0]
    last_pivot_index = 0
    trend = 0

    for i in range(1, length):
        change = (closes[i] - last_pivot) / last_pivot * 100

        if trend >= 0 and change >= pct:
            trend = 1
            zigzag[last_pivot_index] = last_pivot
            last_pivot = closes[i]
            last_pivot_index = i

        elif trend <= 0 and change <= -pct:
            trend = -1
            zigzag[last_pivot_index] = last_pivot
            last_pivot = closes[i]
            last_pivot_index = i

    zigzag[last_pivot_index] = last_pivot
    df["ZigZag"] = zigzag
    return df
