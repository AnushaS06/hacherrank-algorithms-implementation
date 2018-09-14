#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    result=0
    bMax=0
    max1=0
    for i in word:
        j=ord(i)
        j -= 97
        max1=h[j]
        if(max1>bMax):
            result=max1
            bMax=max1
        
    return(len(word)*result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
