import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests as rq
import json

def auth_client(path,scopes): #path(路徑) scopes(url)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path,scopes)
    return gspread.authorize(credentials)

#金鑰路徑(後面要加.json)
path = "c://pyexcel//fifth-mechanism-328110-78c4675f1d24.json"
#url
scopes = ['https://spreadsheets.google.com/feeds']
#自訂函式使用
client = auth_client(path,scopes)
#網址上的key
key = '1kY-PkRHNOiUQiAknxLy0Js-TqsLmm6I2nuB_roUkDAg'
#用key開啟sheet
ws = client.open_by_key(key)
#用索引值0來找sheet(不建議,sheet換位子就會抓錯)
##sheet = ws.get_worksheet(0)
#用sheet名稱來抓工作表(推薦)
sheet = ws.worksheet('老師')
#在3.6位寫上hello
##sheet.update_cell(3,6,'Hello')
#get欄位內的值
print(sheet.cell(8,3).value)
print(sheet.cell(9,3).value)
print(sheet.cell(10,3).value)

