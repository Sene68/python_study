# Task
# The provided code stub reads two integers,  a and b , from STDIN.
#
# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
#
# No rounding or formatting is necessary.

def print_division(a, b):
    print(a // b)
    print(a / b)

if __name__ == '__main__':
    a = 4
    b = 3
    print_division(a, b)