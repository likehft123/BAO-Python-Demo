import requests as rq 
from bs4 import BeautifulSoup as  bt4s

a = 0

#excel格式  用'w'新增title
with open ('school.csv','w',encoding=('utf-8')) as file:
    file.write('學校,地址,電話,網址\n')

for i in range(1,9):

    url = 'https://highschool.yjvs.chc.edu.tw/search/index.php'
    
    param={'city':9}
    param['page'] = i
    ####這集重點###
    data = rq.get(url,params=param)
    ####這集重點###
    data.encoding = 'utf-8'
    data = data.text
    sp = bt4s(data,'html.parser')
    #酷酷的用法(?
    allschool = sp.find(id = 'school-list').find_all('table')
    
    
    for row in allschool:
        item = row.find_all('li')
        #用'a'模式新增 , 'w'是覆蓋
        with open ('school.csv','a',encoding=('utf-8')) as file:
            file.write('{},{},{},{}\n'.format(item[0].text,item[1].text,item[2].text,item[3].text))
        
        #print(str(a)+'.',end='')
        #print(item[0].text,item[1].text,item[2].text,item[3].text)
        
    