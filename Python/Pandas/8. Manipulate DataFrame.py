import pandas as pd
from numpy import nan

# Since we will be working with ratings, we will set the precision of our 
# dataframes to one decimal place.
pd.set_option('precision', 1)

'''
    Create a Pandas DataFrame that contains the ratings some users have given to a
    series of books. The ratings given are in the range from 1 to 5, with 5 being
    the best score. The names of the books, the authors, and the ratings of each user
    are given below:
'''

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data = [3.2, nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])


'''
    Users that have np.nan values means that the user has not yet rated that book.
    Use the data above to create a Pandas DataFrame that has the following column
    labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. Let Pandas
    automatically assign numerical row indices to the DataFrame. 
'''

data = {"Book":books, "Author":authors, "U1":user_1, "U2":user_2, "U3":user_3, "U4":user_4}
rating_db = pd.DataFrame(data)
rating_db.fillna(rating_db.mean(), inplace = True)

print(rating_db)
print()

best_rated = rating_db[(rating_db == 5).any(axis = 1)]['Book'].values
print(best_rated)