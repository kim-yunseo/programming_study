from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#크롬브라우저 실행
driver = webdriver.Chrome()
#주소 접속
driver.get("https://search.danawa.com/dsearch.php?k1=%EC%84%A0%ED%92%8D%EA%B8%B0&module=goods&act=dispMain")

# 상품명 접근
names = driver.find_elements(By.CLASS_NAME, 'goods_title')

for n in names:
    print(n.text)

time.sleep(10)
