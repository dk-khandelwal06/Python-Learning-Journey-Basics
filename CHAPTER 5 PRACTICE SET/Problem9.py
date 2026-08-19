# Can you change the values inside a list which is contained in set S? 

s = {8, 7, 12, "Harry", [1,2]}
print(s) # It will raise a TypeError because lists are mutable and cannot be added to a set.

# No, you cannot change the values inside a list that is contained in a set. In Python, sets can only contain immutable (unchangeable) types, and lists are mutable (changeable). Therefore, trying to include a list in a set will raise a TypeError.


s = {8, 7, 12, "Harry", (1,2)}
print(s) # It will print the set without any error because tuples are immutable and can be added to a set.