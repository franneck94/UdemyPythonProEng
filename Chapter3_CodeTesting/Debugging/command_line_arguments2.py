import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--val1', help='first value (int)', type=int, required=True, dest='val1')
    parser.add_argument('--val2', help='first value (str)', type=str, required=True, dest='val2')
    parser.add_argument('--val3', help='first value (bool)', type=bool, required=True, dest='val3')
    args = parser.parse_args()
    print(args)
    a = args.val1
    b = args.val2
    c = args.val3
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))


if __name__ == '__main__':
    main()
