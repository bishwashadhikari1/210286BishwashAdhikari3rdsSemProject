from django.urls import path
from .consumers import GraphConsumer

ws_urlpatterns = [
    path('ws/graph/<str:groupkoname>/', GraphConsumer.as_asgi())
]