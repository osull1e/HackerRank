#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
"""
Keep in mind some things,
we ened to consider corner cases, 
two blocks together should be the total possible 
surface area - 2. 
"""
def surfaceArea(A):
    #print(A)
    #empty later
    test = [[0] * (len(A[0]) + 2)]
    #print(test)

    for row in A:
        #print(test)
        test.append([0] + row + [0])

    test.append([0] * (len(A[0]) + 2))
    print(test)
    #find the bottom and top
    #Keep track of the total surface area
    totArea = len(A) * len(A[0]) * 2
   
    """
    Side area is the difference in sums
    """
    for i in range(1, len(test)):
        for j in range(1, len(test[i])):
            x = abs(test[i][j] - test[i-1][j])
            print("i, j",test[i][j] , i, j)
            print("i-1, j",test[i-1][j], i, j)
            #print(x)
            totArea = totArea + x
            y = abs(test[i][j] - test[i][j-1])
            print("i, j",test[i][j] , i, j)
            print("i, j-1",test[i][j-1], i, j)
            #print(y)
            totArea = totArea + y
    return totArea

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
