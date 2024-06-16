m,f = map(int,input().split())
answer=0
if (m>=90 and f>=90):
    if (f<95):
        answer=50000
    else:
        answer=100000
print(answer)