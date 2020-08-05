import requests
from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent

URLS={'link':1599} #Link:Price_to_get_Notified

ua = UserAgent()
headers={"User-Agent":ua.random ,'Accept-Language':'zh-tw','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Connection':'keep-alive','Accept-Encoding':'gzip, deflate'}

for url,nprice in URLS.items():
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')

    price=soup.find(id='priceblock_ourprice')
    price=price.get_text()
    price=float(re.sub('[^0-9.]','',price))
    print(price)
    

    if(nprice >= price):
        msg=""
        msg+=""
        #notify(msg)

