import requests 
import random 
from bs4 import BeautifulSoup
import time


def crawl_page(url):
    headers = { 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Whale/3.28.266.14 Safari/537.36"
        ,"Referer": "https://example.com"
        ,'accept-language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
        ,'sec-ch-ua-platform':'Windows'
        ,'sec-ch-ua':'"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="128"'
    }

    # 쿠키 정의
    cookies = {
        "_ttp": "2gPuFvcOoExjpaJjyPeLA26e1VD"
        ,'ak_bmsc':'178BE1DDB28B9CCEFC85C6595120B29C~000000000000000000000000000000~YAAQDjVDF7t07duSAQAAD7ag9hlurMb0HU+p2OsIYR0yJZHdasIZ7bTug7icQMotK7v04QqfT+IMZx4fyq0D4sBAjk+Pgm1hAnmQWOtYUFr5JXgEWB1iFGrYIEeon8fZ/U6ZStO5l9ONfYYvpL2IgeT3mUzMdMwk1vd8YbsAjoCEb2KItqyyHG1PgK4fsXoPJH0BOfLXp+D5VgJObDhBgnPmpg3OhpyQ0WuWxEoh21BmxVS7eYuTDR1b+17ggO9URBxdARuvdZ2w4Y3HuM7I0bsyP1d5Fr6rPL6hPwIBNGRo9eaVsFHcIo6WtyN6rUVVGZkgZWg4XGdMexv77sFc/iOL/t+qV4j0CAOGyAdDPBQh9NtLMN+d+iP/SBu08JHyQ4GFxpL44D/oKuU='
        ,'cmpl_token':'AgQQAPOuF-RO0rNFT0EC9t07_UPCgZvdv4olYNuHVw'
        ,'sessionid':'d8a0b3eece9862b75a6bca80c8ae15a2'
        ,'uid_tt':'e1c4808f3bd37e030849f6571fe65f236253ecb67926851650bcb1276545daa9'
        ,'uid_tt_ss':'e1c4808f3bd37e030849f6571fe65f236253ecb67926851650bcb1276545daa9'
        ,'ttwid':'1%7CyX1t69EMw9_HC9dPdDqtTOvlUnozY9FSopdBZX18fBc%7C1730717131%7C8a1e85cd788016f540b735c22b82667365ba49022930556313ee67581253b405'
        ,'last_login_method':'QRcode'
        ,'tt_csrf_token':'Rohc4QGd-tvyhh3DxDJoKi6Jb9X8LWUzrW-c'
        ,'tt_chain_token':'9FOJlm9pQn4qDtIq3SOjpQ=='
        ,'msToken':'XQ7A8qlhmKXCp2K9GN36DQdL8NR4hqFRdvPoHSubzvwzcGkrGNvLG0aAxqvrr9M8K0rJYrGC1yOeOmdCVj_KfWqT5U-h2N_QqPJritlaDAbTZ9PwHDUWQj8V0RZDQc3me8_iSj2ZLuYQGioMmNFtnpI='
        ,'odin_tt':'214476c53b3409e169e4f974be9e1669c16af354f10be545c4e1b15709d9ccf31e4196e2efc3c9765a161c8a773de0f076639e692f10b507a5c0fb289db26458'
        ,'passport_csrf_token':'cfc18de5b2dfd28cf7f9f25ec9575ea5'
        ,'perf_feed_cache':'{%22expireTimestamp%22:1730887200000%2C%22itemIds%22:[%227433050635857235218%22%2C%227431765996794350881%22%2C%227427188432348253461%22]}'
    }
    # 5초 대기
    rd = random.uniform(5.0,7.0)
    print(rd, "waiting~")
    
    # 페이지 요청
    response = requests.get(url, headers=headers, cookies=cookies)
    
    time.sleep(rd)
    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # BeautifulSoup으로 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 원하는 데이터 추출
        title = soup.title.string if soup.title else 'Title not found'
        
        return title  # 또는 다른 데이터 반환
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# URL 입력
url = 'https://www.tiktok.com/@ohayomynightt'
data = crawl_page(url)
print(data)