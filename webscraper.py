import re
import requests
import random
from bs4 import BeautifulSoup
from configparser import SafeConfigParser

TEST_URL = 'https://en.wikipedia.org/wiki/Area_51'

URL_LIST = ["https://en.wikipedia.org/wiki/Napoleonic_Wars", "https://en.wikipedia.org/wiki/Mediterranean_Sea", "https://en.wikipedia.org/wiki/Python_(programming_language)" ,
    "https://en.wikipedia.org/wiki/Area_51", "https://en.wikipedia.org/wiki/Belgium", "https://en.wikipedia.org/wiki/Video_game_development"]

## main function that gets called from mail file
def main(optionalURL=None):
    url = getURL()
    soup = getSoup(url)
    heading = soup.select("#firstHeading")[0].text
    lastMod = soup.select("#footer-info-lastmod")[0].text
    #heading = soup.title.string
    #paragraphs = soup.select("p")
    #for para in paragraphs:
    #    paragraphText = para
    #    print(paragraphText)
    paragraphText = soup.find("p").findNext("p").get_text()
    return heading.encode('ascii',errors='ignore').decode('ascii'), paragraphText.encode('ascii',errors='ignore').decode('ascii'), url, lastMod

def getURL():
    # make this user customisable somehow
    url = random.choice(URL_LIST) # get random url
    #print(URL_LIST)
    URL_LIST.remove(url) # remove url from list to prevent duplicates
    return url

def getAlternativeURL():
    return 'https://en.wikipedia.org/wiki/Python_(programming_language)'

def getSoup(url):
    response = requests.get(url)

    #if bad response, perform request on alternative URL
    if response.status_code != 200:
        print('Bad Response')
        url = getAlternativeURL()
        response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    return soup

main()

