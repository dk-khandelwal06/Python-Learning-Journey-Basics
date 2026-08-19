# Values can be same but key should not be change because it will just update to the last one.

d = {}

name = input("Enter your friend's name: ")
lang = input("Enter your friend's language: ")
d.update({name: lang})

name = input("Enter your friend's name: ")
lang = input("Enter your friend's language: ")
d.update({name: lang})

name = input("Enter your friend's name: ")
lang = input("Enter your friend's language: ")
d.update({name: lang})

name = input("Enter your friend's name: ")
lang = input("Enter your friend's language: ")
d.update({name: lang})

print(d)