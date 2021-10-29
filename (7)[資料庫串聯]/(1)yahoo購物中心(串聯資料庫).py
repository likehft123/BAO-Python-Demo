import db
from bs4 import BeautifulSoup as bt4s
import requests as rq

url = 'https://tw.buy.yahoo.com/category/40057185'
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

data = rq.get(url,headers=header)
data.encoding = 'utf-8'
data = data.text

sp = bt4s(data,'html.parser')
items = sp.find_all('li',class_='BaseGridItem__grid___2wuJ7 BaseGridItem__multipleImage___37M7b')

for row in items :
    link = row.a.get('href')
    img = row.img.get('srcset').split()[0]
    title = row.find('span',class_='BaseGridItem__title___2HWui').text
    price = row.find('em').text
    price = price.replace('$','').replace(',','')
    
    sql = "select price from product where link='{}'".format(link)
    db.cursor.execute(sql)
    db.conn.commit() 
    
    if db.cursor.rowcount == 0:
        #此處為sql語法
        sql = "insert into product(shop,name,price,photo_url,link,product_type) values('Yahoo','{}','{}','{}','{}',1)".format(title,price,img,link)
        db.cursor.execute(sql) #執行語法
        db.conn.commit() #立即執行,不打可能會放入暫存不生效
    else:
        result = db.cursor.fetchone()
        if result[0] != int(price):
            print('價格不同')            
    # print(title)
    # print(price)
    # print(link)
    # print(img)
    # print()
#將資料庫關閉
db.conn.close()