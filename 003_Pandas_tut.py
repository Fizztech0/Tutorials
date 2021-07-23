# Dataframe is the Object type that Pandas allows to manipulate
import sys
sys.path.append("/Users/SafetyFirst/Library/Python/3.9/lib/python/site-packages")

# import as = dont have to type pandas everytime, but just pd
import pandas as pd
import numpy as np

# together with importing numpy these four lines of code allow for a wider pycharm terminal output when displaying
# dataframe content
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',13)


df = pd.read_csv('003_pokemon_data.csv')
#print(df.head(5))


# Reading Data in Pandas
## Read Headers
#print(df.columns)

## Read each Column
#print(df['Name'][0:5])
#print(df.Name)
#print(df[['Name', 'HP']][0:5])

## Read each row
#print(df.iloc[1])
#for index, row in df.iterrows():
#    print(index, row)
#for index, row in df.iterrows():
#    print(index, row['Name'])
#print(df.loc[df['Type 1'] == "Fire"])

## Read a specific location (R, C)
#print(df.iloc[2, 1])


# Sorting/Describing Data
#print(df.describe())
## ascending sorting by name
#print(df.sort_values('Name'))
##descending sorting
#print(df.sort_values('Name', ascending=False))
## sorting through multiple columns, ascending [1 = True, 0 = False] so first column will be sorted ascending
## and the second descending
#print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))

##Making Chancges to the data

##Adding a column
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#print(df[0:13])
## when adding totals, doublecheck if numbers match!
## , means all columns
#df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#print(df)
## be careful with hardcoding numbers as tables change and that can screw everything up
## -> use variables (i.e. Pythons refractor instead of rename option)
## dropping columns
#print(df.drop(columns=['Legendary', 'Generation']))
## reordering data
## 1 just calling the columns you want
#df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#print(df[['Name', 'Total', 'HP']])
## 2
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:10]]
print(df.head(5))

