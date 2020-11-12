import requests

def apiPOST(url):
    if url is None:
        url = 'http://localhost:3000/'
    x = requests.post(url)
    #print(x.text)
    return x.text

def apiGET(url):
    if url is None:
        url = 'http://localhost:3000/'
    x = requests.get(url)
    #print(x.text)
    extractedURL = apiExtractor(x)
    return x.text

def apiExtractor(data):
    urlTest = data['results'][0]['url']['genre']
    return urlTest