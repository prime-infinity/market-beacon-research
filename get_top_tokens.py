import os
import requests

##get top tokens by marketcap
url = "https://min-api.cryptocompare.com/data/top/mktcapfull?limit=10&tsym=USD"

response = requests.get(url)

print(response.text)

