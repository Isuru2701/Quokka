import pandas as pd
import tensorflow as tf

# using keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

"""
    Steps
    1. Load forestfires.csv
    2. Drop area column
    3. Add new column 'class' and fill with 1 (fire)
    4. Load new dataset for days without fire and add new column 'class' with values 0 (no_fire)
    5. merge two datasets
    6. split into testing and training
    7. build model
    8. compile model
    9. train model
    10. test & evaluate
    
    May or may not use FFMC DMC DC and ISI

"""

# load forestfires.csv

fireData = pd.read_csv('../datasets/forestfires.csv')
fireData.drop(['X', 'Y', 'FFMC', 'DMC', 'DC', 'ISI'], axis=1, inplace=True)

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

print(fireData.head())

# Prep non-fire data
