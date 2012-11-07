import multiprocessing
import os

import kombu

logger = multiprocessing.log_to_stderr()
logger.setLevel(multiprocessing.SUBDEBUG)

connection = kombu.Connection('amqp://guest:guest@localhost//')
queue = connection.SimpleQueue('messaging')

parent = os.getpid()


def p(_):
    s = "{} - {}: Starting loop".format(parent, os.getpid())
    print(s)
    queue.put(s)

    for i in range(4):
        s = "{} - {}: {}".format(parent, os.getpid(), i)
        print(s)
        queue.put(s)

    s = "{} - {}: Ending loop".format(parent, os.getpid())
    print(s)
    queue.put(s)


pool = multiprocessing.Pool(2)

r = pool.imap_unordered(p, range(4))

for i in r:
    pass

pool.terminate()
queue.close()
