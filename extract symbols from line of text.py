txt= input("Enter a line of text:- ")
flobj = filter(lambda ch:not ch.isalnum() ,txt)
listofsymb=list(flobj)
print("List of digits:- ",",".join(listofsymb))