import os

print(os.getcwd())
filename = "platform_usage.py"
if os.path.exists(filename):
    print("Platform code file exits.")
else:
    print("Platform code filde doesnot exits.")
