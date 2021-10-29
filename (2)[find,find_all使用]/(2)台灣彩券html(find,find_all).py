from bs4 import BeautifulSoup as bt4s
import requests as rq

url = 'https://www.taiwanlottery.com.tw/index_new.aspx'

data = rq.get(url)
data.encoding = 'utf-8' #確認編碼正確
data = data.text #轉成文字檔

leto = bt4s(data,'html.parser')
#因class為關鍵字,指定屬性改為class_ =
ball = leto.find('div',class_='ball_box01') 
#找到指定區塊後,想要的內文的屬性都一樣,用find_all抓取,for迴圈印出
numbers = ball.find_all('div',class_='ball_tx ball_yellow')

for row in numbers:
    print(row.text,end='')

print('-'*30)


