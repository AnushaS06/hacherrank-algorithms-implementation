#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.replace(" ","")
    x = math.sqrt(len(s))
    y=int(x)
    if (x!=y):
        i1=y
        j1=i1+1
    else:
        i1=y
        j1=i1
    print(len(s),x,i1,j1)
    res = []
    ret =[]
    for i in range(j1):
        res.append(s[i::j1]+" ")
        #res.append(" ")
    return(res)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = (encryption(s))

    fptr.writelines(result)

    fptr.close()
