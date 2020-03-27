from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

#name to output file
out_file = "samples.csv"

#headers
headers = "Titles, Artist\n"

#opens file, writes headers
f = open(out_file, "a", encoding='utf-8')
f.write(headers)

global titles
global artists
global years

titles = []
artists = []
years = []

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

def find_titles():
    for i in range(1, total_pages):
        page = str(i)
        #opens initial web connection, read, close connection
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
                titles.append(title)
        print(title[1])
def find_artists():
    for i in range(1, total_pages):
        page = str(i)
        #opens initial web connection, read, close connection
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
                try:
                    artist_html = track_html[1]
                    artist = artist_html.text
                    artists.append(artist)
                except:
                    artists.append("Unknown")
                    continue
            print(artist[1])
            
#def write_to_lists():
#    for title, artist in map(titles, artists):
#        f.write(titles[title] + "," + artists[artist] + "," + "\n")

def main():
    find_page_length()
    find_titles()
    find_artists()


if __name__ == "__main__":
    main()