import heapq
import sys
n,m = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))

hq = []

for i in numbers:
    heapq.heappush(hq,-i)

for i in range(m):
    a = heapq.heappop(hq)
    a = -a -1
    heapq.heappush(hq,-a)

print(-hq[0])