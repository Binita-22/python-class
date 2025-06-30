# Write a program that asks the user to enter a number between 1 and 10 using a while loop.
#  Keep asking until they enter a number in that range.
#  Once they do, print "Great choice!" and stop.
validation = True
while validation:
    user_input = int(input("Enter a number between 1 and 10: "))
    if 1 <= user_input <= 10:
        print("Great choice")
        break
    else:
        print("Try again")


# Create a list of your 5 favorite fruits (as strings, like "apple" or "banana"). Then:
# Print the entire list.
# Print the first and last fruit in the list.
# Add a new fruit to the list using the append() method and print the updated list.
My_favorite_fruits = ["apple", "Banana", "mango", "grape"]
first_fruits = My_favorite_fruits[0]
last_fruits = My_favorite_fruits[-1]
My_favorite_fruits.append("strawberry")
print(f"The first fruits name is {first_fruits} and last fruits name is {last_fruits}")
print("The updated list of fruits is ", My_favorite_fruits)


# Ask the user to input two numbers (use input()). Then:
# Add the two numbers together and print the result.
# Multiply the two numbers and print the result.
# Make sure to convert the inputs to numbers (use float() or int()) so you can do math with them!
user_num1 = int(input("Enter a first number: "))
user_num2 = int(input("Enter a second number: "))
sum = user_num1 + user_num2
Multiply = user_num1 * user_num2
print("The sum is", sum)
print("The product is: ", Multiply)
