# websocket/routing.py
from django.urls import re_path
from websocket.consumers import FileProcessorConsumer

websocket_urlpatterns = [
    re_path(r'ws/pdf/$', FileProcessorConsumer.as_asgi()),
]
