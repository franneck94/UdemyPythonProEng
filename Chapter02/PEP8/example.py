import os  # noqa: F401
import sys  # noqa: F401
from typing import Any

import pylint  # noqa: F401
import tensorflow as tf

from .my_lib import print_hello


def my_function_with_many_params(  # noqa: PLR0913, PLR0917
    param1: int,  # noqa: ARG001
    param2: tf.keras.optimizer.Optimzer,  # noqa: ARG001
    param3: tf.keras.optimizer.Optimzer,  # noqa: ARG001
    param4: tf.keras.optimizer.Optimzer,  # noqa: ARG001
    param5: float,  # noqa: ARG001
    param6: Any,  # noqa: ARG001
    param7: Any,  # noqa: ARG001
    param8: Any,  # noqa: ARG001
    param9: Any,  # noqa: ARG001
) -> str:
    return "Hello World!"


def main() -> None:
    # user1 = "Jan"
    # user2 = "Max"
    # user3 = "Marcus"

    # my_list = [user1, user2, user3]

    print_hello()


if __name__ == "__main__":
    main()
