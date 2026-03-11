def arrect():
  while (True):
    l=int(input("Enter the length:- "))
    if l <= 0:
      print("Length cannot be 0---Please enter a value greater than 0")
      continue
    else:
       while (True):
         b=int(input("Enter the breadth:- "))
         if b > 0:
          break
         else:
          print("breadth cannot be 0---Please enter a value greater than 0")
       break
  a=l*b
  p=2*(l+b)
  return a,p



res=arrect()
print("----------------------------------")
print("Area of the given Rectangle = ",res[0])
print("Perimeter of the given Rectangle = ",res[1])

