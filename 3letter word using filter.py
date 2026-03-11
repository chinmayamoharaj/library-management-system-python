lengofwrd = lambda lst: True if 4>=len(lst)>=3  else False

lst= [val for val in input("Enter a list of values separated by space:- ").split(" ")]
flobj = filter(lengofwrd,lst)
listof34=list(flobj)
print("List of 3-4 length of words:- ",listof34)