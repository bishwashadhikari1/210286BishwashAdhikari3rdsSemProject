from django.urls import path
from .consumer import GraphConsumer
ws_urlpatterns = [
    path('dashboard/',GraphConsumer.as_asgi())
]