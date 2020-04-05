from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import sqlite3


total_pages = 0
def find_page_length():
    global total_pages
    #opens initial web connection, read, close connection
    url = 'https://www.whosampled.com/Knxwledge./'
    uClient = ureq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    page_span = page_soup.find_all("span", {"class":"page"})[7]
    page_href = page_span.find('a')
    total_pages = int(page_href.text)

def find_samples():
    conn = sqlite3.connect('samples.db')
    c = conn.cursor()

    for i in range(1, total_pages):
        page = str(i)
        url = 'https://www.whosampled.com/Knxwledge./' + '?sp=' + page
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
                c.execute("INSERT INTO samples VALUES (:artist, :title)", {'title':title, 'artist':artist})
    conn.close()

def main():
    # find_page_length()
    # find_artists()
    pass
if __name__ == "__main__":
    main()