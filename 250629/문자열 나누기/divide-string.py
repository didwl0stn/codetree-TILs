n=int(input())
arr=input().split()
for idx,item in enumerate ("".join(arr)):
    print(item,end="")
    if(idx%5==4):
        print()