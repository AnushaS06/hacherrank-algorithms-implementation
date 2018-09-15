#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    floor=int(5)
    a=0
    a1=0
    for i in range(n):
        floor =((int(floor/2))*3) 
        a=int(floor/3)
        a1+=a
        print(floor,a,a1)
    return(a1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
