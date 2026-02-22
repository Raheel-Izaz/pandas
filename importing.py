import pandas as pd

df = pd.read_csv('employeeData.csv')

df = pd.read_json('projects.json')


print(df.head())