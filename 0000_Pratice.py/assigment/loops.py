# Write a program that uses a for loop to print the numbers 1 to 10, and for each number, print that many stars (*). For example, for the number 3, print ***.

data = "*"
for i in range(10):
    print(data)
    data += "*"
    # i += 1

# Write a program that asks the user to enter a number between 1 and 10 using a while
# loop. Keep asking until they enter a number in that range. Once they do, print "Great choice!" and stop.
data = True
while data:
    user_input_num = int(input("Enter a number between 1 and 10: "))
    if 1 <= user_input_num <= 10:
        print("Great choice, keep it up")
        data = False
    else:
        print("Invalid number! ")
