# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers i < n , print  i^2.

import math

def print_loops(n):
    for i in range(n):
        print(int(math.pow(i,2)))

if __name__ == '__main__':
    n = 5
    print_loops(n)