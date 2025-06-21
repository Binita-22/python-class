# end = vanako default value \n hunxa
file_pointer = open(r"C:\Users\DELL\OneDrive\Desktop\python-class\008_file_exception\file.csv ", "w+")
file_pointer.write("My collage name is ICP. \n")
file_pointer.write("Ma currently 2nd year ma padxu. \n")
file_pointer.write("mero collage suru huni fixed time xina \n")
file_pointer.seek(0)
lines = file_pointer.readlines()
for line in lines:
    print(line, end="")
file_pointer.close()
