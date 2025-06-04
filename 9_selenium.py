# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
search = driver.find_element('name', 'q')
# html코드에서 name이 q인 요소 찾기(검색창)
search.send_keys('날씨') #날씨 입력 
search.send_keys(Keys.RETURN) #엔터키

time.sleep(10)