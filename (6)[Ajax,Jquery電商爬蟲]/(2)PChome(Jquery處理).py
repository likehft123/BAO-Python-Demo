###遇到Jquery解法###
##找到json資料之後,清除JavaScript語法,json資料才能正常呈現##

import requests as rq
import json 

url = 'https://24h.pchome.com.tw/cdn/onsale/v4/20210928/original/data.json&27213822'

data = rq.get(url)
data.encoding = 'utf-8'
data = data.text

#處理JavaScript語法
items = data.split('var') #var在頭尾都有,以var做切割
goods = items[1].strip() #中間的索引值1就是要的js內容
index = goods.find('[{') #這樣可以找到所有的Json字典格式
allgoods = goods[index:-1] #給他-1,防止抓到最後的var

#print(allgoods)

info = json.loads(allgoods)

for row in info:
    goods = row['Nodes']
    for p in goods:
        link = p['Link']['Url']
        price = p['Link']['Text2']
        img = p['Img']['Src']
        title = p['Img']['Title']
        
        print(title)
        print(price)
        print('https:'+link)
        print('https://b.ecimg.tw/'+img)
        print()


