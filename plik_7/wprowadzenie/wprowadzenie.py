# zadanie 1

import pandas as pd

df = pd.read_csv('employees.csv')
print(df.head(10))
print(df.columns)
print(df.isna().sum())

# zadanie 2

selected = df[['Name', 'Department', 'Salary']]
it_filter = df[df['Department'] == 'IT']
high_salary = df[df['Salary'] > 70000]

# zadanie 3

df['Experience'].fillna(df['Experience'].mean(), inplace=True)
df.dropna(subset=['Salary'], inplace=True)
df['Salary'] = df['Salary'].astype(int)

# zadanie 4

df['Monthly Salary'] = df['Salary'] / 12

def label_seniority(exp):
    if exp < 3:
        return 'Junior'
    elif exp <= 7:
        return 'Mid'
    else:
        return 'Senior'

df['Seniority'] = df['Experience'].apply(label_seniority)

# zadanie 5

summary = df.groupby(['Department', 'Seniority']).agg({'Salary':
'mean', 'Name': 'count'})


#zadanie 6

df_sorted = df.sort_values(by='Experience', ascending=False)
top_experienced = df_sorted[['Name', 'Experience',
'Department']].head(5)

# zadanie 7

df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])
df['Age'] = 2025 - df['Date of Birth'].dt.year
older_than_40 = df[df['Age'] > 40]


# zadanie 8

departments = pd.read_csv('departments.csv')
merged = df.merge(departments, on='Department')
print(merged[['Name', 'Department', 'Manager']])


# zadanie 9

pivot = pd.pivot_table(df, values='Salary', index='Department',
columns='Seniority', aggfunc='mean')
crosstab = pd.crosstab(df['Department'], df['Seniority'])

# zadanie 10

export_cols = ['Name', 'Department', 'Salary', 'Monthly Salary',
'Seniority', 'Age']
df[export_cols].to_csv('final_employees.csv', index=False)