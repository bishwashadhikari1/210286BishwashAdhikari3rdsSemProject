
from binance import Client, BinanceSocketManager

def session(apikey,apisecret):
    return Client(apikey, apisecret)


def bsm(sess):
    return BinanceSocketManager(sess)
