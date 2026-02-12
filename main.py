from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import datetime

this_year = datetime.datetime.now()
this_year = this_year.year

driver = webdriver.Chrome()
url = "https://eclass.sch.ac.kr/boards/5e2110140584830a497a4894/posts"
driver.get(url)
time.sleep(3)
html_content = driver.page_source
# url 불러오기 ~ html 콘텐츠 저장

soup = BeautifulSoup(html_content, "html.parser")

# notice 변수에 .xnbql-post-title 클래스 태그를 불러와서 저장(공지의 제목들이 저장되어 있음)
notices = soup.select(".xnbpl-post-title")
# n_year 변수에 .xnbql-createdat 클래스 태그를 불러와서 저장(공지가 올라온 날짜가 저장되어있음)
n_year = soup.select(".xnbpl-body-row-2")

print(f"[{this_year}]년도 공지글")
for info in notices:
    print(info.text,"\n")
    if this_year != n_year.pop(0).text:
        this_year = n_year
        print(f"[{this_year}]년도 공지글")
    