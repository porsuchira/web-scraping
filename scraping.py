import requests
import lxml 
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display
url = 'https://www.tradingview.com/markets/cryptocurrencies/prices-all/'
res = requests.get(url)
#print(res.text[:200])
soup = BeautifulSoup(res.text, 'html.parser')
coin = soup.find_all('a', {'class':'tv-screener__symbol'})
coinLs = []
#price = soup.find_all('td', {'class':'tv-data-table__cell tv-screener-table__cell tv-screener-table__cell--big'})
for c in coin:
    coinLs.append(c.text)

#print(len(price))
#for p in range(2, len(price), 6):
#    print(price[p])
df=pd.DataFrame({'coin':coinLs})
display(df)





