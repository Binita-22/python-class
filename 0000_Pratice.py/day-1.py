# To calculate string length
# user_input = input("Enter your name: ")
# length = len(user_input)
# print(f"The length of user name: {length}")

# Count charater frequency in a string
user_data = input("Enter a name: ")
frequency_of_data = {}
for name in user_data:
    if name in frequency_of_data:
        frequency_of_data[name] = frequency_of_data[name] + 1
    else:
        frequency_of_data[name] = 1

print(" The frequency of data are", frequency_of_data)
