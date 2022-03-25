import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import sys
import creds
import pandas as pd

def get_whisky():
    newlist = []
    url = 'https://www.thewhiskyexchange.com/new-products/standard-whisky'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    new_whisky = soup.find('li', {'class': 'np-postlist__item'}).find_all('li', {'class': 'product-list-item'})

    for item in new_whisky:
        new = {
        'name': item.find('p', {'class': 'name'}).text,
        'spec': item.find('p', {'class': 'spec'}).text,
        'desc': item.find('p', {'class': 'description'}).text.strip(),
        'price': item.find('p', {'class': 'price'}).text,
        }
        newlist.append(new)
    
    df = pd.DataFrame(newlist)
    return df


print(get_whisky())
