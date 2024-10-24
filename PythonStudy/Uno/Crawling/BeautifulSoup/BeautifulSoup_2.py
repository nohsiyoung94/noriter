from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://finance.naver.com/')
bs = BeautifulSoup(html, 'html.parser')

nameList = bs.findAll('span',{'class':'txt'})
print(nameList)
for name in nameList:
    print(name.get_text())