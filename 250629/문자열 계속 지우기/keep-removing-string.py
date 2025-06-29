A = input()
B = input()

# Please write your code here.
while(True):
    if (A.find(B)==-1):
        break
    else:
        temp = A.find(B)
        A = A[:temp] + A[temp+len(B):]
print(A)