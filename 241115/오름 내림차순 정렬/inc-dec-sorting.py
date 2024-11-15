n = int(input())
_list = list(map(int,input().split()))
_list.sort()
for i in _list:
    print(i,end=" ")
print()
_list.sort(reverse=True)
for i in _list:
    print(i,end=" ")