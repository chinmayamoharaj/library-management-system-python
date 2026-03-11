a=input("enter a word:- ")
res = "a vowel word" if ("a" in a or "e" in a or "i" in a or "o" in a or "u" in a) else "Not a vowel word"
print("{} is {}".format(a,res))