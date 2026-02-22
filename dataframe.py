import pandas as pd

# Data Frame is a 2-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.


data = {
    "Name": ["John", "Smith", "Sarah", "David"],
    "Age": [25, 30, 35, 40]
}

df = pd.DataFrame(data,index=['Employee1', 'Employee2', 'Employee3', 'Employee4'])


# Add a new column

df['Department'] = ['HR', 'Finance', 'IT', 'Marketing']

# Add a new row

# new_row = pd.DataFrame([{'Name': 'Emily', 'Age': 28, 'Department': 'Sales'}],index=['Employee5'])
# df = pd.concat([df, new_row])


# Add a new rows

new_rows = pd.DataFrame([{'Name': 'Emily', 'Age': 28, 'Department': 'Sales'},
                         {'Name': 'Michael', 'Age': 32, 'Department': 'Operations'}
                         ],index=['Employee5', 'Employee6'])

df = pd.concat([df, new_rows])

print(df)
# print(df.loc['Employee2'])  # Accessing a row by label
# print(df.iloc[1])  # Accessing a row by integer position