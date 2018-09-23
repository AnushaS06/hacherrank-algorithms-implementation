#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    x=[]
    for j in arr:
        indices = [i for i, x in enumerate(arr) if x == j]
        x.append(len(indices))
    a=x.index(max(x))
    print(a)
    
    count = 0
    for i in arr:
        if(i != arr[a]):
            count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
