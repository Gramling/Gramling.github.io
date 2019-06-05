#Importing previously installed packages needed for webscraping
import nltk
from bs4 import BeautifulSoup
from urllib import request

#store the url we're using
url = "https://github.com/humanitiesprogramming/scraping-corpus"

#using that url, get the HTML from it
html = request.urlopen(url).read()

#took the URL and turned into a soup object
soup = BeautifulSoup(html, 'lxml')
our_text = soup.text
links = soup.find_all("a")[0:10]

#print(our_text[0:2000])
#replaced line breaks with spaces to condense text
#print(soup.text.replace("\n", " "))

links_html = soup.select("td.content a")
this_link = links_html[0]

print(this_link["href"])
