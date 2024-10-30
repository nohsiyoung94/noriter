from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://finance.naver.com/')
bs = BeautifulSoup(html, 'html.parser')

for sb in bs.find('tbody', {'id':'_topItems1'}).tr.next_siblings:
    print(sb)