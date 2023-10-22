import csv

if __name__ == "__main__":

    # Input and output file paths
    input_csv_file = "../datasets/WildFire_Prediction_Data_Set.csv"
    output_csv_file = "../datasets/CLEAN_WildFire_Prediction_Data_Set.csv"




    with open(input_csv_file, "r", newline="") as input_file, open(output_csv_file, "w", newline="") as output_file:
        output_file.write(input_file.read().replace('"', ''))
