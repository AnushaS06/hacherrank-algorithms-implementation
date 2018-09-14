#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    j=0
    a=grades
    for i in a:
        if(i>35):
            j=i+(5-(i%5))
            if((j-i)<3):
                #i=j
                k=a.index(i)
                a[k]=j
    print(a)
    return a
            
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
