import sys
import math
import heapq
import collections
import itertools
import bisect

h,w = map(int,input().split())
bmi = (10000*w) // (h*h)

print(f"{bmi}")
if (bmi>=25):
    print("Obesity")