import requests as rq 
from bs4 import BeautifulSoup as  bt4s

a = 0


for i in range(1,9):
    ###這集重點(最後面)###
    url = 'https://highschool.yjvs.chc.edu.tw/search/index.php?city=9&page='+str(i)
    ###這集重點(最後面)###
    data = rq.get(url)
    data.encoding = 'utf-8'
    data = data.text
    sp = bt4s(data,'html.parser')
    #酷酷的用法(?
    allschool = sp.find(id = 'school-list').find_all('table')
    
    
    for row in allschool:
        a+=1
        item = row.find_all('li')
        print(str(a)+'.',end='')
        print(item[0].text,item[1].text,item[2].text,item[3].text)
        
    
    