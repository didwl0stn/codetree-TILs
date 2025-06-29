a=input()
arr=list(a)
arr[1]=arr[-2]='a'
print("".join(arr))