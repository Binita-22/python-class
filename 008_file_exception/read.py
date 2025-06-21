file_pointer = open(r"C:\Users\DELL\OneDrive\Desktop\python-class\008_file_exception\file.csv", "r")
content = file_pointer.read()
file_pointer.seek(0)  # seek vanako pointer lai move garako
print(content)
another_content = file_pointer.read()
print("Number are", another_content)
