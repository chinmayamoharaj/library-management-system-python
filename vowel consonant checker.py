text=input("Enter a text: ")
print("\t\t Vowels \t\t\t Consonants ")
for i in text:
     if i.lower() in "a,e,i,o,u" :
        print("\t\t",i)
     else:
         print("\t\t\t\t\t\t\t\t",i)


