import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../datasets/CLEANROUND1controldata.csv")




    # Randomly select rows to remove
    df = df.sample(2000, random_state=42)

    #split granular datetime into month and day
    # Convert the datetime column to pandas datetime object
    df['Local time in Braganca'] = pd.to_datetime(df['Local time in Braganca'], format='%d.%m.%Y %H:%M')

    # Extract month, day, and day of the week and create new columns for each
    df['month'] = df['Local time in Braganca'].dt.month
    df['day'] = df['Local time in Braganca'].dt.strftime(
        '%a')  # %a gives abbreviated weekday names (Mon, Tue, Wed, etc.)


    # Save the updated DataFrame with new columns to a new CSV file

    df.to_csv('../datasets/CLEANROUND2controldata.csv', index=False)