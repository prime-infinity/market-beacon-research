import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=500"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": os.getenv("COINGECKO_API_KEY")
}

response = requests.get(url, headers=headers)

print(response.text)