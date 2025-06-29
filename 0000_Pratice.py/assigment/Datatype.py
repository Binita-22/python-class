# Write a program that asks the user to enter a number between 1 and 10 using a while loop.
#  Keep asking until they enter a number in that range.
#  Once they do, print "Great choice!" and stop.

while True:
    user_input = int(input("Enter a number between 1 and 10: "))
    if 1 >= user_input >= 10:
        print("Great choice")
    else:
        print("Try again")
