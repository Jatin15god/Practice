import pandas as pd

items = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items, index = ['Store 1 :', 'Store 2 :'])

print(store_items)
print()

# We access rows, columns and elements using labels.
print('How many bikes are in each store:\n', store_items[['bikes']])
print()
print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
print()
print('What items are in Store 1:\n', store_items.loc[['Store 1 :']])
print()
print('How many bikes are in Store 2:', store_items['bikes']['Store 2 :']) # db[column][row]
print()

# Add new Column
store_items['shirts'] = [15,2]

# Add while Arithmetic Operation
store_items['suits'] = store_items['shirts'] + store_items['pants']

# Add new row
new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]
new_store = pd.DataFrame(new_items, index=['Store 3 :'])
store_items = store_items.append(new_store)

# Add new Column with item in specific store
# Add new watches same as old except in Store 1
store_items['New Watch'] = store_items['watches'][1:]

# Add new Column at certain position
store_items.insert(5, 'shoes', [8,5,3]) # insert(pos, col_name, data_list)

print("Updated Stores 1 :-")
print(store_items)


# Delete Column
store_items.pop('New Watch') # Only for Column

# Delete rows and columns
store_items.drop(['watches', 'shoes'], axis=1, inplace=True)
store_items.drop(['Store 3 :'], axis=0, inplace=True)

# Rename columns and rows
store_items = store_items.rename(columns={'bikes':'hats'}, index={'Store 1 :':'0', 'Store 2 :':'1'})


# Set an existing column as index column
store_items[''] = ['Store 2 :', 'Store 3 :']
store_items = store_items.set_index('')

print("Updated Stores 2 :-")
print(store_items)