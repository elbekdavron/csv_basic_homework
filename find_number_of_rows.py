import csv

def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    return(len(list(data)))

# Read the csv file
data = open("data.csv")



print(find_number_of_rows(data))