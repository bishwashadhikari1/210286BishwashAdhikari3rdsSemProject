import os, sqlite3
def rebase(session):
    os.remove('orders.db')
    db = sqlite3.connect('orders.db')
    c = db.cursor()
    c.execute("""
        CREATE TABLE current_orders(
            one string,
            two string,
            three string,
            ticker string
        )
    """) 
    db.commit()
    db.close()

def store_orders(current_orders, tick, session):
    db = sqlite3.connect('orders.db')
    c = db.cursor()
    try:
        c.execute(
        "INSERT INTO current_orders VALUES(:one, :two, :three, :ticker)", {
            "one": current_orders[0],
            "two": current_orders[1],
            "three": current_orders[2],
            "ticker": tick
        }
        )
    except:
        pass
    db.commit()
    db.close()