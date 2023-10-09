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
print(df.head())

# Define independent and dependent variables
X = df[['month', 'temp', 'RH', 'wind', 'rain']]
Y = pd.DataFrame((df['area']>0).astype(float))
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


print(type(X_train), type(Y_train))

#init model rn
model = Sequential(
    [
        Dense(64, activation='relu', input_shape=(5,)),
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