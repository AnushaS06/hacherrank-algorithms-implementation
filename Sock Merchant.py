#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    mylist = list(set(ar))
    cou=0
    for i in mylist:
        print(ar.count(i),i)
        if(ar.count(i) != 1):
            cou += int(ar.count(i)/2)
    return cou
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
