import pandas as pd
n = int(input('Enter Number of rows to be selected: '))
df = pd.read_csv('Sample.csv').iloc[:,:n]
print(df)
dict = df.to_dict('list')
print(dict)