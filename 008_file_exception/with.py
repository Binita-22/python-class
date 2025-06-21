# with = context manager - yeho hudha .close() garna pardina
with open("file.csv", "w+") as file_pointer:
    file_pointer.write("My collage name is ICP. \n")
    file_pointer.write("Ma currently 2nd year ma padxu. \n")
    file_pointer.write("mero collage suru huni fixed time xina \n")
    file_pointer.seek(0)
    lines = file_pointer.readlines()
    for line in lines:
        print(line, end="")
