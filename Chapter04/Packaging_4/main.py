from fastvector.vector import Vector2D
from fastvector.version import __version__


def main() -> None:
    v = Vector2D(1, 1,)
    print(v)
    print(__version__)


if __name__ == "__main__":
    main()
