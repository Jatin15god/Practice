import pandas as np

groceries = pd.Series(data=[30,6,'Yes','No'], index=['eggs', 'apples', 'milk', 'bread'])

# Access by Index
print("Access by Index -")
print(f"Total Eggs     : {groceries['eggs']}")
print(f"Milk and Bread : {groceries[['milk', 'bread']]}")
print()

# Access by Index No.
print("Access by Index No. -")
print(f"Total Eggs     : {groceries[0]}")
print(f"Milk and Bread : {groceries[[2, 3]]}")
print()

'''
    Because we can access data in any way, so to remove any
    ambiguity to whether we are referrering to index label or
    number index, Series have 2 attributes :
    loc  : location (for labeled data)
    iloc : integer location (for unlabeled data)
'''

# Access by Attributes
print("Access by Attributes -")
print(f"Total Eggs     : {groceries.loc['eggs']}")
print(f"Milk and Bread : {groceries.loc[['milk', 'bread']]}")
print(f"Total Eggs     : {groceries.iloc[0]}")
print(f"Milk and Bread : {groceries.iloc[[2, 3]]}")
print()


# Update
groceries['eggs'] = 2


# Delete
groceries.drop('apples')
# But it doesn't delete element but return modified series
# So for this:

groceries = groceries.drop('apples')
# or
groceries.drop('eggs', inplace=True)