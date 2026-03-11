
def arcir():
        while (True):
          r=int(input("Enter the radius:- "))
          if r > 0:
             break
          else:
             print("Radius cannot be 0---Please enter a value greater than 0")
        a = 3.1416 * (r ** 2)
        p = 2 * 3.1416 * r
        return r, a, p


res=arcir()
print("----------------------------------")
print("Area of the given circle = ",res[1])
print("Perimeter of the given circle = ",res[2])

