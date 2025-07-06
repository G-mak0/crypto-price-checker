# coin_mapping.py

coin_map = {
    'btc': 'bitcoin',
    'bitcoin': 'bitcoin',
    'eth': 'ethereum',
    'ethereum': 'ethereum',
    'doge': 'dogecoin',
    'dogecoin': 'dogecoin'
}


def get_coin_id(symbol):
    """
     Convert user input symbol to CoinGecko coin ID.

     Args:
         symbol (str): Coin symbol entered by user (e.g., 'btc', 'eth')

     Returns:
         str or None: CoinGecko ID if found, otherwise None
     """

    return coin_map.get(symbol.lower())



 # Add coin_mapping module for symbol-to-ID conversion

