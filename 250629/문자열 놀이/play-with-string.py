s,q = map(str,input().split())

for _ in range(int(q)):
    a,b,c = map(str,input().split())
    
    if a=='1':
        s=list(s)
        b=int(b)
        c=int(c)
        temp=s[b-1]
        s[b-1]=s[c-1]
        s[c-1]=temp
        print("".join(s))
    if a=='2':
        s="".join(s)
        s=s.replace(b,c)
        print(s)
    
        