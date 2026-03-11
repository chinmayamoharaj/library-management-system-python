plndrm=lambda s: "It is palindrome" if s==s[::-1] else "Not palindrome"

s=input("Enter any value or word:- ")
print(plndrm(s))
