# pip install selenium
# https://chromedriver.chromium.org/ 

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless') # 백그라운드로 실행

driver = webdriver.Chrome(options=options) # 크롬 드라이버 실행

url = "http://www.naver.com/"
driver.get(url) # 웹 페이지 열기
driver.implicitly_wait(2) # 암묵적 대기

driver.get_screenshot_as_file("webCapture.png") # 스크린샷 저장

driver.quit()
