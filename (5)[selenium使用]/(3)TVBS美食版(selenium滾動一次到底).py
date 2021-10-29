from selenium import webdriver
import time 
from bs4 import BeautifulSoup as bt4s

webpath =  'c:\chromedriver.exe'
driver = webdriver.Chrome(webpath)

driver.implicitly_wait(3)
driver.get('https://supertaste.tvbs.com.tw/food')

for i in range(20):
    #後面為JavaScript語法
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)

#用driver的資料為driver.page_source
sp = bt4s(driver.page_source,'html.parser')

foods = sp.find(id = 'combolistUl')

items = foods.find_all('li')

for row in items:
    #有其中一個li裡面沒東西 所以下面這方法會跳錯
    #link = row.find('a').get('href')
    if len(row.find_all('a')) > 0:
        #因find_all是串列,即可使用索引值
        link = row.find_all('a')[0].get('href')
        img = row.find('img').get('data-original')
        title = row.find('div','txt').text
        print(title)
        print(img)
        print('https://supertaste.tvbs.com.tw/'+link)
        print()
