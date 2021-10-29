import requests as rq 
from bs4 import BeautifulSoup as bt4s


url  = 'https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation'

#台灣鐵路時刻 查詢 
#流程 查詢(檢查) > 上排Network > 左下name找到運算時間最長的項目為querybystation
# > 右下點選Headers 可看到rq的方法post,url,最下面有headers跟param 

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
param = {
    '_csrf': '48761444-0295-4bdf-98cd-bc3e299e95f7',
    'rideDate': '2021/09/16',
    'station': '3300-臺中'
    }

data = rq.post(url,data = param,headers=header)
data.encoding = 'utf-8'
data = data.text
#print(data)

sp = bt4s(data,'html.parser')
stations = sp.find(id='tab1').find_all('tr')

#新增查詢時間功能

qTime = input('請輸入查詢時間(hh/mm):')
qTime += ':00'


#奇數tr內沒有想要的資料(td) 偶數tr才有
#所以在找尋td時 在奇數tr會無結果 為空串列 迴圈去跑會無法索取索引值
#順行時刻表 id為tab1

for row in stations:
    tds = row.find_all('td')
    if len(tds) > 1 :  #以此判斷式來處理空串列
        carTime = tds[1].text
        
        if qTime >= carTime:
            print(tds[0].text.replace('\n','')) #因tds[0]內建許多\n,故以''來替代\n
            print(tds[1].text)
            print(tds[2].text)
            print(tds[3].text.replace('\n',''))
            print()
        

#逆行時刻表同上 只有id不同為tab2
turnstations = sp.find(id='tab2').find_all('tr')


for row in turnstations:
    tds = row.find_all('td')
    if len(tds) > 1 :  #以此判斷式來處理空串列
        print(tds[0].text.replace('\n','')) #因tds[0]內建許多\n,故以''來替代\n
        print(tds[1].text)
        print(tds[2].text)
        print(tds[3].text.replace('\n',''))
        print()
        

        
    
