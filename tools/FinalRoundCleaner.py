import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../datasets/CLEANROUND2controldata.csv")

    # converting days to a number
    day_to_number = {
        'Mon': 1,
        'Tue': 2,
        'Wed': 3,
        'Thu': 4,
        'Fri': 5,
        'Sat': 6,
        'Sun': 7
    }

    # Convert day names to day numbers using map() function
    df['day'] = df['day'].map(day_to_number)
    df['class'] = 0

    df.to_csv('../datasets/FINALCLEANcontroldata.csv', index=False)