from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#크롬브라우저 실행
driver = webdriver.Chrome()
#주소 접속
driver.get("https://comic.naver.com/webtoon?tab=mon")
time.sleep(10)

# 웹툰 제목
names = driver.find_elements(By.CLASS_NAME, 'text')
# web_class= driver.find_elements_by_css_selector(".text")
# css_selector(".~"): class
# css_selector("#~"): id

for n in names:
    print(n.text)
print(len(names))