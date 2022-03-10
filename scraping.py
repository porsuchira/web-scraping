import requests
import lxml 
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display
url = 'https://www.tradingview.com/markets/cryptocurrencies/prices-all/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
tr_tag = soup.find_all('tr', {'class':'tv-data-table__row tv-data-table__stroke tv-screener-table__result-row'})
for obj_tr in tr_tag:
    coin = str(obj_tr.td.div.div.a.text)    
    price = obj_tr.find_all('td', {'class':'tv-data-table__cell tv-screener-table__cell tv-screener-table__cell--big'})[2].text
    print(coin,price)



