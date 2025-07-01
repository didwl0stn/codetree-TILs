A = input()

# Please write your code here.

def temp(string):
    if string==string[::-1]:
        return "Yes"
    else:
        return "No"

print(temp(A))