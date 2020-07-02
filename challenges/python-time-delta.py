'''
Challenge: https://www.hackerrank.com/challenges/python-time-delta/problem

When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
'''

import math
import os
import random
import re
import sys

from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2, fmt):
    return str(int(abs((dt.strptime(t2, fmt) - dt.strptime(t1, fmt)).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    fmt = '%a %d %b %Y %H:%M:%S %z'

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2, fmt)

        fptr.write(delta + '\n')

    fptr.close()