arr = [
    input()
    for _ in range(10)
]

c = input()
cnt = 0
for item in arr:
    if (item[-1]==c):
        print(item)
        cnt+=1

if cnt==0:
    print('None')