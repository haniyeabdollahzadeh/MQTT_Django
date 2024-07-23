# mqtt_integration/urls.py
from django.urls import path
from . import views

mqtt_urlpatterns = [
    path('publish/', views.publish_message_view, name='publish_message'),
    path('subscribe/', views.subscribe_topic_view, name='subscribe_topic'),
    path('messages/', views.display_messages, name='display_messages')
]
