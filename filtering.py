import pandas as pd

df = pd.read_csv('employeeData.csv')

# print(df)

high_salary = df[df['Salary'] > 80000]
active_employees = df[df['IsActive'] == 1]
start_performers = df[(df['PerformanceRating'] >= 4) & (df['IsActive'] == 1) ]


# print(start_performers)
# print(high_salary)
# print(active_employees)