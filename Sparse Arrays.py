#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    # Initialize return query count array O(m)
    query_hits = [0] * len(queries)
    
    # Initialize string dict to remove duplicate string values O(n)
    strings_dict = {}
    for string in strings:
        if string in strings_dict:
            strings_dict[string] += 1
        else:
            strings_dict[string] = 1
    
    # Compare queries in string O(m)
    for i, query in enumerate(queries):
        if query in strings_dict:
            query_hits[i] = strings_dict[query]
    return query_hits
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
