import json
import time
import requests
import sseclient

from kafka import KafkaProducer

KAFKA_SERVER = "kafka:9092"
TOPIC = "wikipedia-edits"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

url = "https://stream.wikimedia.org/v2/stream/recentchange"

while True:
    try:
        print("Connecting to Wikipedia stream...")

        response = requests.get(url, stream=True)

        client = sseclient.SSEClient(response)

        for event in client.events():

            if not event.data:
                continue

            data = json.loads(event.data)

            producer.send(TOPIC, value=data)

            print(
                f"Sent: {data.get('title')} by {data.get('user')}"
            )

    except Exception as e:

        print(e)

        print("Retrying in 5 seconds...")

        time.sleep(5)