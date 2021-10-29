import requests as rq 
from bs4 import BeautifulSoup as bt4s

url = 'https://shopee.tw/search?keyword=switch'

#這組header是蝦皮本身希望google的cookie來讀取(萬用鑰匙?
header = {'cookie':'Googlebot',
          'user-agent':'Googlebot'}

data = rq.get(url,headers=header)
data.encoding = 'utf-8'
data = data.text

sp = bt4s(data,'html.parser')

allitem = sp.find_all('div',class_='col-xs-2-4 shopee-search-item-result__item')

for row in allitem:
    link = row.find('a').get('href')
    title = row.find('div',class_='_10Wbs- _5SSWfi UjjMrh')
    price = row.find_all('span','_1d9_77')
    print(title.text)
    print(link)
    if len(price) == 1:
        print(price[0].text)
    else:
        print(price[0].text,'~',price[1].text)
        
    print()
    