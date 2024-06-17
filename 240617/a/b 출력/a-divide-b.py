a,b=map(int,input().split())
answer=""
for i in range(21):
    if (i == 1):
        answer+="."
    answer+=str(a//b)
    if (a//b==0):
        a*=10
    else:
        a = (a%b)*10

print(answer)