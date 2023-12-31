import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["localhost:9093"],
    value_serializer=lambda v: json.dumps(v).encode(),
)

response = producer.send(topic="topic_1", value={"age": 34}).get()
