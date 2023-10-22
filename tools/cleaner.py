import csv

if __name__ == "__main__":

    # Input and output file paths
    input_csv_file = "../datasets/WildFire_Prediction_Data_Set.csv"
    output_csv_file = "../datasets/CLEAN_WildFire_Prediction_Data_Set.csv"


    # Function to remove double quotes from a string
    def remove_double_quotes(value):
        return value.replace('"', '')


    # Read data from input CSV and write updated data to output CSV
    with open(input_csv_file, "r", newline="") as input_file, open(output_csv_file, "w", newline="") as output_file:
        data = input_file.read()
        data = remove_double_quotes(data)
        output_file.write(data)
