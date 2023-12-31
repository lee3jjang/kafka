const { Kafka } = require("kafkajs");
const express = require("express");

app = express();

const kafka = new Kafka({
  brokers: ["localhost:9093"],
});

const producer = kafka.producer();
producer.connect();

app.get("/", async (req, res) => {
  await producer.send({
    topic: "topic_1",
    messages: [{ value: "operationcwal" }],
  });
  res.send("producer_express");
});

app.listen(3000);
