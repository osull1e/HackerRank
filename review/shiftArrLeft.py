#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    """
    check the modulo of d to the length. 
    that way we know what to return
    so a[1, 2, 3, 4, 5] d=3
    would be a[d:] + a[:d]
    2->rest of elements and all elements up to d
    [3, 4, 5] + [1, 2]
    """
    d = d % len(a)
    return a[d:] + a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
