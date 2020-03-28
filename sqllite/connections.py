
import sqlite3


conn = sqlite3.connect('samples.db')

c = conn.cursor()

# c.execute("""CREATE TABLE samples (
#         artist text,
#         title text
#         )""")

# c.execute("INSERT INTO samples VALUES ('Chantz', 'lofi')")

 

c.execute("SELECT * FROM samples WHERE artist='Gil Scott-Heron'")

# print(c.fetchone())
# #fetchmany
print(c.fetchall())
conn.commit()

conn.close()