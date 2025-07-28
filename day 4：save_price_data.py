import requests
import json
import csv
from datetime import datetime
from Coin_map import coin_map


def get_crypto_price(coin_id='bitcoin', vs_currency='usd'):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {'ids': coin_id, 'vs_currencies': vs_currency}
    response = requests.get(url, params=params)
    data = response.json()
    try:
        return data[coin_id][vs_currency]
    except KeyError:
        return None


def save_to_csv(coin, price):
    filename = "crypto_price_log.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, coin, price])
    print(f"📁 Saved to {filename}")


def save_to_json(coin, price):
    filename = "crypto_price_log.json"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"timestamp": timestamp, "coin": coin, "price": price}

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []

    data.append(entry)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
    print(f"📁 Saved to {filename}")


if __name__ == "__main__":
    user_input = input("Enter the coin symbol (e.g.btc):"). lower().strip()
    if not user_input:
        print("Input can't be empty.")
        exit()
    coin = coin_map.get(user_input, user_input)
    price = get_crypto_price(coin)

    if price is None:
        print("❌ Failed to fetch price. Please check the coin name.")
    else:
        print(f"✅ Current price of {coin.capitalize()}: ${price:,}")
        save_to_csv(coin, price)
        save_to_json(coin, price)
