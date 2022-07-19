
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from dash.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webot.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})


