from random import randint
from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep
from helpers.websocketcall import startbot

from requests import request
from core.core import session
class GraphConsumer(WebsocketConsumer):
    def connect(self, request):
        session(request.user.first_name,request.user.last_name)
        self.accept()
        while True:
            s