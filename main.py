import logging
import itertools
import random
import time
import sys


def main():
    # from  the lab
    logging.basicConfig(
        level=logging.DEBUG,  # Set the logging level
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    # create logger
    logger = logging.getLogger()

    # create faked log messages
    levels = [
        logging.INFO,
        logging.DEBUG,
        logging.WARNING,
    ]
    messages = [
        "GET /foobar",
        "POST /fake/route",
        "POST /fake/faker/route",
        "POST /fake/faker/fakiest/route",
    ]
    status = [400, 401, 200, 201, 500]
    choices = list(itertools.product(levels, messages, status))

    # actually make a randomized log stream
    while True:
        level, message, status = random.choice(choices)
        logger.log(level, message)
        time.sleep(random.random() * 3)


if __name__ == "__main__":
    main()
