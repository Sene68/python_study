# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)


if __name__ == '__main__':
    string  = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    max_width = 4
    result = wrap(string, max_width)
    print(result)