f = open("poems.txt", "r")
data = f.read()
if("twinkle" in data):
    print("The word twinkle is present!!")
else: 
    print("The word twinkle is not present!!")
f.close()