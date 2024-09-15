from numpy import array, median

z = array([2,4,6,8]).reshape(2,2)

''' Using Statistical Functions '''

print("Statistics :\n")

print("Average :    All = ", z.mean(), ", Rows = ", z.mean(axis=1), ", Columns = ", z.mean(axis=0))
print("Sum     :    All = ", z.sum(), ", Rows = ", z.sum(axis=1), ", Columns = ", z.sum(axis=0))
# Same can be applied for following functions.
print("SD      : ", z.std())
print("Median  : ", median(z))
print("Max     : ", z.max())
print("Min     : ", z.min())