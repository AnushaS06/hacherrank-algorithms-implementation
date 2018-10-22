#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect


def climbingLeaderboard(scores, alice):
    rank=sorted(set(scores))
    rank_len = len(rank)
    ret = []
    for i in range(len(alice)):
        newRank = bisect(rank, alice[i])
        print(bisect(rank, alice[i]))
        ret.append(rank_len-newRank+1)
    return(ret)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
