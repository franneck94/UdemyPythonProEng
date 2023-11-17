from __future__ import annotations

from collections.abc import Collection  # noqa: F401 # pyright: ignore
from collections.abc import Container  # noqa: F401 # pyright: ignore
from collections.abc import Iterable  # noqa: F401 # pyright: ignore
from collections.abc import MutableSequence  # noqa: F401 # pyright: ignore
from collections.abc import Sequence  # noqa: F401 # pyright: ignore
from collections.abc import Sized  # noqa: F401 # pyright: ignore
from typing import Any
from typing import Protocol


class SizedMutableIterable(Protocol):
    def __len__(self) -> Any:
        ...

    def __getitem__(
        self,
        idx: int,
    ) -> Any:
        ...

    def __setitem__(
        self,
        idx: int,
        val: Any,
    ) -> None:
        ...


def iterate_over_length(
    obj: SizedMutableIterable,
) -> None:
    for i in range(len(obj)):
        obj[i] = i**2
        print(obj[i])


def main() -> None:
    values: list[Any] = [1, 2, 3]
    iterate_over_length(values)  # pyright: ignore


if __name__ == "__main__":
    main()
