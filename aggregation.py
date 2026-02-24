import pandas as pd

#  Aggregate functions 
            # Reduces a set of values into a single summary value.
            # Used to summarize and analyze data. Often used with groupby() funciton.

df = pd.read_csv('employeeData.csv')



# Whole DataFrame
# print("Mean : ",df.mean(numeric_only=True))
# print("Sum : ",df.sum(numeric_only=True))
# print("Min : ",df.min(numeric_only=True))
# print("Max : ",df.max(numeric_only=True))
# print("Count : ",df.count())

# Single Column

#  DIY (Do it yurself) : Try to calculate the mean, sum, min, max, count for the 'Salary' column.
# print("Mean Salary : ",df['Salary'].mean())


#  groupby() function
#  Used to group data based on one or more columns and perform aggregate functions on the grouped

group = df.groupby('Department')
print("Mean Salary by Department : ",group['Salary'].mean())
print("Sum Salary by Department : ",group['Salary'].sum())
print("Count Salary by Department : ",group['Salary'].count())
