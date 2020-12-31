'''Test code.
'''
import random
import time
from functools import wraps
from timeit import Timer

from vector import Vector2D


def timing(fn):
    @wraps(fn)
    def timer(*args, **kwargs):
        start_time = time.perf_counter()
        fn_result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        time_duration = end_time - start_time
        print('Function {} took: {} s'.format(fn.__name__, time_duration))
        return fn_result
    return timer


@timing
def test_addition_own_implementation():
    for _ in range(100_000):
        v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        v2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        c3 = v1 + v2  # noqa


def test_addition_standard_bib():
    code_str = \
        '''
v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
v2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
c3 = v1 + v2
'''
    import_str = \
        '''
import random
from vector import Vector2D
'''
    timer = Timer(code_str, setup=import_str)
    print('Mean computation time: {}'.format(sum(timer.repeat(repeat=3, number=100_000)) / 3))


def main():
    print('Own timer implementation: ')
    test_addition_own_implementation()
    print('Standard lib timer implementation: ')
    test_addition_standard_bib()


if __name__ == '__main__':
    main()
