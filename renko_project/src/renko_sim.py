import numpy as np
def simulate_renko_profit(prices,brick):
    if brick<=0 or len(prices)<2: return 0,0,0
    last=prices.iloc[0]; lp=False; sp=False; lpnl=0; spnl=0; cnt=0
    for p in prices.iloc[1:]:
        mv=p-last
        while abs(mv)>=brick:
            step=np.sign(mv)*brick; nl=last+step; cnt+=1
            if step>0:
                if sp: spnl+=last-nl; sp=False
                lp=True
            else:
                if lp: lpnl+=nl-last; lp=False
                sp=True
            last=nl; mv=p-last
    return float(lpnl),float(spnl),cnt
