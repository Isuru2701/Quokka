import pandas as pd
import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

# Build dataframe
df = pd.read_csv('datasets/forestfires.csv')
df = df.drop(['X', 'Y', 'day'], axis=1)

# Define independent and dependent variables
X = df['month', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain']
Y = (df['area'] > 0).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#init model rn
model = Sequential(
    [
        Dense(64, activation='relu', input_shape=(11,)),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ]
)

