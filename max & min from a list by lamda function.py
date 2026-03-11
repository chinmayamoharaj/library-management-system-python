findmax=lambda lst: "All are equal" if len(set(lst))==1 else max(lst)
findmin=lambda lst: "All are equal" if len(set(lst))==1 else min(lst)

print("Enter values separated by a space:- ")
lst=[int(val) for val in input().split()]
print("max in {} = {}".format(lst,findmax(lst)))
print("min in {} = {}".format(lst,findmin(lst)))
