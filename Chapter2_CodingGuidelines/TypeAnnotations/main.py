'''Test code.
'''
from vector_type_annotations import Vector2D


def print_value(val: str):
    print(val)


def main():
    v1 = Vector2D(2, 'hallo')
    v1 * 'bye'


if __name__ == '__main__':
    main()
