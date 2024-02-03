from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from collections.abc import Callable


def print_list(
    values: list[int],
    verbose: bool = False,
) -> None:
    if verbose:
        print(values)


def function(
    values: list[int],
    print_fn: Callable[[list[int], bool], None],
) -> None:
    print_fn(values, True)


def main() -> None:
    values = [1, 2, 3]
    function(values, print_list)


if __name__ == "__main__":
    main()
