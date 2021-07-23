# Pandas Commands
## setup
Together with importing numpy these four lines of code allow for a wider pycharm terminal output when displaying
dataframe content
	
	import pandas as pd
	import numpy as np

	desired_width=320
	pd.set_option('display.width', desired_width)
	np.set_printoptions(linewidth=desired_width)
	pd.set_option('display.max_columns',12)

`pd` is abbreviated for pandas

`df` is abbreviated for dataframe

The dataset used here will be the following Pokemon list:

| Index | Name      | Type 1      | Type 2 |   HP	| Attack | Defense | Sp. Atk | Sp. Def | Speed   | Generation | Legendary |
| :---: | :------:  | :---------: |  -----:|:-----: | :----: | :-----: | :-----: | :-----: | :-----: | :------- : | :-------: |
| 1     | Bulbasaur | Grass       | Poison |  45	| 49	 | 49	   | 65	     | 65	   |  45     |  1         | False     |
| 2     | Ivysaur   | Grass       | Poison |  60	| 62	 | 63	   | 80	     | 80	   |  60     |  1         | False     |
| 3     | etc.   | ...       | ... |  ...	| 	 | 	   | 	     | 	   |       |           |      |


## Opening Files
`pd.read_csv('file.csv')` open csv file

`pd.read_excel('file.xlsx')`open excel file

`pd.read_csv('file.txt', delimiter = '\t')` standard delimiter is "," here <kbd>TAB</kbd> is specified

## Reading files
`pandasfile.head(INT)` refers to starting INT number of rows

`pandasfile.tail(INT)` refers to the final INT * rows

## Read Headers
`df.columns` refers to the name of all column names

## Read each Column
`df['column_name'][0:5]` refers to the specified column for rows 0 - 5

`df[['Name', 'HP']][0:5]` adding multiple columns in list format

## Read each row
`df.iloc[1]` refers to the INTEGER location 1 = 2nd row

	for index, row in df.iterrows():
		print(index, row)

iterates through every row and prints it

>so far I cant tell the difference between this and:
>
>    for index in df.iterrows():
>        print(index)

iterating through every element in the "Name" column and print it

	for index, row in df.iterrows():
		print(index, row['Name'])

print all "Fire" types in the "Type 1" column

`print(df.loc[df['Type 1'] == "Fire"])`

> Why does it iterate and print through all elements despite it not being a loop?

## Read a specific location (R, C)


`df['Total'] = df.iloc[:, 4:10].sum(axis=1)`

`,` means all columns

`sum(axis=1)` adds everything horizontally
`iloc[:, 4:10]` the end parameter will not be included, i.e. 10th column

## Filtering data
filtering by one spec

	print(df.loc[df['Type 1'] == 'Grass'])

 filtering by more specs

	new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
	print(new_df)
in pandas we use `&` instead of `and`

`or` is `|`

the above will keep the old index, to add a new one:

	new_df = new_df.reset_index()

to drop the old index and just have the new one:

	new_df = new_df.reset_index(drop=True)

to change it in place:

	new_df.reset_index(drop=True, inplace=True)

>This might supposedly may save memory?

filtering only the Pokemon containing "Mega":

	df.loc[df["Name"].str.contains('Mega')]

reverse selecting with `~`

	df.loc[~df["Name"].str.contains('Mega')]

## Conditional Changes
changing the string "Fire" in the "Type 1" column to "Flamer"

	df.loc[df["Type 1"] == "Fire", "Type 1"] = "Flamer"

use one condition to set the parameter of another column: All Fire types will be set to legendary

	df.loc[df["Type 1"] == "Fire", "Legendary"] = True

use one condition to set multiple others:

	df.loc[df["Type 1"] == "Fire", ["Legendary", "Generation"]] = "TEST VALUE"

change both parameters:

	df.loc[df["Type 1"] == "Fire", ["Legendary", "Generation"]] = ["TEST 1", "TEST2"]

## Aggregate Statistics (Groupby)
showing the mean values (Durchschnitt):

	df.groupby(["Type 1"]).mean()

plus additional sorting:

	df.groupby(["Type 1"]).mean().sort_values("Sp . Atk", ascending=False)

Summing up all values:

	df.groupby(["Type 1"]).sum()

Counting all the entries:

	df.groupby(["Type 1"]).count()

Better count overview by introducing a count column and then filtering with it (as only Type counts are relevant here,
not counting how many HP columns etc. are filled)

	df["count"] = 1
	df.groupby(["Type 1"]).count()["count"]

Counting by multiple parameters, i.e. looking at all the subsets

    df.groupby(["Type 1", "Type 2"]).count()["count"]


