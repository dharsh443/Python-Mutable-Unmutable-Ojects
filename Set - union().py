Value1 = input("Enter the Value 1: ").split()
Value2 = input("Enter the Value 2: ").split()


Value1 = set(Value1)
Value2 = set(Value2)

Output = Value1.union(Value2)

print(Output)
