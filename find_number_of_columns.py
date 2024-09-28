import csv

def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    
    for i in data:
        return len(i)
    
    
    

# Read the csv file
data = open("data.csv")


print(find_number_of_columns(data))