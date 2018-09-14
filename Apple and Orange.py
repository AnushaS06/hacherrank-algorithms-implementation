#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apDist=s-a
    orDist=b-s
    coAp=0
    coOr=0
    for i in apples:
        if(a+i>=s and a+i<=t):
            coAp += 1
    for i in oranges:
        if(b+i>=s and b+i<=t):
            coOr += 1
    print(coAp)
    print(coOr)
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
