import json
import asyncio

from aiokafka import AIOKafkaConsumer


async def consume():
    consumer = AIOKafkaConsumer(
        "topic_1",
        bootstrap_servers="localhost:9093",
        group_id="group-id-2",
    )

    await consumer.start()

    try:
        async for msg in consumer:
            print(msg.value.decode())
    finally:
        await consumer.stop()


asyncio.run(consume())
