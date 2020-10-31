import requests

def apiPOST():

    url = 'http://localhost:3000/'
    x = requests.post(url)
    print(x.text)