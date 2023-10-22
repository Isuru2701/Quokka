import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("datasets/CLEANROUND1controldata.csv")


    df.to_csv('../datasets/CLEANROUND2controldata.csv', index=False)