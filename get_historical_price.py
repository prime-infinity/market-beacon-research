import os
import requests

##get daily historica price data for the prev 2000 days of a token
url = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000"

response = requests.get(url)

print(response.text)

