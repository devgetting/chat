from django.urls import re_path
from .consumers.WebsocketConsumer import WebsocketConsumer

websocket_urlpatterns = [
    re_path(r'ws/websocket/$', WebsocketConsumer.as_asgi())
]