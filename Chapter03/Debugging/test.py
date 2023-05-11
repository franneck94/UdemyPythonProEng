# pylint: disable=import-error
import sys

from vector import Vector2D


def main() -> int:
    v1 = Vector2D(2, -2)
    print(v1)
    v2 = Vector2D(2, 3)
    print(v2)
    v3 = v1 + v2
    print(v3)
    print('Hello world')

    return sys.exit(0)


if __name__ == '__main__':
    main()
