import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO climate (ISO3, PERIOD, TYPE, PHEN) VALUES (?, ?, ?, ?)",
            ('India','1920-1939', 'annual avg', 'precipitation')
            )

#cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#            ('Second Post', 'Content for the second post')
#            )

connection.commit()
connection.close()