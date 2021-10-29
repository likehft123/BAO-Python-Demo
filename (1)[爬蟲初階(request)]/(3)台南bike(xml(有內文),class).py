import requests as rq
import xml.sax  #解xml函式庫

#https://docs.python.org/3/library/xml.sax.html

class BikeHandler(xml.sax.ContentHandler):
    def __inint__(self):
        self.station = ""
        self.rent = ""
        self.space = ""
    #開頭標籤 
    def startElement(self, name, attrs): #attrs屬性
        self.tag = name
    #內文
    def characters(self, content):
        if self.tag == 'StationName':
            self.station = content
        elif self.tag == 'AvaliableBikeCount':
            self.rent = content
        elif self.tag == 'AvaliableSpaceCount':
            self.space = content
    #結束 (印出)
    def endElement(self, name):
        if self.tag == 'StationName':
            print('站名 :',self.station)
        elif self.tag == 'AvaliableBikeCount':
            print('可借 :',self.rent)
        elif self.tag == 'AvaliableSpaceCount':
            print('可停 :',self.space)
            print()
            
if __name__ == "__main__":
    parser = xml.sax.make_parser()
    bike = BikeHandler()
    parser.setContentHandler(bike)
    url = 'http://tbike-data.tainan.gov.tw/Service/StationStatus/Xml'   

    data = rq.get(url) 
    data.encoding = 'UTF-8' #確認編碼正確在指定text 防止亂碼
    data = data.text
    
    file = 'bike.xml'
    
    with open(file,'w',encoding="utf-8") as fobj: #存檔案
        fobj.write(data)
        
    parser.parse(file)
    
    
    
    