n=int(input("enter a number : "))
sum=0
i=1
if n<=0:
    print("Please enter a positive integer")
else:
    while i<=n:
       sum += i
       i += 1
    print("The sum of all natural numbers you have entered = {}".format(sum))