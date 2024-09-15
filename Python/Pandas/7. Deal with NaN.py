import pandas as pd

items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
        {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
        {'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

'''
    Each Dict in list is collection of values in column with their row index.
    They are just like Series (see chapter 5).
'''

store_items = pd.DataFrame(items, index = ['store 1', 'store 2', 'store 3'])


''' Remove NaN '''

# Check which is nan (nan = True)
x = store_items.isnull()
print(x)
print()

# Count the no. of nan values in each column
print("Empty :-")
x = store_items.isnull().sum()
print(x)
print()

# Count all dataset nan values
x = store_items.isnull().sum().sum()
print(f'Total : {x}')
print()

# Count total filled values in each column
print("Filled :-")
print(store_items.count())
print()


''' Drop rows or columns with NaN values '''

# store_items.dropna(axis=1, inplace=True)
# store_items.dropna(axis=0, inplace=True)


''' Fill NaN with something '''

# store_items.fillna(0) (Replace nan with 0)
    # or
store_items.fillna(method='ffill', axis=0, inplace=True) # methods = ffill, backfill
# Copies previous element to nan, according to axis

store_items.interpolate(method='linear', axis=1, inplace=True)

print("Updated Stores :-")
print(store_items)