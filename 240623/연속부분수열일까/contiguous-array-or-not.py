n1, n2 = map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

for i in range(len(arr1)-len(arr2)+1):
    if arr2==arr1[i:len(arr2)+i]:
        print('Yes')
        break
    else:
        if (i==len(arr1)-len(arr2)):
            print('No')