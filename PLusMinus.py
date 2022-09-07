#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pCounter=0
    nCounter=0
    zCounter=0
    for i in range(len(arr)):
        if(arr[i]>0):
            pCounter+=1
        elif(arr[i]==0):
            zCounter+=1
        else:
            nCounter+=1
    print("{:.6f}".format(pCounter/len(arr)))
    print("{:.6f}".format(nCounter/len(arr)))
    print("{:.6f}".format(zCounter/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
    