from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

url = 'https://www.whosampled.com/Knxwledge./'

#opens web connection, read, close connection
uClient = ureq(url)
page_html = uClient.read()
uClient.close

page_soup = soup(page_html, "html.parser")

all_track_connections = page_soup.find_all("div", {"class":"track-connection"})

#for loop?
track_connection = all_track_connections[1]

artist_list = track_connection('a')

print(artist_list)