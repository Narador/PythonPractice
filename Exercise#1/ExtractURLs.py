# Write your code below
# You will need to pip-install the modules(libraries) you'll need (See Useful Libraries in the readme.md)

import requests
from bs4 import BeautifulSoup

def my_spider(max_pages):
    page = 1
    while page <= max_pages:
        site = 'https://www.xkcd.com' + str(page)
        web_code = requests.get(site)
        plain_text = web_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'http'}):
            href = link.get('href')
            print(href)
        page += 1


my_spider(1)
            
