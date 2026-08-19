words = ["Donkey", "ganda", "bad"]

with open("file_for_5.txt","r") as f:
    data = f.read()

for word in words:
    data = data.replace(word,"#" * len(word))

with open("file_for_5.txt","w") as f: 
    f.write(data)