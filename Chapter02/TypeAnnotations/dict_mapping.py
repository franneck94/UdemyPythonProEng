from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from collections.abc import Mapping


def iterate_over_dict(
    my_dict: dict[str, int],
) -> dict[str, int]:
    for key, val in my_dict.items():
        print(key, val)
    return my_dict


def iterate_over_mapping(
    my_dict: Mapping[str, int],
) -> Mapping[str, int]:
    for key, val in my_dict.items():
        print(key, val)
    return my_dict


def main() -> None:
    my_dict = {"Jan": 26, "Peter": 32}
    iterate_over_dict(my_dict)

    my_dict = {"Jan": 26, "Peter": 32}
    iterate_over_mapping(my_dict)


if __name__ == "__main__":
    main()
