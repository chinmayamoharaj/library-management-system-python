n=int(input("enter the number : "))
sum=0
if n<=0:
    print("enter the number greater than 0")
else:
    for i in range (1,n):
       if n%i==0:
           sum=sum+i
    if(n==sum):
        print("{} is a perfect number".format(n))
    else:
        print("{} is not a perfect number".format(n))
