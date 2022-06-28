from core import session
from placeorder import order
from dbrebase import store_orders
import pandas as pd
import talib, numpy

from reduction import ticker_in_order

def candleclose_strategy(time_frame,trade_size,rr,list_of_tickers):
    current_orders = []
    tf = str(time_frame) + "m"
    tf2 = str(2*time_frame)+"m"
    for tick in list_of_tickers:
        klines = session.futures_historical_klines(tick, tf, tf2)
        candle = klines[0]
        candle_open = float(candle[1])
        entry = float(candle[4])
        candle_high = float(candle[2])
        candle_low = float(candle[3])
        if candle_open>=entry:
            sidee='SELL'
            diee='BUY'
            pSide='SHORT'
            sll = candle_high
            tpp = entry -rr*(candle_high - entry)
        else:
            sidee='BUY'
            diee='SELL'
            pSide='LONG'
            sll = candle_low
            tpp = entry + rr*(entry - candle_low)

        positionsize=  trade_size / entry
        current_orders = (order(tick=tick, positionsize=positionsize, side = sidee, diee=diee, entry=entry, tp=tpp, sl=sll, pSide = pSide))
        store_orders(current_orders, tick)


def rsi_strategy(time_frame,trade_size,rr,list_of_tickers, risk_percentage):
    current_order=[]
    candle_closed=[]
    tf = str(time_frame) + "m"
    tf2 = str(100*time_frame)+"m"
    period = 14
    if time_frame<16: 
        overbought=80
        oversold=25
    else:
        overbought=70
        oversold=35
    for tick in list_of_tickers:
        klines=session.futures_historical_klines(tick,tf,tf2)
        last_candle = klines[-1]
        entry = last_candle[4]
        position_size= float(trade_size) / float(entry)
        for candle in klines[0:-1]:
            candle_closed.append(float(candle[4]))
        print(candle_closed)
        last_rsi = talib.RSI(numpy.array(candle_closed),period)[-1]
        print(last_rsi)
        if (ticker_in_order(tick)== False):
            if last_rsi > overbought:
                sidee='SELL'
                diee='BUY'
                pSide='SHORT'
                tp = float(entry) *(1-(rr*risk_percentage/100))
                sl = float(entry) *(1+(risk_percentage/100))
                current_orders = order(tick=tick, positionsize=position_size, side = sidee, diee=diee, entry=entry, tp=tp, sl=sl, pSide = pSide)
                store_orders(current_orders, tick)
            elif last_rsi < oversold:
                sidee='BUY'
                diee='SELL'
                pSide='LONG'
                sl = entry *(1-(risk_percentage/100))
                tp = entry *(1+(rr*risk_percentage/100))
                current_orders = order(tick=tick, positionsize=position_size, side = sidee, diee=diee, entry=entry, tp=tp, sl=sl, pSide = pSide)
                store_orders(current_orders, tick)



def bolingerBands_strategy():
    pass



def referencess():
    # df = pd.DataFrame(session.futures_historical_klines(tick, tf,tf2))
    pass

def macd_strategy():
    pass

