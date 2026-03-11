def sum():
    a=int(input("enter 1st number:- "))
    b=int(input("enter 2nd number:- "))
    c=a+b
    return a,b,c

res=sum()
print("-----------------------")
print("{} + {} = {}".format(res[0],res[1],res[2]))

