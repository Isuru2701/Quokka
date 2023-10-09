import pandas as pd
import tensorflow as tf
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

df = pd.read_csv('datasets/forestfires.csv')
df.drop(['X', 'Y', 'day'], axis=1, inplace=True)

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

# Convert month names to month numbers using map() function
df['month'] = df['month'].map(month_to_number)

X = df[['month', 'temp', 'RH', 'wind', 'rain']]
Y = (df['area'] > 0).astype(float)

#split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1)


#build model
model = Sequential(
    [
        Dense(64, activation='relu', input_shape=(5,)),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ]
)

#setup mobile for compiling
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#test
model.summary()


#train model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))


#evaluate output
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Loss: {loss:.2f}')
print(f'Accuracy: {accuracy:.2f}')



# Make predictions on new data
# [[month, temp, RH, wind, rain]]
# some test samples:
# [[6, 40, 20, 4.3,0.0]]
# [[12, 10, 70, 0,0]]
# [[1, 20, 50, 2.2,0.0]]

new_data = [[6, 40, 20, 4.3,0.0]]
predictions = model.predict(new_data)

# prediction in range 0 - 1
print(f'Chance of forest fire: {1 - predictions[0][0]:3f}')

## multiple prediction
import random as rand
new_data = [(rand.randint(1,12), rand.randint(0,40), rand.randint(0,100), rand.randint(0,10), rand.randint(0,10)) for i in range(100)]

predictions = model.predict(new_data)
for i in range(len(new_data)):
    print(f"month: {new_data[i][0]} temp: {new_data[i][1]} RH: {new_data[i][2]} wind: {new_data[i][3]} rain: {new_data[i][4]}\nchance of forest fire: {1-predictions[i][0]:3f}\n")

#save into models folder. Remember to update the version number
model.save('models/quokkaForesterV1.0.h5')

