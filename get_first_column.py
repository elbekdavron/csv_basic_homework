def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    next(data)
    list_id = []
    for row in data:
        list_id.append(row[:2])
    return list_id
    
    
# Read the csv file
data = open("data.csv")


print(get_first_column(data))