import sqlite3

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2056-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()