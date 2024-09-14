import pandas as pd
import numpy as np

fruits = pd.Series([10, 6, 3], ['apples', 'oranges', 'bananas'])

# Changes amounts of labels
fruits += 2
fruits -= 2
fruits *= 2
fruits /= 2

# To individual index
fruits['bananas'] += 2
fruits.iloc[0] += 2
fruits.iloc[[1,2]] += 2


fruits = np.sqrt(fruits)
fruits = np.exp(fruits)
fruits = np.power(fruits, 2)