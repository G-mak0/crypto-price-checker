🧩 Day 4 - Save Crypto Price to CSV & JSON
This module adds the ability to save real-time price data to both .csv and .json formats using the CoinGecko API.

📁 Files
save_price_data.py: Fetches live price and saves it.

coin_map.py: A mapping table to convert common coin symbols (e.g. btc) to full CoinGecko IDs (e.g. bitcoin).

🚀 Features
Takes user input (btc, eth, etc.)

Maps symbol to proper API format using coin_map

Fetches real-time price

Saves data with timestamp to:

price_data.csv

price_data.json

▶️ How to run
bash
Copy
Edit
python save_price_data.py
✅ Example output (CSV):
makefile
Copy
Edit
timestamp,coin,price
2025-07-28T22:45:01,bitcoin,61234.56
