from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def scroll_fun():
    while True:
    #스크롤 하기 전 높이
        h1= driver.execute_script(
            "return document.documentElement.scrollHeight")
    #print("첫번째 높이",h1)

    #스크롤을 현재 높이만큼 내리기
        driver.execute_script(
            "window.scrollTo(0,document.documentElement.scrollHeight)"
        )
    #영상 로딩 시간(잠시 대기)
        time.sleep(2)

    #스크롤 내린 뒤 높이 값
        h2= driver.execute_script(
            "return document.documentElement.scrollHeight"
        )
    #print("두번째 높이",h2)
    #스크롤 전,후 높이 비교
        if h1 == h2:
            break

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=%EC%9D%B8%EA%B8%B0%EA%B8%89%EC%83%81%EC%8A%B9")
time.sleep(2)

search_input = driver.find_element(By.NAME,'search_query')
#search_input = driver.find_element(By.CSS_SELECTOR,'input.ytSearchboxComponentInput')

search_input.clear() #검색내용 삭제
search_input.send_keys("수면")
btn =  driver.find_element(By.XPATH,'//*[@id="center"]/yt-searchbox/div[1]/div/button')
btn.click()
time.sleep(2)
# search_input.send_keys(keys.ENTER)

scroll_fun()
titles= driver.find_elements(By.XPATH,'//*[@id="video-title"]/yt-formatted-string')

title_list=[] 
for t in titles:
    title_list.append(t.text)
print(f"총 {len(title_list)}개의 제목을 수집하였습니다")

c_result={
    "title":title_list
}
result= pd.DataFrame(c_result)
result2=result.sort_values(by="title",ascending=True)
result2.to_csv("./result.csv", encoding="utf-8-sig")