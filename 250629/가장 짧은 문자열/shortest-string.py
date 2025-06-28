maxs = -1
mins = 21

for _ in range(3):
    n = input();
    if (len(n)>maxs):
        maxs=len(n)
    if (len(n)<mins):
        mins=len(n)
print(maxs-mins)