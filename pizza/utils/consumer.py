import os
import pika
import json

class Consumer:

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.channel = self._init_channel()

    def _init_channel(self):
        connection = pika.BlockingConnection(pika.URLParameters(f'amqp://{self.username}:{self.password}@{self.host}:5672'))
        return connection.channel()

    def _init_queue(self, exchange, queue_name, routing_keys):
        queue = self.channel.queue_declare(queue=queue_name)
        self.channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_keys)
        return queue

    def consume(self, exchange, queue_name, routing_key, callback):
        queue = self._init_queue(
            exchange=exchange,
            queue_name=queue_name,
            routing_keys=routing_key
        )

        self.channel.basic_consume(queue=queue,
                                   on_message_callback=callback
                                   )


consumer = Consumer(
    host=os.environ.get("RABBITMQ_HOST"),
    username=os.environ.get("RABBITMQ_USERNAME"),
    password=os.environ.get("RABBITMQ_PASSWORD")
)
