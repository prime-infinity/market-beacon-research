import os
import requests

##get top 100 tokens by marketcap
url = "https://min-api.cryptocompare.com/data/top/mktcapfull?limit=100&tsym=USD"

response = requests.get(url)

print(response.text)

