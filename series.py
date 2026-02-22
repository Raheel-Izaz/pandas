import pandas as pd

# Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index.  

calories = {
    'Day 1': 1500,
    'Day 2': 2000,
    'Day 3': 2500
}

series = pd.Series(calories)
series.loc["Day 2"] += 200 

print(series[series > 2000])

# data = [101, 102, 103, 104, 105]
# indices = ['a', 'b', 'c', 'd', 'e']
# series = pd.Series(data,index=indices)


# print(series[series > 102])