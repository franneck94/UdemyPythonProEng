from my_package.utils.printing import print_hello_world
from my_package.utils.printing import print_name

from my_package import *


def main() -> None:
    print_hello_world()
    print_name("Jan")
    print(__version__)


if __name__ == "__main__":
    main()
