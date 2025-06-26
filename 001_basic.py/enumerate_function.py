# Create a list
fruits = ["apple", "banana", "orange", "grape", "strawberry"]

for index, fruits in enumerate(fruits, start=1):
    if index % 2 == 0:
        pass
    else:
        print(f"{index}.{fruits}")
