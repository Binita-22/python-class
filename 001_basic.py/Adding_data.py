# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
word = input("Enter only one word: ")

if len(word) < 3:
    result = word
elif word.endswith("ing"):
    result = word + "ly"
else:
    result = word + "ing"

print("Result:", result)
