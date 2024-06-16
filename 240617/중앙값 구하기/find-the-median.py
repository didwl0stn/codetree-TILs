a,b,c = map(int,input().split())

if ((a>b and a<c) or (a<b and a>c)):
    print(f"{a}") 
if ((b>a and b<c) or (b<a and b>c)):
    print(f"{b}") 
if ((c>b and c<a) or (c<b and c>a)):
    print(f"{c}")