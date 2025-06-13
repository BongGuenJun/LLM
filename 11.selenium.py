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
        # driver.execute_script : 자바 스크립트 코드를 사용하게 해주는 역할(스크롤을 올려라)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)

    soup = BeautifulSoup(driver.page_source)

    # 댓글 박스부분을 패턴으로 검색(개발자 도구에서 select 복사)
    review_containers = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div')
    # 작성일 select 부분코드
    review_date = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div > div.css-1ivchjf > p')
    

    for i in range(len(review_containers)):
        # find() 로 불러올때 class 속성은 _ 를 붙어야 한다
        review_text = review_containers[i].find('p', class_='content-text').text
        date = review_date[i].text
        # print(review_text, date)
        review_empty_stars = review_containers[i].find_all('path', {'fill-rule':'evenodd'})
        # print(review_empty_stars)
        stars = 5 - len(review_empty_stars)
        # review 내용을 dict형식으로 list에 저장
        review_dict = {
          'review': review_text,
          'date': date,
          'stars' : stars
        }
        review_list.append(review_dict)

    print(review_list)

    time.sleep(10)

crawl_yanolja_reviews('신라스테이 여수', 'https://www.yanolja.com/reviews/domestic/10046614')