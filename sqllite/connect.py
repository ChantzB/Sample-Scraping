import sqlite3


conn = sqlite3.connect('samples.db')

c = conn.cursor()

 

c.execute("SELECT * FROM samples WHERE artist='2 Chainz'")

# print(c.fetchone())
# #fetchmany
print(c.fetchall())

conn.commit()

conn.close()


