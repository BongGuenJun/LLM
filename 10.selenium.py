# 네이버 웹툰 크롤링

import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=783053&no=134&week=tue')
soup = BeautifulSoup(driver.page_source)
comment_area = soup.findAll('span', {'class', 'u_cbox_contents'})
print('********** 베스트 댓글 **********')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print('-' * 30)

driver.find_element('xpath', '//*[@id="cbox_module_wai_u_cbox_sort_option_tab2"]/span[2]').click()
time.sleep(2)

soup = BeautifulSoup(driver.page_source)
comment_area = soup.findAll('span', {'class', 'u_cbox_contents'})

print('********** 전체 댓글 **********')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print('-' * 30)