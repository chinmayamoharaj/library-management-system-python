
print(" Enter a word or Number :" )
a=input("").upper()
res = " palindrome " if a[::]==a[::-1] else " not palindrome "
print("{} is {}".format(a,res))