#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    lis_name = dir(hidden_4)

    for i in lis_name:
        if i[:2] != '__':
            print(i)
