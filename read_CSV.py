import pandas as pd
n = int(input('Enter Number of rows to be selected: '))
d = pd.read_csv('Sample.csv').iloc[:,:n]
print(d)
dict = d.to_dict('list')
print(dict)
