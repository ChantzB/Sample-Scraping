import sqlite3

# create connection to database
conn = sqlite3.connect('samples.db')
c = conn.cursor()

class sample:
    
    def __init__(self, artist, title):
        self.first = artist
        self.last = title

    def get_artist(self):
        return '{}'.format(self.artist)

    