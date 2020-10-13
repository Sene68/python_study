# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.
#
# Input Format
#
# The first line contains the first name, and the second line contains the last name.


def print_full_name(first_name, last_name):
    print('Hello '+first_name+' '+last_name+'! You just delved into python.')

if __name__ == '__main__':
    first_name = 'Ross'
    last_name = 'Taylor'
    print_full_name(first_name, last_name)