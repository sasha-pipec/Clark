from django.urls import path
from websocket.consumers import MessageWSConsumer

ws_urlpatterns = [
    path('ws/chat/<str:id>', MessageWSConsumer.as_asgi())
]
