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