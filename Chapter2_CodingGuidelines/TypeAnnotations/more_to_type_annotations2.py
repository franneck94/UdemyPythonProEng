from __future__ import annotations

from typing import Callable
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Union


def expand_list(expander: int, values: List[int]) -> List[int]:
    return expander * values


def print_list(values: List[int]) -> None:
    print(values)


def expand_and_print(
    values: List[int],
    expand_ratio: int,
    expand_fn: Callable[[int, List[int]], List[int]],
    print_fn: Callable[[List[int]], None]
) -> None:
    values = expand_fn(expand_ratio, values)
    print_fn(values)


# Optional[List[int]] <=> Union[List[int], None]
def append_value(value: int, my_list: Optional[List[int]] = None) -> List[int]:
    if my_list:
        my_list.append(value)
    else:
        my_list = [value]
    return my_list


def iterate_over_dict(my_dict: Mapping[str, Union[int, float]]) -> None:
    for key, val in my_dict.items():
        print(key, val)


if __name__ == '__main__':
    values = [1, 2, 3]
    expand_ratio = 2

    expand_and_print(values, expand_ratio, expand_list, print_list)

    my_list = append_value(1)
    print(my_list)
    my_list = append_value(2, my_list)
    print(my_list)
    my_list = append_value(3, my_list)
    print(my_list)

    my_dict = {'Jan': 26, 'Peter': 32}
    iterate_over_dict(my_dict)
