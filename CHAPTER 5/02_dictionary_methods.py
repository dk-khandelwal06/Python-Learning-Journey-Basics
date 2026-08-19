# Empty dictionary
d = {}

marks = {
    "Daksh": 100,
    "Parv": 50,
    "Samanvay": 25,
    "List": [1,2,3,4,5],
    10: "Ten"
}

print(type(marks.items()))
print(marks.items())


# Left side of the dictionary is the key and right side is the value.
print(marks.keys())
print(marks.values())


# Hence Dictionary is a mutable data type. We can change the value of a key in the dictionary.
marks.update({"Daksh": 99})
print(marks)
marks.update({"Daksh": 99, "Khushi": 100})



# The main difference between the get() method and the [] operator is that the get() method returns None if the key is not present in the dictionary, while the [] operator raises a KeyError if the key is not present in the dictionary.
print(marks.get("Parth")) # It will return None if the key is not present in the dictionary.
print(marks.get("Daksh"))

print(marks["Daksh"])
# print(marks["Daksh1"]) # This will raise a KeyError if the key is not present in the dictionary.