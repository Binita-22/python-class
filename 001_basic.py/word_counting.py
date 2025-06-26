user_data = input("write the your introduction about you: ")
words = user_data.split(" ")
counter_dict = {}
for word in words:
    if word in counter_dict:
        counter_dict[word] = counter_dict[word] + 1
    else:
        counter_dict[word] = 1
print(counter_dict)
