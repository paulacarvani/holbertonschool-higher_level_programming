#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    total = 0
    for i in range(1, num):
        total += int(argv[i])
    print("{}".format(total))
