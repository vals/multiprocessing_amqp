import multiprocessing
import os

import pika

logger = multiprocessing.log_to_stderr()
logger.setLevel(multiprocessing.SUBDEBUG)

params = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection()
channel = connection.channel()

name = "messaging"

channel.queue_declare(queue=name, durable=True)

parent = os.getpid()


def p(_):
    s = "{} - {}: Starting loop".format(parent, os.getpid())
    print(s)
    channel.basic_publish(exchange=name, routing_key=name, body=s)

    for i in range(4):
        s = "{} - {}: {}".format(parent, os.getpid(), i)
        print(s)
        channel.basic_publish(exchange=name, routing_key=name, body=s)

    s = "{} - {}: Ending loop".format(parent, os.getpid())
    print(s)
    channel.basic_publish(exchange=name, routing_key=name, body=s)

pool = multiprocessing.Pool(1)

r = pool.imap_unordered(p, range(4))

connection.close()
