import paho.mqtt.client as mqtt
from kafka import KafkaProducer
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT"))
MQTT_USER = os.getenv("MQTT_USER")
MQTT_PASS = os.getenv("MQTT_PASS")
MQTT_TOPIC = os.getenv("MQTT_TOPIC")

KAFKA_SERVER = os.getenv("KAFKA_SERVER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")


producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


def on_connect(client, userdata, flags, rc):
    print("Conectado ao HiveMQ com código:", rc)
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    print(f"Mensagem recebida do MQTT: {msg.payload.decode()}")
    producer.send(KAFKA_TOPIC, msg.payload)


client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.tls_set(tls_version=ssl.PROTOCOL_TLS)

client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
