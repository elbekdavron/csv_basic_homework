#Define function,Get coloumn names from a csv file
import csv
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    next(data)
    list_names = []
    for row in data:
        list_names.append(row[1])
    return list_names
    
# Read the csv file
data = open("data.csv")



print(get_column_names(data))