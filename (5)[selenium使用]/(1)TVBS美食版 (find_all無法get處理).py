import requests as rq
from bs4 import BeautifulSoup as bt4s

url = 'https://supertaste.tvbs.com.tw/food'

data = rq.get(url)
data.encoding = 'utf-8'
data = data.text
sp = bt4s(data,'html.parser')

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