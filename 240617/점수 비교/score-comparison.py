a_m,a_e = input().split()

b_m,b_e= input().split()
a_m=int(a_m); b_m=int(b_m); a_e=int(a_e); b_e=int(b_e)

if (a_m > b_m and a_e > b_e):
    print(1)
else:
    print(0)