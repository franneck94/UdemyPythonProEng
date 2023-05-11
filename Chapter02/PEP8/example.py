import os
import sys
import typing

import tensorflow as tf

import pylint

from .my_lib import print_hello


def my_function_with_many_params(
    param1: int,
    param2: tf.keras.optimizer.Optimzer,
    param3: tf.keras.optimizer.Optimzer,
    param4: tf.keras.optimizer.Optimzer,
    param5: float,
    param6,
    param7,
    param8,
    param9,
):
    return "Hello World!"


def main() -> None:
    # user1 = "Jan"
    # user2 = "Max"
    # user3 = "Marcus"

    # my_list = [user1, user2, user3]

    print_hello()


if __name__ == "__main__":
    main()
