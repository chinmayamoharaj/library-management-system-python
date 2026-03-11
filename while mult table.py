n=int(input("enter a number : "))
i=1
if n<=0:
    print("Please enter a positive integer")
else:
    while i<11:
        print("{} x {} = {}".format(n,i,n*i))
        i += 1
    print("="*50)
    print("The execution is completed")