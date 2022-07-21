
import datetime
import math
import websocket, json, time
from helpers.dbrebase import rebase
from helpers.placeorder import leverage_change
from helpers.reduction import reduceonly
from helpers.strategies import candleclose_strategy,rsi_strategy

def choose_strategy(time_frame, trade_size, rr, list_of_tickers, strategy, risk_percentage, session):

    if strategy == 'candleclose':
        candleclose_strategy(time_frame,trade_size,rr,list_of_tickers, session)
    elif strategy =='rsi':
        rsi_strategy(time_frame,trade_size,rr,list_of_tickers, risk_percentage, session)

def startbot(timeframe, trade_size,rr,list_of_tickers,strategy, risk_percentage,session):

    upnl = 0
    b = session.futures_position_information()
 
    notion = 0
    timee = 0
    timee = datetime.datetime.now()
    timey = int(timee.strftime("%Y%m%d%H%M%S"))
    for a in b:
        if a['notional'] != "0":
            notion += float(a['notional'])
            upnl += float(a['unRealizedProfit'])

    # print(f'Positions PnL = {upnl}')



    def closed_candle(ws, message):

        json_message = json.loads(message)
        candle = json_message['k']
        closed = candle['x']
        if closed==True:
            print("running orders")
            time.sleep(1)
            choose_strategy(timeframe, trade_size, rr, list_of_tickers,strategy,risk_percentage, session)
        else:
            reduceonly(session=session)
        ws.close()
    # leverage_change(list_of_tickers, session=session)
    # rebase(session=session)
    if timeframe<60:
        interval =str(timeframe)+"m"
    if timeframe>=60 and timeframe<=1440:
        interval = str(math.ceil(timeframe/60))+'h'
    tick = 'btcusdt'
    wws = 'wss://stream.binance.com:9443/ws/'+tick+'@kline_'+interval
    def closed():
        print('connection closed')
    ws = websocket.WebSocketApp(wws,on_message=closed_candle, on_close=closed)
    ws.run_forever()
    return({'pnl':upnl, 'time':timey})
