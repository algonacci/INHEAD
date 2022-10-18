import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--set", required=True, help="which dataset?")
ap.add_argument("-q", "--quantity", help="how much row?")
args = vars(ap.parse_args())

def check_df(dataset, quantity=args["quantity"]) -> None:
    df = pd.read_csv("data/result/"+dataset+".csv")
    if quantity:
        print(df.head(int(quantity)))
    else:
        print(df)

if __name__ == "__main__":
    check_df(args["set"])