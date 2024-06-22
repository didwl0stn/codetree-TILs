arr=['L','E','B','R','O','S']
char=input()
if char not in arr:
    print("None")
else:
    for i,value in enumerate(arr):
        if value == char:
            print(i)