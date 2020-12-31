import logging
import time
from pathlib import Path


# DEBUG: Detailed debug information
# INFO: Things working as intended
# WARNING: Something unexpected happened
# ERROR: The software cannot perform some function
# CRITICAL: Program crashes for example

# Setup the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Formatter, FileHandler
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(funcName)s:%(message)s')
filepath = Path(__file__).parent.joinpath('log_standard.log')
file_handler = logging.FileHandler(filepath)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def divide_integers(a: int, b: int) -> float:
    try:
        logger.debug('a={}, b={}'.format(a, b))
        result = a / b
        return result
    except Exception as e:
        logger.exception('Exception was raised: {}'.format(e))


def main():
    for _ in range(3):
        print(divide_integers(10, 0))


if __name__ == '__main__':
    main()
