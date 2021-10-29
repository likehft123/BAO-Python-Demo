import requests as rq
import json 

url = 'https://24h.pchome.com.tw/cdn/region/DGBJ/data&27213885'

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
        title = p['Link']['Text']
        link = p['Link']['Url']
        img = p['Img']['Src']
        price = str(p['Link']['Text1'])
        print(title)
        print(price)
        print(link)
        print(img)
        print()
        
        