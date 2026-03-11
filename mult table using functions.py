import sys
def mult(n):
    if n<=0:
        print("Invalid input----please enter positive integer only")
    else:
     print("-----------------------------------")

     print("\tThe multiplication table of {} :".format(n))
     for i in range(1,11):
        print("\t\t {} x {} = {}".format(n,i,n*i))
     print("-----------------------------------")
     sys.exit()
while True:
    try:
     mult(int(input("Enter the number :- ")))
    except ValueError:
     print("Invalid input----please enter positive integer only")
