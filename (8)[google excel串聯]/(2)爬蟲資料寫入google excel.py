import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests as rq
import json
from bs4 import BeautifulSoup as bt4s

def auth_client(path,scopes): #path(路徑) scopes(url)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path,scopes)
    return gspread.authorize(credentials)

#金鑰路徑(後面要加.json)
path = "c://pyexcel//fifth-mechanism-328110-78c4675f1d24.json"
#url
scopes = ['https://spreadsheets.google.com/feeds']
#自訂函式使用
client = auth_client(path,scopes)
#網址上的key
key = '1kY-PkRHNOiUQiAknxLy0Js-TqsLmm6I2nuB_roUkDAg'
#用key開啟sheet
ws = client.open_by_key(key)

sheet = ws.worksheet('yahoo')

yahoourl = 'https://tw.buy.yahoo.com/search/product?p=%E5%90%B9%E9%A2%A8%E6%A9%9F'

data = rq.get(yahoourl)
data.encoding = 'utf-8'
data = data.text
sp = bt4s(data,'html.parser')
items = sp.find_all('li',class_='BaseGridItem__grid___2wuJ7 BaseGridItem__multipleImage___37M7b')

a = 2
for row in items:
    name = row.find('span',class_='BaseGridItem__title___2HWui').text
    price = row.find('em',class_='BaseGridItem__price___31jkj').text
    price = price.replace('$','').replace(',','')
    sheet.update_cell(a,1,name)
    sheet.update_cell(a,2,price)
    a += 1
    #print(name)
    #print(price)