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
    -----------------------------------
    6. split into testing and training
    7. build model
    8. compile model
    9. train model
    10. test & evaluate
    
    May or may not use FFMC DMC DC and ISI

"""

df = pd.read_csv('../datasets/MERGEDDATA.csv')

#6
X = df[['month', 'day','temp', 'RH', 'wind', 'rain']]
y = df['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=101)

# Build NN
model = Sequential(
    [
        Dense(128, activation='relu', input_shape=(6,)),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ]
)

# Compile NN
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train NN
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

loss, accuracy = model.evaluate(X_test, y_test)
print(f'Loss: {loss:.2f}')
print(f'Accuracy: {accuracy:.2f}')

#Save model
model.save('../models/LoraxV1.0.h5')