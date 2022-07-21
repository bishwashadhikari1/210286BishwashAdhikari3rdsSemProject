
import sqlite3
def reduceonly(session):
    try:
        current_orders = order_list(session)
        db = sqlite3.connect('orders.db')
        c = db.cursor()
        print(current_orders)
        a = c.execute("SELECT * from current_orders")
        orders = a.fetchall()
        if current_orders==[]:
            c.execute("DELETE * FROM current_orders")
        for order in orders:
            if (order[0] in current_orders) and (order[1] not in current_orders):
                print(order[0])
                session.futures_cancel_order(symbol=order[3], origClientOrderId=order[0])

                try: 
                    session.futures_cancel_order(symbol=order[3], origClientOrderId=order[2])
                except:
                    pass
            if order[1] in current_orders and order[0] not in current_orders:
                session.futures_cancel_order(symbol=order[3], origClientOrderId=order[1])
                try: 
                    session.futures_cancel_order(symbol=order[3], origClientOrderId=order[2])
                except:
                    pass
        db.close()
    except:
        pass

def order_list(session):
    orders_ids = []
    try:
        all_ord = session.futures_get_open_orders()
        for ord in all_ord:
            orders_ids.append(ord['clientOrderId'])
        return orders_ids
    except:
        pass

def ticker_in_order(tick, session):
    orders = session.futures_get_open_orders()
    for order in orders:
        if tick== order['symbol']:
            return True
    return False