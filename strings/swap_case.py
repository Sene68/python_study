# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    swap = []
    for i in s:
        if (i.isupper()):
            swap.append(i.lower())
        else:
            swap.append(i.upper())
    return ''.join(swap)

if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)