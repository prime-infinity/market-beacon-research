import os
import requests
import csv
import json
import time

# CryptoCompare API base URL
BASE_URL = "https://min-api.cryptocompare.com"

def get_top_coins(limit=100):
    """
    Retrieve top coins by market capitalization
    """
    url = f"{BASE_URL}/data/top/mktcapfull?limit={limit}&tsym=USD"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching top coins: {response.status_code}")
        return []
    
    data = response.json()
    
    # Extract Name and MaxSupply
    top_coins = []
    for coin in data.get('Data', []):
        coin_info = coin.get('CoinInfo', {})
        top_coins.append({
            'Name': coin_info.get('Name', ''),
            'MaxSupply': coin_info.get('MaxSupply', 0)
        })
    
    return top_coins

def get_historical_data(coin_symbol, limit=2000):
    """
    Retrieve historical daily data for a specific coin
    """
    url = f"{BASE_URL}/data/v2/histoday?fsym={coin_symbol}&tsym=USD&limit={limit}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching historical data for {coin_symbol}: {response.status_code}")
        return []
    
    data = response.json()
    
    # Extract relevant fields and add coin symbol
    historical_data = []
    for day_data in data.get('Data', {}).get('Data', []):
        historical_data.append({
            'Coin': coin_symbol,
            'Time': day_data.get('time', ''),
            'High': day_data.get('high', ''),
            'Low': day_data.get('low', ''),
            'Open': day_data.get('open', ''),
            'Close': day_data.get('close', ''),
            'VolumeFrom': day_data.get('volumefrom', ''),
            'VolumeTo': day_data.get('volumeto', '')
        })
    
    return historical_data

def main():
    #print(get_top_coins())
    #print(get_historical_data("BTC"))
    
    # Get top coins
    top_coins = get_top_coins()
    
    # Save top coins to CSV and JSON
    with open('top_coins.csv', 'w', newline='') as csvfile, \
         open('top_coins.json', 'w') as jsonfile:
        # CSV writing
        if top_coins:
            fieldnames = ['Name', 'MaxSupply']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(top_coins)
        
        # JSON writing
        json.dump(top_coins, jsonfile, indent=2)
        
    # Collect historical data for each coin
    all_historical_data = []
    for coin in top_coins:
        coin_symbol = coin['Name']
        try:
            historical_data = get_historical_data(coin_symbol)
            all_historical_data.extend(historical_data)
            
            # Add a small delay to respect API rate limits
            time.sleep(2.5)
        except Exception as e:
            print(f"Error processing {coin_symbol}: {e}")
            
    # Save historical data to CSV and JSON
    if all_historical_data:
        with open('historical_prices.csv', 'w', newline='') as csvfile, \
             open('historical_prices.json', 'w') as jsonfile:
            # CSV writing
            fieldnames = ['Coin', 'Time', 'High', 'Low', 'Open', 'Close', 'VolumeFrom', 'VolumeTo']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_historical_data)
            
            # JSON writing
            json.dump(all_historical_data, jsonfile, indent=2)
    
    print("Data retrieval complete. Check top_coins.csv, top_coins.json, historical_prices.csv, and historical_prices.json")
    

if __name__ == "__main__":
    main()