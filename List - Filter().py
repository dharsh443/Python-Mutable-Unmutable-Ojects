
def is_even(N):
    return N%2==0
Num=eval(input("Enter the Numbers:"))
Even=list(filter(is_even,Num))

print(Even)
