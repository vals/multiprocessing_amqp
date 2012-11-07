import pika

params = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection()
channel = connection.channel()

name = "messaging"

channel.queue_declare(queue=name, durable=True)


def callback(ch, method, properties, body):
    print(body)

channel.basic_consume(callback, queue=name)

channel.start_consuming()
