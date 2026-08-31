from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#크롬브라우저 실행
driver = webdriver.Chrome()
#주소 접속
driver.get("https://www.youtube.com")

#검색창
s_element = driver.find_element(By.XPATH,'//*[@id="center"]/yt-searchbox/div[1]/div/div/form/input')
s_element.send_keys("코코")

# 검색버튼
btn = driver.find_element(By.XPATH,'//*[@id="center"]/yt-searchbox/div[1]/div/button')
btn.click()

time.sleep(10)