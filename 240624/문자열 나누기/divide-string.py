n=int(input())
arr=input().split()
temp="".join(arr)
for i in range(len(temp)//5+1):
    print(temp[5*i:(i+1)*5])