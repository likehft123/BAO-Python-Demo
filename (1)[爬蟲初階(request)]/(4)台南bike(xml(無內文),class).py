import requests as rq
import xml.sax

class BusHandler(xml.sax.ContentHandler):
    
    def startElement(self, name, attrs):
        if name == 'Route':
            print('路線 :',attrs['nameZh'])
            print('起終點 :',attrs['ddesc'])
            print()

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    bus = BusHandler()
    parser.setContentHandler(bus)
    url = 'http://ibus.tbkc.gov.tw/xmlbus/StaticData/GetRoute.xml'   

    data = rq.get(url) 
    data.encoding = 'UTF-8' #確認編碼正確在指定text 防止亂碼
    data = data.text
    
    file = 'bus.xml'
    
    with open(file,'w',encoding="utf-8") as fobj: #存檔案
        fobj.write(data)
        
    parser.parse(file)