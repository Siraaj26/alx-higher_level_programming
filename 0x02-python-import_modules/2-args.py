#!/usr/bin/python3

if __name__ == "__main__":
    """prints the number of and the list of its arguments"""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count))
    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
