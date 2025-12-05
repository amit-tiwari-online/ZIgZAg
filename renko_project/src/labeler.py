import numpy as np, pandas as pd
from renko_sim import simulate_renko_profit
from zigzag import zigzag_pivots, zigzag_legs_from_pivots

def candidate_bricks_for_day(day_prices,pct_min=0.0005,pct_max=0.02,steps=25):
    lc=day_prices.iloc[-1]
    return list(np.linspace(pct_min,pct_max,steps)*lc)

def evaluate_day(day_df,bricks):
    prices=day_df['close']
    blp=-1e18; bsp=-1e18; blb=None; bsb=None; stats=[]
    for b in bricks:
        lp,sp,c=simulate_renko_profit(prices,b)
        stats.append((b,lp,sp,c))
        if lp>blp: blp=lp; blb=b
        if sp>bsp: bsp=sp; bsb=b
    return {"blp":max(0,blp),"bsp":max(0,bsp),"blb":blb,"bsb":bsb,"stats":stats}

def label_days(df,pct_min=0.0005,pct_max=0.02,steps=25,ratio=1.3,thr=1e-6,chop=0.4):
    out=[]
    for day,g in df.groupby(df.index.date):
        if len(g)<5: out.append((day,0,None,None,0,0,0)); continue
        bricks=candidate_bricks_for_day(g['close'],pct_min,pct_max,steps)
        ev=evaluate_day(g,bricks)
        blp,bsp,blb,bsb=ev["blp"],ev["bsp"],ev["blb"],ev["bsb"]
        meanb=np.mean(bricks); chopth=meanb*chop
        label=0
        if blp>bsp*ratio and blp>thr and blb>chopth: label=1
        elif bsp>blp*ratio and bsp>thr and bsb>chopth: label=-1
        piv=zigzag_pivots(g['close'],pct=0.0025); legs=zigzag_legs_from_pivots(piv)
        out.append((day,label,blb,bsb,blp,bsp,len(legs)))
    return pd.DataFrame(out,columns=["date","label","best_long_brick","best_short_brick","best_long_pnl","best_short_pnl","zz_legs"])
