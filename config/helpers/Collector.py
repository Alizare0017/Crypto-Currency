import requests
from bs4 import BeautifulSoup


def currency():
    url = 'https://www.tgju.org/currency'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(attrs={'class':'pointer'})

    #for tag in result:

    print(result.text.split('\n'))

currency()