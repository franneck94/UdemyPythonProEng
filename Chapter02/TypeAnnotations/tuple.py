def print_3d_tuple(
    tpl: tuple[int | float, bool, str],
) -> None:
    for val in tpl:
        print(val)


def print_nd_int_tuple(
    tpl: tuple[int, ...],
) -> None:
    for val in tpl:
        print(val)


def main() -> None:
    tpl = (1, True, "")
    print_3d_tuple(tpl)

    tpl2 = (1.0, True, "")
    print_3d_tuple(tpl2)

    # tpl3 = (1, True)
    # print_3d_tuple(tpl3)

    tpl4 = (1, 2, 3)
    print_nd_int_tuple(tpl4)

    tpl5 = (1, 2)
    print_nd_int_tuple(tpl5)


if __name__ == "__main__":
    main()
