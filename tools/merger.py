import pandas as pd

fireData = pd.read_csv("../datasets/CLEANEDforestfires.csv")

controlData = pd.read_csv("../datasets/FINALCLEANcontroldata.csv")

# Reorder the columns in both DataFrames to have consistent order
fireData = fireData[['month', 'day', 'temp', 'RH', 'wind', 'rain', 'class']]
controlData = controlData[['month', 'day', 'temp', 'RH', 'wind', 'rain', 'class']]

# Concatenate (merge) the two DataFrames vertically
merged_df = pd.concat([fireData, controlData], ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv("../datasets/MERGEDDATA.csv", index=False)
