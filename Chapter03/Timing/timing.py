import random
import time
from collections.abc import Callable
from functools import wraps
from timeit import Timer
from typing import Any

from vector import Vector2D


def timing(fn: Callable) -> Callable:
    @wraps(fn)
    def timer(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        fn_result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        time_duration = end_time - start_time
        print(f"Function {fn.__name__} took {time_duration:.6f}s")
        return fn_result

    return timer


@timing
def test_addition_own_implementation() -> None:
    for _ in range(100_000):
        v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        v2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        r = v1 + v2  # noqa


def test_addition_standard_lib() -> None:
    import_str = """
import random
from vector import Vector2D
"""

    code_str = """
v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
v2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
r = v1 + v2  # noqa
"""

    timer = Timer(code_str, setup=import_str)
    num_runs = 10
    mean_time = sum(timer.repeat(repeat=num_runs, number=100_000)) / num_runs
    print(f"Mean computation time: {mean_time:.6f}s")


def main() -> None:
    test_addition_own_implementation()
    test_addition_standard_lib()


if __name__ == "__main__":
    main()
