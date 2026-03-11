print(" Enter the numbers you want to print multiplication tables of those numbers ")
print("="*80)
x=int(input("Enter how many numbers of multiplication tables you want to print: :- "))
print("="*80)
n=int(input("Enter the number :- "))
list=[]
if n>0:
    list.append(n)
for i in range(1,x):
    val = int(input("Enter another number :- "))
    if val<=0:
        continue
    list.append(val)
for i in list:
    print("---------------------------------")
    for j in range(1,11):
        print("\t\t {} x {} = {}".format(i,j,i*j))