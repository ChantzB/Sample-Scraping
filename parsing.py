from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

url = 'https://www.whosampled.com/Knxwledge./'

titles = []
artists = []

#opens web connection, read, close connection
uClient = ureq(url)
page_html = uClient.read()
uClient.close

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
        titles.append(title)
        try:
            artist_html = track_html[1]
            artist = artist_html.text
            artists.append(artist)
        except:
            artists.append("Unknown")

print(titles)
print(artists)