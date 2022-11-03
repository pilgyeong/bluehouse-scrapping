import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import re

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('chromedriver',options=options)
driver.implicitly_wait(3)

# dataframe to save
df = pd.DataFrame({'번호':[], '분류':[], '제목':[], '만료일':[], '참여인원':[]})
my_list = []
temp_str_list = ['' for x in range(5)]

# web scraping
page_num = 1

while page_num <= 100:
    url = 'https://www1.president.go.kr/petitions/?c=0&only=1&page={}&order=1'.format(page_num)

    driver.get(url)
    driver.implicitly_wait(5)

    # XPATH를 활용해 tag 검색으로 elements 불러오기
    lis = driver.find_elements(By.CSS_SELECTOR, "ul.petition_list>li>div.bl_wrap")

    
    # 모든 element를 확인
    for li in lis:
        # tag 사이 text를 개행 기준으로 쪼개서 TempList에 저장
        category = li.find_element(By.CSS_SELECTOR, "div.bl_category.ccategory.cs.wv_category").text
        
        petition_title_elem = li.find_element(By.CSS_SELECTOR, "div.bl_subject>a.cb.relpy_w")
        petition_title = petition_title_elem.text
        petition_code = re.match(r'.+\/([0-9]+)$', petition_title_elem.get_attribute("href")).group(1)
        
        expire_date = li.find_element(By.CSS_SELECTOR, "div.bl_date.light").text
        agree_num = int(li.find_element(By.CSS_SELECTOR, "div.bl_agree.cs").text.replace(",", "").replace("명",""))

        # TempList를 전체 리스트에 추가
        my_list.append(pd.DataFrame({'번호':[petition_code], '분류':[category], '제목':[petition_title], \
                                    '만료일':[expire_date], '참여인원':[agree_num]}))
            
    page_num = page_num + 1
    time.sleep(10)
    

# merge into full dataframe
df = pd.concat(my_list)
df.reset_index(drop=True, inplace=True)


#df

df.to_csv("../data/bluehouse.csv",index = False)