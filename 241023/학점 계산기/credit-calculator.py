n = int(input())
arr = list(map(float ,input().split()))

sums = 0;
for i in arr:
    sums+= i

print(f'{sums/n:.1f}')
if (sums/n >= 4.0):
    print('Perfect')
elif (sums/n >= 3.0):
    print('Good')
else:
    print('Poor')