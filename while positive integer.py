n=int(input("enter a number: "))
fn=1
if n<=0:
    print("{} is invalid input".format(n))
else:
    while fn<=n :
        print(fn,end="  ")
        fn += 1