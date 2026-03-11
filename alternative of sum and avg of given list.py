n=int(input("How many numbers you want to print? "))
lists=[]
sum=0
if n>0:
    for i in range(1,n+1):
      val=input("Enter {} value:  ".format(i))
      lists.append(val)
      sum += int(val)
print("="*50)
print("The list is :- ",lists)
print("="*50)
print("The sum is :- ",sum)
print("=" * 50)
avg=sum/len(lists)
print("The average is :- ",avg)