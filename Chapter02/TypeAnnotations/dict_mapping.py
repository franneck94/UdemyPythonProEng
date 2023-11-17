from __future__ import annotations

from collections.abc import Mapping


def iterate_over_dict(
    my_dict: Mapping[str, int | float],
) -> Mapping[str, int | float]:
    for key, val in my_dict.items():
        print(key, val)
    return my_dict


def main() -> None:
    # values = [1, 2, 3]
    # expand_ratio = 2

    my_dict = {"Jan": 26, "Peter": 32}
    iterate_over_dict(my_dict)


if __name__ == "__main__":
    main()
