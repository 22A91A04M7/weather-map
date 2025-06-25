import json
import ssl
import os
import time
import random
import paho.mqtt.client as mqtt
from datetime import datetime

# Simulated weather data for multiple Indian states (using major cities)
weather_data_list = [
    {"city": "Mumbai", "temperature": random.randint(30, 36), "humidity": random.randint(60, 80), "weather": "humid"},
    {"city": "Delhi", "temperature": random.randint(35, 43), "humidity": random.randint(20, 40), "weather": "hot"},
    {"city": "Chennai", "temperature": random.randint(32, 38), "humidity": random.randint(65, 85), "weather": "sunny"},
    {"city": "Kolkata", "temperature": random.randint(31, 37), "humidity": random.randint(70, 90), "weather": "cloudy"},
    {"city": "Bengaluru", "temperature": random.randint(25, 30), "humidity": random.randint(50, 70), "weather": "pleasant"},
    {"city": "Hyderabad", "temperature": random.randint(30, 38), "humidity": random.randint(40, 60), "weather": "dry"},
    {"city": "Ahmedabad", "temperature": random.randint(34, 42), "humidity": random.randint(25, 45), "weather": "hot"},
    {"city": "Jaipur", "temperature": random.randint(36, 44), "humidity": random.randint(20, 35), "weather": "sunny"},
    {"city": "Pune", "temperature": random.randint(28, 34), "humidity": random.randint(40, 60), "weather": "cloudy"},
    {"city": "Lucknow", "temperature": random.randint(33, 41), "humidity": random.randint(30, 50), "weather": "hazy"},
]

# AWS IoT config
ENDPOINT = "a14oe8h5jezvxs-ats.iot.us-west-1.amazonaws.com"
PORT = 8883
CA_FILE = r"C:\Users\K.HARINI\project\AmazonRootCA1.pem"
CERT_FILE = r"C:\Users\K.HARINI\project\3f327362443ffa458216234d2863e6c5d57d27b2a62c144a7eabf51a4afb44b1-certificate.pem.crt"
KEY_FILE = r"C:\Users\K.HARINI\project\3f327362443ffa458216234d2863e6c5d57d27b2a62c144a7eabf51a4afb44b1-private.pem.key"

# Verify files exist
for file in [CA_FILE, CERT_FILE, KEY_FILE]:
    if not os.path.isfile(file):
        raise FileNotFoundError(f"❌ Missing file: {file}")
    else:
        print(f"✅ Found: {file}")

# MQTT Setup
client = mqtt.Client(protocol=mqtt.MQTTv311)
client.tls_set(ca_certs=CA_FILE, certfile=CERT_FILE, keyfile=KEY_FILE, tls_version=ssl.PROTOCOL_TLSv1_2)
client.connect(ENDPOINT, PORT)

# Publish weather data for each state
topic = "weather/data"
for entry in weather_data_list:
    entry["timestamp"] = datetime.utcnow().isoformat()
    client.publish(topic, json.dumps(entry))
    print(f"📤 Published weather for {entry['city']}: {entry}")
    time.sleep(1)  # Optional: short delay between messages
