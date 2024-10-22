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

url_body = getBody("https://pythonscraping.com/pages/page3.html")
print(url_body.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())