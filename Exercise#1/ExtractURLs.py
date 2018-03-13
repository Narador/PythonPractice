# Write your code below
# You will need to pip-install the modules(libraries) you'll need (See Useful Libraries in the readme.md)

<<<<<<< HEAD
from html.parser import HTMLParser
from urllib import parse

class HtmlFinder(HTMLParser)
    
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href:'
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
    
    def page_links(self):
        return self.links

    def error(self, message):
        pass
    
=======
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
            
>>>>>>> 7a2db28d8a299d77e279040a0dde4b13bfee3ea3
