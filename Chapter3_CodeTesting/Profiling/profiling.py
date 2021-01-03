'''Test code.
'''
# pylint: disable=import-error
import cProfile
import io
import pstats
import random
import sys
from functools import wraps

from Chapter3_CodeTesting.Profiling.vector import Vector2D


def profile(fn):
    @wraps(fn)
    def profiler(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        fn_result = fn(*args, **kwargs)
        profiler.disable()
        stream = io.StringIO()
        ps = pstats.Stats(profiler, stream=stream).sort_stats('time')
        ps.print_stats()
        print(stream.getvalue())
        return fn_result
    return profiler


@profile
def test_addition_own_implementation():
    for _ in range(100_000):
        v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        v2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        v3 = v1 + v2  # noqa


def main() -> int:
    test_addition_own_implementation()
    return sys.exit(0)


if __name__ == '__main__':
    main()
