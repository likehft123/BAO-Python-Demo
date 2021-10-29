import requests as rq 
from bs4 import BeautifulSoup as  bt4s

url = 'https://www.ptt.cc/bbs/Food/index.html'

data = rq.get(url)
data.encoding = 'utf-8'
data = data.text

sp = bt4s(data,'html.parser')

allfood = sp.find_all('div',class_='r-ent')

for row in allfood:
    print('標題 :'+row.a.text)
    print('日期 :'+row.find('div',class_='date').text)
    print('超連結 :'+'\n'+'https://www.ptt.cc'+row.a.get('href'),end='\n')
    print()