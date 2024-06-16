aa,ab = input().split()
ba,bb = input().split()
ca,cb = input().split()

cnt=0

if(aa=='Y' and int(ab)>=37):
    cnt += 1
if(ba=='Y' and int(bb)>=37):
    cnt += 1
if(ca=='Y' and int(cb)>=37):
    cnt += 1

if (cnt>=2):
    print('E')
else:
    print('N')