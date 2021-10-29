import json as js
import requests as rq 

url = "http://tbike-data.tainan.gov.tw/Service/StationStatus/Json"

data = rq.get(url).text

#print(data)
bike = js.loads(data) #loads !!

for row in bike:
    print("車站 :",row["StationName"])
    print("所在區域 :",row['District'])
    print('可借 :',row['AvaliableBikeCount'])
    print('可停 :',row['AvaliableSpaceCount'])
    print()
    
