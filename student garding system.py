while(True):
    id=int(input("Enter student id :- "))
    if id > 0:
     break
    else:
     print("Kindly enter valid id !!!")

while(True):
  res = "valid"
  name = input("Enter student name :- ").upper()
  n = name.split()
  for i in n:
      if not i.isalpha():
          res = "invalid"
          break
      else:
          res = "valid"
  if res == "invalid":
      print("Please enter a valid name---that contains only alphabets")
  else:
      break
# Enter student marks...
while True:
    om = int(input("Enter Odia mark :- "))
    if om >0:
        break
    else:
        print("Please enter valid mark !!!")

while True:
    em = int(input("Enter English mark :- "))
    if em >0:
        break
    else:
        print("Please enter valid mark !!!")

while True:
    mm = int(input("Enter Mathematics mark :- "))
    if mm >0:
        break
    else:
        print("Please enter valid mark !!!")

while True:
    hm = int(input("Enter Sanskrit / Hindi mark :- "))
    if hm >0:
        break
    else:
        print("Please enter valid mark !!!")

while True:
    sm = int(input("Enter Science mark :- "))
    if sm >0:
        break
    else:
        print("Please enter valid mark !!!")

while True:
    ssm = int(input("Enter Social science mark :- "))
    if ssm >0:
        break
    else:
        print("Please enter valid mark !!!")

# Full mark...
fm = 600
# Total mark...
tm = om+em+mm++sm+hm+ssm
# percentage...
pr = (tm/fm)*100

if tm<=180:
    f="true"
else:
    f="false"
if om<40 or em<40 or mm<40 or sm<40 or hm<40 or ssm<40:
    f="true"
else:
    f="false"
# Displaying student Mark sheet...
print("="*50)
print("\t\t\tStudent id :- ",id)
print("\t\t\tStudent name :- ",name)
print("\t\t\tOdia mark :- ",om)
print("\t\t\tEnglish mark :- ",em)
print("\t\t\tSanskrit mark :- ",sm)
print("\t\t\tMathematics mark :- ",mm)
print("\t\t\tScience mark :- ",sm)
print("\t\t\tSocial science mark :- ",ssm)
print("\t\t\t----------------------------")
print("\t\t\tTotal secured mark :- ",tm)
print("\t\t\tSecured percentage :- ",pr,"%")
print("="*60)
if f=="true":
    print("\t\t\t{} you are failed !!!".format(name))
if (pr>=60):
    print("\t\t\tCongrats {} you have secured First Division ".format(name))
elif (pr>=40):
    print("\t\t\t{} you have secured Second Division ".format(name))
elif (pr>=30):
    print("\t\t\t{} you have secured Third Division ".format(name))
elif (pr<30):
    print("\t\t\t{} you are failed !!!".format(name))




