import pandas as pd

if __name__ == "__main__":

    # Load forestfires.csv
    fireData = pd.read_csv('../datasets/forestfires.csv')
    fireData.drop(['X', 'Y', 'FFMC', 'DMC', 'DC', 'ISI', 'area'], axis=1, inplace=True)

    # Dictionary mapping month names to month numbers
    month_to_number = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }

    # converting days to a number
    day_to_number = {
        'mon': 1,
        'tue': 2,
        'wed': 3,
        'thu': 4,
        'fri': 5,
        'sat': 6,
        'sun': 7
    }

    # Convert month & day names to month & day numbers using map() function
    fireData['month'] = fireData['month'].map(month_to_number)
    fireData['day'] = fireData['day'].map(day_to_number)
    fireData['class'] = 1

    fireData.to_csv('../datasets/CLEANEDforestfires.csv', index=False)