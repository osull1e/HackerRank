#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    """
    I had a difficult time with this one.
    The first thing I did was take n and repeat it k times
    this works because n is a string type, so it repeats
    itself
    """
    print(type(n))
    print(type(k))
   # print (n)
   # print (k)
    x = (n*k)
    """
    now that we have x repeating, we can sum the digits. 
    however the number may be larger than 10 so we simply
    check, if it is less than 10, we print.
    if it is not then we return x to the new function with only the parameter
    x. we needed two methods for this because superDigit takes two
    and the recursive function only takes one. 
    """
    x = sum(int(digit) for digit in str(x))
    #just checking values as I go
    print (x)
    if x < 10:
        return x
    else:
        return recFunction(x)
    return 0
#This is the function that is actually recursive
def recFunction(x):
    x = sum(int(digit) for digit in str(x))
    if x < 10:
        return x
    else:
        return recFunction(x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
