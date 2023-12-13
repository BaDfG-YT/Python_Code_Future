import pandas as pd

df = pd.read_csv('Customers.csv', sep=';')

# возраст больше 30 и доход меньше 30000
df1 = df[(df['Age'] > 30) & (df['Income'] < 30000)]
print(df1)

# по профессии юристы и с опытом работы больше 5 лет
df2 = df[(df['Profession'] == 'Lawyer') & (df['Work Experience'] > 5)]
print(df2)
