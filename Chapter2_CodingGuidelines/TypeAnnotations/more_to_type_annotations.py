from __future__ import annotations

from typing import Dict
from typing import Iterable
from typing import List
from typing import NewType
from typing import Tuple
from typing import TypeVar
from typing import Union


AllowedContainers = Union[Dict, List]

Name = NewType('Name', str)
UserId_NT = NewType('UserId_NT', str)
UserId_TV = TypeVar('UserId_TV', str, int)

T = TypeVar('T', int, float, complex)
Vec = Iterable[Tuple[T, T]]


def print_sequence_values(sequence: AllowedContainers):
    for val in sequence:
        print(val)


def print_user_id1(users: Dict, user_id: UserId_NT) -> Name:
    return users[user_id] # users.get(user_id)


def print_user_id2(users: Dict, user_id: UserId_TV) -> Name:
    return users[user_id]


def inner_product(v: Vec[T]) -> T:
    return sum(x * y for x, y in v)


def main():
    l1 = [1, 2, 3]
    print_sequence_values(l1)
    d1 = {'a': 1, 'b': 2}
    print_sequence_values(d1)
    t1 = (1, 2, 3)
    print_sequence_values(t1)

    users = {'1234': 'jan'}
    u1 = '1234'
    print_user_id1(users, u1)
    # u2 = 1234
    # print_user_id1(users, u2)
    # u3 = []
    # print_user_id1(users, u3)

    v1 = [[1, 1],
          [2, 2]]
    print(inner_product(v1))


if __name__ == '__main__':
    main()
