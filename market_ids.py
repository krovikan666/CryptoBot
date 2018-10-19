from coinmarketcap import Market

market = Market()

coin_to_id = {}


def setup_ids():
    listing = market.listings()
    for coin in listing['data']:
        coin_to_id[coin['symbol'].upper()] = coin['id']

setup_ids()