class CoinModel:
    def __init__(self, coin_data, CONVERT_CURRENCY):
        # name, symbol, price, volume_24, market_cap, CONVERT_CURRENCY
        self.name = coin_data['name']
        self.symbol = coin_data['symbol']
        self.price = coin_data['quote'][CONVERT_CURRENCY]['price']
        self.volume_24 = coin_data['quote'][CONVERT_CURRENCY]['volume_24h']
        self.market_cap = coin_data['quote'][CONVERT_CURRENCY]['market_cap']

    def to_dict(self):
        return {
            'name': self.name
        }
