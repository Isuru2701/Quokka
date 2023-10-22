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



