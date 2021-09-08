#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_arg = len(sys.argv)
    if total_arg == 1:
        print("0 arguments.")
    elif total_arg == 2:
        print("{} argument:".format(total_arg - 1))
    else:
        print("{} arguments:".format(total_arg - 1))
    for i in range(1, total_arg):
        print("{}: {}".format(i, sys.argv[i]))
