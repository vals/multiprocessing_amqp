import kombu

connection = kombu.Connection('amqp://guest:guest@localhost//')
queue = connection.SimpleQueue('messaging')

while True:
    try:
        message = queue.get(block=False)

    except Exception:
        pass

    else:
        content = message.payload
        print(content)
        message.ack()

queue.close()
