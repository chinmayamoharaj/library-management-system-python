# Find the biggest number of two numbers and check the equality using Ternary operator.

a=int(input("enter first number:- "))
b=int(input("enter second number:- "))
res = a if a>b else b if b>a else "Both values are equal"
print("The biggest number is {}".format(res))

