from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import sqlite3
import datetime

# initial db creation
conn = sqlite3.connect('samples.db')
c = conn.cursor()
producers = []
db_producers = []

def create_artcles_table():
    c.execute("Drop table if exists Articles");
    c.execute("CREATE TABLE Articles(Article_ID Integer primary key autoincrement, Title text NOT Null, Content varchar(500) Not Null, Link text Not Null, Date text NOT null, Producer_ID INTEGER NOT NULL, FOREIGN KEY (Producer_ID) REFERENCES producers(Producer_ID))");

def inital_db_create():

    c.execute("DROP TABLE IF EXISTS producers");
    c.execute("DROP TABLE IF EXISTS samples");
    c.execute("CREATE TABLE producers(Producer_ID INTEGER PRIMARY KEY AUTOINCREMENT, Slug slug, Name text NOT NULL, Info text)");
    c.execute("CREATE TABLE samples(Song_ID INTEGER PRIMARY KEY AUTOINCREMENT, Producer_ID INTEGER NOT NULL, Artist text NOT NULL, Title text NOT NULL, FOREIGN KEY (Producer_ID) REFERENCES producers(Producer_ID))");

    #I used two lists so the database didn't have characters like "-" and "%".. since samples are linked by Producer_ID, no issues should occur. 
    db_producers = ['Knxwledge', 'Madlib', 'Alchemist', 'Kaytranada', 'J Dilla', 'Kanye West', 'DJ Premier', '9th Wonder', 'Pete Rock', 'Dr. Dre', 'Marley Marl', 'RZA', 'Statik Selektah', 'Evidence', 'MF DOOM', 'Cookin Soul']
    producers = ['Knxwledge.', 'Madlib', 'The-Alchemist', 'Kaytranada', 'J-Dilla', 'Kanye-West', 'DJ-Premier', '9th-Wonder', 'Pete-Rock', 'Dr.-Dre', 'Marley-Marl', 'RZA', 'Statik-Selektah', 'Evidence', 'MF-DOOM', 'Cookin%27-Soul']

    with conn:
        for producer in db_producers:
            c.execute("INSERT INTO producers VALUES(:Producer_ID, :Name, :Info)", {'Producer_ID': None,'Name':producer, 'Info':None});


def find_samples():
    for producer in producers:
        total_pages = 0
        #opens initial web connection, read, close connection
        url = 'https://www.whosampled.com/' + producer + '/'
        uClient = ureq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")

        page_span = page_soup.find_all("span", {"class":"page"})[7]
        page_href = page_span.find('a')
        total_pages = int(page_href.text)

        for i in range(1, total_pages):
            page = str(i)
            url = 'https://www.whosampled.com/' + producer + '/' + '?sp=' + page
            uClient = ureq(url)
            page_html = uClient.read()
            uClient.close()

            page_soup = soup(page_html, "html.parser")
            all_track_connections = page_soup.find_all("div", {"class":"track-connection"})
        
            for connection in range(len(all_track_connections)):
                track_connection = all_track_connections[connection]

                track_connection_list = track_connection('li')

                for track in range(len(track_connection_list)):
                    track_list = track_connection_list[track]
                    track_html = track_list('a')
                    title_html = track_html[0]
                    title = title_html.text
                    try:
                        artist_html = track_html[1]
                        artist = artist_html.text
                    except:
                        artist = "UNKNOWN"
                        continue
                with conn:
                    c.execute("INSERT INTO samples VALUES (:Song_ID, :PID, :Artist, :Title)", {'Song_ID':None, 'PID':producers.index(producer)+1, 'Artist':artist, 'Title':title})

def main():#be sure you're running correct function. Not all functions meant to be run everytime.
    pass
if __name__ == "__main__":
    main()