import multiprocessing
import os

import kombu
from kombu.pools import connections

# logger = multiprocessing.log_to_stderr()
# logger.setLevel(multiprocessing.SUBDEBUG)

connection = kombu.Connection('amqp://guest:guest@localhost//')
con_pool = connections[connection]


parent = os.getpid()

messages = set()


def p(_):
    with con_pool.acquire() as c:
        queue = c.SimpleQueue('messaging')

        s = "{} - {}: Starting loop".format(parent, os.getpid())
        print(s)
        queue.put(s)
        messages.add(s)

        for i in range(4):
            s = "{} - {}: {}".format(parent, os.getpid(), i)
            print(s)
            queue.put(s)
            messages.add(s)

        s = "{} - {}: Ending loop".format(parent, os.getpid())
        print(s)
        queue.put(s)
        messages.add(s)

        queue.close()


pool = multiprocessing.Pool(16)

r = pool.imap_unordered(p, range(64))

for i in r:
    pass

print(len(messages))

pool.terminate()
