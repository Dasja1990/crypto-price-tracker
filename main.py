# Updated to track issues: multi-coin and real-time updates planned
# crypto-price-tracker
# Fetch current price from CoinGecko and allow selecting a coin.

import requests

def get_price(coin_id="bitcoin"):
    """
    Returns the USD price for a given coin_id (e.g., 'bitcoin', 'ethereum').
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": "usd"}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data.get(coin_id, {}).get("usd")
    except Exception as e:
        print("Error fetching price:", e)
        return None

if __name__ == "__main__":
    # Example usage
    coin = "bitcoin"
    price = get_price(coin)
    print(f"{coin} price (USD):", price)
