# Swap first 2 chars of 2 strings.
data = input("enter a only one word: ")
output = " "
for i in range(len(data)):
    if i == 0:
        output += data[1]
    else:
        if i == 1:
            output += data[0]
        else:
            output += data[i]
print(output)

name = input("Enter your first name and last name: ")
info = name.split()
swap = ""
for i in range(len(info)):
    if i == 0:
        swap += info[-1]
    else:
        if i == 1:
            swap += info[0]
        else:
            swap += info[i]
print(swap, end=(" "))
