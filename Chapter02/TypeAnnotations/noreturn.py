import sys
from typing import NoReturn


def function1() -> None:
    print("Hello World")


def function2() -> NoReturn:
    print("Hello World")
    sys.exit(-1)


def function3() -> NoReturn:
    print("Hello World")
    raise ValueError


def main() -> None:
    function1()
    function2()
    function3()


if __name__ == "__main__":
    main()
