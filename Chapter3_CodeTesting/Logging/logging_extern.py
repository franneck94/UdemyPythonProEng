# pip install loguru
# Github: https://github.com/Delgan/loguru
from pathlib import Path

from loguru import logger


# DEBUG: Detailed debug information
# INFO: Things working as intended
# WARNING: Something unexpected happened
# ERROR: The software cannot perform some function
# CRITICAL: Program crashes for example

# Setup the logger
filepath = Path(__file__).parent.joinpath('log_loguru.log')
logger.add(filepath, rotation='1 Week')


@logger.catch
def divide_integers(a: int, b: int) -> float:
    logger.debug('a={}, b={}'.format(a, b))
    result = a / b
    return result


def main():
    for _ in range(3):
        print(divide_integers(10, 0))


if __name__ == '__main__':
    main()
