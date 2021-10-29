import requests as rq 
from bs4 import BeautifulSoup as bt4s
import json
import pandas as pd 

#全球確診數
print('------全球------')
url = 'https://covid19dashboard.cdc.gov.tw/dash2'

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

data = rq.get(url,headers=header)
data.encoding = 'utf-8'
data = data.text

covid = json.loads(data)
alldead = covid['0']

print('全球確診人數 :',alldead['cases'])
print('全球死亡人數 :',alldead['deaths'])
print()
print('------台灣------')

url = 'https://covid19dashboard.cdc.gov.tw/dash3'

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

data = rq.get(url,headers=header)
data.encoding = 'utf-8'
data = data.text

covid = json.loads(data)
alldead = covid['0']

print('台灣確診人數 :',alldead['確診'])
print('台灣死亡人數 :',alldead['死亡'])

