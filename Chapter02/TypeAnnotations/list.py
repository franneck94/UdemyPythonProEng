def append_list(
    lst: list[float] | list[int],
    val: float | int,
) -> None:
    lst.append(val)  # type: ignore


def main() -> None:
    lst = [1, 2, 3]
    append_list(lst, 4)


if __name__ == "__main__":
    main()
