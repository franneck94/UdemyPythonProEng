from typing import NamedTuple
from typing import TypedDict


class User(NamedTuple):
    name: str
    age: int


# total=False: if not all attrs have to be set
class Point2D(TypedDict, total=False):
    x: int
    y: int
    label: str | int


def main() -> None:
    user1 = User("Jan", 29)
    print(user1)
    # user1.age = 12

    a: Point2D = {"x": 1, "y": 2, "label": "good"}  # OK
    print(a)

    b: Point2D = {"x": 1, "y": 2, "label": 2}  # OK
    print(b)

    c: Point2D = {"x": 0, "label": "bad"}  # Fails type check
    print(c)

    print(c.keys(), c.values(), c.items())


if __name__ == "__main__":
    main()
