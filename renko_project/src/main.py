import pandas as pd
import matplotlib.pyplot as plt
from src.zigzag import compute_zigzag

# 1) Load file
df = pd.read_excel("data/BATS_MSFT_5_1.xlsx.xlsx")

# 2) Compute zigzag (5% threshold)
df = compute_zigzag(df, pct=5)

# 3) Plot
plt.figure(figsize=(14,6))
plt.plot(df["Close"], label="Close Price")
plt.plot(df["ZigZag"], label="ZigZag", linewidth=2)
plt.legend()
plt.title("ZigZag Indicator")
plt.show()
