n=int(input("Enter a number: "))
for i in range(2,n):
    if n%i==0:
        print("{} is not a prime number".format(n))
        break
else:
    print("{} is a prime number".format(n))

