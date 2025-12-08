import pandas as pd
from src.zigzag import compute_zigzag
import matplotlib.pyplot as plt

df = pd.read_excel("data/BATS_MSFT_5_1.xlsx")

dfz = compute_zigzag(df, pct=5)

plt.plot(dfz["Close"], label="Close")
plt.plot(dfz["ZigZag"], label="ZigZag")
plt.legend()
plt.show()
