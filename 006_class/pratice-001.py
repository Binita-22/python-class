# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def intro(self):
#         print("inside intro")
#         print(self)
#         print("inside intro")


# obj = Animal("Tiger")
# obj.intro()
# print("Outside the class")
# print(obj)


class converter:
    def __init__(self):
        pass

    def fahrenheit_to_celsius(self):
        F = int(input("enter the value of fahrenheit: "))
        Cel = (F - 32) * 5 / 9
        print("The value of Celcius is: ", {Cel})

    def celsius_to_fahrenheit(self):
        C = int(input("enter the value of celsius: "))
        Far = (C * 9 / 5) + 32
        print("The value of Faranite is:", {Far})


print(" 1. Choose 1 to calculate the Faranaite. ")
print("2. chose 2 to calculate the celcius.")
user_choice = int(input("Enter your choice:"))
conv = converter()
if user_choice == 1:
    conv.fahrenheit_to_celsius()
elif user_choice == 2:
    conv.celsius_to_fahrenheit()
else:
    print("Invalid number.")
