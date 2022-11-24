from my_package.printing import print_hello_world
from my_package.version import __version__


def main() -> None:
    print_hello_world()
    print(__version__)


if __name__ == "__main__":
    main()
