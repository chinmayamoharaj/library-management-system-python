lst1=[val for val in input("Enter words separated by space:- ").split(" ")]
lst2=[val for val in input("Enter words separated by space:- ").split(" ")]
if len(lst1)>len(lst2):
    for i in range(len(lst1)-len(lst2)):
        lst2.append(" ")
elif len(lst2)>len(lst1):
    for i in range(len(lst2)-len(lst1)):
        lst1.append(" ")
concatination=list(map(lambda x,y:x+y,lst1,lst2))
print("\t\t\t\tList-1\t\t\t\t\tList-2\t\t\t\t\t\tConcatination")
print("------------------------------------------------------------------------------------------------")
print("\t{}\t{}\t{}".format(lst1,lst2,concatination))
