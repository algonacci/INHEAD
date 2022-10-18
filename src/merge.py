import glob
import pandas as pd
from sklearn.utils import shuffle
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--set", required=True, help="dataset type")
args = vars(ap.parse_args())

csv_files = glob.glob("data/"+args["set"]+"_raws/*.csv")
print(csv_files)

def merge_file() -> pd.DataFrame:
    df_append = pd.DataFrame()
    for file in csv_files:
        df_temp = pd.read_csv(file)
        df_append = df_append.append(df_temp, ignore_index=True)

    shuffled = shuffle(df_append, random_state=1)
    shuffled.reset_index(drop=True, inplace=True)
    shuffled.to_csv("data/result/"+args["set"]+".csv", index=False)
    print("""
                        __  __                         _ 
                       |  \/  | ___ _ __ __ _  ___  __| |
                       | |\/| |/ _ \ '__/ _` |/ _ \/ _` |
                       | |  | |  __/ | | (_| |  __/ (_| |
                       |_|  |_|\___|_|  \__, |\___|\__,_|
                                        |___/            

    """)
    return shuffled

if __name__ == "__main__":
    merge_file()