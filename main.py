# crypto-price-tracker - simple starter
# This script fetches the current price of a cryptocurrency using CoinGecko API.

import requests

def get_price(coin_id="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": "usd"}
    resp = requests.get(url, params=params)
    data = resp.json()
    return data.get(coin_id, {}).get("usd")

if __name__ == "__main__":
    print("This is a starter file. Add more functionality in future commits.")
  
