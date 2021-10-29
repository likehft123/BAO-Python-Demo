import pymysql

#與資料庫做連接
conn = pymysql.connect(host='localhost',
                       user = 'root',
                       passwd='123456789',
                       db='lcc')
#對資料庫下指令要用的
cursor = conn.cursor()

