#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    """
    #in arr[i am rows][i am cols]
    print("should be 111",[arr[0][:3]])
    print("should be 010",[arr[1][:3]])
    print("should be 111",[arr[2][:3]])
    #we can simplify
    #also note i decided to work down
    firstArr = arr[0][:3] + arr[1][:3] + arr[2][:3]
    secondArr = arr[3][0:3] + arr[4][:3] + arr[5][0:3]

    thirdtArr = arr[0][4:] + arr[1][4:] + arr[2][4:]
    fourthArr = arr[3][4:] + arr[4][4:] + arr[5][4:]

    #fifthArr = [arr[0][3:] + [arr[1][3:]] + arr[2][3:]]
    #sixthArr = [arr[3][3:] + [arr[4][3:]] + arr[5][3:]]
    #now we should sum
    sumOne = sum(firstArr)
    sumTwo = sum(secondArr)
    sumThr = sum(thirdtArr)
    sumFo = sum(fourthArr)
    #lets check
    print(sumOne, sumTwo, sumThr, sumFo)
    """
    """
    crap, I thought the array could be divided in to 
    four each time. Thats not the case. we need to adjust to 
    scroll through. We schould not save each new array
    just calculate the max value as we go.
    #Testing the sum of the array to check my indexing
    sum = []
    for i in range(0,4):
        for j in range(0,4):
            sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

        
    print(max(sum))
    """
    
    return(max([sum(arr[i][j:j+3] + [arr[i+1][j+1]] + arr[i+2][j:j+3]) for i in range(0,4) for j in range(0,4)]))
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
