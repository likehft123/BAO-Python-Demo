####Ajax資料抓法####
##F12 > NetWork > Fetch/XHR > 從Preview找到資料 > 複製url > reponse找到json##

import requests as rq
import json 

url = 'https://www.kkday.com/zh-tw/product/ajax_get_top_products?areaCode=A01-001-00019&upLimit=20&showLmit=4&csrf_token_name=6478a523329df1d252a3e39147bfcd29'

data = rq.get(url)
data.encoding = 'utf-8'
data = data.text

item = json.loads(data)
allitem = item['data'] #資料在'data'key裡

for row in allitem: #從data裡面找到資料的key
    title = row['name']
    info = row['introduction']
    img = row['img_url']
    price = row['price']
    link = row['url']
    
    print('標題 :',title)
    print('介紹 :',info)
    print('圖片 :',img)
    print('價格 :',price,'元')
    print('文章連結 :',link)
    print()
    












