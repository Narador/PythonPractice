from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# opening the page
page = urlopen('http://www.xkcd.com/')

# parsing the page using html.parser (you can choose between 4 in bs4)
soup = BeautifulSoup(page, 'html.parser')

# loop to find all in the document and apply regular expressions to get
# only the http links
for link in soup.findAll('a', attrs={'href': re.compile('^http://')}):
    print(link.get('href'))

print('SUCCESS!')
