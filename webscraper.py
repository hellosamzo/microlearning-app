import re
import requests
import random
from bs4 import BeautifulSoup

TEST_URL = 'https://en.wikipedia.org/wiki/Area_51'

## main function that gets called from mail file
def main():
    #print('main function')
    url = getURL()
    soup = getSoup(url)
    #print('URL: ' + url)
    heading = soup.select("#firstHeading")[0].text
    #heading = soup.title.string
    #paragraphs = soup.select("p")
    #for para in paragraphs:
    #    paragraphText = para
    #    print(paragraphText)
    paragraphText = soup.find("p").findNext("p").get_text()
    print('Heading: ' + heading)
    return heading.encode('ascii',errors='ignore').decode('ascii'), paragraphText.encode('ascii',errors='ignore').decode('ascii'), url
    #.encode('ascii', 'ignore')


def getURL():
    # make this user customisable somehow
    urlList= ["https://en.wikipedia.org/wiki/Napoleonic_Wars", "https://en.wikipedia.org/wiki/Mediterranean_Sea", "https://en.wikipedia.org/wiki/Python_(programming_language)"]
    return random.choice(urlList) # returns random URL 

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

