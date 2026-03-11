import sys


import sys
def length(t):
    if t.isdigit():
        print("Don't enter digits----Enter only text")
    elif len(t.strip())==0:
        print("You must enter a text")
    else:
     val=t.split()
     print("--------------------------------------------")
     print("The length of :")
     for i in val:
        print("\t\t {} :- {} ".format(i,len(i)))
     print("--------------------------------------------")
     sys.exit()
while True:
 length(input("Enter the text :- "))
