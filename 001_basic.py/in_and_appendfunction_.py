# check if charater of name  belong to vowel letter
User_name = input("Enter a name: ")
Vowel_Letter = ["a", "e", "i", "o", "u"]
user_name_vowel_letter = []
for character in User_name:
    if character not in Vowel_Letter:
        pass
    else:
        user_name_vowel_letter.append(character)
print(user_name_vowel_letter)
