from functools import reduce
Num=eval(input("Enter the Number:"))
Even=list(filter(lambda N:N%2==0,Num))
Double=(lambda N:N*2,Num)
Add=reduce(lambda a,b:a+b,Num)
print(Add)
