import requests 
from bs4 import BeautifulSoup 
import smtplib
import time

URL='https://www.amazon.in/dp/B07HGMQX6N?pf_rd_r=H098FEC434S420CYWZY2&pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0' }

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id= "productTitle").get_text()

    print(title.strip())

    price = soup2.find(id='priceblock_ourprice').get_text().strip()
    price=price.strip()
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

    converted_price=float(new_p)
    print(converted_price)

    if(converted_price>10000):
        send_mail()

def send_mail():
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('architmaheshwari60@gmail.com', '9837910699')

    subject='Price Fell Down'
    body='Check the amazon link https://www.amazon.in/dp/B07HGMQX6N?pf_rd_r=H098FEC434S420CYWZY2&pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e'
    
    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'architmaheshwari0@gmail.com',
        'amaheshwari_be17@thapar.edu',
        msg
    )
    print('HEY EMAIL SENT')

    server.quit()

while(True):
    
    check_price()
    time.sleep(60*60)