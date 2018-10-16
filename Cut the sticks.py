#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    count = []
    c=0
    bc=0
    for i in range(len(arr)):
        a=min(arr)
        for j in range(len(arr)):
            if(arr[j] != 99999):
                arr[j] -= a
                c += 1
            else:
                bc += 1
            if(arr[j] <= 0):
                arr[j] = 99999
        if(bc != len(arr)):
            count.append(c)
        c=0
        bc=0
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
