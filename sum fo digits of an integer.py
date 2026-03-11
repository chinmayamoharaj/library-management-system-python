n=int(input("enter a number of two or more digits : "))
x=str(n)
sum=0
for i in x:
    sum = sum + int(i)
print("The sum of digits {} = {}".format(n,sum))