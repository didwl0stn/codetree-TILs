n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def temp(n):
    cnt = 1
    num = max(arr)*cnt
    while(True):
        for i in range(len(arr)):
            if (num%arr[i]!=0):
                cnt+=1
                num = max(arr)*cnt
                break
            if(i==len(arr)-1):
                return num
        
    

print(temp(n))
