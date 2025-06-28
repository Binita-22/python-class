# Replace first char occurrences with $.
data = input("Enter a word: ")
first = data[0]
result = " "
for i in range(len(data)):
    if i == 0:
        result += data[i]
    else:
        if data[i] == first:
            result += "$"
        else:
            result += data[i]
print(result)
