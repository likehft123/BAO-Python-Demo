from bs4 import BeautifulSoup as bt4s
#id 在html語法裡,通常有"唯一性"

html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

soup = bt4s(html_doc,'html.parser')

#find 只抓取'第一個'
h2 = soup.find('h2') #抓到標籤<h2>Test Header</h2>
p = soup.find('p')
#print(h2.text) #要呈現內容使用.text
#print(p.text)

#find_all 符合地都抓,呈陣列[]型態  #因是陣列故無法直接使用.text,可用[0]索引值.text
h2_arr = soup.find_all('h2')
p_arr = soup.find_all('p')
#print(h2_arr)  
#print(p_arr)  

a = soup.find('a')
a_text = a.text   #優先抓第一個屬性
href1 = a.get('href')  #可指定要哪一個屬性
#print(a_text)  
#print(href1)   

alllink = soup.find_all('a')

for row in alllink :
    id1 = row.text
    link = row.get('href')
    print(id1)
    print(link)
    print()
    
