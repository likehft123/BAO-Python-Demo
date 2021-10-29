from selenium import webdriver
import time 
from bs4 import BeautifulSoup as bt4s

webpath =  'c:\chromedriver.exe'
driver = webdriver.Chrome(webpath)

driver.implicitly_wait(3)
driver.get('https://tw.buy.yahoo.com/category/40057185')

height = 700
for i in range(20):
    #後面為JavaScript語法
    driver.execute_script('window.scrollTo(0,{})'.format(height))
    height += 700
    time.sleep(1)

#用driver的資料為driver.page_source
sp = bt4s(driver.page_source,'html.parser')



