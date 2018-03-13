from bs4 import BeautifulSoup
import urllib.request

#fetching url
bryan = urllib.request.urlopen("https://www.xkcd.com/")

# BRYAN: for this, it looks like you are trying to convert the document to
# unicode for characters. With beautiful soup, it automatically converts
# incoming documents to unicode so you don't have to worry about it unless
# the document doesnt specify an encoding type and bs can't autodetect one
troy = BeautifulSoup(bryan, from_encoding=bryan.info().get_param('charset'))

#'a' href are headers to where all the links are

# Bryan: with this for loop, it looks like you are correctly printing any links
# but for ANY href tags, and that is why you get all of the junk I was talking
# about. This is most easily done using regular expressions.
# Look at my for loop in the example and you will see I specify the atribute
# and compile the regular expression for "starts with(^)http://"

for link in troy.find_all('a', href=True):
    print(link['href'])
