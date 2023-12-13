import pandas as pd

df = pd.read_csv('Customers.csv', sep=';')


if df.isna().sum().sum() != 0:
    df.dropna(inplace=True)


dfg = df.groupby('Profession')['Income'].mean()
print(dfg)
