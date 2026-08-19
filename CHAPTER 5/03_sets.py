s = {1,3,5,7,9,11,13,15,17,19}

# To make empty set we have to use set() function. If we use {} then it will create an empty dictionary.
e = set()
print(type(e))

# Set do not repeat the elements. It will only keep unique elements.
s1 = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10}
print(s1)

# List can sort the elements but set can not sort the elements. Set is an unordered collection of unique elements.
list = [1,5,6,2,3,8,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
print(list)
list.sort()
print(list)

a = set(list)
print(a)

b = {1,4,2,67,2,3,4,89,56,5,5,5}
print(b)
