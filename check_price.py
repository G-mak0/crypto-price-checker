from Coin_map import get_coin_id
import requests


def get_crypto_price(coin_id='bitcoin', vs_currency='usd'):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': coin_id,
        'vs_currencies': vs_currency
    }
    response = requests.get(url, params=params)
    data = response.json()

    print("DUBUG>>>Raw response:", data)
    try:
        price = data[coin_id][vs_currency]
        return price
    except KeyError:
        return None


symbol = input("Enter the coin symbol (btc / eth / doge): ").lower()
coin = get_coin_id(symbol)

if coin is None:
    print("❌ Unsupported coin symbol. Please enter a valid one.")
    exit()


threshold = float(input("Enter your price alert threshold: "))
price = get_crypto_price(coin)

if coin is None:
    print("❌ Unsupported coin symbol. Please enter a valid one.")
    exit()


if price is None:
    print("❌ could not fetch price. Make sure the coin name is valid.")
else:
    print(f"✅ Current price of {coin.capitalize()}: ${price:,}")

    if price > threshold:
        print("💡 Price is above your threshold. You might consider selling.")
    elif price < threshold:
        print("📉 Price is below your threshold. Might be a good time to buy.")
    else:
        print("⚖️ Price is exactly at your threshold.")
