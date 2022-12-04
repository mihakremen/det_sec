import pandas as pd

df = pd.read_csv('https://www.dropbox.com/s/9nmxal5tjxv4qo6/dataset_CSD_full.csv?dl=1')
df = df.loc[:, 'Lang'].values
print(df)