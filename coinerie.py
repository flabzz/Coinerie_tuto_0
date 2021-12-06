#pip install pycoingecko

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

from my_coins import my_coins

my_wallet = 0

def get_price(coin):
    price = cg.get_price(ids=[coin], vs_currencies=['usd'])
    return price[coin]["usd"]

###############################################################################
# Exemple :
print(get_price("bitcoin"))
###############################################################################