from bs4 import BeautifulSoup as bt4s
import requests as rq

url = 'https://www.setn.com/ViewAll.aspx?PageGroupID=0'

data = rq.get(url)
data.encoding = 'utf-8'
data = data.text
parser = bt4s(data,'html.parser') #要記得

news = parser.find_all('div',class_='col-sm-12 newsItems')

for row in news:
    h3 = row.find('h3')  #因裡面有兩個a故在往內指定h3確保只有一個a
    title = h3.find('a').text 
    link = h3.find('a').get('href')
    time = row.find('time').text
    
    print('標題 :',title)
    print('時間 :',time)
    print('連結 :','\n'+link)
    print()