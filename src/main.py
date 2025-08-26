from math_operations import add
from math_operations import sub

a = int(input("Enter the first number: "))
b = int(input("Enter the 2nd number: "))

f = input("Tell what to preform (add/sub): ")

if f == "add":
    result = add(a,b)
    print(f"result of add is {result}")
else:
    result = sub(a,b)
    print(f"the result of sub is {result}")


