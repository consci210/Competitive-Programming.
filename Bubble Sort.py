#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    totalswap = 0 
    for i in range (n-1):
        for j in range (i+1 ,n):
            if a[i] > a[j]:
                a[i],a[j]= a[j] , a[i]
                totalswap+=1
    
    print ("Array is sorted in" , totalswap , "swaps." )    
    print("First Element:" , a[0])
    print("Last Element:", a[-1])
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
