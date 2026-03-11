n=int(input("How many numbers you want to print? "))
lists=[]
if n>0:
    for i in range(1,n+1):
      val=input("Enter {} value:  ".format(i))
      lists.append(val)
print("="*50)
print("The list is :- ",lists)
