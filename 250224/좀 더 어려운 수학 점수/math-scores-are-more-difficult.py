a_math, a_eng = map(int,input().split())
b_math, b_eng = map(int,input().split())

if (a_math==b_math):
    if (a_eng>b_eng):
        print('A')
    else:
        print('B')
else:
    if (a_math>b_math):
        print('A')
    else:
        print('B')