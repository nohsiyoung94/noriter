import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TikTokDownloader:
    def __init__(self, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'):
        self.user_agent = user_agent
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def setup_options(self):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-infobars")
        options.add_argument("--window-position=0,0")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-certificate-errors-spki-list")
        options.add_argument(f"user-agent={self.user_agent}")
        return options


    def get_video_links(self, user_id):
        url = f'https://www.tiktok.com/@{user_id}'
        links = []
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#main-content-others_homepage [class*="DivShareLayoutMain"] a'))
            )
            video_elements = self.driver.find_elements(By.CSS_SELECTOR, '#main-content-others_homepage [class*="DivShareLayoutMain"] a')
            links = [element.get_attribute('href') for element in video_elements]
        except Exception as e:
            print(f"An error occurred while getting video links: {e}")
        
        return links

    def download_video(self, video_url):
        try:
            self.driver.get(video_url)
            self.add_cookies(self.driver)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'video source'))
            )
            video_source = self.driver.find_element(By.CSS_SELECTOR, 'video source').get_attribute('src')
            self.real_download(video_source)
        except Exception as e:
            print(f"An error occurred while downloading video: {e}")
    def endBrowser(self):
        self.driver.quit()

    def add_cookies(self, driver):
        cookies = [
            {'name': 's_v_web_id', 'value': 'verify_m31k762e_Fct6kkgA_qLaH_4Cuc_AHF6_HQ3NidkaoDYD'},
            {'name': 'tt_chain_token', 'value': '9FOJlm9pQn4qDtIq3SOjpQ'},
            {'name': 'tt_csrf_token', 'value': 'NdbxJy6ZEk82Nk_2YCc5qeNdQQM'},
            {'name': 'uid_tt_ss', 'value': 'e1c4808f3bd37e030849f6571fe65f236253ecb67926851650bcb1276545daa9'}
        ]
        for cookie in cookies:
            driver.add_cookie(cookie)

    def real_download(self, src):
        headers = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Whale/3.28.266.14 Safari/537.36"
            ,"Referer": "https://example.com"
            ,'accept-language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
            ,'sec-ch-ua-platform':'Windows'
            ,'sec-ch-ua':'"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="128"'
        }
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
        download_response = requests.get(src, headers=headers,cookies=cookies)
        if download_response.status_code == 200:
            video_filename = src.split('/')[-1] + '.mp4'
            with open(video_filename, 'wb') as file:
                file.write(download_response.content)
            print(f'Downloaded video from {src} and saved as {video_filename}')
        else:
            print(f'Failed to download video from {src}, status code: {download_response.status_code}')

def main():
    #user_id = input('Enter TikTok user ID: ')
    user_id ='bb._0808'
    downloader = TikTokDownloader()
    video_links = downloader.get_video_links(user_id)
    for video_url in video_links:
        downloader.download_video(video_url)
    downloader.endBrowser()

if __name__ == '__main__':
    main()
