lst=[]
lsts=[]
i=1
n=int(input("Enter a value : "))
if n%2==0:
    lst.append(n)
else:
    lsts.append(n)
while i>0:
    val = int(input("Enter another value : "))
    if (val==0):
        break
    if val%2==0:
        lst.append(val)
    else:
        lsts.append(val)

print("="*50)
print("Even numbers list is :- ",lst)
print("="*50)
print("Odd numbers list is :- ",lsts)