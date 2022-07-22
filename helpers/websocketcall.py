
import datetime
import math
import websocket, json, time
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



def stopbot(session):   
    open_symbols_list = []
    a = session.futures_position_information()
    for b in a:
        position=[]
        if float(b['positionAmt']) !=0.0:  
            sym = b['symbol']
            session.futures_cancel_all_open_orders(symbol = sym)


            position = [b['symbol'], b['positionSide'], b['positionAmt'], b['markPrice']]
            open_symbols_list.append(position)


    for position in open_symbols_list:
        if position[1]=='SHORT':
            side='BUY'
            pSide='LONG'
        else:
            side='SELL'
            pSide='SHORT'
        try:
            print(session.futures_create_order(
            symbol=position[0],
            side='BUY',
            positionSide='SHORT',
            type='STOP_MARKET',
            quantity=abs(float(position[2])),
            closePosition = True,
            timeInForce= 'GTC',
            stopPrice=float("{:.4}".format(position[3])),

        ))
        except:
            try:
                print(session.futures_create_order(
                symbol=position[0],
                side='BUY',
                positionSide='SHORT',
                type='TAKE_PROFIT_MARKET',
                quantity=abs(float(position[2])),
                closePosition = True,
                timeInForce= 'GTC',
                stopPrice=float("{:.4}".format(position[3])),

                ))
            except:
                print('failed to close')
