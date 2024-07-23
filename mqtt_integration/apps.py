# mqtt_integration/apps.py
from django.apps import AppConfig
from .mqtt import connect_mqtt

class MqttIntegrationConfig(AppConfig):
    name = 'mqtt_integration'

    def ready(self):
        # Start the MQTT client when Django starts
        connect_mqtt()
