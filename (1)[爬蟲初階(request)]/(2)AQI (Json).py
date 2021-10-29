import json as js
import requests as rq 

url = "https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json"

data = rq.get(url).text

allair = js.loads(data)

air = allair['records']

#print(air)

for row in air:
    print('站名 :',row['SiteName'])
    print('狀態 :',row['Status'])
    print('AQI :',row['AQI'])
    print('風向 :',row['WindDirec'])
    print()
    
    
