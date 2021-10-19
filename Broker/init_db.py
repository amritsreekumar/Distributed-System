import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO climate (TYPE, ISO3, PHEN, SUBSCRIBE, default_msg) VALUES (?, ?, ?, ?, ?)",
            ('subscriber1', 'USA', 'Precipitation', 'Subscribe', 'Nothing available at this time')
            )

#cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#            ('Second Post', 'Content for the second post')
#            )

connection.commit()
connection.close()