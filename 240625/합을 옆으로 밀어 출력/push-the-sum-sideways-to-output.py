n=int(input())
k=0
for _ in range(n):
    k+=int(input())
k = str(k)[1:] + str(k)[0]
print(k)