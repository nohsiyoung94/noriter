from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
"""
for child in bs.find('table').children:
    print(child)
"""
#siblings
for sb in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sb)
#parent
print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
