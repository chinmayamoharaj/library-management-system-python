
while(True):
  res="valid"
  n=input("Enter your name :- ")
  val=n.split()
  for i in val:
      if not i.isalpha():
          res="invalid"
          break
      else:
          res="valid"
  if res=="invalid":
      print("Please enter a valid name---that contains only alphabets")
  else:
      print("Your name {}---is valid".format(n))
      break





