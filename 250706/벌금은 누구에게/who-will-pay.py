N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

count=[0] * N
ans=-1
for i in student:   
    count[i-1]+=1
    if (count[i-1]>=K):
        ans=i
        break
print(ans)