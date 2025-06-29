import os
import platform

print(os.getcwd())
system = platform.system()

if system == "darwin":
    print("mac user")
elif system == "Linux":
    print("Linux user")
elif system == "windows":
    print("windows users")
