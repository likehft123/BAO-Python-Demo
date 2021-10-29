from bs4 import BeautifulSoup as bt4s
import requests as rq

url = 'https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/foreign-exchange-rates'

data = rq.get(url)
data.encoding = 'utf-8' #確認編碼正確
data = data.text #轉成文字檔

sp = bt4s(data,'html.parser')
#因class為關鍵字,指定屬性改為class_ =
rate = sp.find(id = 'inteTable1') 

countryR = rate.find_all('tr',class_='tableContent-light')

for row in countryR:
    tds = row.find_all('td')
    #print(tds[0].text)
    for r in tds:
        print(r.text)