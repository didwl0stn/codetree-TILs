# n,m = map(int,input().split())
# def lcm(n,m):
#     if n<m:
#         n,m=m,n
#     if m==0:
#         return n
#     if n%m==0:
#         return m
#     else:
#         return lcm(m,n%m)

# print(n*m//lcm(n,m))
import math
n,m = map(int,input().split())
print(math.lcm(n,m))