import requests 
from bs4 import BeautifulSoup 
#import smtplib
import time
#from twilio.rest import Client 
import xlwt
import os
from os import path

URL1='https://www.moneycontrol.com/india/stockpricequote/miningminerals/vedanta/SG'
URL2='https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/alkemlaboratories/AL05'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0' }

def ttitle(soup2):
    ttitle = soup2.find("h1", {"class" :"pcstname"}).get_text()
    ttitle=str(ttitle).strip()
    return ttitle

def pprice(soup2):
    price=soup2.find_all("div", {"class":"pcnsb div_live_price_wrap"})[0].find("span").get_text()
    price=str(price).strip()
 
    new_p=""
    for i in price:
        if i==',':
            continue
        elif i=='₹':
            continue
        elif i==' ':
            continue

        elif i=='.':
            break
        else:
            new_p=new_p+i 

    converted_price=int(new_p)
   
    return converted_price
    
    
def check_price():
    page1 = requests.get(URL1, headers=headers)
    soup1 = BeautifulSoup(page1.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    page2 = requests.get(URL2, headers=headers)
    soup3 = BeautifulSoup(page2.content, "html.parser")
    soup4 = BeautifulSoup(soup3.prettify(), "html.parser")
    
    title=[]
    price=[]
    cp=[63.30,2445]
    qty=[100,2]


    
    x=ttitle(soup2)
    y=pprice(soup2)
    title.append(x)   
    price.append(y)

    x=ttitle(soup4)
    y=pprice(soup4)
    title.append(x)   
    price.append(y)

    
    

    #print(price)
    
        
    DATA=(("Name","Price","Qty","Price","Current","net"),
            (title[0],price[0],qty[0],cp[0],price[0],(price[0]-cp[0])*qty[0]),
            (title[1],price[1],qty[1],cp[1],price[1],(price[1]-cp[1])*qty[1])
        )
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet("My Sheet")
    for i, row in enumerate(DATA):
        for j, col in enumerate(row):
            ws.write(i, j, col)
        ws.col(0).width = 256 * max([len(row[0]) for row in DATA])
    wb.save("Downloads/myworkbook.xls")
    print("WORKBOOK CREATED")
     
    #sleep(1000)

    '''
    if(price>70):
        send_mail()
        sendSMS()
        time.sleep(100)
    '''
'''
def sendSMS(): 
  
    account_sid = 'ACcd5d5855ecb8836912db277d284fe8b0'
    auth_token = 'f47141676886f3e580f1e08cd437f8ab'
    
    client = Client(account_sid, auth_token) 
    
    the value of 'from' with the number  
    received from Twilio and the value of 'to' 
    with the number in which you want to send message.
    message = client.messages.create( 
                                from_='+12057827504', 
                                body ='SELL YOUR STOCKS', 
                                to ='+919837910699'
                            ) 
    
    print(message.sid) 



def send_mail():
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('architmaheshwari60@gmail.com', '9837910699')

    subject='Sell your stock'
    body='Price reached the bar you set, sell the stock'
    
    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'architmaheshwari0@gmail.com',
        'amaheshwari_be17@thapar.edu',
        msg
    )
    print('HEY EMAIL SENT')

    server.quit()
'''
while(True):
    

    check_price()
    ##time.sleep(60)
    #os.remove("C:/Users/shadow/Downloads/myworkbook.xls")
    break
           