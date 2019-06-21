from bs4 import BeautifulSoup
import requests


def scrape(url):
    try:
        # Returns a response object
        resp = requests.get(url)
        # Response obj -> String
        src = resp.text
        # Making a BeautifulSoup Object
        soup = BeautifulSoup(src, 'lxml')
        # Finds the first <article> tag in the soup
        article = soup.find('article')
        # Returns the headline:
        headline = article.h2.a.text
        print(headline, "\n")
        # Returns string: the summary within <p> tag of the article
        summary = article.find("div", class_='entry-content').p.text
        print(summary, "\n")
        # Gets the <iframe> info
        vid_src = article.find("iframe", class_="youtube-player")[src]
        print(vid_src, "\n")

        vid_id = vid_src.split('/')
        print(vid_id)
    except Exception:
        print("Unexpected Error! Damn man!")


scrape("http://coreyms.com/")
