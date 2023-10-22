import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('../datasets/MERGEDDATA.csv')


    # df = df.iloc[:1000]
    df.loc[df['class'] == 1, 'temp'] += 20
    df.loc[df['class'] == 0, 'temp'] += 10
    df.loc[df['class'] == 0, 'RH'] += 10
    df.loc[df['RH'] > 100, 'RH'] = 100
    df.loc[df['class'] == 0, 'rain'] += 2
    df["rain"] =  df['rain'] + 2

    df = df.iloc[:1000]



    df.to_csv('../datasets/SHIFTEDATA.csv', index=False)