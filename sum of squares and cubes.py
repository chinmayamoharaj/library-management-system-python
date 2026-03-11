n=int(input("Enter a number: "))
s=0
ss=0
sc=0
i=1
if n<=0:
    print("Please enter a positive integer")
else:
    print("="*50)
    print("Natural nums\t Squares\t Cubes")
    print("="*50)
    while i<=n:
        print("{}\t\t\t\t {}\t\t\t  {}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        sc=sc+i**3
        i=i+1
    print("="*50)
    print("{}\t\t\t\t {}\t\t\t {}".format(s,ss,sc))
