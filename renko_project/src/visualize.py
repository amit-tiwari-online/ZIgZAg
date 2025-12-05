import matplotlib.pyplot as plt
import pandas as pd
def plot_price_with_labels(df,lab,out="fig_price_with_labels.png"):
    plt.figure(figsize=(16,6)); plt.plot(df['close'])
    for _,r in lab.iterrows():
        d=pd.to_datetime(r['date'])
        col='green' if r['label']==1 else 'red' if r['label']==-1 else 'grey'
        plt.axvspan(d,d+pd.Timedelta(days=1),color=col,alpha=0.1)
    plt.savefig(out); plt.close()

def plot_brick_hist(lab,out="fig_brick_hist.png"):
    b=lab[['best_long_brick','best_short_brick']].melt()['value'].dropna()
    plt.hist(b, bins=20); plt.savefig(out); plt.close()
