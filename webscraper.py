import re
import requests
from bs4 import BeautifulSoup

TEST_URL = 'https://en.wikipedia.org/wiki/Napoleonic_Wars'

## main function that gets called from mail file
def main():
    print('main function')
    soup = getSoup(TEST_URL)
    heading = soup.find(id='firstHeading')
    print(heading)
    return heading


def getAlternativeURL():
    return 'https://en.wikipedia.org/wiki/Python_(programming_language)'

def getSoup(url):
    response = requests.get(url)

    #if bad response, perform request on alternative URL
    if response.status_code != 200:
        url = getAlternativeURL()
        response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    return soup

main()

