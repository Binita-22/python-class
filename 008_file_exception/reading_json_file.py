import json

file_path = r"C:\Users\DELL\OneDrive\Desktop\python-class\.vscode\extensions.json"

with open(file_path, "r") as fp:
    text_content = fp.read()
    content_dictionary = json.loads(text_content)
    print(content_dictionary["recommendations"][0])

# <-----------------------------second-dictionary----------------------------------->
data = '{"Name": "Binita", "Age": 21, "Address": "Pokhara"}'
dictionary_content = json.loads(data)
print(dictionary_content)
pair = dictionary_content.items()
keys = dictionary_content.keys()
values = dictionary_content.values()

for item in pair:
    print(item)


# ALternatively
for key, value in pair:
    print(value)


for value in values:
    print(value)
