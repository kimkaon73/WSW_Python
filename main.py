from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import datetime

# url을 이용해 response를 가져오고 html에 response에서 받아온 html 정보를 저장
# 페이지 이동을 위한 변수 page 생성
page = 1
url = f"https://www.dreamspon.com/scholarship/list.html?page="+str(page)
response = requests.get(url)
html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, "html.parser")

# 광고 혹은 배너의 정보를 받아오지 않도록 범위를 'tbody' 태그로 제한
NoticeList = soup.find('tbody')

# 목록에서 title 태그 내에 저장된 제목만을 추출
SubTitle = NoticeList.select('.title')

# 목록에서 title 태그 내에 저장된 링크를 Link 리스트에 저장
Link = []
for ToLink in SubTitle:
    Link.append("https://www.dreamspon.com"+ToLink.find('a')['href'])

# Link를 가져오기 위한 변수 LinkNum을 생성
LinkNum = 0
for title in SubTitle:
    print(title.text,"\n"+Link[LinkNum])
    print()
    LinkNum+=1