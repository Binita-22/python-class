# Ask the user to input the current temperature (as a number). Then:

# If the temperature is above 30, print "It's hot! Wear sunglasses!"
# If the temperature is between 15 and 30 (inclusive), print "It's nice outside! Enjoy!"
# If the temperature is below 15, print "It's cold! Wear a jacket!

user_num = float(input("Enter your current temperature in number: "))
if user_num <= 15:
    print("It is cold wear a jacket!")
elif 15 < user_num <= 30:
    print("It's nice outside! enjoy!")
else:
    print("It is hot! wear sunglasses!")


# Ask the user to input a number. Use an if statement to check if the number is even or
#  odd, and print the result. (Hint: A number is even if number % 2 == 0.)
user_num1 = int(input("Enter a number: "))
if user_num1 % 2 == 0:
    print(f"The given number {user_num1} is even")
else:
    print(f"The given number {user_num1} is odd number.")
