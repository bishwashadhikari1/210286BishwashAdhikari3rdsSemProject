from cgitb import text
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from django.contrib.auth.models import User
from core.core import session
from helpers import websocketcall
from preferances.models import Preferances

list_of_tickerss = ['DGBUSDT', '1INCHUSDT','OPUSDT', 'DEFIUSDT', 'ANKRUSDT', 'KNCUSDT', 'BTCDOMUSDT', 'HOTUSDT', 'ZILUSDT', 'LTCUSDT', 'BATUSDT', 
'REEFUSDT', 'ONTUSDT', 'TRBUSDT', 'BELUSDT', 'GMTUSDT', 'ATOMUSDT', 'RENUSDT', 'ADAUSDT', 'LRCUSDT', 'DOGEUSDT', 'SOLUSDT', 'DOTUSDT', 'NKNUSDT', 'STMXUSDT', 'XEMUSDT',
'BNXUSDT', 'DUSKUSDT', 'ICXUSDT', 'SUSHIUSDT', 'DASHUSDT', 'IOTAUSDT', 'IOSTUSDT', 'MKRUSDT', 'WAVESUSDT', 'TLMUSDT', 'CRVUSDT', 'EOSUSDT', 
'DARUSDT', 'KLAYUSDT', 'NEARUSDT', 'ZENUSDT', 'LINKUSDT', 'WOOUSDT', 'FLOWUSDT', 'UNFIUSDT', 'BANDUSDT', 'ANTUSDT', 'TRXUSDT', 'DENTUSDT', 
'RSRUSDT', 'EGLDUSDT', 'GALUSDT', 'C98USDT', 'SANDUSDT', 'ALPHAUSDT', 'MANAUSDT', 'GTCUSDT', 'MATICUSDT', 'XMRUSDT', 'ALICEUSDT',
'OMGUSDT', 'IOTXUSDT', 'ROSEUSDT', 'KAVAUSDT', 'CELOUSDT', 'BTCUSDT', 'AAVEUSDT', 'ONEUSDT', 'ALGOUSDT', 'COMPUSDT', 'YFIUSDT', 'XRPUSDT', 'GRTUSDT',
'BNBUSDT','ARPAUSDT', 'RVNUSDT','ATAUSDT', 'VETUSDT', 'SXPUSDT', 'CHRUSDT', 'ZRXUSDT', 'IMXUSDT', 'LPTUSDT', 'DYDXUSDT',
'BTSUSDT', 'ARUSDT', 'MASKUSDT', 'LITUSDT', 'CTSIUSDT', 'SKLUSDT', '1000XECUSDT', 'MTLUSDT', 'BLZUSDT','HBARUSDT', 'COTIUSDT', 'KSMUSDT',
'PEOPLEUSDT', 'HNTUSDT','API3USDT','QTUMUSDT', 'BAKEUSDT', 'FILUSDT', 'OCEANUSDT', 'FTMUSDT', 'NEOUSDT', 'SNXUSDT', 'RLCUSDT', 
'AUDIOUSDT', 'THETAUSDT','CVCUSDT', 'CELRUSDT', 'STORJUSDT', 'FLMUSDT', 'APEUSDT', 'ETHUSDT', 'ZECUSDT', 'SFPUSDT', 'UNIUSDT', 'ENJUSDT', 'GALAUSDT', 
'ETCUSDT', 'CTKUSDT', 'XTZUSDT', 'FTTUSDT', 'SCUSDT', '1000SHIBUSDT', 'RAYUSDT', 'RUNEUSDT', 'XLMUSDT', 'ENSUSDT', 'JASMYUSDT', 'SRMUSDT', 'LINAUSDT', 
'CHZUSDT','BALUSDT', 'OGNUSDT', 'AXSUSDT', 'AVAXUSDT', 'TOMOUSDT', 'BCHUSDT']
class GraphConsumer(WebsocketConsumer):
    def connect(self):

        self.group_name = self.scope['url_route']['kwargs']['groupkoname']

        print(self.group_name)
        userr = User.objects.get(username = self.group_name)
        print(userr.first_name)
        print(userr.last_name)
        binance_client = session(userr.first_name, userr.last_name)
        pref = Preferances.objects.get(user_id = userr.id)
        self.accept()

        print(pref.risk, pref.positionsize,pref.strategy, pref.timeframe,pref.rrratio)
        for i in range(1000):
            diction = websocketcall.startbot(risk_percentage=pref.risk, trade_size=pref.positionsize,strategy = pref.strategy, timeframe=pref.timeframe,rr =pref.rrratio, list_of_tickers=list_of_tickerss[0:pref.noticker], session=binance_client)
            print(diction['pnl'])
            self.send(json.dumps(diction))    
        print("#######CONNECTED############")

    def disconnect(self, close_code):
        self.channel_layer.group_discard(self.channel_name, 'render_updates_group')
        print("DISCONNECED CODE: ", close_code)

    def receive(self, text_data=None, bytes_data=None):

        self.send(text_data=text_data)
