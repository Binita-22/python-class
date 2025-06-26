# Create a class and display its Namespace
class Namespace:
    def __init__(self, name, address, phonenumber):
        self.name = name
        self.address = address
        self.phonenumber = phonenumber


obj = Namespace("Bishwash", "Pokhara", "9812345645")

print("Namespace =", obj.__dict__, end="")


# Create class Student and display its type, __dict__ keys, and module
class student:
    def __init__(self, name, address, phonenumber):
        self.name = name
        self.address = address
        self.phonenumber = phonenumber


obj = student("Bishwash", "Pokhara", "9865432234")
print("Type of object:", type(obj))
data = obj.__dict__
for key, values in data.items():
    print(key, values)

# Define function student_data() to print ID, name, and class if given
def student_data(name, classes, std_id):

    print("student id is: {std_id}")
    if