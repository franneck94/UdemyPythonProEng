from typing import Any
from typing import Optional


def function1(param: Any) -> None:
    print(param)


def function2(param: Optional[int] = None) -> int:  # noqa: UP007
    if param is None:
        return 0
    return param * 2


def function3(param: int = -1) -> int:
    if param == -1:
        return 0
    return param * 2


def main() -> None:
    function1(1)
    function2()


if __name__ == "__main__":
    main()
