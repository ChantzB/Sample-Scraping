from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import re
import sqlite3

conn = sqlite3.connect('samples.db')
c = conn.cursor()

def highlights_db():
    c.execute("Drop table if exists Highlights")
    c.execute("CREATE TABLE Highlights(id Integer primary key autoincrement, Content varchar(100), Img BLOB)")

def top_samples():
    url = 'https://www.whosampled.com/'
    uClient = ureq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    top_samples = page_soup.find_all('div', class_="sample-cell-meta")
    images = page_soup.find_all('div', class_="sample-cell")
    for sample in range(len(top_samples)):
        image = images[sample]('img')
        file = image[0].get('src')

        full = top_samples[sample].text
        text = re.search('\n(.*)\n', full)
        Content = text.group(1)
        with conn:
            c.execute("INSERT INTO Highlights VALUES(:id, :Content, :Img)", {'id': None, 'Content': Content, 'Img': file})

def main():#be sure you're running correct function. Not all functions meant to be run everytime.
    highlights_db()
    top_samples()
if __name__ == "__main__":
    main()