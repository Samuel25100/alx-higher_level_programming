#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chk = 0
    indent = [".", ":", "?"]
    for i in text:
        if chk == 0:
            if i == ' ':
                continue
            else:
                chk = 1
        if chk == 1:
            if i in indent:
                print(i)
                print()
                chk = 0
            else:
                print(i, end="")
