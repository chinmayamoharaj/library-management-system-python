n=input("Enter a text : ")
nonvowels=[]
for i in n:
  if i.isalpha():  # it ignores spaces and symbols
    if i not in 'aeiou':
        nonvowels.append(i)
print("Nonvowels:",nonvowels)