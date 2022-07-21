

def precision_order(tick, positionsize, side, diee, entry, tp, sl, pSide, session):
    actual_order = session.futures_create_order(
        symbol=tick,
        side=side,
        positionSide=pSide,
        quantity=positionsize,
        type='MARKET',
        # timeInForce= 'GTC',
        # price=entry,
        )
    stop_order = session.futures_create_order(
        side=diee,
        positionSide=pSide,
        symbol=tick,
        type='STOP_MARKET',
        timeInForce= 'GTC',
        stopPrice=sl,
        quantity = positionsize
        )
    prof_order = session.futures_create_order(
        side=diee,
        positionSide=pSide,
        symbol=tick,
        type='TAKE_PROFIT_MARKET',
        timeInForce= 'GTC',
        stopPrice=tp,
        quantity = positionsize
        )
    pId=prof_order['clientOrderId']
    sId=stop_order['clientOrderId']
    oId=actual_order['clientOrderId']
    return [pId, sId,oId]

def order(tick, positionsize, side, diee, entry, tp, sl, pSide, session):
    try:
        return precision_order(tick, positionsize, side, diee, entry, tp, sl, pSide, session)
    except:
        try:
            positionsiz= "{:.4f}".format(positionsize)
            positionsize=float(positionsiz)
            tpp= "{:.4f}".format(tp)
            tp=float(tpp)
            sll= "{:.4f}".format(sl)
            sl=float(sll)            
            return precision_order(tick, positionsize, side, diee, entry, tp, sl, pSide, session)
        except:
            try:
                positionsiz= "{:.3f}".format(positionsize)
                positionsize=float(positionsiz)
                tpp= "{:.3f}".format(tp)
                tp=float(tpp)
                sll= "{:.3f}".format(sl)
                sl=float(sll)            
                return precision_order(tick, positionsize, side, diee, entry, tp, sl, pSide, session)
            except:
                try:
                    tpp= "{:.2f}".format(tp)
                    tp=float(tpp)
                    sll= "{:.2f}".format(sl)
                    sl=float(sll) 
                    positionsiz= "{:.2f}".format(positionsize)
                    positionsize=float(positionsiz)
                    return precision_order(tick, positionsize, side, diee, entry, tp, sl, pSide, session)
                except:
                    print('order failed', tick)

def leverage_change(list_of_tickers,session):
    print("CHANGING LEVERAGE...")
    for tick in list_of_tickers:
        try:
            session.futures_change_leverage(symbol=tick, leverage=75)
        except:
            try:
                session.futures_change_leverage(symbol=tick, leverage=50)
            except:
                try:
                    session.futures_change_leverage(symbol=tick, leverage=25)
                except:
                    try:
                        session.futures_change_leverage(symbol=tick, leverage=20)
                    except:
                        pass

    print("LEVERAGE CHANGED SUCCESSFULLY")

