n=int(input("Enter how many multiplication table you want: "))
if n<=0:
    print("Invalid input : Kindly enter a positive number")
else:
    for i in range(1,n+1):
        print("----------------------------------")
        print("The multiplication table of {} is :- ".format(i))
        for k in range(1,11):
            print("\t\t {} x {} = {}".format(i, k, i * k))



