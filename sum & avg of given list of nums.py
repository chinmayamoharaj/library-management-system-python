def conint():
    lst=[]
    s1 = int(input("Enter a number: "))
    lst.append(s1)
    while True:
     s2=int(input("Enter another number: "))
     if s2>0:
         lst.append(s2)
         continue
     elif s2==0:
         break
    print("------------------------------------------------")
    total = sum(lst)
    average = total / len(lst)
    return total, average

print("------------------------------------------------")
res=conint()
print("The total sum =",res[0])
print("The average =",res[1])
