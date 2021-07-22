import sqlite3

# define connection and cursor

# connection is used to connect to a database db
# referencing a database that doesnt exist = new one will be created
connection = sqlite3.connect('001_store_transaction.db')

# creating a cursor to interact with the db through sql commands
# allows to create and modify tables within the db
cursor = connection.cursor()

# create stores table

# use sqp statement to create a table called stores
# in it rows with entries store_id and location
# we specify the type of fields: store_id = integer, location = text string
# primary key sets up store_id key to be unique for each row in the table
# allows other tables to reference or relay to it using store_id as a foreign key attribute
command1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

# here foreign key references the primary key in another table
command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT,
FOREIGN KEY(store_id) REFERENCES stores(store_id))"""

cursor.execute(command2)

# add to stores

# add records to the table stores
# insert rows into the table
cursor.execute("INSERT INTO stores VALUES (21, 'Mineapolis, MN')")
cursor.execute("INSERT INTO stores VALUES (95, 'Chicago, IL')")
cursor.execute("INSERT INTO stores VALUES (64, 'Iowa City, IA')")

# add to purchases

cursor.execute("INSERT INTO purchases VALUES (54, 21, 15.49)")
cursor.execute("INSERT INTO purchases VALUES (23, 64, 21.12)")

# get results

# see the data contained in the table with select statement, here it is select all
cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)

# upadte

cursor.execute("UPDATE purchases SET total_cost = 3.67 WHERE purchase_id = 54")

# delete

cursor.execute("DELETE FROM purchases WHERE purchase_id = 54")

# python printout

cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)
