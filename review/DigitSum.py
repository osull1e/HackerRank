#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    """
    So this works for all cases but is not recursive. 
    I dont like that I cant solve this recursively 
    becuase of a time out error
    """
    ###################################
    x = (int(n)*k)
    y = x % 9
    print(y if y else 9)
    if y > 0:
        return y
    else:
        return 9
    ##################################



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
