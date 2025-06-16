import pandas as pd

# Zadanie 1: Wczytanie i inspekcja danych

df = pd.read_csv('employees.csv')
print(df.head(10))
print(df.columns)
print(df.isna().sum())


# Zadanie 2: Selekcja i filtrowanie danych

selected = df[['Name', 'Department', 'Salary']]
filter_it = df[df['Department'] == 'IT']
print(filter_it)
high_salary = df[df['Salary'] > 70000]
print(high_salary, end='\n\n')


# Zadanie 3: Obsługa braków danych

df['Experience'] = df['Experience'].fillna(df['Experience'].mean())
df.dropna(subset=['Salary'], inplace=True)
df['Salary'] = df['Salary'].astype(int)
print(df, end='\n\n')

# Zadanie 4: Tworzenie nowych cech

df['Monthly Salary'] = df['Salary'] / 12
def label_seniority(exp):
    if exp < 3:
        return 'Junior'
    elif exp <= 7:
        return 'Mid'
    else:
        return 'Senior'

df['Seniority'] = df['Experience'].apply(label_seniority)

print(df[['Name', 'Experience', 'Salary', 'Monthly Salary', 'Seniority']].head(), end='\n\n')


# Zadanie 5: Grupowanie i agregacja

summary = df.groupby(['Department', 'Seniority']).agg({'Salary':
'mean', 'Name': 'count'})


# Zadanie 6: Sortowanie i najwięksi

df_sorted = df.sort_values(by='Experience', ascending=False)
top_experienced = df_sorted[['Name', 'Experience',
'Department']].head(5)

print(top_experienced, end='\n\n')


# Zadanie 7: Praca z datami i wiekiem

df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])
df['Age'] = 2025 - df['Date of Birth'].dt.year
older_than_40 = df[df['Age'] > 40]

print(older_than_40, end='\n\n')

# Zadanie 8: Łączenie DataFrame'ów

departments = pd.read_csv('departments.csv')
merged = df.merge(departments, on='Department')
print(merged[['Name', 'Department', 'Manager']], end='\n\n')

# Zadanie 9: Tabele przestawne i krzyżowe

pivot = pd.pivot_table(df, values='Salary', index='Department',
columns='Seniority', aggfunc='mean')
crosstab = pd.crosstab(df['Department'], df['Seniority'])

print(pivot, end='\n\n')

print(crosstab)

# Zadanie 10: Eksport danych

export_cols = ['Name', 'Department', 'Salary', 'Monthly Salary',
'Seniority', 'Age']
df[export_cols].to_csv('final_employees.csv', index=False)

