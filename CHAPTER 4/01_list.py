# Lists Are 'Mutable'

list = ["Daksh","Parv","Narendra","Archana",5,2.36,False,"Avaneesh","Harshil","Shreyansh"]

print(list[0])

# print(list[69])   # "ERROR"

print(list[5])
print(list[8])

list[5] = 5.26
list[8] = "Harsh"
# Unlike Strings, 'Lists' are mutable !!


print(list[5])
print(list[8])




# Slicing

print(list[0:4])