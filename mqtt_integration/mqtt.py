import paho.mqtt.client as mqtt
from .mqtt_settings import MQTT_BROKER, MQTT_PORT

received_messages = []
subscribed_topic = None
subscribed_topics = ['red', 'yellow', 'green']

def on_connect(mqtt_client, userdata, flags, rc):
    global subscribed_topic
    if rc == 0:
        print('Connected successfully')
        #mqtt_client.subscribe('red')
        for topic in subscribed_topics:
            mqtt_client.subscribe(topic)
            subscribed_topic = topic
    else:
        print('Bad connection. Code:', rc)


def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic
    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
    if subscribed_topic == topic:
        received_messages.append({'topic': topic, 'message': payload})
    


mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message



def connect_mqtt():
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()


def publish_message(topic, message):
    mqtt_client.publish(topic, message)


def subscribe_topic(topic):
    mqtt_client.subscribe(topic)

def get_received_messages():
    return received_messages

connect_mqtt()
