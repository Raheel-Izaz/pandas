import pandas as pd

# Data Cleaning : is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. It is an essential step in the data analysis process to ensure that the data is accurate and reliable for analysis.
# About 75% of work done with Pandas is data cleaning.


df = pd.read_csv('employeesDirtyData.csv')

# 1. Drop irrelevant columns
df = df.drop(columns=['EmploymentType','HireDate'])

# 2. Handling Missing
# df=df.dropna(subset=['ExperienceYears']) # Drop rows with missing values
df = df.fillna({'ExperienceYears': 0,'IsActive':'FALSE'}) # Fill missing values

# 3. Handling Inconsistent Data
df['IsActive'] = df['IsActive'].replace({'true':'TRUE','YES':'TRUE'})
df['IsActive'] = df['IsActive'].replace({'TRUE':1,'FALSE':0})


#  4. Standardize Data
df['FirstName'] = df['FirstName'].str.lower()

#  5. Fix Data Types

df['IsActive'] = df['IsActive'].astype(bool)
df = df.drop_duplicates()
print(df)
print(df.info())


# print(df[df.duplicated()])