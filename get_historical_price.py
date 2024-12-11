import os
import requests

##get historica price data of a token
url = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=SHIB&tsym=USD&limit=5"

response = requests.get(url)

print(response.text)

