def append_list(
    lst: list[int],
    val: int,
) -> None:
    lst.append(val)


def main() -> None:
    lst = [1, 2, 3]
    append_list(lst, 4)

    # lst2 = [1.0, 2.0, 3.0]
    # append_list(lst2, 4)


if __name__ == "__main__":
    main()
