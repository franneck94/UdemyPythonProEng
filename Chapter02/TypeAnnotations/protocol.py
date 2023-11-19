from __future__ import annotations

from typing import Protocol


class SizedProtocol(Protocol):
    def __len__(self) -> int:
        ...


def iterate_over_length(
    obj: SizedProtocol,
) -> None:
    print(len(obj))


def main() -> None:
    values = [1, 2, 3]
    iterate_over_length(values)

    values2 = (1, 2, 3)
    iterate_over_length(values2)

    # values3 = 3
    # iterate_over_length(values3)


if __name__ == "__main__":
    main()
