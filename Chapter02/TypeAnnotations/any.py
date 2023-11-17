from typing import Any


def function(a: Any) -> Any:
    return 2 * a


def main() -> None:
    function(2)
    function(2.0)
    function([])


if __name__ == "__main__":
    main()
