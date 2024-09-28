import csv

def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   header = next(data)
   return header

# Read the csv file
data = open("data.csv")


print(get_first_row(data))