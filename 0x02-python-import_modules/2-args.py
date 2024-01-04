#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} arguments:".format(len(sys.argv) - 1))
    for count, arg in enumerate(sys.argv):
        if count != 0:
            print("{}: {}".format(count, arg))
