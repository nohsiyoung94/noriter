from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://finance.naver.com/')
bs = BeautifulSoup(html, 'html.parser')

title = bs.findAll(text = '삼성전자')
print(len(title))

textCls = bs.findAll(class = 'txt')
