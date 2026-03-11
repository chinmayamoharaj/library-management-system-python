n=int(input("enter the number : "))
if n<=0:
    print("the input is invalid")
else:
    if n%2==0:
        n -= 1
    while n>0:
        print(n, end="  ")
        n -= 2


