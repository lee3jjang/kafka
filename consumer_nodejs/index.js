const { Kafka } = require("kafkajs");

const kafka = new Kafka({
  brokers: ["localhost:9093"],
});

const consumer = kafka.consumer({
  groupId: "group-id-1",
});

const initKafka = async () => {
  await consumer.connect();
  await consumer.subscribe({
    topic: "topic_1",
    fromBeginning: true,
  });
  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      console.log(message.value.toString());
    },
  });
};

initKafka();
