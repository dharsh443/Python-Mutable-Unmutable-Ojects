Value1=input("Enter the Value !:").split()
Value2=input("Enter the Value 2:").split()
Value1=set(Value1)
Value2=set(Value2)
Output=Value2.difference(Value1)
print(Output)
