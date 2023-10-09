import pandas as pd
import tensorflow as tf
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

# Build dataframe
df = pd.read_csv('datasets/forestfires.csv')
df.drop(['X', 'Y', 'day', 'FFMC', 'DMC', 'DC', 'ISI'], axis=1, inplace=True)
df.dropna(inplace=True)

# Dictionary mapping month names to month numbers
# needed this outside there's an error with the df
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

# Convert month names to month numbers using map() function
df['month'] = df['month'].map(month_to_number)


# Define independent and dependent variables
X = df[['month', 'temp', 'RH', 'wind', 'rain']]
Y = pd.DataFrame((df['area']>0).astype(float))
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print(X_train.dtypes, "|||", Y_train.dtypes)


print(type(X_train), "||||", type(Y_train))

#init model rn
model = Sequential(
    [
        Dense(64, activation='relu', input_shape=(1,)),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ]
)

# make model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#model summary
model.summary()

# Train model
model.fit(X_train, Y_train, epochs=600, batch_size=32, validation_data=(X_test, Y_test))