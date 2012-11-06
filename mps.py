from logbook.queues import RabbitMQSubscriber
from logbook import StderrHandler

std_handler = StderrHandler()

with std_handler:
    subscriber = RabbitMQSubscriber('amqp://guest:guest@localhost//')
    subscriber.dispatch_forever()
