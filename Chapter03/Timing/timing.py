'''Test code.
'''
import sys
from timeit import Timer

import numpy as np


NUM_RUNS = 3


def test_addition_standard_bib() -> None:
    code_str = '''
v1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
v2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
v3 = v1 + v2
'''
    import_str = '''
import random
from vector import Vector2D
'''
    timer = Timer(code_str, setup=import_str)
    times = timer.repeat(repeat=NUM_RUNS, number=1)
    times = [t * 1_000_000_000.0 for t in times]
    mean_time = np.mean(times)
    print(f'Times: {times}, Mean computation time: {mean_time}')


def main() -> int:
    print('Standard lib timer implementation: ')
    test_addition_standard_bib()
    return sys.exit(0)


if __name__ == '__main__':
    main()
