from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
from bs4 import BeautifulSoup
def getBody(url):
    try:
        html = urlopen(url)
    except  HTTPError   as  e:
        print(e)
    except  URLError   as  e:
        print(e)
    else:
        bs = BeautifulSoup(html, 'html.parser')
        try:
            body = bs.body
        except AttributeError as e:
            return None
        return body

url_body = getBody("https://finance.naver.com/")
if url_body == None:
    print('바디태그가 없습니다.')
else:
    print(url_body)