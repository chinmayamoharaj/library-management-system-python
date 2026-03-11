text = input("Enter a text: ")

vowels = []
consonants = []

for ch in text:
    if ch.isalpha(): #it ignores spaces and symbols
        if ch.lower() in "aeiou":
            vowels.append(ch)
        else:
            consonants.append(ch)

print("Vowels:", vowels)
print("Consonants:", consonants)