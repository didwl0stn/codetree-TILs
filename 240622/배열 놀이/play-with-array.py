n,q=map(int,input().split())
arr = list(map(int,input().split()))
while(q>0):
    command = list(input().split())
    if len(command)==2:
        a,elem=command
        if a=='1':
            print(arr[int(elem)-1])
        if a=='2':
            if (int(elem) in arr):
                print(arr.index(int(elem))+1)
            else:
                print('0')
    if len(command)==3:
        a,s,e=command
        for i in arr[int(s)-1:int(e)]:
            print(i,end=" ")
        print("")
    q-=1