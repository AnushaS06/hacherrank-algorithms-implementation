#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    b=set(a)
    b=list(b)
    c=[]
    flag=False
    for i in range(len(b)):
        b[i]=int(b[i])
        x = [j for j, x in enumerate(a) if x == b[i]]
        if(len(x)==2):
            c.append(abs(int(x[0])-int(x[1])))
            flag=True
    if(flag==True):
        return(min(c))
    return(-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
