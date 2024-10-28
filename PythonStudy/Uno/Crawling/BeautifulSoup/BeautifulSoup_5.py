from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

imgs = bs.findAll('img',{'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for img in imgs:
    print(img['src'])

#lambda
print(bs.findAll(lambda tag: len(tag.attrs)==2))

print(bs.findAll(lambda tag:tag.get_text() =='Or maybe he\'s only resting?'))

