from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

titles = []
artists = []

#opens initial web connection, read, close connection
url = 'https://www.whosampled.com/Knxwledge./'
uClient = ureq(url)
page_html = uClient.read()
uClient.close

page_soup = soup(page_html, "html.parser")

def find_page_length():
    #div id content
    page_wrapper = page_soup.find_all("div", {"class":"pagination-wrapper"})
    


def find_samples():
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

def main():
    pass

if __name__ == "__main__":
    main()