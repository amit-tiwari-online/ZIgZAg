import pandas as pd
def zigzag_pivots(prices,pct=0.0025):
    arr=prices.values; idx=prices.index
    piv=[]; lp=arr[0]; ltype=None
    for i,val in enumerate(arr[1:],1):
        ch=(val-lp)/lp
        if ltype in (None,"low"):
            if ch>=pct:
                ltype="high"; lp=val; piv.append((idx[i],float(val),"high"))
        else:
            if ch<=-pct:
                ltype="low"; lp=val; piv.append((idx[i],float(val),"low"))
        if piv and piv[-1][2]=="high" and val>piv[-1][1]:
            piv[-1]=(idx[i],float(val),"high"); lp=val
        if piv and piv[-1][2]=="low" and val<piv[-1][1]:
            piv[-1]=(idx[i],float(val),"low"); lp=val
    return piv

def zigzag_legs_from_pivots(piv):
    legs=[]
    for i in range(1,len(piv)):
        p1,p2=piv[i-1],piv[i]
        direction="up" if p2[1]>p1[1] else "down"
        legs.append({"start_ts":p1[0],"end_ts":p2[0],"start_price":p1[1],"end_price":p2[1],"direction":direction})
    return legs
