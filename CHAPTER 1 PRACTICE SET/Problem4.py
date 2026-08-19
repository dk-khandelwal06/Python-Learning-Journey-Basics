# Taken From CHAT GPT (folder ka naam batao aapko uski files de dega)

import os

# Specify the directory path (you can also use '.' for current directory)
directory_path = '/'  # current directory

# Get the list of files and directories
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
