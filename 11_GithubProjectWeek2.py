import os
import sqlite3
 
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
 
# Create a table again for holding a path and bytes, just like before
table = 'CREATE TABLE my_files (id integer primary key, full_path TEXT, bytes INTEGER)'
cursor = connection.cursor()
cursor.execute(table)
connection.commit()

my_files = {}
i = 0
for root, directories, files in os.walk('.'):
    for _file in files:
        #print(f"File found: {_file}")
        full_path = os.path.join(root, _file)
        bytes = os.path.getsize(full_path)
        my_files[full_path] = bytes

print(my_files)
print(type(my_files))
print(my_files['.\\01_ExploringDataStructuresInPython.py'])

t = list(my_files.items()) # Conversion of dictionary into a list of tuples

for elem in t:
    query = 'INSERT INTO my_files(full_path, bytes) VALUES(?, ?)'
    cursor.execute(query, elem)
    connection.commit()

print("\n1st Query:")
query = 'SELECT full_path, bytes FROM my_files WHERE bytes>3000 LIMIT(10)'
for i in cursor.execute(query):
    print(i)

print("\n2nd Query:")
query = 'SELECT full_path, bytes FROM my_files LIMIT(20)'
for i in cursor.execute(query):
    print(i)
    
print("\n3rd Query:")
query = 'SELECT full_path, bytes FROM my_files WHERE full_path LIKE "%json%"'
for i in cursor.execute(query):
    print(i)

 
