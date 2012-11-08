import multiprocessing
import os

import logbook
from logbook.queues import RabbitMQHandler

log = logbook.Logger(os.getpid())

m_handler = RabbitMQHandler('amqp://guest:guest@localhost//', bubble=True)


def p(_):
    with RabbitMQHandler('amqp://guest:guest@localhost//', bubble=True):
        log.info("{}: Starting loop".format(os.getpid()))

        for i in range(50):
            log.info("{}: {}".format(os.getpid(), i))

        log.info("{}: Ending loop".format(os.getpid()))

with m_handler:

    log.info("1 {}".format(os.getpid()))
    log.info("2 {}".format(os.getpid()))
    log.info("Start {}".format(os.getpid()))

    pool = multiprocessing.Pool(16)
    log.info(None)

    r = pool.imap_unordered(p, range(100))

    for i in r:
        pass

    pool.terminate()

    log.info("Three {}".format(os.getpid()))
    log.info("Two {}".format(os.getpid()))
    log.info("One {}".format(os.getpid()))
    log.info("End {}".format(os.getpid()))
