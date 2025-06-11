import time
from selenium import webdriver
from bs4 import BeautifulSoup

def crawl_yanolja_reviews(name, url):
  review_list = []
  driver = webdriver.Chrome()
  driver.get(url)
  time.sleep(2)

  scroll_count = 3
  for i in range(scroll_count):
    driver.excute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
  soup = BeautifulSoup(driver.page_source)

  review_containers = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div')
  review_date = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div > div.css-1ivchjf > p')
  
  for i in range(len(review_containers)):
    print(i)
  
  time.sleep(10)

crawl_yanolja_reviews('신라스테이 여수', 'https://www.yanolja.com/reviews/domestic/10046614')