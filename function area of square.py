
def arsqr():
        while (True):
          s=int(input("Enter the length of one side:- "))
          if s > 0:
             break
          else:
             print("Length cannot be 0---Please enter a value greater than 0")
        a=s**2
        p=4*s
        return a,p


res=arsqr()
print("----------------------------------")
print("Area of the given square = ",res[0])
print("Perimeter of the given square = ",res[1])

