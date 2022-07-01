
import math
import websocket, json, sqlite3, time
from core import session
from dbrebase import rebase
from placeorder import leverage_change
from reduction import reduceonly
from strategies import candleclose_strategy,rsi_strategy

def choose_strategy(time_frame, trade_size, rr, list_of_tickers, strategy, risk_percentage):

    if strategy == 'candleclose':
        candleclose_strategy(time_frame,trade_size,rr,list_of_tickers)
    elif strategy =='rsi':
        rsi_strategy(time_frame,trade_size,rr,list_of_tickers, risk_percentage)




def startbot(timeframe, trade_size,rr,list_of_tickers,strategy, risk_percentage):

    def closed_candle(ws, message):
        json_message = json.loads(message)
        candle = json_message['k']
        closed = candle['x']
        print(closed)
        if closed==True:
            print("running orders")
            time.sleep(1)
            choose_strategy(timeframe, trade_size, rr, list_of_tickers,strategy,risk_percentage)
        else:
            reduceonly()
            print('reducing')

    leverage_change(list_of_tickers)
    rebase()
    if timeframe<60:
        interval =str(timeframe)+"m"
    if timeframe>=60 and timeframe<=1440:
        interval = str(math.ceil(timeframe/60))+'h'
    tick = 'btcusdt'
    wws = 'wss://stream.binance.com:9443/ws/'+tick+'@kline_'+interval

    ws = websocket.WebSocketApp(wws,on_message=closed_candle)
    ws.run_forever()


