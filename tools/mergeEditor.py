import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('../datasets/MERGEDDATA.csv')

    df['temp'] = df['temp'] + 15

    df.to_csv('../datasets/SHIFTEDATA.csv', index=False)