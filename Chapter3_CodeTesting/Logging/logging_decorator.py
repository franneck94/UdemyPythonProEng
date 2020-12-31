import time
from datetime import datetime
from functools import wraps


def log(fn):
    @wraps(fn)
    def logger(*args, **kwargs):
        args_values_types = [(a, type(a)) for a in args]
        kwargs_values_types = [(k, v, type(v)) for k, v in kwargs.items()]
        arguments = args_values_types + kwargs_values_types
        time = datetime.utcnow()
        time = time.strftime('%H:%M:%S')
        try:
            fn_result = fn(*args, **kwargs)
            print('Function {} was called at {} with params {} and returned {}'.format(
                fn.__name__, time, arguments, fn_result))
            return fn_result
        except Exception as e:
            print('Function {} was called at {} with params {} and raised an exception {}'.format(
                fn.__name__, time, arguments, e))
    return logger


@log
def divide_integers(a: int, b: int) -> float:
    result = a / b
    return result


def main():
    for _ in range(10):
        time.sleep(1.5)
        print(divide_integers(10, 0))


if __name__ == '__main__':
    main()
