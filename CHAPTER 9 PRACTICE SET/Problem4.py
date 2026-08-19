word = "Donkey"

with open("file.txt","r") as f:
    data = f.read()

datanew = data.replace("Donkey","######")

with open("file.txt","w") as f: 
    data = f.write(datanew)