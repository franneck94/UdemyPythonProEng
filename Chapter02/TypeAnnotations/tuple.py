from typing import Union


def print_3d_tuple(
    tpl: tuple[int, float, str],
) -> None:
    for val in tpl:
        print(val)


def print_nd_int_tuple(
    tpl: tuple[Union[int, float], ...],  # noqa: UP007
) -> None:
    for val in tpl:
        print(val)


def main() -> None:
    tpl1 = (1, 1.0, "1")
    print_3d_tuple(tpl1)
    # tpl2 = (1.0, 1.0, "1")
    # print_3d_tuple(tpl2)

    tpl3 = (1,)
    print_nd_int_tuple(tpl3)
    tpl4 = (1, 2)
    print_nd_int_tuple(tpl4)
    tpl5 = (1.0,)
    print_nd_int_tuple(tpl5)


if __name__ == "__main__":
    main()
