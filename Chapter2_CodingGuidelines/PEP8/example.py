import sys

import numpy as np
import pandas as pd

from .my_lib import print_hello


def my_function_with_many_params(
    param1,
    param2,
    param3,
    param4,
    param5,
    param6,
    param7,
    param8,
    param9
):
    return "Hello World!"


user1 = "Jan"
user2 = "Max"
user3 = "Marcus"

my_list = [
    user1,
    user2,
    user3
]


if __name__ == "__main__":
    print_hello()
