from confluent_kafka import Consumer, KafkaError

conf = {'bootstrap.servers': 'localhost:9092', 'group.id': 'python-consumer-group', 'auto.offset.reset': 'earliest'}
topic = 'order-topic' # Tên topic trong Kafka

consumer = Consumer(conf)
consumer.subscribe([topic])

running = True
while running:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(f"Consumer error: {msg.error()}")
            break

    print(f"Received message: {msg.value().decode('utf-8')}")

consumer.close()