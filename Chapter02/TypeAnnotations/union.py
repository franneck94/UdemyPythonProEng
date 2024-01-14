from typing import Union


def function1(param: Union[int, float]) -> None:  # noqa: PYI041, UP007
    print(param)


def function2(param: int | float | list) -> None:  # noqa: PYI041
    print(param)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
