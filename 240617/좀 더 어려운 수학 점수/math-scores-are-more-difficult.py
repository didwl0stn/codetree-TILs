a_m,a_e,b_m,b_e = map(int, input().split() + input().split())
if (a_m > b_m):
    print('A')
elif (a_m == b_m):
    if (a_e>b_e):
        print('A')
    if (b_e>a_e):
        print('B')
else:
    print('B')