import requests as rq 
from bs4 import BeautifulSoup as  bt4s

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
header = {'cookie':'over18=1'}

for i in range(3):
    print('第{}頁'.format(i+1))
    data = rq.get(url,headers=header)  #加上header  or cookie
    data.encoding = 'utf-8'
    data = data.text
    
    sp = bt4s(data,'html.parser')
    
    allfood = sp.find_all('div',class_='r-ent')
    
    for row in allfood:
        print('標題 :'+row.a.text)
        print('日期 :'+row.find('div',class_='date').text)
        print('超連結 :'+'\n'+'https://www.ptt.cc'+row.a.get('href'),end='\n')
        print()
    
    url = 'https://www.ptt.cc'+sp.find_all('a','btn wide')[1].get('href')