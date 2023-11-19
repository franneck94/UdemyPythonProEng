from typing import Union


def function1(param: Union[int, float]) -> None:
    print(param)


def function2(param: int | float | list) -> None:
    print(param)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
