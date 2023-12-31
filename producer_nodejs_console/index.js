const { Kafka } = require("kafkajs");

const kafka = new Kafka({
  brokers: ["localhost:9093"],
});

const producer = kafka.producer();
await producer.connect();

//////////////////////////////////////////
await producer.send({
  topic: "topic_1",
  messages: [{ value: "showmethemoney" }],
});
