plndrm = lambda lst: True if lst==lst[::-1] else False

lst= [val for val in input("Enter a list of values separated by space:- ").split()]
flobj = filter(plndrm,lst)
listofplnd=list(flobj)
print("List of palindromes:- ",listofplnd)