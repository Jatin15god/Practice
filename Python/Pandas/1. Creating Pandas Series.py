import pandas as pd
#from pandas import Series

# Series is 1D array like object
groceries = pd.Series(data=[30,6,'Yes','No'], index=['eggs', 'apples', 'milk', 'bread'])
print("Data:")
print(groceries)
print()

print(f"Shape     : {groceries.shape}")
print(f"Dimension : {groceries.ndim}")
print(f"Size      : {groceries.size}")
print(f"Values    : {groceries.values}")
print(f"Index     : {groceries.index}")
print()