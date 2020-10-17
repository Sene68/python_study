# You are given a string S.
# Your task is to find out if the string S contains:
# alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    s = 'qA2'
    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False
    for ch in s:
        if ch.isalnum():
            isalnum = True
        if ch.isalpha():
            isalpha = True
        if ch.isdigit():
            isdigit = True
        if ch.islower():
            islower = True
        if ch.isupper():
            isupper = True

    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)