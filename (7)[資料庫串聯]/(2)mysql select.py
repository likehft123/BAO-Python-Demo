import db

#where為判斷式
sql = "select shop,name,price from product where price > 10000"

db.cursor.execute(sql)
db.conn.commit()


result = db.cursor.fetchall() #fetchall()抓取全部,fetchone()抓取一筆

#rowcount 數量
if db.cursor.rowcount != 0 :
    print(result)
else:
    print('找不到符合的商品')    