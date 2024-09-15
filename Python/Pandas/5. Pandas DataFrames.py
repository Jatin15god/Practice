import pandas as pd

# DataFrame is a 2D array like Data Structure

items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

'''
    Keys  : Column Headers (Bob, Alice)
    Index : Row Headers (bike, book, etc.)
    Value : Value

    Without index, rows assigned numerical Headers.
'''

Shopping_Cart = pd.DataFrame(items)

print(Shopping_Cart)
print()

print(f"Shape     : {Shopping_Cart.shape}")
print(f"Dimension : {Shopping_Cart.ndim}")
print(f"Size      : {Shopping_Cart.size}")
print(f"Values    : {Shopping_Cart.values}")
print(f"Index     : {Shopping_Cart.index}")
print()

# We can select specific column or row
Bob_Cart = pd.DataFrame(items, columns=['Bob'])
print(Bob_Cart)
Select_Cart = pd.DataFrame(items, index=['pants', 'wool'])
# Adding a random index doesn't affect Dataframe
print(Select_Cart)
