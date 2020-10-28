# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.
#
# alison heck => Alison Heck
#
# Given a full name, your task is to capitalize the name appropriately.

#!/bin/python3

import math
import os
import random
import re
import sys

def capitalize(s):
    l = []
    l = s.split(" ")

    for i in range(0, len(l)):
        l[i] = l[i].capitalize()
        x = ' '.join(l)

    return x

if __name__ == '__main__':
    s = 'chris alan'
    result = capitalize(s)
    print(result)