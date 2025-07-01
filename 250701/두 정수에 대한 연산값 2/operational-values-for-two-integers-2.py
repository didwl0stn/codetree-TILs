a, b = map(int, input().split())

# Please write your code here.

def temp(a,b):
    minVal = min(a,b) + 10
    maxVal = max(a,b)*2
    return minVal, maxVal

a,b = temp(a,b)
print(a,b,sep=" ")