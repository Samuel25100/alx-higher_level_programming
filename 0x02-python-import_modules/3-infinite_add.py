#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    if len(sys.argv) < 1:
        print("0")
    else:
        for count, arg in enumerate(sys.argv):
            if count != 0:
                result += int(arg)
        print(result)
