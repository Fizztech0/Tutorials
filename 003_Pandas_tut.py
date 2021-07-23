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
pd.set_option('display.max_rows', None)


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
#df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#cols = list(df.columns)
#df = df[cols[0:4] + [cols[-1]] + cols[4:10]]
#print(df.head(5))

## saving to csv
## saving the modified file with the added total of all pokemon values and new sorting
##index=False, otherwise it would insert a indexing column at the front, which the df already has
## to csv, excel and TAB separated .txt
#df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#cols = list(df.columns)
#df = df[cols[0:4] + [cols[-1]] + cols[4:10]]
#df.to_csv('pokemon_data_modified.csv', index=False)
#df.to_excel('pokemon_data_modified.xlsx', index=False)
#df.to_csv('pokemon_data_modified.txt', index=False, sep='\t')

## Filtering data
## filtering by one spec
#print(df.loc[df['Type 1'] == 'Grass'])
## filtering by two specs
## in pandas we use "&" instead of the "and" we'd normally use
## equally "or" is
#new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
#print(new_df)
## this will keep the old index, to get rid of it:
#new_df = new_df.reset_index(drop=True)

#select Mega
#new_df.reset_index(drop=True, inplace=True)

#inverse select for non-Mega
#new_df = df.loc[~df["Name"].str.contains('Mega')]

# REGEX segment ommitted
#filtering for either or
#print(df.loc[(df["Type 1"] == "Grass") | (df["Type 1"] == "Fire")])

## Conditional Changes

##changing strings
#df.loc[df["Type 1"] == "Fire", "Type 1"] = "Flamer"

## one condition to set the parameter of another column
#df.loc[df["Type 1"] == "Fire", ["Legendary", "Generation"]] = ["TEST 1", "TEST2"]

## Aggregate Statistics (Groupby)
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

#print(df.groupby(["Type 1"]).mean().sort_values("HP", ascending=False))

#print(df.groupby(["Type 1"]).sum())

#print(df.groupby(["Type 1"]).count())

df["count"] = 1
print(df.groupby(["Type 1", "Type 2"]).count()["count"])



#print(df)


