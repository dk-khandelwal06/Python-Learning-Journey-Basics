# Taken From CHAT GPT

import os

# Select the directory whose content you want to list
directory_path = '/'

# Use the os module to list the directory content
try:
    contents = os.listdir(directory_path)
    print()
    print(f"Contents of directory '{directory_path}':")
    print()
    for item in contents:
        print(item)
        print()
except FileNotFoundError:
    print()
    print("The directory does not exist.")
    print()
except PermissionError:
    print()
    print("You do not have permissions to access this directory.")
    print()
