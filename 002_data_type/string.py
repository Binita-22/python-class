# Count character frequency in a string.
user_input = input("Enter a letter: ")
user_data = {}
for word in user_input:
    if word in user_data:
        user_data[word] = user_data[word] + 1
    else:
        user_data[word] = 1
print(user_data)

# Get string of first and last 2 chars.
data = input("Enter a string: ")
if len(data) <= 2:
    print("Empty string")
else:
    print("output: ", data[:2] + data[-2:])
