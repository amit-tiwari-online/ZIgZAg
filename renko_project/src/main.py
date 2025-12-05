from data_loader import load_data
from labeler import label_days
from visualize import plot_price_with_labels, plot_brick_hist

def main():
    df=load_data("data/sample_data.csv")
    lab=label_days(df)
    lab.to_csv("trend_labels.csv",index=False)
    plot_price_with_labels(df,lab)
    plot_brick_hist(lab)

if __name__=="__main__":
    main()
