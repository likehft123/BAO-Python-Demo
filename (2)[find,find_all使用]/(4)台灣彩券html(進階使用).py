from bs4 import BeautifulSoup as bt4s
import requests as rq

#因威力採,38樂合彩,大樂透,49樂合彩 的class都是contents_box02
#故特此操作


url = 'https://www.taiwanlottery.com.tw/index_new.aspx'

data = rq.get(url)
data.encoding = 'utf-8' #確認編碼正確
data = data.text #轉成文字檔

leto = bt4s(data,'html.parser')

allitem = leto.find_all('div',class_='contents_box02')

first = allitem[0]  #因威力彩與38樂合彩號碼相同,大樂透與49樂合彩號碼相同
second = allitem[2]  #故將此分為兩個不同號碼區塊
#一區號碼顏色class為綠
green = first.find_all('div',class_= 'ball_tx ball_green')
red  = first.find('div',class_='ball_red')
count = 0

for row in green:
    if count > 5:  #因1~6個數字為為排序狀態,6~12個數字為前面的排序狀態
        print(row.text,end='')  #故用此方法直接取排序後的數字
    count+=1
print('特別號 :'+red.text)
#二區號碼顏色class為黃
yellow = second.find_all('div',class_= 'ball_tx ball_yellow')
red  = second.find('div',class_='ball_red')
count = 0

for row in yellow:
    if count > 5:  #因1~6個數字為為排序狀態,6~12個數字為前面的排序狀態
        print(row.text,end='') #故用此方法直接取排序後的數字
    count+=1
print('特別號 :'+red.text)
    
