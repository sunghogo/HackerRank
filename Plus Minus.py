#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    ratios = {'Positive': 0, 'Negative': 0, 'Zero': 0}
    n = len(arr)
    for i in range(n):
        if arr[i] > 0:
            ratios['Positive'] += (1/n)
        elif arr[i] < 0:
            ratios['Negative'] += (1/n)
        else:
            ratios['Zero'] += (1/n)
    for value in ratios.values():
        print(f'{value:.6f}')
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
