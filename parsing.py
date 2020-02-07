from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

url = 'https://www.whosampled.com/Knxwledge./'

#opens web connection, read, close connection
uClient = ureq(url)
page_html = uClient.read()
uClient.close

page_soup = soup(page_html, "html.parser")

all_track_connections = page_soup.find_all("div", {"class":"track-connection"})

#for loop
track_connection = all_track_connections[1]

track_connection_list = track_connection('li')

for track in range(len(track_connection_list)):
    track_list = track_connection_list[track]
    track_html = track_list('a')
    title_html = track_html[0]
    artist_html = track_html[1]
    title = title_html.text
    artist = artist_html.text

print(title, artist)