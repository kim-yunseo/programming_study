from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬브라우저 실행
driver = webdriver.Chrome()
#주소 접속
driver.get("https://www.example.com")

p= driver.find_element(By.TAG_NAME, 'p')
print("p태그 첫번째 요소를 가져옴")
print(p)
print(type(p))
print(p.text)

p1= driver.find_elements(By.TAG_NAME, 'p')
print("p태그 모든 요소를 가져옴")
for a in p1:
    print(a.text)

time.sleep(5)