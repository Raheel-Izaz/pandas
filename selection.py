import pandas as pd


# df = pd.read_csv('employeeData.csv')
df = pd.read_csv('employeeData.csv', index_col='FirstName')

# Selection By Column
# print(df['FirstName'].head())
# print(df['EmployeeID'].head())

# print(df[['FirstName', 'LastName']].head())
# print(df)

# Accessing a row by label

# print(df.loc['Ali']) 

# print(df.loc['Ali', ['EmployeeID', 'Department']]) 

# print(df.loc['Usman':'Saad', ['EmployeeID', 'Department']]) 


# print(df.iloc[2:17]) 

# print(df.iloc[2:17, 0:2]) 

# Difference between loc and iloc is that loc is label based and iloc is integer position based. Means the stop index is exclusive in iloc and inclusive in loc.



# Exercise 

employeeName = input("Enter the employee name: ")

try:
    print(df.loc[employeeName])
except KeyError:
    print(f"{employeeName} not found.")


