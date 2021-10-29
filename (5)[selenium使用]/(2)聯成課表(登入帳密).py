import requests as rq
from bs4 import BeautifulSoup as bt4s

session =rq.session()

url = 'https://member.lccnet.com.tw/login.asp?ACT=login'

param = {'NO':'104243496',
         'PWD':'Aa24612318',
         'rmAccount':'ON'}

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

data = session.post(url,data = param,headers = header)
data.encoding = 'big5'
data = data.text

myclass = session.get('https://member.lccnet.com.tw/myclass_index.asp',headers = header)
myclass.encoding = 'big5'
myclass = myclass.text
sp=bt4s(myclass,'html.parser')
data = sp.find(id = 'table85')
trs = data.find_all('tr')
for row in trs:
    tds = row.find_all('td')
    for i in tds:
        print(i.text.strip()) #去空白strip()
#print(myclass)

