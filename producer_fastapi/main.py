import json

from fastapi import FastAPI
from aiokafka import AIOKafkaProducer

app = FastAPI()


@app.get("/")
async def index():
    producer = AIOKafkaProducer(
        bootstrap_servers="localhost:9093",
    )

    await producer.start()
    try:
        value_json = json.dumps({"message": "sangjin"}).encode()
        await producer.send_and_wait(
            "topic_1",
            value=value_json,
        )
    finally:
        await producer.stop()
