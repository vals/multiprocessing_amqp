import multiprocessing
import os

import logbook
from logbook.queues import RabbitMQHandler

log = logbook.Logger(os.getpid())

m_handler = RabbitMQHandler('amqp://guest:guest@localhost//', bubble=True)


def p(_):
    log.info("{}: Starting loop".format(os.getpid()))

    for i in range(4):
        log.info("{}: {}".format(os.getpid(), i))

    log.info("{}: Ending loop".format(os.getpid()))

with m_handler:
    log.info("Start {}".format(os.getpid()))

    pool = multiprocessing.Pool(4)

    r = pool.imap_unordered(p, range(4))

    for i in r:
        pass

    pool.terminate()

    log.info("End {}".format(os.getpid()))
