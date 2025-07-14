import requests
import matplotlib.pyplot as plt
from datetime import datetime
from Coin_map import get_coin_id


def fetch_price_history(coin_id='bitcoin', vs_currency='usd', days=30):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart'
    params = {
        'vs_currency': vs_currency,
        'days': days
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data['prices']


def plot_price_chart(prices, coin_id='bitcoin'):
    dates = [datetime.fromtimestamp(p[0]/1000).date() for p in prices]
    values = [p[1] for p in prices]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o', linestyle='-', color='teal')
    plt.title(f"{coin_id.capitalize()} - Price Trend (Last 30 Days)")
    plt.xlabel('Date')
    plt.ylabel('Price(USD)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


symbol = input("Enter coin (e.g., btc, eth): ").lower()
coin_id = get_coin_id(symbol)
if coin_id is None:
    print("❌ Invalid coin symbol.")
    exit()
print(f"📊Fetching price history for {coin_id}...")
price_history = fetch_price_history(coin_id)
plot_price_chart(price_history, coin_id)


# commit message:
add plot_price_chart.py for price trend visualization (Day 30)

