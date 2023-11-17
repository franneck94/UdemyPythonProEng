from __future__ import annotations

from collections.abc import Callable
from collections.abc import Mapping
from typing import List  # noqa: F401
from typing import Optional
from typing import Union


def foo(param: list[float]) -> None:  # noqa: ARG001
    pass


def expand_list(expander: int, values: list[int]) -> list[int]:
    return expander * values


def print_list(values: list[int]) -> None:
    print(values)


def expand_and_print(
    values: list[int],
    expand_ratio: int,
    expand_fn: Callable[[int, list[int]], list[int]],
    print_fn: Callable[[list[int]], None],
) -> None:
    values = expand_fn(expand_ratio, values)
    print_fn(values)


# Optional[List[int]] <=> Union[List[int], None]
def append_value(value: int, my_list: Optional[list[int]] = None) -> list[int]:
    if my_list:
        my_list.append(value)
    else:
        my_list = [value]
    return my_list


def iterate_over_dict(my_dict: Mapping[str, Union[int, float]]) -> None:
    for key, val in my_dict.items():
        print(key, val)


if __name__ == "__main__":
    values = [1, 2, 3]
    expand_ratio = 2

    expand_and_print(values, expand_ratio, expand_list, print_list)

    my_list = append_value(1)
    print(my_list)
    my_list = append_value(2, my_list)
    print(my_list)
    my_list = append_value(3, my_list)
    print(my_list)

    my_dict = {"Jan": 26, "Peter": 32}
    iterate_over_dict(my_dict)
