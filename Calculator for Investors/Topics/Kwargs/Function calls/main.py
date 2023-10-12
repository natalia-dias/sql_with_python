import pandas as pd
source = '/Users/ndias/Downloads/hyperskill-dataset-87937638.txt'
data = pd.read_csv(source)
print(data.head())
# data.
print('____')
print(data.set_index('Name').head(10))