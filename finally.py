from bs4 import BeautifulSoup
import urllib.request

#fetching url
bryan = urllib.request.urlopen("https://www.xkcd.com/")
troy = BeautifulSoup(bryan, from_encoding=bryan.info().get_param('charset'))

#'a' href are headers to where all the links are
for link in troy.find_all('a', href=True):
    print(link['href'])
