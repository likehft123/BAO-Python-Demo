import requests as rq 
from bs4 import BeautifulSoup as bt4s
import json
import pandas as pd 
import datetime 

#字串處理 帶入參數的時間
today1 = str(datetime.date.today())
today = today1.split('-') 
a = '/'
today = a.join(today)
date = []
date.append(str(today))

url = 'https://www.thsrc.com.tw/TimeTable/Search'

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

#參數內若無值 可不用給
param = {  
    'SearchType': 'S',
    'Lang': 'TW',
    'StartStation': 'TaiZhong',
    'EndStation': 'TaiPei',
    'OutWardSearchDate': date,
    'OutWardSearchTime': '20:00',
    'ReturnSearchDate': date,
    'ReturnSearchTime': '20:00'
    }

data = rq.post(url,data=param,headers=header)
data.encoding = 'utf-8'
data = data.text
#print(data) #發現回傳值非html 為Jqurry,Ajax(?)

#從Network > Response 可找到json格式 丟到online parser 能看到完整json格式
highway = json.loads(data)
#站務資料在這裡面
station = highway['data']['DepartureTable']['TrainItem']

number= list()
startTime = list()
endTime = list()
duration = list()



for row in station :
    goTime = row['DepartureTime'] + ':00' #發車時間
    qTime = '20:00:00' #自訂時間
    if goTime >= qTime:  #可篩選車次
        #因StationInfo裡是串列包字典,必須使用for一個個抓
        info = row['StationInfo']
        for i in info:
            if i['Show']:  #==True
                print(i['StationName'],end=',')
        print()
        
        number.append(row['TrainNumber'])
        startTime.append(row['DepartureTime'])
        endTime.append(row['DestinationTime'])
        duration.append(row['Duration'])

#將資料製成表格
th = pd.DataFrame({'車次':number,
                   "出發時間":startTime,
                   '到達時間':endTime,
                   '乘車時間':duration},
                   columns=['車次','出發時間','到達時間','乘車時間'])#欄位名稱
print(th)




