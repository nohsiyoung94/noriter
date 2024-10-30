from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://finance.naver.com/')
bs = BeautifulSoup(html, 'html.parser')

list = bs.find(string='국제 시장 환율').parent.parent.next_siblings
for s in list:
    print(s)