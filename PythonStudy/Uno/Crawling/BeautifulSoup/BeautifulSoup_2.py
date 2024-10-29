from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://finance.naver.com/')
bs = BeautifulSoup(html, 'html.parser')
nameList = bs.findAll('img', limit=5)
for name in nameList:
    print(name)