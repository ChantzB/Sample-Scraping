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


Date = datetime.date.today().strftime("%B %d, %Y")
#In order to scrape within one function, and provide the code. I will comment out each articel as I go. 
def add_article():

    #knxwledge article
    # Title = "Knxwledge 1988"
    # Name = "Kxnwledge"
    # url = 'https://pitchfork.com/reviews/albums/knxwledge-1988/'
    # uClient = ureq(url)
    # page_html = uClient.read()
    # uClient.close()
    # page_soup = soup(page_html, "html.parser")
    # paragraphs = page_soup.find_all('p')
    # Content = paragraphs[0].text

    #madlib
    # url = 'https://www.complex.com/music/madlib-interview-best-hip-hop-producer-2019'
    # uClient = ureq(url)
    # page_html = uClient.read()
    # uClient.close()
    # page_soup = soup(page_html, "html.parser")
    # Title = page_soup.find_all('h1', class_="story-title story-title__featured")[0].text
    # Content = page_soup.find_all('h4', class_="sub-title")[0].text
    # Name = 'Madlib'
    # paragraphs = page_soup.find_all('p')

    #beat battles
    url = 'https://www.vulture.com/2020/04/verzuz-instagram-live-battles-ranked.html'
    uClient = ureq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    Title = page_soup.find_all('h1', class_="headline-primary")[0].text
    Content = page_soup.find_all('p', class_="clay-paragraph")[0].text
    Name = 'RZA'

    with conn:
        c.execute("INSERT INTO Articles VALUES (:Article_ID, :Title, :Content, :Link, :Date, :Producer_id)", {'Article_ID':None, 'Title': Title, 'Content':Content, 'Link':url, 'Date': Date,'Producer_id':Name})
        
def main():#be sure you're running correct function. Not all functions meant to be run everytime.
    # create_artcles_table()
    add_article()
    pass
if __name__ == "__main__":
    main()