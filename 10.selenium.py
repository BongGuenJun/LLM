# 네이버 웹툰 댓글 크롤링
# https://comic.naver.com/webtoon/detail?titleId=702672&no=1&week=finish
import time
from selenium import webdriver
# python -m pip install bs4
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=702672&no=1&week=finish')
soup = BeautifulSoup(driver.page_source)
comment_area = soup.find_all('span',{'classs':'u_cbox_contents'})
print('******* 베스트 댓글 *******')
for i in range(len(comment_area)):
  comment = comment_area[i].text.strip()
  print(comment)
  print('-'*30)

# /html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]
# 전체댓글 클릭릭
driver.find_element('xpath','/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]').click()
time.sleep(2) # 클릭후 불러오기전 아래코드가 실행되는것을 방지지

soup = BeautifulSoup(driver.page_source) #다시 페이지 소스 들고오기기
comment_area = soup.find_all('span',{'classs':'u_cbox_contents'})
print('******* 전체 댓글 *******')
for i in range(len(comment_area)):
  comment = comment_area[i].text.strip()
  print(comment)
  print('-'*30)

time.sleep(10)

