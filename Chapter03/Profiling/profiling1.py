"""Test code.
"""
import cProfile
import io
import pstats
import random
from functools import wraps
from pathlib import Path
from typing import Any, Callable

from vector import Vector2D


FILE_PATH = Path(__file__).parent.joinpath("profiling_stats.prof")


def profile(fn: Callable) -> Callable:
    @wraps(fn)
    def profiler(*args: Any, **kwargs: Any) -> Any:
        profiler = cProfile.Profile()
        profiler.enable()
        fn_result = fn(*args, **kwargs)
        profiler.disable()
        stream = io.StringIO()
        stats = pstats.Stats(profiler, stream=stream)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        print(stream.getvalue())
        stats.dump_stats(filename=FILE_PATH)
        return fn_result

    return profiler


@profile
def test_addition_own_implementation() -> None:
    for _ in range(100_000):
        v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        v2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        c3 = v1 + v2  # noqa


def main() -> None:
    test_addition_own_implementation()


if __name__ == "__main__":
    main()
