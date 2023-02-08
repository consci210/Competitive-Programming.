#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    i = n-1
    check_num = arr[-1]
    while arr[i-1] > check_num and i > 0  :  
        arr[i] = arr[i-1]
        checker = arr[i]
        print (*arr)
        i-=1
    arr[i] = check_num 
    print(*arr) 
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
