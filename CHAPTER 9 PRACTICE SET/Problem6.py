with open("log.txt") as f:
    data = f.read()

if ("python" in data):
    print("Yes, python is present !!")
else:
    print("No, python is not present !!")