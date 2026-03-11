lst= input("Enter a line of text:- ")
flobj = filter(lambda ch:ch.isdigit() ,lst)
listofdig=list(flobj)
print("List of digits:- ",listofdig)