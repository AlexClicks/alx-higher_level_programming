#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    sum1 = 0
    for i in range(1, len(argv)):
        sum1 += int(argv[i])
    print("{:d}".format(sum1))
