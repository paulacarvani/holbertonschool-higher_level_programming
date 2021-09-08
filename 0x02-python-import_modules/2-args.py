#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_arg = len(sys.argv)
    print("{} arguments:".format(total_arg - 1))
    for i in range(1, total_arg):
        print("{}: {}".format(i, sys.argv[i]))
