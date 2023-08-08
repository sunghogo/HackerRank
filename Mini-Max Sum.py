#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    n = len(arr)
    asc_sorted_arr = sorted(arr)
    min_4 = asc_sorted_arr[0]
    max_4 = asc_sorted_arr[n-1]
    for i in range(1, n-1):
        min_4 += asc_sorted_arr[i]
        max_4 += asc_sorted_arr[i]
    print(min_4, max_4)
            

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
