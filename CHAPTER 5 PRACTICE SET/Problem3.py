# If we use curly braces to create a set with mixed data types, it will create a set containing both an integer and a string.
# 18 and "18" are considered different elements in the set, so both will be included in the set.

s = {18, "18"}

print(type(s))  