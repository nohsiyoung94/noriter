from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://finance.naver.com/')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('div', {'class':'section_strategy'}).descendants:
    print(child)
    
"""
#siblings
for sb in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sb)
#parent
print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
"""