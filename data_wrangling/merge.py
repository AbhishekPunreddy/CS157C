import pandas as pd

# Read the files into two dataframes.
df1 = pd.read_csv('credits.csv')
df2 = pd.read_csv('movies_metadata.csv')

# Merge the two dataframes, using _ID column as key
df3 = pd.merge(df1, df2, on = 'id')
df3.set_index('id', inplace = True)

# Write it to a new CSV file
df3.to_csv('CSV3.csv')