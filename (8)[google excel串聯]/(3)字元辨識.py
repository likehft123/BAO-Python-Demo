import pytesseract
from PIL import Image #打開圖片檔用的

#r絕對路徑
path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#路徑
pytesseract.pytesseract.tesseract_cmd = path
#開啟圖片
# img = Image.open(r"002.png")
# text = pytesseract.image_to_string(img,lang='chi_tra')

# img = Image.open(r"003.png")
# text = pytesseract.image_to_string(img,lang='eng')

img = Image.open(r"001.png")
text = pytesseract.image_to_string(img,lang='eng',config='--psm 10 -c tessedit_char_whitelist=0123456789')

print(text.strip())












