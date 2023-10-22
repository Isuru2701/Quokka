import csv

import pandas as pd

if __name__ == "__main__":

    df = pd.read_csv('../datasets/controldata.csv')
    print(df.head())
    print("\n")
    print(df.columns)

    #no precipitation -> 0
    df["RRR"] = df["RRR"].map(lambda x: 0 if x == "No precipitation" or x == "Trace of precipitation" or x=="NaN" else x)

    #drops
    """
    all except Time, T,U, FF, RRR
    """
    df.drop(["Po", "P", "Pa","DD", "ff10", "ff3","N","WW","W1","W2","Tn","Tx","Cl","Nh","H","Cm","Ch","VV", "Td", "tR", "E", "Tg", "E'", "sss"], inplace=True , axis=1)
    df.dropna(inplace=True)
    df['T'] = df['T'].replace(',', '.', regex=True)
    df['T'] = df['T'].replace('"', '', regex=True)
    df['RRR'] = df['RRR'].replace(',', '.', regex=True)
    df['RRR'] = df['RRR'].replace('"', '', regex=True)
    df.to_csv('../datasets/CLEANROUND1controldata.csv', index=False)